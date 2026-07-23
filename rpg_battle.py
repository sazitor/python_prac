import random

class Character:
    def __init__(self, name, hp, attack, crt=0.2, escape_rate=0.5, hold_rate=0.5, accuracy=0.9, evasion=0.1):
        self.name = name
        self.max_hp = hp    
        self.hp = hp    
        self.attack = attack  
        self.crt = crt
        self.escape_rate = escape_rate
        self.hold_rate = hold_rate
        self.accuracy = accuracy  # 命中率
        self.evasion = evasion    # 回避率

player1 = Character("プレイヤー", 100, 20,crt = 0.3,escape_rate = 1,hold_rate = 0.5,accuracy = 0.9,evasion = 0.1)    
enemy1 = Character("スライム", 80, 15,crt = 0.2,hold_rate = 0.2,accuracy = 0.9,evasion = 0.1)
enemy2 = Character("ゴブリン", 60, 18,crt = 0.35,hold_rate = 0.5,accuracy = 0.9,evasion = 0.1)
enemy3 = Character("ドラゴン", 150, 25,crt = 0.2,hold_rate = 0.7,accuracy = 0.9,evasion = 0.1)

enemies = random.sample([enemy1, enemy2, enemy3],2)
for e in enemies:
    print(e.name + "が現れた！")

defeated_names = []

while True:
    command = input("コマンドを入力してください（1=攻撃, 2=防御,3=回復,4=逃げる）: ") 
    gurad = False
    is_crt = False
    en_crt = False

    if command == "1":
        alive_enemies = []
        for e in enemies:
            if e.hp > 0:
                alive_enemies.append(e)

        for i, e in enumerate(alive_enemies, 1):
            print(f"{i}:{e.name}(HP:{e.hp})")
        enemies_choice = int(input("どの敵を攻撃しますか？: "))
        target_enemy = alive_enemies[enemies_choice - 1]
        enemy = target_enemy

        accuracy_check = random.random()
        if accuracy_check > player1.accuracy - enemy.evasion:
            print(player1.name + "の攻撃は外れた！")
        else:  
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
    all_defeated = True
    for e in enemies:
        if e.hp > 0:
            all_defeated = False
        else:
            if e.name not in defeated_names:
                print(e.name+"を倒した！")
                defeated_names.append(e.name)

    if all_defeated:
        print("すべての敵を倒した！")
        break   


    if command == "4":
        if random.random() < player1.escape_rate - enemy.hold_rate:
            print(player1.name+"は逃げ出した！")
            break
        else:
            print(player1.name+"は逃げられなかった！")
    for e in enemies:
        if e.hp > 0:
            enemy_accuracy_check = random.random()
            if enemy_accuracy_check > e.accuracy - player1.evasion:
                print(e.name+"の攻撃は外れた！")
            else:   
                if random.random() < e.crt:
                    en_crt = True
                damage = e.attack
                if en_crt == True:
                    print(e.name+"のクリティカル！")
                    damage = damage * 2
                if gurad == True:
                    damage = int(damage / 2)
                player1.hp -= damage
                print(e.name +"の攻撃")
                print(player1.name+"に"+ str(damage)+"のダメージ！")
                print(player1.name+"の残りHP:"+str(player1.hp))
    if player1.hp <= 0:
        print(player1.name+"は倒された…")
        break

