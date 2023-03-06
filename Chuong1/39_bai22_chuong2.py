gianiemyet=int(input("Nhap Gia niem yet: "))
chietkhau=int(input("Nhap Chiet khau:"))
VAT=(gianiemyet-chietkhau)*0.01
giaban=gianiemyet-chietkhau+VAT
print("Gia ban",giaban)
