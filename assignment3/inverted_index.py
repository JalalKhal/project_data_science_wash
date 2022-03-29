import MapReduce
import sys
mr=MapReduce.MapReduce() #mapReduce object

def mapper(record):#function mapper
    words=record[1].split()
    for word in list(set(words)):
        mr.emit_intermediate(word,record[0])

def reducer(key,iterator_document):#function reducer
    mr.emit((key,iterator_document))

inputdata=open(sys.argv[1])
mr.execute(inputdata,mapper,reducer) #execution
