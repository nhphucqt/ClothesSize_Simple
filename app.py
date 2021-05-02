def ChonSizeAo():
    print('\nChọn loại áo:')
    for i in range(len(AoTypesList)):
        print(i,'-',AoTypesList[i][0])

    print('\nNhập chỉ số áo:',end=' ')
    AoID = int(input())
    while AoID < 0 or AoID >= len(AoTypesList):
        print('Chỉ chấp nhận chỉ số từ 0 ->',len(AoTypesList)-1)
        print('Nhập chỉ số áo:',end=' ')
        AoID = int(input())

    print('\nNhập chiều cao (155-183):', end=' ')
    height = int(input())
    while height < 155 or height > 183:
        print('Chỉ chấp nhận chiều cao từ 155cm -> 183cm')
        print('Nhập chiều cao (155-183):', end=' ')
        height = int(input())

    for i in range(1,len(AoTypesList[AoID])):
        item = AoTypesList[AoID][i]
        if item[1] <= height and height <= item[2]:
            print()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Loại áo:',AoTypesList[AoID][0])
            print('Chiều cao:',height,'cm')
            print('Size áo phù hợp:',item[0])
            print('Dài Áo:',item[3],'cm')
            print('Ngang Ngực:',item[4],'cm')
            print('Dài Tay:',item[5],'cm')
            print('Rộng Vai:',item[6],'cm')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print()
            break

def ChonSizeQuan():
    print('\nChọn loại quần:')
    for i in range(len(QuanTypesList)):
        print(i,'-',QuanTypesList[i][0])

    print('\nNhập chỉ số quần:',end=' ')
    QuanID = int(input())
    while QuanID < 0 or QuanID >= len(QuanTypesList):
        print('Chỉ chấp nhận chỉ số từ 0 ->',len(QuanTypesList)-1)
        print('Nhập chỉ số quần:',end=' ')
        QuanID = int(input())

    print('\nNhập cân nặng (51-84):', end=' ')
    weight = int(input())
    while weight < 51 or weight > 84:
        print('Chỉ chấp nhận cân nặng từ 51Kg -> 84Kg')
        print('Nhập cân nặng (51-84):', end=' ')
        weight = int(input())

    for i in range(1,len(QuanTypesList[QuanID])):
        item = QuanTypesList[QuanID][i]
        if item[1] <= weight and weight <= item[2]:
            print()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Loại quần:',QuanTypesList[QuanID][0])
            print('Cân nặng:',weight,'Kg')
            print('Size quần phù hợp:',item[0])
            print('Rộng Cạp Đo 1/2:',item[3],'cm')
            print('Rộng Ngang Mông 1/2:',item[4],'cm')
            print('Rộng Ngang Ống 1/2:',item[5],'cm')
            print('Dài Quần:',item[6],'cm')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print()
            break

def ChonSize():
    print('Bạn muốn chọn size cho:')
    print('0 - Áo')
    print('1 - Quần')
    print()

    print('Nhập chỉ số:',end=' ')
    ID = int(input())
    while ID < 0 or ID > 1:
        print('Chỉ số chỉ có thể là 0 (Áo) hoặc 1 (Quần)')
        print('Nhập chỉ số',end=' ')
        ID = int(input())

    if ID == 0: ChonSizeAo()
    else: ChonSizeQuan()

    print('||||||||||||||||||||||||||||||||||||||||||||||||||\n')

print("~~~~~~~~~~~~~~~ Chương trình chọn số đo quần áo ~~~~~~~~~~~~~~~\n")

AoTypesList = []
with open('ao.txt',encoding='utf-8') as fi:
    ls = fi.read().split('\n')
    for i in range(len(ls)):
        if i%6==0:
            AoTypesList.append([ls[i]])
        else:
            AoTypesList[-1].append(ls[i].split())
            AoTypesList[-1][-1][1] = int(AoTypesList[-1][-1][1])
            AoTypesList[-1][-1][2] = int(AoTypesList[-1][-1][2])
    # for i in AoTypesList:
    #     print(i)
    #     print()

QuanTypesList = []
with open('quan.txt',encoding='utf-8') as fi:
    ls = fi.read().split('\n')
    for i in range(len(ls)):
        if i%5==0:
            QuanTypesList.append([ls[i]])
        else:
            QuanTypesList[-1].append(ls[i].split())
            QuanTypesList[-1][-1][1] = int(QuanTypesList[-1][-1][1])
            QuanTypesList[-1][-1][2] = int(QuanTypesList[-1][-1][2])

while True:
    ChonSize()