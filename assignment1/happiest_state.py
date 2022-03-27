import operator
import sys
import json


def getwordscore(word, dictscores):
    if word in dictscores.keys():
        return dictscores[word]
    return 0


def main():
    afinnfile = open(sys.argv[1],"r")
    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    file = open(sys.argv[2], "r")
    encode = file.readlines()
    dict_state = {}
    for line in encode:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            score = 0
            place = tweet['place']
            texte = tweet['text'].split(" ")
            for word in texte:
                score += getwordscore(word, scores)
            if place is not None:
                if place['country_code'] not in dict_state.keys():
                    dict_state[place['country_code']] = score
                else:
                    dict_state[place['country_code']] += score
    print(sorted(dict_state.items(), key=operator.itemgetter(1), reverse=True)[:1][0][0])

    file.close()


if __name__ == '__main__':
    main()
