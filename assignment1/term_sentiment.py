import sys
import json

def lines(fp):
    print(str(len(fp.readlines())))

def getwordscore(sentence,word,dictscores):
    #sentence is a list which have the words of the sentence
    keys=dictscores.keys()
    if word in keys:
        return dictscores[word]
    len=0
    for w in sentence:
        if w in keys:
            if dictscores[w]>=0:
                len+=1
            else:
                len-=1

    return len






def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.


    encode = tweet_file.readlines()
    dict_ncarry={}

    for line in encode:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            texts = tweet['text'].split(" ")
            for word in texts:
                dict_ncarry[word]=getwordscore(texts,word,scores)
                print("{} {:f}".format(word,dict_ncarry[word]))
    tweet_file.close()
    sent_file.close()


if __name__ == '__main__':
    main()
