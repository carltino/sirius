from speech.recognizer import recognize_speech 
from speech.tts import speak 
from nlp.intent import process_intent 

def main(): 
    while True: 
        command = recognize_speech() 
        if not command: 
            continue 
        intent = process_intent(command) 
        if intent == "general query": 
            speak("This is a general query. Let me find an answer for you.") 
        elif intent == "device control": speak("Sure, I will control the device for you.")
        elif intent == "set a reminder": speak("I will set a reminder for you.") 
        else: speak("I am not sure what you mean.") 
        
if __name__ == "__main__": main()


