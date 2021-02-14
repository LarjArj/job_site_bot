
import parse
import nltk
import patterns
import groupBySimilarties
import pytextrank, spacy
import scattertext as st
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 




#generate word cloud
text = "copy_text_from_job_description_in_link_provided_above" # the input of the wordcloud generator
#generate the wordcloud object, set the height and width, set the random_state parameter to ensure
reproducibility of results and set the stopwords parameter so that the irrelevant words such as pronouns are discarded.
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='blue', collocations=False, stopwords = STOPWORDS).generate(text)
# text is the input to the generate() method
#draw the figure
#Set figure size
plt.figure(figsize=(40, 30))
# Display image
plt.imshow(wordcloud) 
# No axis 
plt.axis("off")
plt.show()







    nlp = spacy.load('en')
    convention_df = st.SampleCorpora.ConventionData2012.get_data(
    ).assign(
    parse=lambda df: df.text.apply(nlp),
    party=lambda df: df.party.apply(
        {#'democrat': #'Democratic', 
         #'republican': '#Republican'}.get
    )
)
corpus = st.CorpusFromParsedDocuments(
    convention_df,
    category_col='party',
    parsed_col='parse',
    feats_from_spacy_doc=st.PyTextRankPhrases()
).build(
).compact(
    st.AssociationCompactor(2000, use_non_text_features=True)

class Stats_Graph_Manager:
    def __init__(self):
        pass
 
        

def graph(self):

    #still thinking about what would be the best way to do so

    # Strategy for no
    pass
        




class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }




