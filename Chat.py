import os

msg = []

nome = input("Nome: ")

while True:
    #limpando terminal

    os.system('cls')

    if len(msg) > 0:
        for n in msg:
            print(n['nome'], "-", n['texto'])

    print("_______________")
    print("Digite 'fim' para sair!")

    #obtendo o txt
    txt = input("Mensagem: ")
    if txt == "fim":
        break

    #adiconando msg na lista
    msg.append({
        "nome": nome,
        "texto": txt
    })
