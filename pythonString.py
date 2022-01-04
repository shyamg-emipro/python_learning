# In this program we are going to see use of many available string methods in python
str1 = "{0}This is a test string for the purpose of the demonstration of various functions.{1}"

# count() occureance of a specified value in string
print(str1.count("i"))

# endswith() True if ends with a specified value
print(str1.endswith("}"))

# find() find and return first letter position of first occureance of a value
print(str1.find("is"))

# format() used to insert numeric value into string
print(str1.format({10},{20}))

# index() is same as find except it throws an exeption if string is not found
print(str1.index("is"))

# isspace() returns True if all characters are whitespaces
print("      ".isspace())

# lstrip() strip whitespaces from the left side only
print("         hello world".lstrip())

# replace() it replaces existing character and return new modified string
print("hi, my name is kapil.".replace("kapil","karan"))

# rfind() return position of first letter of a last occurance of the specified value
print("karan is a student of arts, karan has its own art galary".rfind("karan"))

# rindex() is same as rfind but it throws exception instead of returning false
print("karan is a student of arts, karan has its own art galary".rindex("karan"))

# rstrip() returns the right trim version of string
print("     Hello World!       ".rstrip())

# zfill()
print("343".zfill(8))

# strip() it removes whitespaces from the begining and ending
print("        hello             ".strip(),"world")