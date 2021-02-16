from Auto import Auto

alvari_uus_auto = Auto("Audi", "A6", 2017)
minu_uus_auto = Auto("Tesla", "Mudel 3", 2020)

print(alvari_uus_auto.kirjeldus())
alvari_uus_auto.odomeeter()
alvari_uus_auto.odomeeteri_nait = 3
alvari_uus_auto.uuenda_odomeeter(-2)
alvari_uus_auto.suurenda_odomeeter(30)
alvari_uus_auto.odomeeter()

print(minu_uus_auto.kirjeldus())
minu_uus_auto.odomeeter()
minu_uus_auto.odomeetri_nait = 5