#while loop比較適合在不確定要執行幾次的狀態下使用，比起forloop

#問使用者買的商品名稱、價格，然後把它輸入的東西加入一個清單
#建立二維度清單，清單中的清單，有名字後價格

products = [] 
while True:
	name = input('請輸入商品名稱')
	if name == 'q':
		break
	price = input('請輸入商品價格')	
	#p = [] #小火車
	#p.append(name)
	#p.append(price)
	#上面三行簡寫成 >>p = [name, price ]

	#products.append(p)
	#大火車 #把p，也就是使用者輸入的東西存入清單	
	#其實也可以根本不用創作小火車，直接:
	products.append([name, price])  

	
	#注意這是和if同樣位置（同行），如果放在break下面位置，就跑不出來
print(products)

#建立二維度清單，清單中的清單，有名字後價格