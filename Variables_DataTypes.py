name = "prem"
age = 20
height = 5.9
is_student = True
hobbies = ["Reading", "Singing", "Coding"]
favorite_color = "Light"
favorite_numbers = (3,27,2005)
# Printing the variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print("Hobbies:", hobbies)
print("Favorite Color:", favorite_color)
print("Favorite Numbers:", favorite_numbers)

#type of each variable
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))
print("Type of hobbies:", type(hobbies))    
print("Type of favorite_color:", type(favorite_color))
print("Type of favorite_numbers:", type(favorite_numbers))

#input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old.")

# Example of using input to get a list of hobbies
hobbies = input("Enter your hobbies: ").split(',')
print("Your hobbies are:", hobbies)

# Example of using input to get favorite numbers
favorite_numbers = input("Enter your favorite numbers separated by commas: ").split(',')
favorite_numbers = tuple(map(int, favorite_numbers))
#map function hai jo list ke har element ko go through karta hai aur function apply karta hai
print("Your favorite numbers are:", favorite_numbers)


# student hai ya nahi
is_student = input("Are you a student? (yes/no): ").strip().lower() 
#.strip() whitespace remove karta hai 
# .lower() lowercase mein convert karta hai
is_student = is_student == 'yes'
print("Are you a student?", is_student)

input_favorite_movies = input("Enter your favorite movies : ").split(',')
input_favorite_movies = tuple(map(str.strip, input_favorite_movies))
