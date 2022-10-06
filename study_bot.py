import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import requests
import random
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello I am Study Bot. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prathamop07@gmail.com', 'Pratham@8766')
    server.sendmail('prathamop07@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'name' in query:
            speak("hello! my name is Study bot, i am here to assist you")

        elif 'how are you' in query:
            speak("i am well, thank you. i hope you are well too. how may i help you today?")
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'joke' in query:
            jokes = ["Why did the melon jump into the lake? It wanted to be a water-melon",
                    "How does the ocean say hello? It waves.",
                    "What kind of music do planets like? Neptunes.",
                    "Why do bees have sticky hair? Because they use honeycombs.",
                    "Why does Humpty Dumpty love autumn?  Because Humpty Dumpty had a great fall.",
                    "Why are ghosts good cheerleaders?  Because they have a lot of spirit!",
                    "What is an astronaut’s favorite key on a keyboard? The space bar."]
            random1 = random.randint(0,7)
            speak(jokes[random1])

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'date' in query:
            date_obj = datetime.date.today()
            speak(f"Today's date is {date_obj}")

        elif 'day' in query:
            day = datetime.datetime.now().strftime('%A')
            speak(f"Current day is {day}")

        #lectures
        elif 'software engineering lecture' in query:
            webbrowser.open("https://meet.google.com/jfr-cjcg-ucs")

        elif 'theory of computation lecture' in query:
            webbrowser.open("https://meet.google.com/kdo-vhtm-hsn")

        elif 'data structure lecture' in query:
            webbrowser.open("https://meet.google.com/wtv-rhzw-hhj")

        elif 'database management system lecture' in query:
            webbrowser.open("https://meet.google.com/gdm-cvhk-ifq")

        #tutorials
        elif 'software engineering tutorial' in query:
            webbrowser.open("https://meet.google.com/rig-xngu-grc")

        elif 'theory of computation tutorial' in query:
            webbrowser.open("https://meet.google.com/qjs-gzpd-kcb")

        elif 'data structure tutorial' in query:
            webbrowser.open("https://meet.google.com/wtv-rhzw-hhj")

        elif 'database management system tutorial' in query:
            webbrowser.open("https://meet.google.com/oxz-grqd-gdd ")

        #labs
        elif 'software engineering lab' in query:
            webbrowser.open("https://meet.google.com/rig-xngu-grc ")

        elif 'theory of computation lab' in query:
            webbrowser.open("https://meet.google.com/nnk-ypax-qqc ")

        elif 'data structure lab' in query:
            webbrowser.open("https://meet.google.com/wtv-rhzw-hhj")

        elif 'database management system lab' in query:
            webbrowser.open("https://meet.google.com/oxz-grqd-gdd")

        elif 'software engineering notes' in query:
            webbrowser.open("https://drive.google.com/drive/folders/1fDffT8LiUNb5vEZt6c_Ok-_57PoniFvX?usp=sharing")

        elif 'database management system notes' in query:
            webbrowser.open("https://drive.google.com/drive/folders/1XjcuV0HKq3VCNclhFVrFKePNLAeoGQdD?usp=sharing")

        elif 'theory of computation notes' in query:
            webbrowser.open("https://drive.google.com/drive/folders/1UDh1zCoUceehMfyAfRF779J_DYA4yqXI?usp=sharing")

        #edu plus portal
        elif 'edu plus' in query:
            webbrowser.open("https://learner.vierp.in/")

        #volp classroom
        elif 'classroom' in query:
            webbrowser.open("https://classroom.volp.in/login")

        elif 'song' in query:
            speak("What song should be played?")
            song = takeCommand()
            music_dir = 'F:\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, f'{song}.mp3'))


        elif 'sql developer' in query: 
            codePath1 = "C:\\App\\sqldeveloper-21.4.1.349.1822-x64\\sqldeveloper\\sqldeveloper.exe"
            os.startfile(codePath1)

        elif 'word' in query:
            codePath2 = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.exe"
            os.startfile(codePath2)

        elif 'powerpoint' in query:
            codePath3 = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
            os.startfile(codePath3)

        elif 'excel' in query:
            codePath4 = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.exe"
            os.startfile(codePath4)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gajbhiyepratham876@gmail.com";    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry but, I am not able to send this email")  

        elif 'weather' in query:
            speak("For which city the weather should be reported: ")
            city = takeCommand()
            url = f"https://www.google.com/search?q=weather {city}"
            html = requests.get(url).content
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            data = str.split('\n')
            sky = data[1]
            print(f"Sky is  and Temperature in {city} city is {temp}")
            speak(f"Sky is  and Temperature in {city} city is {temp}")
 
        elif 'exit' in query:
            speak("Thank you for using study bot. Have a good day")
            exit(1)