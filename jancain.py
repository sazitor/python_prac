import random
computer = random.choice(["グー","チョキ","パー"])
player = input("グー、チョキ、パーのどれかを入力してください: ")
print("コンピュータの手:", computer)
if player == computer:
    print("引き分けです！")
elif (player == "グー" and computer == "チョキ") or (player == "チョキ" and computer == "パー") or (player == "パー" and computer == "グー"):
    print("あなたの勝ちです！")
else:
    print("コンピュータの勝ちです！")
    
                                                