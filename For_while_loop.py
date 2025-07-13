# difference between range and range(start, end)
for i in range(5):
    print(i)
for i in range(1,6):
    print(i)
for i in range(1, 11, 2):
    print(i)
for i in range(10, 0, -2):
    print(i)

#while loop
i = 1
while i <= 5:   
    print(i)
    i += 1  


for ch in "Love":
    print(ch)

colors = ["red", "blue", "green"]
for color in colors:
    print(color)


for i in range(10):
    if i == 5:
        break               #break = exit the loop  
    print(i)    

for i in range(5):
    if i == 2:
        continue            #continue = skip particular 
    print(i)



#table generator
num  = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

