#while loop比較適合在不確定要執行幾次的狀態下使用，比起forloop

#問使用者買的商品名稱、價格，然後把它輸入的東西加入一個清單
#建立二維度清單，清單中的清單，有名字後價格

products = [] 
while True:
	name = input('請輸入商品名稱')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	price = int(price)	
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

#--------------

for p in products: #Ｐ是小清單！把小清單從大清單一個個拿出來
	print(p[0],'的價格是',p[1])#印出小火車的第零格＝name，和價格

 #---創建檔案！

with open('products.csv', 'w', encoding= 'utf-8') as f: #w是寫入，創造檔案,存成csv就是存成excel
	f.write('商品名稱,價格\n') #在數字上面寫上一層簡介，注意空格跳行符號
	for p in products:
			f.write(p[0] + ',' + str(p[1])+ '\n')  #逗點可以幫助excel分隔，把名稱和價格分開
			#任何程式有open就有close,python是用with open 來自動close
			#str(p[1]) 字串只能與字串家

