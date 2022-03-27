import sys
import json


def hw():
    print('Hello, world!')


def lines(fp):
    print(str(len(fp.readlines())))


def getwordscore(word, dictscores):
    if word in dictscores.keys():
        return dictscores[word]
    return 0


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    encode = tweet_file.readlines()
    scores_tw = []

    for line in encode:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            score = 0
            texte = tweet['text'].split(" ")
            for word in texte:
                score += getwordscore(word, scores)
            scores_tw.append(score)
            print(score)
    tweet_file.close()
    sent_file.close()


if __name__ == '__main__':
    main()
