from Auto import Auto
from elektriauto import elektriauto

minu_uus_auto = Auto("Audi", "A6", 2017)
alvari_uus_auto = Auto("Tesla", "Mudel 3", 2020)

print(alvari_uus_auto.kirjeldus())
alvari_uus_auto.odomeeter()
alvari_uus_auto.odomeeteri_nait = 3
alvari_uus_auto.uuenda_odomeeter(2)
alvari_uus_auto.suurenda_odomeeter(30)
alvari_uus_auto.odomeeter()

tesla = elektriauto("Tesla", "Mudel S", 2019)
print(tesla.kirjeldus())
tesla.aku_kirjeldus()
tesla.odomeeter()
tesla.suurenda_odomeeter(50)
tesla.odomeeter()

print(minu_uus_auto.kirjeldus())
minu_uus_auto.odomeeter()
minu_uus_auto.odomeetri_nait = 5
minu_uus_auto.tangi(30)