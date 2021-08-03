# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 09:39:10 2020

@author: gaoka
"""

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def clean(cha):
    c_cha=[]
    num=len(cha)
    for i in range(0,num):
        if(is_number(cha[i]) and (cha[i]!="4" and cha[i]!="3" and cha[i]!="2" and cha[i]!="1" and cha[i]!="0")):
            continue            
        if(cha[i]=="1:" or cha[i]=="0:"):
            continue
        if(cha[i][-4:-2]=="e-"):
            continue
        if(len(cha)>2 and (cha[i][-2:]=="1:" or cha[i][-2:]=="0:")):
            c_cha.append(cha[i][0:-2])
        else:
            c_cha.append(cha[i])
    return c_cha

outfile=open("test-multigpu.out")
lines=outfile.read().splitlines()
num=len(lines)

for i in range(num):
    l=lines[i]
    l=l.split()
    if(l[-1]=="return:"):
        break

comp=0.0   
acc=0.0 
for j in range(i+1,num,5):
    sl=lines[j]      
    sl=sl.split()
    if(sl[5]=="INFO"):
        break
    comp=comp+1
    tl=lines[j+3]  
    tl=tl.split()
    se=clean(sl[3:])
    tn=clean(tl[4:])
    if(se==tn):
        acc=acc+1
    else:
        print(comp-1)
        print(se)
        print(tn)
       
print(acc/comp)
    

