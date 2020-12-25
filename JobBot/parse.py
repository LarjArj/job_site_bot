import spacy
from spacy.lang.en.stop_words import  STOP_WORDS
from string import punctuation
import en_core_web_sm
import indeedBot
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


class Parse_Manager:

    def __init__(self):
        ##Handles formatting scraped  information from job postings
        self.info= Info()
        self.jobs = indeedBot.traverse()
        self.bigJobStr=jobInfo_2_Str(jobs)

        self.tokens_as_is=self.tokenize(self.bigJobStr,self.info,"NO PUNCT")
        self.tokens_lowercase=[token.lower() for token in self.tokens_as_is]
        self.tokens_w_punct_as_is=self.tokenize(self.bigJobStr,self.info,"PERIOD/COMMA")
        self.tokens_w_punct_lowercase=[token.lower() for token in self.tokens_w_punct_as_is]

        self.bigrams=list(nltk.bigrams(self.tokens_lowercase))
        self.trigrams=list(nltk.trigrams(self.tokens_lowercase))
        self.frequentWords=getFrequencyTable(tokens_lowercase)


        self.taggedWords = self.classifyWord(self.tokens_w_punct_lowercase,self.info)


        self.nouns=self.groupPartsOfSpeech(self.taggedWords,self.info.noun_tags)
        self.verbs=self.groupPartsOfSpeech(self.taggedWords,self.info.verb_tags)
        self.adjectives=self.groupPartsOfSpeech(self.taggedWords,self.info.adj_tags)
        self.prepositions=self.groupPartsOfSpeech(self.taggedWords,self.info.prepositional_tags)
    
    
    def jobInfo_2_Str(self,jobs):
        output=[]
        for job in jobs:
            output.append(jobs)
        return "".join(output)


    def tokenize(self,string,info,punct_type):
        nlp = en_core_web_sm.load()
        doc = nlp(bigText)
        punctuation=info.punctuation if punct_type == "NO PUNCT" else info.punct_except_period_comma
        tokens = [token.text for token in doc]
        newTokens =[]
        for char in tokens:
            if char in self.unwanted or char in self.punctuation:
                pass   
            newTokens.append(char)
        return newTokens

    
    def getFrequencyTable(self,words):
        Hash={}
        for word in words:
            if token not in Hash:
                Hash[word]=1
            else:
                Hash[word]+=1
        return Hash

    def classifyWord(self,word,info):
        taggedWords=[]
        tokens = self.tokens_lowercase
        for token in tokens:
            #if token not in info.unwanted:
            word = nltk.word_tokenize(newWord)
            tagged = nltk.pos_tag(word)
            taggedWords.append(tagged[0])

        return taggedWords

    #Verbs, Adjectives, Prepositions, Nounds
    def groupPartsOfSpeech(self,taggedWords,tags):
        group={}
        for i,word in enumerate(taggedWords):
            if word[1] in tags:
                group[word[0]] = word[1]
        return groups


    def bulletPointDescFields(self):
        pass
        


class Info:

    def __init__(self):
    
        self.stop_words = list(STOP_WORDS) + unwanted
        self.punctuation = {"\n","\n\n",":","/",",",".",")","(","-",'”'} 
        self.punct_except_period_comma = {"\n","\n\n",":","/",")","(","-",'”'}

        self.unwanted = {"details","equal","opportunity","employer",'does','not','discriminate','against','applicants',
            'race','religion','color','disability','medical','condition','legally',
            'protected','genetic','information','national','origin','gender','sexual','orientation','marital','gender','identity',,
            'sex','pregnancy','childbirth','related','medical','conditions','age',
            'veteran','status','legally','protected','characteristics','applicant','with',
            'mental','physical','disability'}

        self.verb_tags = set("VB","VBD","VBN","VBP","VBZ")
        self.adj_tags = set("JJ")
        self.noun_tags = set("NN","NNS","NNPS")
        self.prepositional_tags = set("TO","IN")

    




 







        
    