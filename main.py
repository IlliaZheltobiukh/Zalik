a = open("text.txt", 'r', encoding='utf8')
tegword = input("Введіть потрібне слово: ")
list = a.read().split('\n\n')
c = 0
for i in list:
    for t in i.split():

        if t == tegword:
            print("Абзац знайдено: " + i + "\n")
            c += 1
            break

if c == 0:
    print("Слово не знайдено.")