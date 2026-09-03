TempoViagem = float(input('Digite o tempo de viagem em horas: '))
VelocidadeMedia = float(input("Digite a velocidade média em km/h: "))
litrosConsumidos = (TempoViagem * VelocidadeMedia) / 12
print(f"A quantidade de litros consumidos na viagem será: {litrosConsumidos} litros")
