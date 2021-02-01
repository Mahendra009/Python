import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    # for wishMe

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mr. Srivastava!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon Mr. Srivastava!")

    else:
        speak("Good Evening Mr. Srivastava!")

        speak("Arunima at your service, tell me what can I do for you now?")

def takeCommand():
    r= sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listing...")
        r.energy_threshold =3500
        r.dynamic_energy_threshold = False
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("searching...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            if 'ok Arunima' in query:
                print("")  

        except Exception as e:
           # print(e)
            speak("Say that again please...")
            return "None"
        return query

       


if __name__ == "__main__":
    
    wishMe() # for wishMe

    # for takeCommand
    while True:
        query= takeCommand().lower()

    # logic for excuting task based on query.

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("OK got it")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_folder = 'E:\\music\\panjabi'
            songs = os.listdir(music_folder)
           # print(songs)
            os.startfile(os.path.join(music_folder, songs[0]))
            speak("Here is your music enjoy Mr.srivastava")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing'+ song)
            pywhatkit.playonyt(song)
            speak("Here is your music enjoy Mr.srivastava")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak(f"sir,the current time is {strTime}")

        elif 'are you single' in query:
            speak("no, I am in a relationship with mahendra srivastava for 10 years so get lost")

        elif 'jokes' in query:
            speak(pyjokes.get_joke())

        elif 'stop' in query:
            speak("I am going to sleep now see you soon. Thank You Mr. Srivastava")
            quit= exit()

        else:
            speak("Is there anything else that I can do for you Mr.Srivastava!")
            
            


