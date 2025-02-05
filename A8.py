"""******************************
#Pāvels Petrovs, pp23055
#A8. Dots naturāls skaitlis n. Izdrukāt tos skaitļa n reizinātājus, kuri ir kāda naturāla skaitļa kvadrāti.
#Programma izveidota: 30.09.2023
******************************"""

while True:
    n = int(input("Ievadiet naturālu skaitļu n: "))
    if n <= 0: #Pārbaude, vai 'n' ir naturāls skaitlis
        print("N nav naturals skaitlis")
        print()
        continue #Ja 'n' nav naturāls skaitlis, tad programma atkal prasa ievadīt naturālu skaitļu 'n'.

    print("Naturāla skaitļa kvadrāti:", end = " ")
    for i in range(1, n + 1): #Sāk for cilpu, kas atkārtojas caur skaitļiem no 1 līdz 'n'. Tas ietver 'n' diapazonā, izmantojot 'n + 1'.
        if n % (i * i) == 0: #Pārbauda, ​​vai 'i' ir ideāls kvadrāts, kas sadala 'n' bez atlikuma.
            print(i * i, end = " ")
    print()

    ok = int(input("Vai turpināt (1) vai beigt (0)?\n",))
    print()
    if ok != 1: #Pārbauda, ​​vai vērtība 'ok' nav vienāda ar 1. 
                #Ja tā, programma beidzas. Ja 'ok' ir vienāds ar 1 programma atkārtojas no sākuma, liekot lietotājam ievadīt jaunu vērtību 'n'.
        break

