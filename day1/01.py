# =========================
# 1. 基础数据
# =========================

commoditys: dict[int, str] = {
    0: "苹果",
    1: "香蕉",
    2: "牛奶"
}

price: list[float] = [5.5, 3.0, 8.0]

number: list[int] = [10, 5, 0]


# =========================
# 2. 判断商品是否存在
# 这个你已经会了
# =========================

def commoditys_exist(commodity: str) -> bool:
    if commodity in commoditys.values():
        return True

    return False


# =========================
# 3. 根据商品名称找到商品编号
# 这个你自己补
# =========================

def get_commodity_id(commodity: str) -> int:
    for commodity_id, commodity_name in commoditys.items():
        if commodity_name == commodity:
            return commodity_id

# =========================
# 4. 根据商品编号查询库存
# =========================

def get_stock(commodity_id: int) -> int:

    # TODO:
    # number 是库存列表
    # commodity_id 是商品编号
    #
    # 想一想应该怎么从 number 中取数据
    return number[commodity_id]


# =========================
# 5. 根据商品编号查询价格
# =========================

def get_price(commodity_id: int) -> float:

    # TODO:
    # price 是价格列表

    return price[commodity_id]


# =========================
# 6. 判断库存够不够
# =========================

def can_buy(stock: int, buy_number: int) -> bool:

    # TODO:
    # 如果库存 >= 购买数量
    # 返回 True
    # 否则返回 False
    if stock < buy_number:
     return False
    else:
     return True


# =========================
# 7. 计算总金额
# =========================

def calculate_total(
    commodity_price: float,
    buy_number: int
) -> float:

    # TODO:
    # 单价 × 数量

    return commodity_price * buy_number


# =========================
# 8. 整个程序的主流程
# =========================

def main():

    print("===== 商品下单系统 =====")

    # 用户输入商品
    commodity: str = input("请输入商品名称：")

    # 第一关：判断商品是否存在
    exist: bool = commoditys_exist(commodity)

    if exist == False:
        print("商品不存在")
        return

    print("商品存在")

    # 第二步：获得商品编号
    commodity_id = get_commodity_id(commodity)

    if commodity_id is None:
        print("无法获取商品编号")
        return

    print("商品编号：", commodity_id)

    # 第三步：根据商品编号获得库存
    stock = get_stock(commodity_id)

    print("当前库存：", stock)

    # 用户输入购买数量
    buy_number: int = int(input("请输入购买数量："))

    # 第四步：判断购买数量是否合法
    if buy_number <= 0:
        print("购买数量必须大于0")
        return

    # 第五步：判断库存
    buy_result = can_buy(stock, buy_number)

    if buy_result == False:
        print("库存不足")
        return

    # 第六步：查询价格
    commodity_price = get_price(commodity_id)

    print("商品单价：", commodity_price)

    # 第七步：计算总金额
    total = calculate_total(
        commodity_price,
        buy_number
    )

    print("===== 下单成功 =====")
    print("商品：", commodity)
    print("数量：", buy_number)
    print("总金额：", total)


# =========================
# 9. 启动程序
# =========================

if __name__ == "__main__":
    main()