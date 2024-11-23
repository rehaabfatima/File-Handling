file=open("example.txt" , "r")
print("File in read mode" )
print(file.read())
file.close()

file_write=open("example.txt", "w")
print("File in write mood")
file_write.write("I am currently learning at Punjab Group of Colleges for women faisalabad. I am 16 years old")
file_write.close()

file_append=open("example.txt", "a")
file_append.write("file in append mode")
file_append.write("I am opening this file in append mode now")
file_append.close()
