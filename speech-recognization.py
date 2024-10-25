import speech_recognition as sr
import aifc #this no supports in latest version it is removed from latest version python 3.13.0

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")  # Added noise adjustment
        r.adjust_for_ambient_noise(source)       # Calibrate for noise
        print("Speak something:")
        audio = r.listen(source)
        
        print("Processing...")
        text = r.recognize_google(audio)
        print("You said: {}".format(text))

except sr.RequestError as e:
    print("Could not request results; check your network connection.")
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except Exception as e:
    print(f"An error occurred: {e}")
