import MapReduce
import sys

mr=MapReduce.MapReduce() #mapReduce object


def mapper(record):#function mapper
    mr.emit_intermediate(record[0],1)


def reducer(key,iterator_values):#function reducer
    mr.emit((key,len(iterator_values)))


inputdata=open(sys.argv[1])
mr.execute(inputdata,mapper,reducer)



