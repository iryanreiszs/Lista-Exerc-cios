#Exercício 1

x = int(input('Escolha um número inteiro: '))
y = int(input('Escolha outro número inteiro: '))
print ('Qual a soma desses números:', (x + y))

#Exercício 2

x_valor_em_metros = int(input('Escolha um valor em metros: '))
print('y valor convertido de metros para milímetros =', x_valor_em_metros * 1000)

#Exercício 3

Dia = int(input('Dias: ')) * 86400
Horas = int(input('Horas: ')) * 3600
Minutos = int(input('Minutos: ')) * 60
Segundos = int(input('Segundos: '))
print(Dia + Horas + Minutos + Segundos)

#Exercício 4

Salário = float(input('Salário (em R$): '))
Aumento = float(input('Aumento (em %): '))
Novo = Salário + Salário * Aumento / 100
print (f'Novo salário: {Novo:.2f}')

#Exercício 5

Preço = float(input('Qual o preço da mercadoria (em R$)?'))
Desconto = float(input('Qual o desconto(em %)?'))
Valor_do_preço = Preço - Preço * Desconto / 100
print('O valor total da mercadoria será de: ',f'R${Valor_do_preço:.2f}')

#Exercício 6

Distância = float(input('Qual a distância a ser percorrida na viagem (em Km)?'))
Velocidade_média = int(input('A Velocida Média esperada nessa viagem em (Km/h) será de:'))
Tempo_de_viagem = Distância / Velocidade_média
print('O tempo da viagem (em horas)será de: ',f'{Tempo_de_viagem:.2f} horas')

#Exercício 7

TemperaturaC = int(input('Escolha uma temperatura em (°C) para ser transformada em fahrenheit: '))
Temperatura_em_Fahrenheit = TemperaturaC * 9 / 5 + 32
print(' A temperatura em Fahrenheit é de: ',f'{Temperatura_em_Fahrenheit}')

#Exercício 8

TemperaturaF = float(input('Escolha uma temperatura em (°F) para ser transformada em (°C)'))
Temperatura_em_Celsius = (TemperaturaF - 32) / 1.8
print(' A temperatura em Celsius será de: ',f'{Temperatura_em_Celsius:.2f}')

#Exercício 9

Dias = int(input('Por quantos dias o carro foi alugado?'))
Distância_percorrida = float(input('Qual a distância total percorrida percorrida (em Km)?'))
Preço_a_pagar = (Dias * 60) + (0.15 * Distância_percorrida)
print('O preço a pagar será de ',f' {Preço_a_pagar:.2f} R$')

#Exercício 10

Cigarros_por_dia = int(input('Quantos cigarros fuma por dia?'))
Anos_fumados = int(input('Fuma faz quantos anos?'))
Total_cigarros = Cigarros_por_dia * Anos_fumados * 365
Minutos_totais_perdidos = 10 * Total_cigarros
Dias_perdidos = Minutos_totais_perdidos / (1440)
print(f'Você perdeu aproximadamente {Dias_perdidos:.2f} dias de vida pelo hábito de fumar')

#Exercício 11

print (len(str(2 ** 10000)))

#Exercício 12

a = int(input('Qual o valor do lado (a) do triângulo? '))
b = int(input('Qual o valor do lado (b) do triângulo? '))
c = int(input('Qual o valor do lado (c) do triângulo? '))
if a + b > c and a + c > b and b + c > a:
 if a != b and a != c and b != c:
    print ('O triângulo existe e é escaleno')
 if a == b and a != c:
    print ('O triaângulo existe e é isósceles')
 if a == b and a == c:
    print (' O triângulo existe e é equilátero')
else:
    print ('O triângulo não existe')

#Exercício 13

year = int(input('Escolha um ano: '))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
 print ('O ano é bissexto')
else:
 print ('O ano não é bissexto')

#Exercício 14

peso = float(input('Quantos Kg de peixe João trouxe? '))
excedente = (peso - 50)
multa = (excedente * 4)
if peso > 50:
    print(f'João pagará uma multa de:R${multa:.2f}')
else:
    print(f'João não pagará multa por peso excedente')

#Exercício 15

a = float(input('Escolha um número: '))
b = float(input('Escolha outro número: '))
c = float(input('Escolha novamente outro número: '))
if a > b and a > c:
    print(f'O maior valor entre os números escolhidos é: {a}')
elif a < b and b > c:
    print(f'O maior valor entre os números escolhidos é: {b}')
elif a < c and c > b:
    print(f'O maior valor entre os números escolhidos é: {c}')
if a == b and a == c:
    print(f'O maior valor não existe pois todos os números são iguais, mas podendo ser {a}')

#Exercício 16 

a = float(input('Escolha um número: '))
b = float(input('Escolha outro número: '))
c = float(input('Escolha novamente outro número: '))
maior = max(a, b, c)
menor = min(a, b, c)
print(f'O maior número é:{maior}')
print(f'O menor número é:{menor}')

#Exercício 17

money = float(input('Quantos reais você ganha por hora? '))
horas_mês = int(input('Quantas horas você trabalha por mês? '))
sb = horas_mês * money
ir = sb * 0.11
inss = sb * 0.08
sind = sb * 0.05
sl = sb - ir - inss - sind
print(f'Salário Bruto: R$ {sb:.2f}')
print(f'IR (11%): R$ {ir:.2f}')
print(f'INSS (8%): R$ {inss:.2f}')
print(f'Sindicato (5%): R$ {sind:.2f}')
print(f'Salário Líquido: R$ {sl:.2f}')

#Exercício 18

area = float(input('Qual o tamanho da área (em metros quadrados) a ser pintada? '))
litros = area / 3
latas = int(litros / 18)
if litros % 18 != 0:
 latas += 1
preço = latas * 80
print(f'Você precisará de {latas} lata(s) de tinta')
print('O preço total é:R$ ',f'{preço:.2f}')

#Exercício 19

nota = float(input('Digite uma nota: '))
while nota < 0 or nota > 10:
    print('Digite uma nota de 0 a 10: ')
    nota = float(input('Digite uma nota: '))

#Exercício 20

usuário = input('Digite seu usuário: ')
senha = input ('Digite sua senha: ')
while usuário == senha:
    print('A senha deve ser diferente do usuário')
    usuário = input('Digite seu usuário: ')
    senha = input ('Digite sua senha: ')

#Exercício 21

a = 80000
b = 200000
anos = 0
while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    anos = anos + 1
print (anos)
    
#Exercício 22

n = int(input('Digite um número: '))

a, b = 1, 1
k = 1

while k <= n-2:
    a, b = b, a + b
    k = k + 1

print (b)

#Exercício 23

a = int(input('Digite um valor para (a): '))
b = int(input('Digite um valor para (b): '))
while a % b != 0:
    a, b = b, a%b
print(f'O MDC é: {b}')