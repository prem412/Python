#condition 
# If, Elif, Else, and Nested If 

age = 18 
if age >= 18:
    print("You can vote.")

age = 16 
if age >= 18:
    print("you can vote.")
else:
    print("You cannot vote.")



marks = 70

if marks >= 80:
    print("class A")
elif marks >= 60:
    print("class B")
elif marks >= 40:
    print("class C")
else:
    print("fail")




# Nested If 
age = 20
indian = True
if age >= 18:
    if indian:
        print("You can vote.")
    else:
        print("You cannot vote.")
else: 
    print("You cannot vote.")