import speech_recognition as sr
# import pyttsx3

recognizer = sr.Recognizer()

while True:
    try:

        with sr.microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic,duration=0.5)
            audio = recognizer.listen(mic)

            text = recognizer.recognizer_google(audio)
            text = text.lower()

            print(f"Recognized {text}")

    except sr.UnknownValueError():
        recognizer = sr.recognizer()
        continue
