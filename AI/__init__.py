import os
import pyrebase
import threading
import json
import nltk

if __name__ == "__main__":
    from colorprint import ColorPrint as _
    import colorprint as __
else:
    from AI.colorprint import ColorPrint as _
    import AI.colorprint as __

firebase = {
  "apiKey": "AIzaSyC0d4ntBwxyOwjW7_koP5Q1d8bSxLQssL4",
  "authDomain": "servermanager-2db49.firebaseapp.com",
  "databaseURL": "https://servermanager-2db49-default-rtdb.firebaseio.com",
  "projectId": "servermanager-2db49",
  "storageBucket": "servermanager-2db49.appspot.com",
  "messagingSenderId": "108940988457",
  "appId": "1:108940988457:web:83375a492788db8cea4c38",
  "measurementId": "G-JLS6RNSDVV"
}

if not os.path.exists("save.json"):
    f = open("save.json","w")
    f.close()

awake = False
class Initialize:
    def __init__(self, wake : bool | None=False) -> None:
        f = open("save.json","r")
        try: data = json.loads(f.read())
        except: data = None
        f.close()
        self.wake = wake

        if data != None:
            self.learn = data
        else: self.learn = None

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