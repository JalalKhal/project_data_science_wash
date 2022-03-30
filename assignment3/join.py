import itertools

import MapReduce
import sys
mr=MapReduce.MapReduce() #mapReduce object


def mapper(record):#function mapper
    mr.emit_intermediate(record[1],record)

def reducer(key,iterator_records):#function reducer
    records_orders=[]
    records_lineitem=[]
    for l in iterator_records:
        if l[0]=='order':
            records_orders.append(l)
        if l[0]=='line_item':
            records_lineitem.append(l)
    products=list(itertools.product(records_orders,records_lineitem))
    join=[]
    for (l1,l2) in products:
        mr.emit(l1+l2)


inputdata=open(sys.argv[1])
mr.execute(inputdata,mapper,reducer)#execution







