import spacy
from spacy.lang.en.stop_words import  STOP_WORDS
from string import punctuation
import en_core_web_sm
import indeedBot
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import wikipedia
import re

#jobs = indeedBot.traverse()

class Words_Phrases:
    def __init__(self,jobs):
        self.jobs = jobs # Raw Input of all the jobs
        self.jobs_str = "".join(self.jobs)
        self.tokens = tokenize(self.jobs_str)
        self.lowercase_tokens = [token.lower() for token in tokens]
        self.tokenized_by_sentence = tokenize_sentences(self.jobs_str)

        self.taggedWords = [classify(token) for token in self.lowercase_tokens]

        self.tokenFrequency = getFrequency(self.lowercase_tokens)
        self.bigrams,self.trigrams = None, None

        self.keywords = None
        self.phrases = None
        self.similarPhrases = None
        self.frequencyOfKeywords = None
        self.frequencyOfSimilarPhrases = {}
    





def tokenize(string):
    nlp = en_core_web_sm.load()
    doc = nlp(string)
    punctuation = {"\n","\n\n",":","/",",",".",")","(","-",'”'} 
    tokens = [token.text for token in doc]
    #stop_set = {word: True for word in list(STOP_WORDS)}

    newTokens =[]
    for char in tokens:
        if char in punctuation:
            continue
        newTokens.append(char)
    return newTokens

def tokenize_sentences(string): #tokenizes and tags by sentence,
    custom_sent_tokenizer = PunktSentenceTokenizer(string)
    tokenized = custom_sent_tokenizer.tokenize(string)
    new = []
    for sentence in tokenized:
        tagged = []
        sent = re.split("' '|\n|\n\n|/|,|'”'|(|)|:",sentence)
        for word in sent:
            tagged.append(classifyWord(word))
        
        new.append(tagged)


            
    return  new



def getFrequency(words):
    table={}
    for word in words:
        if token not in table:
            table[word]=1
        else:
            table[word]+=1
    return table


def get_Bi_Tri_grams(string):
    return (nltk.bigrams(string),nltk.trigrams(string))


def getPhrases(String,pattern):
    pass

def getSimilarPhrases(phrases):
    pass




def classifyWord(token):
    
    word = nltk.word_tokenize(token)
    tagged = nltk.pos_tag(word)
    if tagged[0][0] == tagged[0][1]:
        tagged[0][1] = "UNTAG"
                                      # Reason for this if statement is because 
                                      # # nltk.pos_tag  #returns a 2-D array in the form of  ["cat",
    return tagged










        
        




    























