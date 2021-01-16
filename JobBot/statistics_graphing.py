
import parse
import nltk
import patterns
from parse import Words_Phrases
from patterns import Pattern_Manager

patterns_manager = Pattern_Manager()


class Stats_Graph_Manager:
    def __init__(self):
        # keys represent a percentage ex. 1-10 equals 1% to 10%
        self.similarityScoreRanges = {"1-10":[],"10-20":[],"30-40":[],"40-50":[],
        "50-60":[],"60-70":[],"70-80":[],"80-90":[],"90-100"}

        self.AP=self.bucketPhrases(patterns_manager.AP_nC2_scores,self.similarityScoreRanges)
        self.NP=self.bucketPhrases(patterns_manager.NP_nC2_scores,self.similarityScoreRanges)
        self.VP=.self.bucketPhrases(patterns_manager.VP_nC2_scores,self.similarityScoreRanges)



    # since similar phrases have been sorted based on similarity
    #  this just assigns to buckets based on percentage... bound to be duplicates
    #  this can be adressed when actuallu graphing 
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
        

def graph(self):

    #still thinking about what would be the best way to do so

    # Strategy for no
    pass
        





