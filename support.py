def print_func(par):
    print("hello:"+par)
    return


money = 2000
def addMoney():
    global money
    money+=200
    print("总金额为："+str(money))
    return

addMoney()

