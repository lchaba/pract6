file =  open('input.txt', 'r') 
min = 10000000
x = int(file.read(1))
if x//2 < min:
    min = x//2
y = int(file.read(3))
if y//6 < min:
    min = y//6
z = int(file.read(5))
if z < min:
    min = z       

with open('output.txt', 'w') as f:
    f.write(str(min))
print(min)

