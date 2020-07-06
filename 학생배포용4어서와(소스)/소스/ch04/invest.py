year = 0
balance = 1000
while balance < 2000:
    year = year + 1
    interest = balance*0.05
    balance = balance + interest

print("기간: ", year)
print("총액: ", balance)
