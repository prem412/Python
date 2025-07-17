feedback = input("Enter your feedback: ")
file = open("demo.txt", "w")
file.write(feedback + "\n")
print("Your feedbck is submitted!")


# input liya aur use feedback variable me daala
# demo file open kari , aur uska reference file me daala , Write mode
# file ko write kiya (replace whole content) aur usme feedback (likh)daal diya
# aur print karva diya ki ha bhai feedback submit ho gaya

