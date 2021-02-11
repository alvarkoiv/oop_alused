import random

from sodur import sodur
#loome 2 eksemplari sodur klassi põhjal
sodur1 = sodur()
sodur2 = sodur()
#väljastame iga soduri tervise väärtuse
print("1. soduri tervis = " + str(sodur1.tervis))
print("2. soduri tervis = " + str(sodur2.tervis))
#võistluse algoritm
while (sodur1.tervis == 0 or sodur2.tervis == 0):
    soduri_nr = random.randint(1, 2)
    if(soduri_nr == 1):
        print("Esimene lööb teist")
        sodur2.tervis -= 20
        print(("2. soduri tervis = ") + str(sodur2.tervis))
    if(soduri_nr == 2):
        print("Teine lööb esimest")
        sodur1.tervis -= 20
        print("1. soduri tervis = ") + str(sodur1.tervis)
    if(sodur1.tervis == 0 or sodur2.tervis == 0):
        break

if(sodur1.tervis == 0):
    print("Teine sõdur on võitnud")
if(sodur2.tervis == 0):
    print("Esimene sõdur on võitnud")
if(sodur1.tervis == 0 and sodur2.tervis == 0):
    print("Keegi ei võitnud")