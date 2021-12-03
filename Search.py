#!/usr/bin/env python
# coding: utf-8

# In[16]:


import json
import ast
data_file = open("inv_index_data_10000.json", "r")
data_from_file = data_file.read()
data_file.close()
dictionary = ast.literal_eval(data_from_file)


def standart(searc):
    lst = searc.replace('\n', '')
    lst = list(lst)
    marks = '''!()-[]{};?@#$%:'"\,./^&;*_'''

    for i in range(len(lst)):
        if lst[i] in marks:
            lst[i] = " ";
    # Удаление всех знаков препинания
    lst = ''.join(lst).lower().split("  ")

    it = 0;
    while it != len(lst):
        lst[it] = lst[it].split(" ")
        it=it+1

    flat_list = []
    for sublist in lst:
        for item in sublist:
            flat_list.append(item)

    while True:
        try:
            flat_list.remove('')
        except:
            break
    return(flat_list)


search = standart(input('Введите запрос:'))


for key in dictionary.keys():
    for word in search:
        wordlist = list(word)
        keylist = list(key)
        [i for i in keylist if not i in wordlist or wordlist.remove(i)]
        
        marks = '''!()-[]{};?@#$%:'"\,./^&;*_'''
        wordstr = str(wordlist)
        
        for x in wordstr:  
            if x in marks:  
                wordstr = wordstr.replace(x, "")
        
        
        wordlist_r = list(word)
        keylist_r = list(key)
        [i for i in wordlist_r if not i in keylist_r or keylist_r.remove(i)]
        
        wordstr_r = str(keylist_r)
        
        for x in wordstr_r:  
            if x in marks:  
                wordstr_r = wordstr_r.replace(x, "")
        
        if (len(wordstr) + len(wordstr_r)) <= 2:
            print(dictionary.get(key))
            print(key)
            print(word)


# In[17]:





# In[18]:





# In[40]:





# In[ ]:




