import speech_recognition as sr
import os
import pandas as pd
from thefuzz import fuzz
from thefuzz import process

csv = pd.read_csv('./data/quran.csv')
texts = csv['text'].to_list()

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Say something...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=3)
        print("Recognizing...")
    try:
        r.pause_threshold = 0.5
        text = r.recognize_whisper(audio, language='arabic', model='small')
        print(text)
        if len(text) > 0:
            result = process.extract(text, texts, limit=3)
            print(result)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
