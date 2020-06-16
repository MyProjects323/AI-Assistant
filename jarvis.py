# pip install pyttsx3
# (Help us to convert text to voice from our system assistant)
import pyttsx3
import datetime 
import speech_recognition as sr # pip install SpeechRecognition
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
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour < 16:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Jarvis at your service sir...Please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "null"

    return query

takeCommand()
