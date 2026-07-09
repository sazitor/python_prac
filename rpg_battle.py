class Character:
    def __init__(self,name,hp,attack):
        self.name = name
        self.hp = hp
        self.attack = attack

player1 = Character("プレイヤー", 100, 20)    
enemy1 = Character("スライム", 80, 15)

while True:
    command = input("コマンドを入力してください（1=攻撃, 2=防御）: ") 
    gurad = False
    if command == "1":
        enemy1.hp -= player1.attack
        print(player1.name +"の攻撃"+enemy1.name+"に"+str(player1.attack)+"のダメージ！")
        print(enemy1.name+"の残りHP:"+str(enemy1.hp))
    if command == "2":
        print(player1.name+"は防御した！")
        gurad = True
        
 
    if enemy1.hp <= 0:
        print(enemy1.name+"を倒した！")
        break
    if enemy1.hp > 0:
        damage = enemy1.attack
        if gurad == True:
            damage = int(damage / 2)
        player1.hp -= damage





        
        print(enemy1.name +"の攻撃"+player1.name+"に"+ str(damage)+"のダメージ！")
        print(player1.name+"の残りHP:"+str(player1.hp))
    if player1.hp <= 0:
        print(player1.name+"は倒された…")
        break

