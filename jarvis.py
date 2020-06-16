# pip install pyttsx3
# (Help us to convert text to voice from our system assistant)
import pyttsx3
import datetime 
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current Time is : ")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is : ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Sir!")
    time()
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

def sendEmail(to,content):
    server = smtplib.SMTP("email", 587)
    server.ehlo()
    server.starttls()
    server.login("email","password")
    server.sendmail('email',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send mail'in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "reciept email"
                sendEmail(to,content)
                speak("Email has been sent")
                speak("The message sent in email is :",content)

            except Exception as e:
                print(e)
                speak("Unable to send the Email..")

        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            

        elif 'offline' in query:
            speak("Jarvis is going Offline...")
            quit()


        
        
