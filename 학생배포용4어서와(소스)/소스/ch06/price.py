prices = [ 100, 200, 300, 400, 500 ]
cheapest  = prices[0]
for i in range(1, len(prices)):
	if prices[i] < cheapest  :
		cheapest  = prices[i]
print("가장 싼 가격은 ", cheapest)
