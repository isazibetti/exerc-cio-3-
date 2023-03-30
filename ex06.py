qtde= int(input('informe a quantidade:'))
valorUnit = float(input('informe o valor unitário:'))
desconto = float(input('informe o desconto:'))

totalSemDesconto = qtde * valorUnit
totalComDesconto = totalSemDesconto - (totalSemDesconto * desconto/100)

print(f'o total sem desconto será R$ {totalSemDesconto:.2f}')
print(f'O total com desconto será R$ {totalComDesconto:.2f}')