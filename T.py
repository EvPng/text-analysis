import sys
import string
import nltk
from nltk.corpus import stopwords
import pandas

texts = ""

def main():

    with open('01.txt', 'r') as f:
        texts = "".join(line.rstrip('\n') for line in f)
    
    texts = texts.lower()
    texts = texts.replace(r'[^\w\s]','')
    stop = stopwords.words('english')
    
    words = texts.split()
    for w in words:
        if w in stop:
            words.remove(w)
        
    print(len(words))
     
    
    print(check('social', words))

    
    freq = pandas.Series(words).value_counts()[:50]
    print(freq)



def check(word, words):
    """Return true if word is in file else false"""
    COUNT = 0
    for elem in words:
        if elem.lower() == word:
            COUNT = COUNT + 1
    return COUNT


if __name__ == "__main__":
    main()

