#檢查檔案在不在
import os

#讀取清單
def load_list(filename):
	product = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續，跳到下一行程式
			name, price = line.strip().split(',')
			product.append([name, price])
	print(product)
	return product
	
#讓使用者輸入
def user_input(product):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		# p = [name, price]
		# p.append(name)
		# p.append(price)
		product.append([name, price])
	return product

#印出所有購買紀錄
def print_product(product):
	for p in product:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write(filename,product):
	with open(filename, 'w', encoding='utf-8') as f: 
	#encoding='utf-8'世界共通的編碼
		f.write('商品,價格\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n')
	#csv檔通常會用逗點做區隔,寫入一定要字串

#main function
def main():
	#檢查檔案在不在
	filename = 'product.csv'
	if os.path.isfile(filename): #os.path.isfile()檢查有沒有這個檔案
		print('有這個檔案!以下是檔案紀錄')
		product = load_list(filename)
		product = user_input(product)
		print_product(product)
		write('product.csv', product)
	else:
		print('找不到檔案...')

main()