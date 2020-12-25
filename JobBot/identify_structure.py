
import parse
from parse import Parse_Manager

parse = Parse_Manager()






def identifyVerb(text,verbs):
    phrases = []
    for i,token in enumerate(text):
        if token in verbs:
            phrase=expandFrom(i,text)
            phrases.append((verbs[token],phrase))
            
    return phrases




def expandFrom(idx,text):
    phrase = []
    for i in range(idx,len(text)):
        char = text[i]
        phrase.append(char)
        if char == ".":
            break
    return phrase

            










