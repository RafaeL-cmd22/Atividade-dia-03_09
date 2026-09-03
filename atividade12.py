AnoNascimento = int(input("Digite o ano de nascimento:"))
AnoAtual = int(input("Digite o ano atual:"))

idadeAtual = AnoAtual - AnoNascimento
idadeFutura = idadeAtual + 17
print(f"idade atual: {idadeAtual} anos")
print(f"idade daqui a 17 anos: {idadeFutura} anos")
