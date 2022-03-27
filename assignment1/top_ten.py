import operator
import sys
import json

file = open(sys.argv[1], "r")  # open file stream twiter
encode = file.readlines()
frequency_htags = {}
n = 0  # number of hastags in tweets

for line in encode:
    tweet = json.loads(line)
    if 'text' in tweet.keys():
        hashtags = tweet['entities']['hashtags']
        for h in hashtags:
            if h['text'] not in frequency_htags.keys():
                frequency_htags[h['text']] = 1
            else:
                frequency_htags[h['text']] += 1
            n += 1
sort_dict = sorted(frequency_htags.items(), key=operator.itemgetter(1),reverse=True)[:10]
for (hash, freq) in sort_dict:
    print("{} {:f}".format(hash, freq))
file.close()
