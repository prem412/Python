file = open("demo.txt", "r")   # OPEN() thi file khule ,  "r" means read mode , file ma reference store thaay demo.txt no
content = file.read()          # Content variable ma demo.txt red thai jaay
print(content)                 # Print thaay
file.close()                   # bandh thaay

file = open("demo.txt", "w")   
content = file.write("Hello this is prem")  #demo vadi file aakhe aakhi replace thai jase je aaama lakhyu chhe enathi 
print(content)
file.close 

file = open("demo.txt" , "a")       # Append karva
file.write("\nHello this is me")
file.close()


# LINE BY LINE Read karva
file = open("demo.txt", "r")
for line in file:
    print(line.strip())
file.close()