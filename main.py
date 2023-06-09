import speech_recognition as sr
import time


def callback(recognizer: sr.Recognizer, audio: sr.audio.AudioData):
    try:
        print("You said " + recognizer.recognize_google(audio, language="en-US"))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some unrelated computations for 5 seconds
for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

print("stop listening")
# calling this function requests that the background listener stop listening
stop_listening(wait_for_stop=False)

# do some more unrelated things
while True: time.sleep(0.1)
# we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping
