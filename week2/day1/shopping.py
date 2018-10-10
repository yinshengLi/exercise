#__author:iruyi
#date:2018/9/19

salary = int(input("输入你的工资："))

product_list = ['bicycle:1000','mac pro:9000','pyhton book:50']
count = 1
for product in product_list:
    print(count, ' ', product)
    count += 1
choose = input('选择购买的商品编号：')
buy_list = []
while choose != 'quit':
    if choose.isdigit():
        choose = int(choose)
        if choose >=0 and choose < len(product_list):
            pro = product_list[choose -1]
            price = pro.split(':')[1]
            if int(price) > salary:
                print("余额不足")
            else:
                buy_list.append(pro)
                salary = salary - int(price)
                print('余额为：', salary)
            choose = input('选择购买的商品编号：')
        else:
            print('请选择正确的商品编号')
            choose = input('选择购买的商品编号：')
    else:
        print('请选择正确的商品编号')
        choose = input('选择购买的商品编号：')

print('已购买商品：')
print(buy_list)