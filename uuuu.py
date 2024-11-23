file=open("example.txt")
counter=0

content=file.read()

Colist= content.split("\n")

for i in Colist:
    if i:
        counter+=1

print("This is the number of the line in the paragraph")
print(counter)