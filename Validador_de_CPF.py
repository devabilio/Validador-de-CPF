def limpar_cpf(cpf):
    return cpf.replace('.', '').replace('-', '')


def tem_digitos_iguais(cpf):
    return cpf == cpf[0] * len(cpf)


def calcular_digito(cpf_base, peso_inicial):
    soma = 0
    peso = peso_inicial

    for numero in cpf_base:
        soma += int(numero) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        return 0
    else:
        return 11 - resto


def validar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    # validações iniciais
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    if tem_digitos_iguais(cpf):
        return False

    # primeiro dígito
    base = cpf[:9]
    digito1 = calcular_digito(base, 10)

    # segundo dígito
    base2 = base + str(digito1)
    digito2 = calcular_digito(base2, 11)

    # validação final
    return cpf[-2:] == f"{digito1}{digito2}"


def main():
    while True:
        cpf = input("Digite o CPF: ")

        if validar_cpf(cpf):
            print("CPF válido ✅")
        else:
            print("CPF inválido ❌")


# rodar programa
main()
