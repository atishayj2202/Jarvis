from gtts import gTTS
import playsound
import os


def speak(myText):
    language = 'en'
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("output.mp3")
    print("saved file")
    playsound.playsound("output.mp3")
    print("sound played")
    os.remove("output.mp3")
