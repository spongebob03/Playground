f = open("test.txt","r")
data=f.read()
f.close()
dic={}
for i in data:
    dic[i]=data.count(i)
print(dic)

f=open("proverbs.txt","w")
f.write(str(dic))
f.close()
