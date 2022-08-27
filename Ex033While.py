print('--' * 7)
print('LOJA BARATO!')
total = totmil = menor = cont = 0
barato = ' '
while True:
    print('--' * 7)
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco >= 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'A soma dos produtos é R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1.000')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')

