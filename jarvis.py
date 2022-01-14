//hey I'm sargent ramzi. and I maked this small AI project for beginner student's. this project name is JARVIS.

# Import the required module for text  
# to speech conversion

import pyttsx3    
import webbrowser    // webbrowser module is a convenient web browser controller. 
import speech_recognition as sr

# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 178)

#print=sg.Print
name = input("enter your name---> ")

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 

def takeCommand():
      
    r = sr.Recognizer()
      
    with sr.Microphone() as source:
        print ('\U0001F600')
        print("Listening...") 
        r.energy_threshold = 500
        r.pause_threshold = 0.7
        r.non_speaking_duration = 0.2        
        audio = r.listen(source)
    
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
    
    except Exception as e: 
        print(e)
        #print("Unable to Recognizing your voice.")
        #speak("Sorry, I didn't get that.")
        return "None"

    return query 

if __name__ == '__main__': 
    query=takeCommand().lower()
    while True : 
        query=takeCommand().lower()
        if 'program' in query : 
            print('in')
            speak('i am online')
            while True:
                query=takeCommand().lower()
                if 'help'in query : 
                    speak('ok what a question.')
                    print ('\U0001F607')
                    while True:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print ('\U0001F600')
                            print("Listening...") 
                            r.energy_threshold = 500
                            r.pause_threshold = 0.7
                            r.non_speaking_duration = 0.2        
                            audio = r.listen(source)
    
                        try: 
                            print("Recognizing...")     
                            find1 = r.recognize_google(audio, language ='en-in') 
                            #print(f"User said: {query}\n") 
                            webbrowser.open(f'https://www.google.com/search?q={find1}')
                            speak(f'i got it {find1}')   
            
                        except Exception as e: 
                            print(e)
                        if 'stop' in find1:
                            speak('i got it lets go back')
                            break    
                if 'sleep' in query : 
                    speak('i got it\n ok i am going to sleep')
                    break
            if 'bye' in query: 
                print(f'ok bye {name}')
                break
