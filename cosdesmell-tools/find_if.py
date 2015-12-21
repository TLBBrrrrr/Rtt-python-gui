import os
import os.path

#rootdir="e:/cy"
rootdir="d:/github/django"

keyword="if"
keyword2="else"

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
                    num_of_line=num_of_line+1
                    if line.find(keyword)!=-1:
                        if line.find(keyword2)!=-1:
                            result.write(str(num_of_line)+"  "+line+"\n")
            except UnicodeDecodeError:
                continue
            else:
                result.write(whole+"\n")
                for line in t:
                    num_of_line=num_of_line+1
                    if line.find(keyword)!=-1:
                        if line.find(keyword2)!=-1:
                            result.write(str(num_of_line)+"  "+line+"\n")


result.close()
print("end")
