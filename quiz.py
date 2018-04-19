# f = open('files/relative_data.txt', 'r') #relative path
f = open('/home/ubuntu/workspace/files/relative_data.txt', 'r') #absolute path

lines = f.read()  #f.readlines makes one line into one element
f.close()
print(lines)