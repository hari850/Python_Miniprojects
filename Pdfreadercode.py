#!/usr/bin/env python
# coding: utf-8

# #  Audiobook

#     Pdf reader

# In[21]:


import pyttsx3 
import PyPDF2


# In[22]:


my_pdf = open('C:\\Users\\admin\\Downloads\\Hands_on_Machine_Learning_with_Scikit_Le.pdf','rb')


# In[37]:


pdfreader = PyPDF2.PdfFileReader(my_pdf)


# In[38]:


pages = pdfreader.numPages


# In[43]:


page = pdfreader.getPage(10)


# In[44]:


speaker = pyttsx3.init()


# In[45]:


text = page.extractText()
    


# In[46]:


speaker.say(text)


# In[48]:


speaker.runAndWait()


# In[ ]:




