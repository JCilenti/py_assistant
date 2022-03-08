import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
from datetime import datetime

# creating our virtual assitant with pyttsx3

def time_tracking():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(type(current_time))
    print(int(current_time))
    return current_time

def assistant(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def greeting():
    if time_tracking() < 12:
        assistant("Good Morning, Mr. Cilenti")
    elif time_tracking() == 12:
        assistant("Good Afternoon, Mr. Cilenti")
    else:
        assistant("Good Evening, Mr. Cilenti")

def audio_input():
    aud = sr.Recognizer()
    with sr.Microphone as source:
        print("[LISTENING AND PROCESSING...]")
        aud.pause_threshold = 0.7
        audio = aud.listen(source)
        try:
            print("[UNDERSTANDING...]")
            phrase = aud.recognize_google(audio, language='en-us')
            print("you said, ", phrase)
        except Exception as exp:
            print(exp)
            print("Can you please repeat that?")
        return "None"
    return phrase

def theTime(self):
    time = str(datetime.datetime.now())
    print(time) 
    hour = time[11:30]
    min = time[14:16]
    assistant(self, "The time right now is" + hour + "Hours and" + min + "Minutes")

if __name__ == '__main__':
    print("[SYSTEM BOOTING...]")
    print("[GATHERING LIBRARIES...]")
    print("[CHECKING FOR UPDATES...]")
    print("[STARTING...]")
    greet = "My name is Atomas. I am your virtual assistant for Linux. How may I help you?"
    assistant(greet)
    greeting()
