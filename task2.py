def read_csv(fout):
    datalist=[]
    fout.readline()
    for line in fout:
        line=line.strip()
        datalist.append(line.split(','))

    return datalist


def traverse(line,street_datalist,checkvalue):
    counter=0
    for data in street_datalist:
                if data[10].upper() == checkvalue.upper():
                    if line[9] == data[23]:
                        counter+=1
    return counter   

def busstops(street_datalist,bus_datalist):
    aacount=0
    nscount=0
    incount=0
    for line in bus_datalist:
        if line[7].upper() == 'Accessible'.upper():
            for data in street_datalist:
                if data[10].upper() == 'ARTERIAL'.upper():
                    if line[9] == data[23]:
                        aacount+=1
            
        elif line[7].upper() == 'Non-Standard'.upper():
            for data in street_datalist:
                if data[10].upper() == 'LOCAL STREET'.upper(): 
                    if line[9] == data[23]:
                        nscount+=1
            
        elif line[7].upper() == 'Inaccessible'.upper():     
            for data in street_datalist:
                if data[10].upper() == 'MINOR COLLECTOR'.upper(): 
                    if line[9] == data[23]:
                        incount+=1
            
    print('The Number of bus Stops which are Accessible and in a ARTERIAL road::',aacount)
    print('The Number of bus Stops which are Non-Standard and in a LOCAL STREET::',nscount)
    print('The Number of bus Stops which are Inaccessible and in a MINOR COLLECTOR::',incount)

def printsomedata(bus_datalist):
        print('|Stop Number|Location|FCODE|')
        print('|'+'---------|'*3)
        for line in bus_datalist[0:100]:
            print(('| {} | {} | {} |').format(line[3],line[6],line[10]))


fout=open('Street_Centrelines.csv','r')
street_datalist=read_csv(fout)
fout=open('Bus_Stops.csv','r')
bus_datalist=read_csv(fout)
busstops(street_datalist,bus_datalist)
printsomedata(bus_datalist)
