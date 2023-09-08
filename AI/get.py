import os
import numpy as np
import json
import wikipedia
import random
import pickle 
import nltk

if __name__ == "__main__":
    import train
else: import AI.train
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lemmatizer = WordNetLemmatizer()

try:
    intents = json.loads(open('intents.json').read())
    words = pickle.load(open('words.pkl','rb'))
    classes = pickle.load(open('classes.pkl','rb'))
    model = load_model('chatbot_model.h5')
except:
    train.Training()
    intents = json.loads(open('intents.json').read())
    words = pickle.load(open('words.pkl','rb'))
    classes = pickle.load(open('classes.pkl','rb'))
    model = load_model('chatbot_model.h5')

class Information:
    def clean_up_sentence(sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
        return sentence_words

    def bag_of_words (sentence):
        sentence_words = Information.clean_up_sentence(sentence)
        bag = [0] * len(words)
        for w in sentence_words:
            for i, word in enumerate(words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)

    def predict_class (sentence):
        bow = Information.bag_of_words(sentence)
        res = model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({'intent': classes [r[0]], 'probability': str(r[1])})
        return return_list

    def get_response(intents_list, intents_json):
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice (i['responses'])
                break
        return result
    
    def search(inp) -> str:

        if inp.lower() == 'exit':
            print("Exiting the program.")

        try:
            result = wikipedia.summary(inp, sentences=1)
            return f"According to Wikipedia:\n{result}"
        except wikipedia.exceptions.PageError:
            return "No matching page found on Wikipedia. Please refine your search."
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Ambiguous search term. Please specify your query: {', '.join(e.options)}"
        except wikipedia.exceptions.RedirectError as E:
            return
    def AI(msg : str):
        f = open("save.json","r")
        data = json.loads(f.read())
        f.close()
        count = -1
        responsive_greetings = data["greetings_responsive"]
        responsive_questions = data["questions"]
        for i in data["greetings"]:
            count += 1
            if msg.__contains__(i) or msg.__contains__(str(i).lower()) or msg.__contains__(str(i).replace(" ",",")):
                return responsive_greetings[count]
        for i in data["questions"]:
            if msg.__contains__(i) or  msg.__contains__(str(i).lower()) or msg.__contains__(str(i).replace(" ",",")):
                return responsive_questions[count]
        
class System(Exception):
    def command(cmd : str | list, echo : bool | None=False):
        if echo != True:
            os.system("@echo off")
        if type(cmd) is list:
            for word in cmd:
                os.system(word)
        else:
            if not cmd.isspace() or not cmd == None:
                if "@echo off" in cmd:
                    cmd = cmd.replace("@echo off","")
                    os.system("@echo off &"+cmd)
                if cmd.__contains__("cls") or cmd.__contains__("clear"):
                    os.system("clear" if os.name == "posix" else "cls")
            else:
                raise System("Something unexpected happend !")
    def Console():
        os.system("clear" if os.name == "posix" else "cls")
        while True:
            message = input("AI : ")
            if message.__contains__("search"):
                Information.search(message)
            else:
                ints = Information.predict_class(message)
                res = Information.get_response(ints, intents)
                print(res)

System.Console()