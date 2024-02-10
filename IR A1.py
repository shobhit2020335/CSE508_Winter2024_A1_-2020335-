#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[9]:


#Q1

import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')

def process_files(original_folder_path, processedFolder):
    if not os.path.exists(original_folder_path):
        print(f"Error: The folder '{original_folder_path}' does not exist.")
        return
    
    if not os.path.exists(processedFolder):
        os.makedirs(processedFolder)

    
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)

   
    files_processed = 0

   
    printCount = 0

  
    processedTokens = {}

    
    for filename in os.listdir(original_folder_path):
        
        if filename.endswith(".txt"):
            originalFolder = os.path.join(original_folder_path, filename)
            processed_file_path = os.path.join(processedFolder, filename)

            with open(originalFolder, 'r') as file:
                content = file.read()

           
            content = content.lower()

            
            tokens = word_tokenize(content)

            
            tokens = [token for token in tokens if token not in stop_words]

           
            tokens = [''.join(char for char in token if char not in punctuation) for token in tokens]

           
            tokens = [token for token in tokens if token.strip()]

           
            processedTokens[filename] = tokens

            if printCount < 5:
                print(f"Original content of {filename} before processing:")
                print(content)
                print()
                print(f"Processed content of {filename} after processing:")
                print(" ".join(tokens))
                print()
                printCount += 1

           
            with open(processed_file_path, 'w') as file:
                file.write(" ".join(tokens))

            files_processed += 1

    return processedTokens




# In[10]:


#Q2

import os
import pickle

def read_processed_files(processedFolder):
    processedTokens = {}
    for filename in os.listdir(processedFolder):

        if filename.endswith(".txt"):
            file_path = os.path.join(processedFolder, filename)

            with open(file_path, 'r') as file:
                content = file.read()

            tokens = content.split()

            processedTokens[filename] = tokens
    return processedTokens

def create_iIndex(processedTokens):
    iIndex = {}

    for filename, tokens in processedTokens.items():

        for token in tokens:
            if token not in iIndex:
                iIndex[token] = [filename]
            else:
                if filename not in iIndex[token]:
                    iIndex[token].append(filename)
    return iIndex

def save_iIndex(iIndex, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(iIndex, file)

def load_iIndex(file_path):
    with open(file_path, 'rb') as file:
        iIndex = pickle.load(file)
    return iIndex


# In[11]:


#Q3

def create_pIndex(processedFolder):
    pIndex = {}

    for filename in os.listdir(processedFolder):

        if filename.endswith(".txt"):
            file_path = os.path.join(processedFolder, filename)

            with open(file_path, 'r') as file:
                content = file.read()

            tokens = word_tokenize(content)

            unique_tokens = list(set(tokens))
            token_positions = {token: [i for i, t in enumerate(tokens) if t == token] for token in unique_tokens}

            for token, positions in token_positions.items():
                if token not in pIndex:
                    pIndex[token] = {filename: positions}
                else:
                    if filename not in pIndex[token]:
                        pIndex[token][filename] = positions
                    else:
                        pIndex[token][filename].extend(positions)
    return pIndex

def save_pIndex(pIndex, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(pIndex, file)

def load_pIndex(file_path):
    with open(file_path, 'rb') as file:
        pIndex = pickle.load(file)
    return pIndex


# In[12]:


#RUN ALL 

processedFolder = "C:\\Users\\SHOBHIT\\Downloads\\irdatasetsA1Processed"
iIndexFile ="C:\\Users\\SHOBHIT\\Downloads\\iIndex.pickle" 
pIndexFile ="C:\\Users\\SHOBHIT\\Downloads\\pos_index.pickle" 

processedTokens = read_processed_files(processedFolder)

iIndex = create_iIndex(processedTokens)

save_iIndex(iIndex, iIndexFile)

loaded_iIndex = load_iIndex(iIndexFile)

print("Inverted Index:")
for key, value in loaded_iIndex.items():
    print(f"{key}: {value}")

pos_index = create_pIndex(processedFolder)
save_pIndex(pos_index, iIndexFile)
loaded_pos_index = load_pIndex(iIndexFile)
print("Positional Index:")
for key, value in loaded_pos_index.items():
    print(f"{key}: {value}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




