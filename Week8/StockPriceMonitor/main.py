from theobservers import Investor, Stock

stock = Stock()
ali = Investor("Ali")
sara = Investor("Sara")

stock.subscribe(ali)
stock.subscribe(sara)

print("*" *100)
print("Stock Updates")
stock.set_price(105) 
stock.set_price(112) 