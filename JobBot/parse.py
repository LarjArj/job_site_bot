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

#Jobs = indeedBot.traverse()

class Words_Phrases:
    def __init__(self):
        #self.jobs = Jobs # Raw Input of all the jobs
        #self.jobs_str = "".join(self.jobs)
        #self.tokens = tokenize(self.jobs_str)
        #self.lowercase_tokens = [token.lower() for token in tokens]
        #self.tokenized_by_sentence = tokenize_sentences(self.jobs_str)

        #self.taggedWords = [classify(token) for token in self.lowercase_tokens]

       # self.tokenFrequency = getFrequency(self.lowercase_tokens)
        self.bigrams,self.trigrams = None, None

        self.keywords = None
        self.phrases = None
        self.similarPhrases = None
        self.frequencyOfKeywords = None
        self.frequencyOfSimilarPhrases = {}
    





def tokenize(string):
    nlp = en_core_web_sm.load() # From SpaCy Library
    doc = nlp(string)           # helps tokenize
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
    custom_sent_tokenizer = PunktSentenceTokenizer(string) # From nltk library helps tokenize by sentence
    tokenized = custom_sent_tokenizer.tokenize(string)
    new = []
    for sentence in tokenized:
        tagged = []

        sent = tokenize(sentence)
        ##sent = re.split("' '|\n|\n\n|/|,|\|'”'|(|)|:",sentence)
        for word in sent:

            classified =classifyWord(word)
            if len(classified):
                tagged.append(classified[0])

            if len(tagged) >=14:
                new.append(tagged)
                tagged = []
        
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


def get_Bi_Tri_grams(string): # nltk function splits entire text in pairs of words or triplets
    return (nltk.bigrams(string),nltk.trigrams(string))


def getPhrases(String,pattern):
    pass

def getSimilarPhrases(phrases):
    pass


def classifyWord(token): # nltk use of tokenization and tagging words 
    try:
        word = nltk.word_tokenize(token)
        tagged = nltk.pos_tag(word)
        if tagged[0][0] == tagged[0][1]:
            tagged[0][1] = "UNTAGABLE"
    
        if tagged[0][0].find("ing") != -1:
            tagged[0][1] = "CVB"

    except:
        print("error")                                # Reason for this if statement is because               word - tag
                                      # # nltk.pos_tag  #returns a 2-D array in the form of  [("cat",NN")]
                                     # If tagged array is like both elements in tuple equal each other the
                               # part of speech was not tagged
    return tagged










        
        




    























