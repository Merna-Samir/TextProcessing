#!/usr/bin/env python
# coding: utf-8

# # Text Processing

# In[35]:


#pip install nltk


# In[36]:


import nltk
nltk.download('punkt')


# # THE TEXT 

# In[3]:


from nltk.tokenize import sent_tokenize, word_tokenize
example_string = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult. boys"""
example_string 


# # Tokenizing

# In[4]:


sent_tokenize(example_string)


# In[24]:


word_tokenize(example_string)


# # Filtering Stop Words

# In[34]:


nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[7]:



words_in_quote


# In[25]:


words_in_quote = word_tokenize(example_string)
stop_words = set(stopwords.words("english"))
stop_words


# In[30]:


filtered_list = []
for word in words_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
filtered_list = [word for word in words_in_quote if word.casefold() not in stop_words ]
filtered_list


# # Stemming

# In[32]:


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
words = word_tokenize(example_string)
words


# In[16]:


stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
stemmed_words


# In[33]:


from nltk.tokenize import word_tokenize
words_in_sagan_quote = word_tokenize(example_string)
words_in_sagan_quote


# In[19]:


import nltk
nltk.download('averaged_perceptron_tagger')


# In[20]:


nltk.pos_tag(words_in_sagan_quote)

