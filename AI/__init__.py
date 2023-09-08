import os
import threading
import json
import nltk

try:
    import train
    from colorprint import ColorPrint as _
    import colorprint as __
except ModuleNotFoundError:
    from AI.train import Training
    from AI.colorprint import ColorPrint as _
    import AI.colorprint as __

if not os.path.exists("intents.json"):
            f = open("intents.json","w")
            f.writelines("""
{"intents": [
    {"tag": "greeting",
        "patterns": ["Hi there", "How are you", "Is anyone there?","Hey","Hola", "Hello", "Good day"],
        "responses": ["Hello", "Good to see you again", "Hi there, how can I help?"],
        "context": [""]
    },
    {"tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time"],
        "responses": ["See you!", "Have a nice day", "Bye! Come back again soon."],
        "context": [""]
    },
    {"tag": "thanks",
        "patterns": ["Thanks", "Thank you", "That's helpful", "Awesome, thanks", "Thanks for helping me"],
        "responses": ["My pleasure", "You're Welcome"],
        "context": [""]
    },
    {"tag": "query",
        "patterns": ["What is RealViper?"],
        "responses": ["RealViper is a YT Channel"],
        "context": [""]
    } 
]}""")
f.close()

if not os.path.exists("chatbot_model.h5"):
    if __name__ == "__main__":
        train.Training()
    else: Training()

awake = False
class Initialize:
    def __init__(self, wake : bool | None=False) -> None:
        self.wake = wake

    def Awake(self):
        while self.wake == True:
            _.print_info("[Info]",""); print(" Loading AI")
            T = threading.Thread(target=Initialize.Start, args=(self,3,))
            T.start()
            nltk.download('punkt')
            nltk.download('wordnet')
            T.join()
        if self.wake == False:
            _.print_colour("[-]","green",""); print(" Function get and set loaded !")
    
    def Done(self):
        self.wake = False
        _.print_colour("[+]","blue",""); print(" Finishing")
        
    @classmethod
    def Start(cls, self, time : int | str | None=3):
        #os.system("timeout "+str(time)+" > nul")
        cls.Done(self)
        
class Init(Initialize):
    def __init__(self, wake : bool | None = awake) -> None:
        super().__init__(wake)

if awake == False:
    Init(wake = True).Awake()
