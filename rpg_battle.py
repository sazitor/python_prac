import random

class Character:
    def __init__(self, name, hp, attack, crt=0.2, escape_rate=0.5, hold_rate=0.5):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.crt = crt
        self.escape_rate = escape_rate
        self.hold_rate = hold_rate

player1 = Character("プレイヤー", 100, 20,crt = 0.3,escape_rate = 1)    
enemy1 = Character("スライム", 80, 15,crt = 0.2,hold_rate = 0.2)
enemy2 = Character("ゴブリン", 60, 18,crt = 0.35,hold_rate = 0.5)
enemy3 = Character("ドラゴン", 150, 25,crt = 0.2,hold_rate = 0.7)

enemy = random.choice([enemy1, enemy2, enemy3])
print(enemy.name+"が現れた！")
while True:
    command = input("コマンドを入力してください（1=攻撃, 2=防御,3=回復,4=逃げる）: ") 
    gurad = False
    is_crt = False
    en_crt = False

    if command == "1":
        if random.random() < player1.crt:
            is_crt = True
        if is_crt == True:
            print(player1.name+"のクリティカル！")
            enemy.hp -= player1.attack * 2
            print(player1.name +"の攻撃"+enemy.name+"に"+str(player1.attack * 2)+"のダメージ！")
            print(enemy.name+"の残りHP:"+str(enemy.hp))
        else:
            enemy.hp -= player1.attack
            print(player1.name +"の攻撃"+enemy.name+"に"+str(player1.attack)+"のダメージ！")
            print(enemy.name+"の残りHP:"+str(enemy.hp))
    if command == "2":
        print(player1.name+"は防御した！")
        gurad = True
        
    if command == "3":
        player1.hp += 30
        if player1.hp > player1.max_hp:
            player1.hp = player1.max_hp
        print(player1.name+"は回復した！")
        print(player1.name+"の残りHP:"+str(player1.hp))
    
    if enemy.hp <= 0:
        print(enemy.name+"を倒した！")
        break
    if command == "4":
        if random.random() < player1.escape_rate - enemy.hold_rate:
            print(player1.name+"は逃げ出した！")
            break
        else:
            print(player1.name+"は逃げられなかった！")
    if enemy.hp > 0:
        if random.random() < enemy.crt:
            en_crt = True
        
        damage = enemy.attack
        if en_crt == True:
            print(enemy.name+"のクリティカル！")
            damage = damage * 2
        if gurad == True:
            damage = int(damage / 2)
        player1.hp -= damage





        
        print(enemy.name +"の攻撃"+player1.name+"に"+ str(damage)+"のダメージ！")
        print(player1.name+"の残りHP:"+str(player1.hp))
    if player1.hp <= 0:
        print(player1.name+"は倒された…")
        break

