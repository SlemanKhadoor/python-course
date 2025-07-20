# modes r read.  
f = open("test.txt","r")
print(f.read())
f.close()
#--------------------
#read it line by line
f = open("test.txt","r")
all_lines = f.readlines()
for line in all_lines:
    print(line)

#--------------------
# MODE w write.  it will create it if not exist
# it will overwrite each time

# append a  it's kind of write
# it will append on the content of the file