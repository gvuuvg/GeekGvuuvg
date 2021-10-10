# 模拟购物车

money = float(input("输入钱包余额："))
# 编码，名称，价格，库存
goods_list = [{"编码": "g1001", "名称": "矿泉水", "价格": 1, "库存": 100},
              {"编码": "g1002", "名称": "笑气", "价格": 50, "库存": 10},
              {"编码": "g1003", "名称": "永磁铁", "价格": 10, "库存": 150}]
cart = []
print("商品有：")
# enumerate可以将元素的索引及元素本身作为一个元组返回
for i, j in enumerate(goods_list):
    print(i, j)
seq = int(input("输入商品编号："))
buy_count = int(input("输入商品购买数量："))
# 完成支付,库存扣减，购物车添加商品，打印购买明细及余额
money -= goods_list[seq].get("价格") * buy_count
goods_list[seq]["库存"] -= buy_count
good = {"编码": goods_list[seq]["编码"],
        "名称": goods_list[seq]["名称"],
        "价格": goods_list[seq]["价格"],
        "数量": buy_count}
cart.append(good)
print("购买了", cart)
print("剩余%.2f" % money)

#
# g = goods_list[seq]
# del g["库存"]
# g["数量"] = buy_count
# cart.append(g)

def buy():
    pass