Todo = []

while True:
    order = input("命令を入力してください(1:追加,2:表示,3:削除,4:終了)：")
    
    if order == "1":
        task = input("タスクを入力してください:")
        Todo.append(task)

    elif order == "2":
       for i, task in enumerate(Todo, 1):
        print(f"{i}. {task}")

    elif order == "3":
        for i, task in enumerate(Todo, 1):
            print(f"{i}. {task}")
        del_num = int(input("削除するタスクの番号を入力してください: "))
        if 1 <= del_num <= len(Todo):
            removed = Todo.pop(del_num - 1)
            print(f"{removed}を削除しました。")
        else:
            print("タスクが見つかりませんでした。")
    
    elif order == "4":
        print("終了します。")
        break

    else:
        print("無効なコマンドです。もう一度入力してください。")
    1

