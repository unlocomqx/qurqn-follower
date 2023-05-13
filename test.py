import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    r.pause_threshold = 0.5
    t = r.recognize_vosk(audio, language='ar-AR')
    print(t)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
