#CALCULADORA EM PYTHON

print('********* CALCULADORA PYTHON *********')
print('SELECIONE O NÚMERO DA OPÇÃO DESEJADA: ')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

operacao = int(input('Informe a operação desejada: 1/2/3/4: ')) 
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if (operacao > 4):
    print('Operação Inválida')
elif (operacao == 1):
        resultado = n1+n2
        print('o resultado da soma é: ',resultado)
elif (operacao == 2):
        resultado = n1-n2
        print('o resultado da subtração é: ',resultado)
elif (operacao == 3):
        resultado = n1*n2
        print('o resultado da multiplicação é: ',resultado)
else:
    (operacao == 4)
    resultado = n1/n2
    print('o resultado da divisão é: ',resultado)      
