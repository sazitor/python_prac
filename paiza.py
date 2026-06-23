word = input()
current = word[0]
count = 1

for i in word[1:]:
    if i == current:
        count += 1
    else:
        print(current + str(count), end="")
        current = i
        count = 1

print(current + str(count))
    