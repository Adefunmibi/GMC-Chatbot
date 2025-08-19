#!/usr/bin/env python
# coding: utf-8

#import necessary libraries
import nltk
nltk.download('punkt')
nltk.download("averaged_perceptron_tagger")
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
import string
nltk.download('wordnet')
nltk.download('punkt_tab')
import streamlit as st


#Load the text file and preposess the data
with open (r'C:\Users\CORONA\Desktop\Deployment\Tobacco_leaves.txt',encoding='utf-8') as f:
    data=f.read().replace('\n',' ')


#Break the data text into sentences
sent_tokenize(data)

#Get the first sentence
# sent_tokenize(data)[0]

#Tokenize text into sentences
sentences=sent_tokenize(data)


#Define a function to process each sentence
def preprocess(sentence):
    #Tokenize the sentence to word
    words=word_tokenize(sentence)
    #Remove stopwords and punctuation
    words=[word.lower() for word in words if word.lower()\
           not in stopwords.words("english") and word not in string.punctuation]
    #Lemmatizer the words
    lemmatizer=WordNetLemmatizer()
    words=[lemmatizer.lemmatize(word) for word in words]

    return words



corpus=[preprocess(sentence) for sentence in sentences]


#Define the function to get the most relevant sentence in a given query
def get_most_relevant_sentence(query):
    #preprcess the query

    query=preprocess(query)
    #Compute the similarities between the query and each sentence in the text
    max_similarity=0
    most_relevant_sentence=""
    for sentence in corpus:
        similarity=len(set(query).intersection(sentence))/float(len(set(query).union(sentence)))
        if similarity > max_similarity:
            max_similarity=similarity
            most_relevant_sentence=" ".join(sentence)

    return most_relevant_sentence        


def chatbot(question):
    #find most relevant sentence
    most_relevant_sentence=get_most_relevant_sentence(question)
    #return answer
    return most_relevant_sentence



chatbot("History of tobacco")



#Create a streamlit app
def main():
    st.title("Smokers:A delve into Tobacco leaves")
    st.write("Hello! I'm a chatbot.Ask me anything about facts for Smokers.")
    #Get the users question
    question= st.text_input("You:")
    #Create a button to submit the questions

    if st.button("Submit"):
        #Call the chatbot functions with the question and display the response
        response=chatbot(question)
        st.write("Chatbot: " + response)

if __name__ == "__main__":
    main()