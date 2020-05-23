print('Calculadora IMC')
weight = float (input('Insira o peso (kg): '))
height = float (input('Insira a altura (m): '))
imc = weight/(height ** 2)

print('IMC = {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.6 <= imc < 24.9:
    print('Peso Normal')
elif 25 <= imc < 29.9:
    print('Sobrepeso')
elif 30 <= imc < 34.9:
    print('Obesidade grau 1')
elif 35 <= imc < 39.9:
    print('Obesidade grau 2')
elif imc >= 40:
    print('Obesidade grau 3')   