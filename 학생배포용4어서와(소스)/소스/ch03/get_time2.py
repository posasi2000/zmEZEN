#get_time1.py

import time
now = time.localtime()
print ("1현재시간  ", time.asctime())

if (now.tm_hour < 11) :
    print("Good morning")
elif (now.tm_hour < 15) :
    print("Good afternoon")
elif (now.tm_hour < 20) :
    print("Good evening")
else :
    print("Good night")

print()
week=['월요일','화요일','수요일','목요일','금요일','토요일','일요일' ] 
b=time.localtime()
print(b.tm_year,'년 ', b.tm_mon, '월 ', b.tm_mday, '일',  week[b.tm_wday])
print(b.tm_hour,'시 ', b.tm_min, '분 ', b.tm_sec, '초')    
