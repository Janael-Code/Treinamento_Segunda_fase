import decimal_outra
import baseDecimalToOutra

numero = str(input("Digite o Numero a ser convertido :")).upper()
base = int(input("""Qual a base
[ 1 ]- Hexadecimal
[ 2 ]- Octadecimal
[ 3 ]- Binária
[ 4 ]- Decimal :"""))

baseFutura = int(input("""Escolha a base para convesão:
[ 1 ]- Hexadecimal
[ 2 ]- Octadecimal
[ 3 ]- Binária
[ 4 ]- Decimal :"""))


if base == 1:
  if baseFutura == 1:
    print(numero)
  
  elif baseFutura == 2:
    res = decimal_outra.baseDecimalParaOutra(numero, 16)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 18)
    print(res1)
  
  elif baseFutura == 3:
    res = decimal_outra.baseDecimalParaOutra(numero, 16)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 2)
    print(res1)

  elif baseFutura == 3:
    res = decimal_outra.baseDecimalParaOutra(numero, 16)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 10)
    print(res1)

elif base == 2:   
  if baseFutura == 1:
    res = decimal_outra.baseDecimalParaOutra(numero, 10)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 16)
    print(res1)
  
  elif baseFutura == 2:
    res = decimal_outra.baseDecimalParaOutra(numero, 18)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 18)
    print(res1)
  
  elif baseFutura == 3:
    res = decimal_outra.baseDecimalParaOutra(numero, 18)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 2)
    print(res1)

  elif baseFutura == 3:
    res = decimal_outra.baseDecimalParaOutra(numero, 18)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 10)
    print(res1)


elif base == 3:
  if baseFutura == 1:
    res = decimal_outra.baseDecimalParaOutra(numero, 2)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 16)
    print(res1)
  
  elif baseFutura == 2:
    res = decimal_outra.baseDecimalParaOutra(numero, 2)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 18)
    print(res1)
  
  elif baseFutura == 3:
    res = decimal_outra.baseDecimalParaOutra(numero, 2)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 2)
    print(res1)

  elif baseFutura == 3:
    res = decimal_outra.baseDecimalParaOutra(numero, 2)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 10)
    print(res1)


elif base == 4:
  if baseFutura == 1:
    res = decimal_outra.baseDecimalParaOutra(numero, 10)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 16)
    print(res1)
  
  elif baseFutura == 2:
    res = decimal_outra.baseDecimalParaOutra(numero, 10)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 18)
    print(res1)
  
  elif baseFutura == 3:
    res = decimal_outra.baseDecimalParaOutra(numero, 10)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 2)
    print(res1)

  elif baseFutura == 3:
    res = decimal_outra.baseDecimalParaOutra(numero, 10)
    res1 = baseDecimalToOutra.base_DecimalPara_Outra(res, 10)
    print(res1)