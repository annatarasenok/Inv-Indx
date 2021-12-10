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

search_results_list = list()

for word in search:
    search_res_temp = list()
    for key in dictionary.keys():
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
        
        if (len(wordstr) + len(wordstr_r)) == 0:
            search_res_temp.extend(list(dictionary.get(key).keys()))
            
    search_results_list.append(search_res_temp)
result = search_results_list[0]
if len(search_results_list) > 1:
    for i in range(len(search_results_list) - 1):
        result = list(set(result) & set(search_results_list[i+1]))
    print(result)
else:
    print(result)
            
