#below we used True or Fals as our value. what if Truth is 5 or "hello"
old_enough = True
has_licence = True

if old_enough and has_licence: #: means true
    print("you can drive now")
else:
    print("you are not of age") 

#what if Truth is 5 or "hello"  eg

old= "hello"
licence = 5

if old_enough and has_licence: #: means true
    print("you can drive now")  #you can drive now #you can drive now
else:
    print("you are not of age")

#it printed you can drive now because python coverted 5 and "hello" to boolean lie
print(bool(5))        #True or Truthy
print(bool("hello"))     #True or Truthy

print(bool(0))         #False or falsy
print(bool(""))     #False or falsy

#google what is truthy and Falsey to see all data types that are True or False



