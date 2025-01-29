import speech_recognition as sr 
def recognize_speech(): 
    recognizer = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening...") 
        audio = recognizer.listen(source) 
        try: 
            text = recognizer.recognize_google(audio) 
            print(f"You said: {text}") 
            return text 
        except sr.UnknownValueError: 
            print("Sorry, I did not understand that.") 
            return "" 
        except sr.RequestError as e:
             print(f"Error with the speech recognition service: {e}") 
             return ""