import pyttsx3
import webbrowser
import speech_recognition as sr
import os
import datetime
import wikipedia
import comtypes.client

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good morning!")
    elif hour>12 and hour<4:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Iam Soona Paana ,ippo enna pannumnu soldra")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!!!")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f'User said:{query}\n')
    except Exception as e:
        print("Say that again please")
        speak("Thirumba sollunganey")
        return None
    return query

if __name__=="__main__":
    wishme()
    while True:
        query=takecommand()
        if query:
            query=query.lower()
            if 'wikipedia' in query:
                speak("Searching  Wikipedia...")
                query=query.replace("wikipedia", "")
                result=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(result)
                speak(result)
            elif 'open youtube' in query:
                webbrowser.open("youtube.com") 
            elif 'open spotify' in query:
                webbrowser.open('spotify.com')
            elif 'play music' in query:
                music_dir='D:\music'
                songs=os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))
            elif 'play movies' in query:
                movie_dir='D:\Movies'
                movies=os.listdir(movie_dir)
                print(movies)
                os.startfile(os.path.join(movie_dir,movies[0]))
            else:
                speak("varenda chinnasaamy")
        else:
            exit()