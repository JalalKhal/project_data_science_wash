import MapReduce
import sys

mr=MapReduce.MapReduce() #mapReduce object

def hash(p1,p2):
    hash=0
    for c in p1:
        hash+=ord(c)
    for c in p2:
        hash+=ord(c)
    return hash
def mapper(record):#function mapper
    mr.emit_intermediate(hash(record[0],record[1]),record)


def reducer(key,iterator_values):#function reducer
    cpt=0# boolean flag
    for (i1,i2) in iterator_values:
        for (j1,j2) in iterator_values:
            if i1==j2 and i2==j1: #two cases: if i1 is one of i2's friends cpt=1 else cpt stay equal to 0
                cpt=1
        if cpt==0:#cpt==0 means that i2 is a one i1's friends but the reciprocal is false, that's ok
            mr.emit((i2,i1))
            mr.emit((i1,i2))




inputdata=open(sys.argv[1])
mr.execute(inputdata,mapper,reducer)



