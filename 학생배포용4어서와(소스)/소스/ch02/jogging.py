hour = 6
minute = 50
time = 10 + 3*7 + 10
minute = minute + time
hour = hour + minute // 60
minute = minute % 60
print(hour, minute)
