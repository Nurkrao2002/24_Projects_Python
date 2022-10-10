from textblob import TextBlob
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import nltk
nltk.download()
import re
import numpy as np

file=open('Pride and Prejudice by Jane Austen.txt' ,encoding="utf-8-sig"); 
t=file.read();
t = t.replace('“', ''); 
t = t.replace('”', '');
t = t.replace('_', ''); 
matches = re.findall('Chapter '+'\d{1,2}\s', t) 
print(matches)
for match in matches:
    t = re.sub(match, match.replace('\n','.'), t)
 
t = t.replace('\n', ' '); 
blob = TextBlob(t) 

df=pd.DataFrame(columns=['Sentence', 'Tags','Polarity','Subjectivity','Number of Words','Number of Nouns','Number of Verbs','Number of Adjectives'])
sentencecount=0 #Counter for sentences
totalwords={} #Empty dictionary for keeping track of unique words
propernouns={} #Empty dictionary for keeping track of unique proper nouns
 
#Cycling through all the sentences in the text file
for sentence in blob.sentences:
    #Counters for nouns, verbs, and adjectives in current sentence
    nouns=0
    verbs=0
    adjectives=0
 
    #Printing pertinent information
    print('-------------------------------------------------New Sentence-------------------------------------------------')
    print(sentencecount)
    print(sentence) #Current sentence
    print(sentence.sentiment.polarity) #Current sentence polarity
    print(sentence.sentiment.subjectivity) #Current sentence subjectivity
    print(sentence.tags) #Current sentence words and their part of speech (POS) tag
 
    #Entering data into dataframe
    df.at[sentencecount, 'Sentence']= str(sentence)
    df.at[sentencecount, 'Tags'] = str(sentence.tags)
    df.at[sentencecount, 'Polarity'] = sentence.sentiment.polarity
    df.at[sentencecount, 'Subjectivity'] = sentence.sentiment.subjectivity
    df.at[sentencecount, 'Number of Words'] = len(sentence.words)
 
    #Cycling through every word in current sentence
    for word in sentence.tags:
 
        #Checks if current word is in the unique word dictionary
        if word not in totalwords: #If not, adds it to unique word dictonary with value of 1 (first appearance)
            totalwords[word] = 1
        else: #If it is, adds 1 to its value for subsequent appearances
            totalwords[word] += 1
 
        #List of tags https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
 
        if word[1] == 'NNP': #Checks if current word is proper noun so it can add it to the proper noun dictionary
            if word not in propernouns:
                propernouns[word] = 1
            else:
                propernouns[word] += 1
 
        #Cheks if current word is a noun, verb, or adjective so it can add to the corresponding count
        if word[1]=='NN' or word[1]=='NNS':
            nouns+=1
        if word[1] == 'VB' or word[1]=='VBD' or word[1]=='VBG' or word[1]=='VBN' or word[1]=='VBP' or word[1]=='VBZ':
            verbs += 1
        if word[1] == 'JJ' or word[1]=='JJR' or word[1]=='JJS':
            adjectives += 1
 
    #Entering word count data into dataframe
    df.at[sentencecount, 'Number of Nouns'] = nouns
    df.at[sentencecount, 'Number of Verbs'] = verbs
    df.at[sentencecount, 'Number of Adjectives'] = adjectives
 
    #Counter for sentences
    sentencecount+=1

print('------------------------------------------------Text Information------------------------------------------------')
print(df.head())
print('Total Number of Sentences: ',sentencecount)
print('Total Number of Words: ',df['Number of Words'].sum()-61*2) #-61*2 because of 61 chapters and 2 words Chapter and ##
print('Total Number of Nouns: ',df['Number of Nouns'].sum()-61) #-61 because of 61 chapters, chapter is a noun
print('Total Number of Verbs: ',df['Number of Verbs'].sum())
print('Total Number of Adjectives: ',df['Number of Adjectives'].sum())
print('Total Number of Unique Words: ', len(totalwords))
print('Total Number of Unique Proper Nouns: ', len(propernouns))
 
plt.show()