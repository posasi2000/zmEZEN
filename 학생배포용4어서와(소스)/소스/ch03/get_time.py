import time
now = time.localtime()
print ("현재시간은 ", time.asctime())

if (now.tm_hour < 11) :
    print("Good morning")
elif (now.tm_hour < 15) :
    print("Good afternoon")
elif (now.tm_hour < 20) :
    print("Good evening")
else :
    print("Good night")
