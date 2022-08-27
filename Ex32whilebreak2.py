cont = conth = contm = 0
while True:
    print('-=-' * 7)
    print('CADASTRO DE PESSOAS')
    print('-=-' * 7)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo == 'F' and idade < 20:
        contm += 1
    if sexo == 'M':
        conth += 1
    if idade > 18:
        cont += 1
    print('-' * 23)
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

print('programa finalizado!')
print(f'{cont} Pessoas tem mais de 18 anos! ')
print(f'{conth} Homems foram cadastrados')
print(f'{contm} Mulheres tem menos de 20 anos')

