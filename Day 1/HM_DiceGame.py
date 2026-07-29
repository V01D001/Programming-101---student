'''
dice game: momxmarebeli sheiyvans ricxvs 1-idan 6-is chatvlit(
tu ricxvi iqneba 6 ze magali an 1 ze dabali daiweros "sheiyvanet mxolod 1-6 ricxvebi) .
tu ricxvi daemtxveva random ricxvs(aseve 1-6) gamoitanet "you win" + random ricxvi , ricxvi.
sxva shemtxvevashi "you lose" + ricxvi , random ricxvi
'''
import random

Input = int(input("Choose number between 1 - 6: "))
rand = random.randint( 0, 6)

if Input not in range(0, 6):
    print("sheiyvanet mxolod 1-6 ricxvebi")
elif Input == rand:
    print("You Win! Random Number = " , random , "Your number = " , Input)
else:
    print("You Lose, Random Number = " ,  rand , "Your Number = " , Input)