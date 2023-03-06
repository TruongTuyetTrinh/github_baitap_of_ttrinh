Toan=int(input(''))
Ly=int(input(''))
Hoa=int(input(''))
g=(Toan*2+Ly*3+Hoa)/6
if g<3:
    print('Kem')
elif g<5:
    print('Yeu')
elif g<6:
    print('Trung binh')
elif g<7:
    print('Trung binh Kha')
elif g<8:
    print(' Kha')
elif g<9:
    print(' Gioi')
else:
    print(' Xuat sac')

    