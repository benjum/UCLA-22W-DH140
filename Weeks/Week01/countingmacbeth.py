import requests
from nltk.tokenize import word_tokenize

target_url = "https://www.gutenberg.org/files/1533/1533-0.txt"
response = requests.get(target_url)
with open('macbeth.txt','w',encoding='utf-8') as f:
    f.write(response.text)
	
document_text = open('macbeth.txt', 'r')
text_string = document_text.read().lower()
text_tokens = word_tokenize(text_string)

frequency = {}
for word in text_tokens:
    count = frequency.get(word,0)
    frequency[word] = count + 1
	
frequency_list = frequency.keys()
for words in frequency_list:
    #print(words, frequency[words])
    if 'macbeth' in words:
        print(words, frequency[words])