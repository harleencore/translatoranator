import speech_recognition as sr
import pyttsx3 as tts
import os
import sys


engine = tts.init()


r = sr.Recognizer()

with sr.Microphone() as source:
    print("START SPEAKING")
    audio = r.listen(source)
    print("TIME'S UP!")

try:
    print("You said: " + r.recognize_google(audio))
    print("playing audio file...")
    engine.say(r.recognize_google(audio))
    engine.runAndWait()
except:
    print("something went wrong")
    pass
