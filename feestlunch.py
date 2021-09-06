# berekening feestlunch
# info: Je wilt 17 croissantjes van elk 39 eurocent en 2 stokbroden van elk 2,78 euro kopen. 
# je hebt 3 kortingsbonnen van 50 eurocent. Hoeveel geld moet je betalen? Laat Python dat uitrekenen.
# alle waardes op een rijtje: aantal croissantjes: 17, croissant prijzen 0.39 euro, aantal stokbroden: 2
# stokbrood prijs: 2.78 euro, aantal kortingsbonnen: 3, kortingsbon waarde: 0.50 euro

import time

print('We gaan het totaal bedrag berkenen van de feestlunch.')

time.sleep(1)
print('')

print('Vul hier de gevraagde waardes in centen')
croissant_amount = int(input('Aantal croissantjes: '))             # croissant
single_croissant_price = int(input('Prijs per croissant: '))
stokbrood_amount = int(input('Aantal stokbroden: '))               # stokbrood
single_stokbrood_price = int(input('Prijs per stokbrood: '))
coupon_amount = int(input('Aantal kortingsbonnen: '))              # kortingsbon
single_coupon_price = int(input('Waarde van een enkele kortingsbon: '))

price_croissant = croissant_amount*single_croissant_price       
price_stokbrood = stokbrood_amount*single_stokbrood_price
price_coupon = coupon_amount*single_coupon_price
price_after_coupon = price_croissant + price_stokbrood - price_coupon
price_after_coupon_2decimals = round(price_after_coupon, 2)
price_after_coupon_str = str(price_after_coupon_2decimals)

print('')

print('De totaalprijs van de feestlunch is ' + price_after_coupon_str + f' eurocent. In euro\'s is dat €{price_after_coupon/100},- ') # result in cents and euro's