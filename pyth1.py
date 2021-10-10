import os
import socket
import string

path = '/home/data'
new_file=open('/home/data/result.txt','w')

files = []
file_dict={}
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
            a=os.path.join(r, file)
            with open(a, 'r') as f:
                num_words=0
                for line in f:
                    words=line.split()
                    num_words+= len(words)
                file_dict.update({file:num_words})
                
    new_file.write("\nText files : ""\n")
for key, value in file_dict.items():
    
    new_file.write(""+str(key)+"\n")

for key, value in file_dict.items():
    
    new_file.write("\nFile "+str(key)+" contains a total of "+str(value)+" words\n")
    

val=0
for v in file_dict.values():
    val+=v
new_file.write("\nEach file's total word count  : "+str(val))

words = open('/home/data/IF.txt').read().lower().translate(line.maketrans("", "", string.punctuation)).split()

uniques = []
for word in words:
  if word not in uniques:
    uniques.append(word)

counts = []
for unique in uniques:
  count = 0
  for word in words:
    if word == unique:
      count += 1
  counts.append((count, unique))

counts.sort()
counts.reverse()

new_file.write("\n \nThe top three most often used terms are : (word,count) ""\n")
for i in range(min(3, len(counts))):
  count, word = counts[i]
  new_file.write(""+ word +" "+ str(count) +"\n")
  
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
new_file.write("\nMy System Name : " + hostname)
new_file.write("\n \nMy System IP Address : " + IPAddr)

new_file = open('/home/data/result.txt', 'r')

file_contents = new_file.read()

print(file_contents)

new_file.close()


