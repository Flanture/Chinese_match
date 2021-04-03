import re
def quchong(infile,outfile):
    head=False
    infopen = open(infile,'r',encoding='gb2312')
    outopen = open(outfile,'a',encoding='utf-8')
    lines = infopen.readlines()
    list_1 = []
    for line in lines:
        excep3="【第"
        situ1=re.match(excep3,line)
        if(not situ1):
            if(head):
                outopen.write(line)
        else:
            if line not in list_1:
                head=True
                list_1.append(line)
                outopen.write(line)
            else:
                head=False
        
    infopen.close()
    outopen.close()
quchong("E://total.txt","E://quchong.txt")