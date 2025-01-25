#Programa para calcular el imc de una persona

print("Calcula tu IMC")

peso=float(input('Tu peso en kg: '))
if peso<0:
    print('El peso no es valido')
else:
    altura=float(input('Tu altura en m: '))
if peso<0:
    print('El peso no es valido')
else:
    imc=peso / (altura*altura)
print("Tu IMC es de: ", imc)
if imc<18.5:
    print('Bajo de peso')
elif imc<25:
    print('Eres normal')
elif imc <30:
    print('Tienes SOBREPESO')
elif imc <35:
    print('Tienes OBESIDAD')
elif imc <40:
    print('Tienes OBESIDAD II')
elif imc <45:
    print('Tienes OBESIDAD III')
elif imc>50:
    print('Morfido')
