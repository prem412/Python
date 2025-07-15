# def greet():
#     print("Hello, World!")

# greet()



# def greet(name):
#     print(f"Hello, {name}!")

# greet("prem")




# def add(x, y):
#     return x + y

# ans = (add(5, 3))
# print(ans)  





# def greet(name= "Love"):
#     print("Hello",name)

# greet()
# greet("Prem")







def get_stats(marks):
    avg = sum(marks) / len(marks)
    total = sum(marks)
    return avg, total

a, t = get_stats([10, 20, 30])
print("Average:", a)
print("Total:", t)
