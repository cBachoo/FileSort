import os
data = open('./dataset.txt', 'r').read().split()

for value in data:
    f = open("./result/" + str(value), 'w')
    f.write(value)

files = []
for i in os.listdir('./result'):
    files.append(i)
    

print(files) 