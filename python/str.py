##string -- sequence of characters
##string is immutable(unchangeable)  --- add , remove , delete , update , sort 
#string is ordered 
##string is denoted by - '',"",""" """ --- multiline string

# n1 = " pvt ltd"
# print(name)
# print(type(name)) 

# text = "my company name is " + name
# print(text)

# print(name + n1)
# print(name.upper())
# print(name.lower())
# print(name.swapcase())
# print(name.title())          ## capitalize first letter of every word
# print(name.capitalize())     ## capitalize first letter of string
# print(name.casefold())         ##caseless comparison
# print(name.strip())               ##left aur right dono se space remove krega
# print(name.lstrip())
# print(name.rstrip())    
# print(name.replace("pvt","pvt ltd"))
# print(name.split(" "))
# print(name.partition("z"))
# print(name.center(50,"*"))
# print(name.ljust(50,"*"))
# print(name.rjust(50,"*"))
# print(name.count("a"))
# name = "UpFlairs pvt"
# print(name.endswith("a"))
# print(name.startswith("U"))
# print(name.rpartition("pvt"))
# print(name.removeprefix("Up"))
# print(name.removesuffix("pvt"))
# print(name.isalpha())            #alphabets only
# print(name.isdigit())            #digits only
# print(name.isalnum())            #alphabets and digits only
# print(name.islower())
# print(name.isupper())
# print(name.isspace())
# print(name.istitle())

# print(name.encode("utf-8"))

# age = 10 
# text = "my age is" + age
#formatted string //f-string
# text = f"my age is {age}"
# print(text)

# text = "my name is \"jai\""
# ##take quotes diff outside and inside  
# print(text)

##indexing and slicing 
##indexing -- single character access 
##slicing -- multiple character access

#"hello" -- 
#0 1 2 3 4 -- positive 
#-5 -4 -3 -2 -1 -- negative
#h e l l o

# n1  = "upflairs"
# print(n1[1])
# print(n1[-3])
# [start:end:step/jump]
# print(n1[2:8])
# print(n1[::3])