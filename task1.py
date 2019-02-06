def read_csv(fout):
    datalist=[]
    fout.readline()
    for line in fout:
        line=line.strip()
        datalist.append(line.split(','))

    return datalist

def fetch_tuple(datalist):
    #fetching the tuple
    tuple_list=[]
    for data in datalist:
        tup=(data[2],data[4],data[6],data[7])
        tuple_list.append(tup)   
    return tuple_list


def fetch_maintain_data(datalist):
    #creating Dictionary
    maintain_dic=dict()
    for data in datalist:
        if data[12] not in maintain_dic:
            maintain_dic[data[12]]=0
        else:
            maintain_dic[data[12]]=maintain_dic[data[12]]+1
    return maintain_dic
    
    
def fetch_unique_owner(datalist):
    owner_set=set()
    #creating owner list
    for data in datalist:
        owner_set.add(data[11])
    return owner_set

def fetch_street_class_data(datalist):
    street_class_dic=dict()
    for data in datalist:
            if data[10] not in street_class_dic:
                street_class_dic.setdefault(data[10],[data[2]])
            else:
                street_class_dic[data[10]].append(data[2])
    return street_class_dic
    
    
    

   
    

fout=open('Street_Centrelines.csv','r')
datalist=read_csv(fout)
print('THE DICTIONARY OF STREET CLASS WITH THEIR STREETS LIST :::')
print(fetch_street_class_data(datalist)
print('THE TUPLES OF (STR_NAME, FULL_NAME,FROM_STR,TO_STR)::::')
print(fetch_tuple(datalist))
print('DICTIONARY OF MAITAINENACE DATA WITH THEIR OCCURANCE::::')
print(fetch_maintain_data(datalist))
print('UNIQUE OWNERS DATAS::::')
print(fetch_unique_owner(datalist))
