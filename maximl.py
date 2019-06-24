String=input()
result=''
count=0
maxi=[]
for i in range(len(String)):
    if(not String[i] in result):
        result =result+String[i]
        count+=1
    else:
        result=String[i]
        maxi.append(count)
        count=1
print(max(maxi))
