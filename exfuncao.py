def collatz(number):
    if number % 2 == 0:
        print(f'{number}//2 = {number//2}')
        return number//2
    else:
        print(f'3 * {number} + 1 = {3*number+1}')
        return 3*number+1
    
def inserir():
    try:
          numero = int(input("Digite um número: "))
          while numero != 1:
                 numero = collatz(numero)
    except ValueError:
        print('Caractere inválido.Digite um número inteiro.')

        