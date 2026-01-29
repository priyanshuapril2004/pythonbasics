sentence=(input("Enter the sentence "))
word= sentence.spilt()
freq={}
for words in word:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
s_freq=dict()        
