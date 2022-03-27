import sys
import json
import re

file = open(sys.argv[1], "r")  # open file stream twiter
encode = file.readlines()
frequency = {}
n = 0  # number of word in tweet in which have splitted by " "

for line in encode:
    tweet = json.loads(line)
    if 'text' in tweet.keys():
        texts = tweet['text'].split(" ")
        for word in texts:
            if len(list(re.findall("^[a-zA-Z0-9]", word))) != 0 and word.startswith(
                    'http') != True and word.startswith('#') != True:
                if word not in frequency.keys():
                    frequency[word] = 1
                else:
                    frequency[word] += 1
                n += 1
for line in encode:
    tweet = json.loads(line)
    if 'text' in tweet.keys():
        texts = tweet['text'].split(" ")
        for word in texts:
            if len(list(re.findall("^[a-zA-Z0-9]", word))) != 0 and word.startswith(
                    'http') != True and word.startswith('#') != True:
                print("{} {:.3f}".format(word, frequency[word] / n))

file.close()
