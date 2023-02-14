a = float (input ())
b = float (input ())
#2
if (-100 < a < 1) and (1 < b < 10 ):
    print ("True") 
elif (2 < a < 100) and (11 < b < 20 ):
    print ("True")
elif (101 < a < 200) and (21 < b < 30 ):
    print ("False")
else:
    print ("False")
#3
if (-100 < a < 1) or (1 < b < 10 ):
    print ("True") 
elif (2 < a < 100) or (11 < b < 20 ):
    print ("True")
elif (101 < a < 200) or (21 < b < 30 ):
    print ("False")
else:
    print ("False")
#4
c = input()
d = input()
if (20 > len(c) > 5) and (len(d) <10):
    print("True")
else:
    print("No")