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
            print(f"Sky is {sky} and Temperature in {city} city is {temp}")
            speak(f"Sky is {sky} and Temperature in {city} city is {temp}")