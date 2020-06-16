# pip install pyttsx3
# (Help us to convert text to voice from our system assistant)
import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is JARVIS AI Assistant")