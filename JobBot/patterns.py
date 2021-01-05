import parse
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import indeedBot
import parse
from parse import Words_Phrases
from itertools import combinations 
from difflib import SequenceMatcher



words_phrases = Words_Phrases()

#nltk library used for tagging and chunking words/phrases

# some common tags found here #https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/
# example of chunking #https://pythonprogramming.net/chunking-nltk-tutorial/

#Sample Syntax for nltk chunking regex expressions 

#"NP: {<DT>?<JJ>*<NN>}" 
#r""" N: {<DT|JJ|VBG.*>+} 
#     P: {<IN>}""""

# To keep as simple as possible I have centered on 3-4 
# patterns of types of phrases (this is just for now, may need some revision as time goes forward)

#NP = NounPhrase ex  "Computer Knowledge" then whatever follows after 
#VP = VerbPhrase ex " programming with python and building sustainable systems" then whatever follows after
#NPP = NounPrepPhrase ex # (not implemented yet)
#AP= Adjective Phrase # "good with computers" "skilled at match" then whatever follows after

#basic idea is to use certain tags and slice the rest of the phrase since the entire scraped text is split by sentence 
# this may lead to certain phrases being duplicated but perhaps this can be overcome with some simple caching

#nltk.chunk output looks something like this, output can be tricky to work with since 
#[Tree('S', [Tree('VP', [('creating', 'VBG')]), ('great', 'JJ'), ('big', 'JJ'), ('and', 'CC'), ('projects', 'NNS')])]


class Pattern_Manager:
    def __init__(self):
        self.cache=[]

        self.tokenized_sent = words_phrases.tokenized_by_sentence
        self.extractedNP = getPattern(NounPhrase,self.tokenized_sent,'NP')
        self.extractedVP = getPattern(VerbPhrase,self.tokenized_sent,'VP')
        self.extractedAP = getPattern(AdjPhrase,self.tokenized_sent,'AP')


        self.VP_nC2_scores = similarityScore(phraseCombinations(self.extractedVP))
        self.NP_nC2_scores = similarityScore(phraseCombinations(self.extractedNP))
        self.AP_nC2_scores = similarityScore(phraseCombinations(self.extractedAP))

def parseTree(tree, target):
    from nltk import Tree
    string = []
    targetFound = False
    for i in range(len(tree)):
        child = tree[i]
        if isinstance(child,Tree) and child.label()==target:
            targetFound = not targetFound
            for j in range(len(child)):
                string.append(child[j][0])
        else:
            string.append(child[0])
    
    return "".join(string) if targetFound else None
    
            
def getPattern(sentences,pattern,phrase_type):
    phrases = []
    for sent in sentences:
        chunkedPhrase=nltk.RegexpParser(pattern)
        tree=chunkedPhrase.parse(sent)
        string=parseTree(tree,phrase_type) 
        if string is None:
            continue
        phrases.append(string)
    return phrases


# n C 2 combinations where n equal number of phrases
def phraseCombinations(phrases):
    Combinations = combinations(phrases, 2) 
    output = []
    for combo in list(Combinations):
        output.append(combo)
    return output
    
def similarityScore(pairCombo):
    scores = []
    for combo in pairCombo: # sequence matcher func is inbuilt
        score =  SequenceMatcher(None, combo[0], combo[1]).ratio()
        scores.append((combo[0],combo[1],score))
    return scores.sort(key=lambda ele: ele[2])




VerbPhrase = r"""
VP: {<VB|VBD|VBG|VBN|VBP|VBZ*>+} 
"""

AdjPhrase = r""" 
ADJ: {<JJ|JJR|JJS><IN|TO>+} 
"""

NounPhrase = r""" 
NP: {<NN|NNS|NNP|NNPS><NN|NNS|NNP|NNPS>+} 
"""

NounPrepPhrase = r""" 
NPP: {<NN|NNS|NNP|NNPS><IN|TO>+} 
"""
