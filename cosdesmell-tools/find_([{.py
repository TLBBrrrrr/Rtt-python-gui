import os
import os.path

#rootdir="e:/cy"
rootdir="d:/github/django"

keyword="multiply-nested"

result=open("e:/cy/result-"+keyword+".txt","w")

for parent,dirnames,filenames in os.walk(rootdir):
    #for dirname in dirnames:
     #   print (parent+" "+dirname)
    for filename in filenames:
        fname,fpy=os.path.splitext(filename)
        #whole=os.path.join(parent,filename)
        whole=parent+'/'+filename
        if fpy==".py":
            #print(whole)
            t=open(whole,"r")
            num_of_line=0
            try:
                result.write(whole+"\n")
                for line in t:
                    num=0
                    for k in line:
                        if k=="(" or k=="[" or k=="{" :
                            num=num+1
                    if num>=2:
                        result.write(str(num_of_line)+"  "+line+"\n")
            except UnicodeDecodeError:
                continue
            else:
                result.write(whole+"\n")
                for line in t:
                    num=0
                    for k in line:
                        if k=="(" or k=="[" or k=="{" :
                            num=num+1
                    if num>=2:
                        result.write(str(num_of_line)+"  "+line+"\n")

result.close()
print("end")
