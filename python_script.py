import re
import g
lob
files=glob.glob('./input/*.txt')
o1=open('output_1','w')
o2=open('output_2','w')
o3=open('output_3','w')
for f in files:
    current_file=open(f,'r')
    lines=current_file.readlines()
    print lines
    for line in lines:
        type_length=re.compile('([A-Z0-9]{3,4}[ ]{3,6}[0-9 ][0-9 ][0-9])')
        if re.search('Short description:',line):
            o2.write(f.replace('.txt','')+'|'+line)
            o3.write(line)
        elif re.search('Field count:',line):
            o2.write(f.replace('.txt','')+'|'+line)
            o3.write(line)
        elif re.search(type_length,line)==None:
            o3.write(line)
        else:
            t=[w for w in line.strip().split(' ') if w != '' and w != 'X']
            rw=[f.replace('.txt',''),t[0],t[1],t[2],' '.join(t[3:])]
            if rw[-1]=='':
                o1.write(rw[0]+'|'+rw[1]+'|'+rw[2]+'|'+rw[3]+'\n')
            else:
                o1.write('|'.join(rw)+'\n')
o1.close(),o2.close(),o3.close()
            
        
    
