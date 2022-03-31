import MapReduce
import sys

mr=MapReduce.MapReduce()#mapReduce object

def mapper(record):#the mapper function
    mr.emit_intermediate(record[1][:len(record[1])-10],record[0])


def reducer(intermediate_key,iterator_values):#the reducer function
    mr.emit(intermediate_key)


inputdata=open(sys.argv[1])#load data
mr.execute(inputdata,mapper,reducer)#execution