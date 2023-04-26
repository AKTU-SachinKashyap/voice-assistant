import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime




def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recogninig...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")



def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    reat = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
speechtx("hello i am jarvis sir. please tell me how may I help you")

if __name__=='__main__':
    while True:
    # if sptext().lower() == " hey Akash" :
     
        data1 = sptext().lower()

        if "your name" in data1:
            name = "my name is akash"
            speechtx(name)

        elif "your task" in data1:
            tasks = "my task is notification reminder"
            speechtx(tasks)

        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)

        elif 'google' in data1:
            webbrowser.open("https://www.google.com ")

        elif 'open youtube' in data1:
            webbrowser.open("youtube.com")

        elif "exit"in data1:
             speechtx("thank you sir")
             break 
