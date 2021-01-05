
import parse
import nltk
import indeedBot
from parse import Parse_Manager
from parse import Info

# make use of nltk chunking 


parse_manager = Parse_Manager()
info = Info()


class Patterns:

   # r"""
#NP: {<NN><NN>+}
    #{<ADJ><NN>+}
#"""

    #VB verb, base form take
    #VBD verb, past tense took
    #VBG verb, gerund/present participle taking
    #VBN verb, past participle taken
    #VBP verb, sing. present, non-3d take
   # VBZ verb, 3rd person sing. present takes

    def __init__(self):
        
        self.regEx = r"""NP: {}"""
        self.verb_noun = {"VB":r"""NP: {<VB><NN>}""" ,"VBD":r"""NP: {<VBD><NN>}""",
            "VBG":r"""NP: {<VBG><NN>}""" ,"VBN":r"""NP: {<VBN><NN>}""" ,
            "VBP":r"""NP: {<VBP><NN>}""",
            "VBZ":r"""NP: {<VBZ><NN>}""" }

        #programming,building,working
        self.verb_nouns = {"VB":r"""NP: {<VB><NN>+<NN>}""" ,"VBD":r"""NP: {<VBD><NN>+<NN>}""",
            "VBG":r"""NP: {<VBG><NN>+<NN>}""" ,"VBN":r"""NP: {<VBN><NN>+<NN>}""" ,
            "VBP":r"""NP: {<VBP><NN>+<NN>}""",
            "VBZ":r"""NP: {<VBZ><NN>+<NN>}""" }

        

    p

# use nltk functionality to extract phrases with a certain structure




def chunkPhrases(taggedWords,pattern):
    phrases = []
    chunk = nltk.RegexpParser(pattern)
    phrases.append(chunk.parse(taggedWords))
    return phrases
    

    















    










