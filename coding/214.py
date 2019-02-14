import time
# f = open('214.txt', 'w+')
sentence = "Darling, I love you forever!"
for char in sentence.split():
    allChar = []
    for y in range(12, -12, -1):
        lst = []
        lst_con = ''
        for x in range(-60, 40):
            formula = ((x * 0.04) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            if formula <= 0:
                lst_con += char[(x) % len(char)]
            else:
                lst_con += ' '
        lst.append(lst_con)
        allChar += lst
    print('\n'.join(allChar))
    # time.sleep(1)

    # f.write('\n'.join(allChar))
