def counter(num_1, num_2, math):
    if math == "+":
        answer = num_1 + num_2
    elif math == "-":
        answer = num_1 - num_2
    elif math == "*":
        answer = num_1 * num_2
    elif math == "/":
        answer = num_1 / num_2
    else:
        print("error! 演算子を正しく入力してください")
        answer = None

    if answer is not None:
        print(answer)

try:
    num_1 = float(input("数字を入力: "))
    math = input("演算子+ - * /のうちいずれかを入力: ")
    num_2 = float(input("数字を入力: "))
    counter(num_1, num_2, math)
except ZeroDivisionError:
    print("error! 0で割ることはできません")
except ValueError:
    print("error! 数字を正しく入力してください")
    
