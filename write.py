f = open('newfile.txt','a')   #'w'  <-- write 'a' <-- append
lines = ["hellow","world","welcome"]
text = "\n".join(lines)
f.writelines(text) #f.write() OR f.writelines() <-- writes it into one line
f.close()