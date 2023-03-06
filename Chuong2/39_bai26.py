Hoten=str(input('Ho ten: '))
Songaycong=int(input('So ngay cong: '))
Dongiangaycong=int(input('Don gia ngay cong: '))
Hesophucap=float(input('He so phu cap: '))
Tamung=int(input('Tam ung: '))
Luong=Dongiangaycong*Songaycong*Hesophucap
Thuclinh=Luong-Tamung
print('Nhan vien ',Hoten,',',' Co tien luong=',round(Luong,1),',',' Tam ung=',round(Tamung,1),' va Thuc linh=',round(Thuclinh,1),sep='')
