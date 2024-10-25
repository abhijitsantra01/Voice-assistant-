import pyttsx3
engine = pyttsx3.init() 

""" RATE"""
rate = engine.getProperty('rate')   
# print (rate)                       
engine.setProperty('rate', 115)     


"""VOLUME"""
volume = engine.getProperty('volume')   
# print (volume)                         
engine.setProperty('volume',0.85)   

"""VOICE"""
voices = engine.getProperty('voices')      
#engine.setProperty('voice', voices[0].id)  
engine.setProperty('voice', voices[1].id)   

engine.say("Hello babu")
engine.say('My current speaking rate is ')
engine.runAndWait()
engine.stop()
