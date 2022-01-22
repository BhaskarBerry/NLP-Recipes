# -*- coding: utf-8 -*-
"""
convert speech to text
The simplest way to do this by using Speech Recognition and PyAudio
examples are Siri, Alexa’s Google Voice

Note: Check the library - pip install PyAudio
"""

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please say something")
    audio = r.listen(source)
    print("Time Over , Thanks")

try:
    print("I Think you said :"+r.recognize_google(audio))
except:
    pass

