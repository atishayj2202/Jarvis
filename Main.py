import speech_recognition as sr
from TtS import speak

r = sr.Recognizer()


def starter():
    with sr.Microphone() as source:
        print("Relistening")
        # r.energy_threshold = 500
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print("listen")

        try:
            text = r.recognize_google(audio)
            print(text)
            text = text.lower()
            if -1 != text.find("jarvis"):
                print("done")
                speak("Hello Sir! How can I help you.")
            else:
                print("Speak Jarvis")
                starter()
        except:
            print("error")
            starter()
print("out")

starter()
