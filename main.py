fluxo_caixa = []

print("----------")
print("@ Fluxo Caixa")
print("----------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("3 - Sair\n")

def adicionar_transacao():
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor
    })

while True:
    opcao = int(input("Digite a opção: "))

    if opcao == 1 or opcao == 2:
        adicionar_transacao()
    elif opcao == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")

# Nota Fiscal

total = 0
for fc in fluxo_caixa:
    print("Nome:", fc['nome'], ", Valor: R$", fc['valor'])
    total += fc['valor']

print("Saldo atual: R$", total)
