
import parse
import nltk
import patterns
from parse import Words_Phrases
from patterns import Pattern_Manager

patterns_manager = Pattern_Manager()

#looking out for four main Phrase Types
 #VP : Verb Phrase  

#  possible sub-types of a "VP" phrase
                              #examples          Verb                                 Noun
#  1) has  noun following it somewhere after  |  "building,re-usable and maintainable code" 

VerbPhraseNoun = r"""
VP: {<VB|VBD|VBG|VBN|VBP|VBZ|CVB*>+} 
N: {<NN|NNS|NNP|NNPS>+}      #program computers
"""


#                                            
#                                                Verb         Verb          Verb
#  2) verbs following verbs  aka ("verb run") | "programming, creating, and scaling "
#                           
#                          Verb          Verb          Verb            Noun
#  3) verb run -> noun  |  "programming, creating, and scaling large projects"
#                                                        VP
#  4)  ending as a verb  |   "blah blah blah .... team building"


 #APP : Adjective Prepositional Phrases

#   examples
#   "good at"   | "skilled in " | "experienced with" | 
# 
#   *should be followed by one or more nouns some point after

AdjPhrase = r""" 
ADJ: {<JJ|JJR|JJS><IN|TO>+} 
N: {<NN|NNS|NNP|NNPS>+} 
"""

# NPP : Noun Prep Phrase
# examples

# "knowledge of" | "comfortable with" | "ability to "| "aptitude for"
#   *should be followed by one or more nouns some point after


NounPrepPhrase = r""" 
NPP: {<NN|NNS|NNP|NNPS><IN|TO>+} 
N: {<NN|NNS|NNP|NNPS>+}
"""


# NN : Noun Noun
#     "computer science knowledge"

phraseStructure = {"VP":{1:[],2:[],3:[],4:[]},"APP":[],"NPP":[],"NN":[]}

class Similarity_Analyzer:
    def __init__(self):
        # keys represent a percentage ex. 1-10 equals 1% to 10%
        self.similarityScoreRanges = {"1-10":[],"10-20":[],"30-40":[],"40-50":[],
        "50-60":[],"60-70":[],"70-80":[],"80-90":[],"90-100"}

        self.APP=self.bucketPhrases(patterns_manager.AP_nC2_scores,self.similarityScoreRanges)
        self.NP=self.bucketPhrases(patterns_manager.NP_nC2_scores,self.similarityScoreRanges)
        self.VP=self.bucketPhrases(patterns_manager.VP_nC2_scores,self.similarityScoreRanges)


    # since similar phrases have been sorted based on similarity
    #  this just assigns to buckets based on percentage... bound to be duplicates
    #  this can be adressed when actually graphing 
    def bucketPhrases(self,phrases,scoreBuckets):
        table = scoreBuckets
        for pair in phrases:
            score = pair[2] * 100
            key = self.getKey(score)
            table[key].append(pair[0])
            table[key].append(pair[1])
        return table

    # just a function to get a key for the respective hash table
    def getKey(self,num):
        if num<=10:
            return "1-10"
        ten = num % 10
        temp = (ten*10,(ten*10)+10)
        return str(temp[0])+"-"+str(temp[1])

    def groupByMeaning(self,bucketedPhrases,phraseType): #POP = part of phrase - ex. VB... use this 
                                                         # to group phrases even furthrt
        POPtable = {}
        for key in  bucketedPhrases:
            phrases = bucketedPhrases[key]
            for phrase in phrases:
                self.tagPhraseStruct(phrase)


   def hasNoun(self,phrase):
        Noun = r"""
        N: {<NN|NNS|NNP|NNPS>+} 
        """
        tree=patterns.chunker(Noun,phrase)
        parsed = patterns.parseTree(tree,"N")
        return True if parsed is not None else False
    
    
    def isVerbRun(self,phrase):
        VerbPhrase = r"""
        ING: {<VBG|CVB*>+} """
        tree=patterns.chunker(VerbPhrase,phrase)
        from nltk import Tree
        lenING = 0
        numING = 0
        for i in range(len(tree)):
            child = tree[i]
            if isinstance(child,Tree) and child.label()=="ING":
                lenING = max(lenING,len(child)
                numING += 1
        return True if lenING >=2 or numING >=2 else False

    def tagPhraseStruct(self,phrase,phraseType):

        if phraseType == "VP":
            if not self.isVerbRun(phrase) and self.hasNoun(phrase):
                phraseStructure["VP"][1].append(phrase)
                return
            if self.isVerbRun(phrase):
                phraseStructure["VP"][2].append(phrase)
                return
            if self.isVerbRun(phrase) and self.hasNoun(phrase):
                phraseStructure["VP"][3].append(phrase)
                return
            #if ends_as_verb:
                #pass

        elif phraseType == "APP":
            if self.hasNoun(phrase):
                phraseStructure["APP"].append(phrase)
                return
        elif phraseType == "NPP":
            if self.hasNoun(phrase):
                phraseStructure["NPP"].append(phrase)
                return
                
        elif phraseType == "NN":
            if self.Noun_Noun(phrase):
                phraseStructure["NN"].append(phrase)
                return

