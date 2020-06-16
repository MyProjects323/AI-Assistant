# pip install pyttsx3
# (Help us to convert text to voice from our system assistant)
import pyttsx3
import datetime 

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Sir!")
    speak("The current Time is : ")
    time()
    speak("The current date is : ")
    date()
    speak("Jarvis at your service sir...Please tell me how can I help you?")

wishme()
