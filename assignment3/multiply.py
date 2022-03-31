import MapReduce
import sys

mr=MapReduce.MapReduce()#mapReduce object

def mapper(record):#the mapper function
    if record[0]=='a':
        for k in range(5):
            mr.emit_intermediate((record[1],k),record)
    if record[0]=='b':
        for k in range(5):
            mr.emit_intermediate((k,record[2]),record)

def reducer(intermediate_key,iterator_values):#the reducer function
    (i,k)=intermediate_key
    dicta={}# aij for j
    dictb={}#blk for l
    sum=0#it's (a*b)(i,k)
    for (matrix,l,j,value) in iterator_values:
        if matrix=='a':
            dicta[(l,j)]=value
        if matrix=='b':
            dictb[(l,j)]=value
    for p in range(5):
        if (i,p) in dicta.keys() and (p,k) in dictb.keys():
            sum+=dicta[(i,p)]*dictb[(p,k)]#value=dot product of dicta and dictb
    mr.emit((i, k,sum))#print the result


inputdata=open(sys.argv[1])#load data
mr.execute(inputdata,mapper,reducer)#execution