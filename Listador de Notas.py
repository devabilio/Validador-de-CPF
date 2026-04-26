import time
import os
while True:
    notas = []

    for x in range(3):
        cd_ao = input("ID: ")
        nt = float(input("Nota: "))
        rst = [cd_ao, nt]
        notas.append(rst)
    os.system("cls")

    for n in notas:
        cd_ao = n[0] #nome do aluno
        rst = n[1] #nota do aluno
        print (f"Nome:{cd_ao}")
        print (f"Nota:{rst}")
    time.sleep(10)
    os.system("cls")
    print ("Notas Listadas! Até!!")
    time.sleep(3)
    break
