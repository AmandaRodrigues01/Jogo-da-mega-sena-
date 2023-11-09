import random
quant =1
#lista = [random.randint(1,61), random.randint(1,61), random.randint(1,61),random.randint(1,61),random.randint(1,61),random.randint(1,61)]

#lista = [[1,2, 3,4,5 ,6]]
import time
print('-------JOGO DA MEGA SENA--------')
vezes = int(input('Quantos jogos você quer que eu Sorteie?:'))

print(F'--== SORTEANDO {vezes} JOGOS--==')
time.sleep(0.5)
print('Analisando...')
time.sleep(0.5)
for vezes in range(1,vezes+1):
       for quant in range(vezes):
            
          lista = [random.randint(1,61), random.randint(1,61), random.randint(1,61),random.randint(1,61),random.randint(1,61),random.randint(1,61)]
          
          lista.sort(reverse=False)
          lista * vezes
         
          time.sleep(0.5)
         
       print(f'Jogo {vezes}:{lista}')
time.sleep(0.4)
print('--==--==BOA SORTE--==--==')

computador =[random.randint(1,61),random.randint(1,61),random.randint(1,61),random.randint(1,61),random.randint(1,61),random.randint(1,61)]
computador.sort(reverse=False)
time.sleep(1)
print('Os números SORTEADOS FORAM...')
time.sleep(3)
if computador in lista:
      print(f'os numeros sorteados foram {computador} PARABÉNS VOCE GANHOU !!!')
if computador[0] and computador[1] and computador[2] and computador[3] and computador[4] in lista or computador[5] or computador[6] in lista:
     print(f'os numeros sorteados foram {computador} PARABÉNS VOCE GANHOU a QUADRA !!!')

     if computador[0]and computador[1] and computador[2] and computador[3] and computador[4] and computador[5] in lista:
          print(f'os numeros sorteados foram {computador} PARABÉNS VOCE GANHOU a QUINA !!!')
else:
     print(f'Que Pena! Os números sorteados foram {computador} e eles nao estao no seu sorteio,\n mais sorte da PROXÍMA VEZ!!')
