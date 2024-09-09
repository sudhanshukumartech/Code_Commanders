import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import webbrowser
import wikipedia

# This is Logger for the application
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)



#Taking the male voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

def speak(text):
    """This function converts text to a voice

    Args:
        text
    returns:
        voice
    """
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    """This function takes command & recognize

    Returns:
        text as query
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return "None"
    return query


#this function will wish you
def wish_me():
    hour = (datetime.datetime.now().hour)
    
    if hour >=0 and hour <=12:
        speak("Good Morning sir! How are you doing?")
    
    elif hour >=12 and hour <=18:
        speak("Good afternoon sir! How are you doing?")
    
    else:
        speak("Good evening sir! How are you doing?")
    
    speak("I am JARVIS.Tell me sir how can i help you?")




wish_me()
while True:

    query = takeCommand().lower()
    print(query)
    
    if "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")

    
    elif "name" in query:
        speak("My name is JARVIS")

    
    elif "exit" in query:
        speak("Good bye sir")
        exit()

    elif "open google" in query:
        speak("ok sir. please type here what do you want to read")
        webbrowser.open("google.com")

    
    elif "open facebook" in query:
        speak("ok sir. opening facebook")
        webbrowser.open("facebook.com")

    
    #This query for search something from wikipedia
    elif 'wikipedia' in query:
        speak("Searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia ")
        print(results)
        speak(results)




