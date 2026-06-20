try:
    num_1 = int(input("数字を入力: "))
    num_2 = int(input("数字を入力: "))
    print(num_1 / num_2)
except ZeroDivisionError:
    print("0では割れません")
except ValueError:
    print("数字を入力してください")