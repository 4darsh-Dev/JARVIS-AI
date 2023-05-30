
import pyttsx3

from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

#set rate
engine.setProperty('rate', 190)

#set volume
engine.setProperty('volume', 1.0)

#set voice female
voices = engine.setProperty('voices')
engine.setProperty('voice', voices[1].id)

#Text to sepeech conversion

def speak(text):
    engine.say(text)
    engine.runAndWait()
