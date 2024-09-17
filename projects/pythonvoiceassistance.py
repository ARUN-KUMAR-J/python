import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()
def record():
    while(1):
        try:
            with sr.Microphone() as source:
                print("Listening!!!")
                r.pause_threshold=5
                audio=r.listen(source) 
                print("recognizing...")
                mytext=r.recognize_google(audio,language='en-in')
                return mytext  
        except sr.RequestError as e:
            print(f'could not request reults :{e}')
        except sr.UnknownValueError:
            print("Unknown error occured")
def output_text(text):
    f=open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return
while(1):
    text=record()
    output_text(text)
    print("wrote text")
    exit()