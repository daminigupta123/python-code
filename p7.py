amount = int(input())     
denomination = int(input())  

notes = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}


denoms = [100, 50, 20, 10, 5, 2, 1]


start_index = denoms.index(denomination)

for i in range(start_index, len(denoms)):
    match denoms[i]:
        case 100:
            notes[100] = amount // 100
            amount %= 100
        case 50:
            notes[50] = amount // 50
            amount %= 50
        case 20:
            notes[20] = amount // 20
            amount %= 20
        case 10:
            notes[10] = amount // 10
            amount %= 10
        case 5:
            notes[5] = amount // 5
            amount %= 5
        case 2:
            notes[2] = amount // 2
            amount %= 2
        case 1:
            notes[1] = amount // 1
            amount %= 1

for d in denoms[start_index:]:
    print(f"{d} rupees note: {notes[d]}")
