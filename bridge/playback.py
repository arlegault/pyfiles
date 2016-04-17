#!/usr/bin/env python
from ctypes import *
import pyaudio
import sys
import speech_recognition as sr
import requests

def callback(recognizer, audio):
    
    try:
        print "You said " + recognizer.recognize_google(audio)
    except LookupError:
        print "Oops! Didn't catch that"


r = sr.Recognizer()
m = sr.Microphone()

with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

import time
time.sleep(5)
stop_listening()
