
import parse
import patterns
import indeedBot
from parse import Words_Phrases
from patterns import Pattern_Manager
import groupBySimilarities 
from groupBySimilarities import Similarity_Analyzer

class NLP_Manager:

    def __init__(self):
        self.words_phrases = Words_Phrases()
        self.pattern_manager = Pattern_Manager()
        self.similarity_analyzer = Similarity_Analyzer()
        self.allPhrases = similarity_analyzer.getAllPhrases()
        #self.jobs = indeedBot.traverse(#jobTitle,#location)
    
    
    def relevantPhrases(self,allPhrase):
        seen = {}
        StatisticallyRelevantPhrases = []
        for phrase in allPhrase:
            if seen[phrase]:
                continue
            if phrase not in seen:
                seen[phrase] = True
            StatisticallyRelevantPhrases.append(phrase)
        return StatisticallyRelevantPhrases

        

            


            

    
    # def RelevantPhrases(self,allPhrases):
    #     seen = {}
    #     StatisticallyRelevantPhrases = []
    #     for phrase in allPhrases:
    #         if seen[phrase]:
    #             continue
    #         if phrase not in seen:
    #             seen[phrase] = True
    #         StatisticallyRelevantPhrases.append(phrase)
    #     return StatisticallyRelevantPhrases




    





        
        



# this file will act as the modularized object that will acess and control all NLP functions 
# and tasks on a high level for the overall project














#stopwords = list(STOP_WORDS)

#jobDescList=indeedBot.traverse()

#nlp = en_core_web_sm.load()

#doc = nlp(jobDescList) # need to iterate