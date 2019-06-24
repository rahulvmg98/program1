String=input()
result=''
for i in range(len(String)):
    if(not String[i] in result):
        result =result+String[i]
print(len(result))
        
