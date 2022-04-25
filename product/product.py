product = []

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

with open('product.csv', 'w') as f:
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')
#csv檔通常會用逗點做區隔
#寫入一定要字串