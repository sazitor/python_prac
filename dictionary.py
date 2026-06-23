dic = {}
spell = input()

for i in spell:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1

max_char = ""
max_count = 0

for char, count in dic.items():
    if count > max_count:
        max_char = char
        max_count = count
    elif count == max_count:
        if char < max_char:
            max_char = char

print(max_char, max_count)