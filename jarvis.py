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

time()