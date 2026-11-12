import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  print(text)
  engine.say(text)
  engine.runAndWait()
speak("hello world!")
