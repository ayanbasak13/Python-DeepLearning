fptr = open('file.txt')
lines = fptr.readlines()
count=0


for line in lines :
    for i in line :
        if i.isupper() :
            count +=1

 
print(count)