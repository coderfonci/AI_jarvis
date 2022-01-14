//hey I'm sargent ramzi. and I maked this small AI project for beginner student's. this project name is JARVIS. 

# Import the required module for text  
# to speech conversion
import pyttsx3
#import speech_recognition as sr
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os



engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-35)


name = input('Enter your name: ')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#def self_intro():
#speak(f'hello{name}, i am a robot. and i can help you for a your better life.......')
speak(f'hallo my name is robot ')
def wishMe(name):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning!{name}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon!{name}")   

    else:
        speak(f"Good Evening!{name}")  

    #engine.say(. Please tell me how may I help you")       


def user(name):
    #name = input("Enter your name: ")
    #input(f'enter any key for continue: {name}')
    speak(f'how was your day to day!{name}') 
    resp = input("good, fine, okay:" )
    for i in ["good","fine","okay"]:
        if i in resp:
            speak(f"That's good to know, {name}.")
            print(f"That's good to know, {name}.")

def finder():
    find = input('copy and paste\n*open youtube\n*open google:  ')
    return find


if __name__ == "__main__": 
    #self_intro()
    while True:
        wishMe(name)
        user(name)
        #engine.runAndWait()
        while True: 
            find = finder().lower()
            if 'open youtube' in find: 
                x = 0
                while True:
                    hey = x = x +1
                    serach = input(f"{hey}->serach youtube: ")
                    find = webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={serach}")
                    #webbrowser.open(find)
                    quit = input("quit for type-> q : ")
                    if quit=="q": 
                        break
            elif 'google' in find:
                x =0
                while True:
                    hey = x = x + 1
                    find = input(f"{hey}->serach Google or type of url: ")
                    webbrowser.open_new_tab(find)
                    quit = input('quit for type-> q : ')
                    if quit == "q":
                        break    
            elif 'stackoverflow' in find:
                webbrowser.open_new_tab("stackoverflow.com")
            elif 'time' in find:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
