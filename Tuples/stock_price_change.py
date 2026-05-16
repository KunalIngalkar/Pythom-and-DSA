'''

3. Stock Price Change
Stock prices for a week are stored in a tuple. Calculate the price difference between the first and the last
day of the week using indexing.

'''

#stock_prices = (150, 155, 148, 160)
#stock_prices = (200, 190, 180)
stock_prices = (100,) 

first_day_price = stock_prices[0]
last_day_price = stock_prices[-1]

price_change = last_day_price - first_day_price

print(price_change)