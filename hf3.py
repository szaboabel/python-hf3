kor=int(input("életkor: "))

if kor >= 18:
    print("nagykorú")
elif kor < 18:
    print("kiskorú")


ev=int(input("születési év: "))

if ev <= 1900 or ev >= 2021:
    print("valószinűtlen évszám")
elif ev > 2004:
    print("kiskorú")
elif ev <= 2004:
    print("nagykorú")


kmin=int(input("hívás kezdete perc: "))
ksec=int(input("hívás kezdete másodperc: "))
vmin=int(input("hívás vége perc: "))
vsec=int(input("hívás vége másodperc: "))

hivash1=kmin/60
hivash2=vmin/60
hivasmin1=ksec/60
hivasmin2=vsec/60
ora=hivash2-hivash1
perc=hivasmin2-hivasmin1
if ora < 24 and perc < 1440:
    print(f"A hívás{ora}óra és {perc}perc")
else:print("Nem érvényes időadat")