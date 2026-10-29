

def exercicio_1():
    """Leia dois números e mostre a soma deles."""
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input('Digite o segundo número:'))
    sum = num1 + num2
    print('A soma dos dois número é:', sum)



def exercicio_2():
    """Leia um número e informe se ele é par ou ímpar."""
    number = int(input('Digite um número: '))
    if number % 2 == 0:
     print('O número é par.')
    else:
     print('O número é ímpar.')


def exercicio_3():
    """Leia a idade de uma pessoa e informe se ela é maior de idade."""
    idade = int(input('Digite sua idade : '))
    if idade >= 18:
        print('Você é maior de idade.')
    else:
        print('Você é menor de idade.')


def exercicio_4():
    """Leia três números e mostre qual deles é o maior."""
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))

    if num1 >= num2 and num1 >= num3:
        print('O maior número é:',num1)
    elif num2 >= num1 and num2 >= num3:
        print('O maior número é:',num2)
    else:
        print('O maior número é',num3)


def exercicio_5():
    """Leia uma palavra e mostre quantas letras ela possui."""
    palavra = input('Digite uma palavra: ')
    print('A palavra posssui', len(palavra), 'letras.')

