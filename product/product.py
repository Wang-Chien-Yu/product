product = []
#讀取清單
# with open('product.csv', 'r', encoding='utf-8') as f:
# 	for line in f:
# 		name, price = line.strip().split(',')
# 		product.append([name, price])
# print(product)

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	# p = [name, price]
	# p.append(name)
	# p.append(price)
	product.append([name, price])
print(product)

for p in product:
	print(p[0], '的價格是', p[1])

with open('product.csv', 'w', encoding='utf-8') as f: 
#encoding='utf-8'世界共通的編碼

	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')
#csv檔通常會用逗點做區隔
#寫入一定要字串