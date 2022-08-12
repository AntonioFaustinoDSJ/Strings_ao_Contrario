from time import sleep
print()
print('-=-'*5, 'STRINGS AO CONTRÁRIO', '-=-'*5)
print()
txt = str(input('Digite o seu nome: ')).strip().upper()

print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)

print('Seu nome ao contrário é:', end=' ')

lenTXT = len(txt)
sliTXT = txt[lenTXT::-1]
print(sliTXT)

print()
print('-=-'*17)

