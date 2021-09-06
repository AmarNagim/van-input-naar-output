# info: van input naar output 
# Maak een programma person.py dat de gebruiker om zijn naam, adres, postcode en woonplaats vraagt met duidelijke prompts.
# Laat het programma daarna een adreskaart (met lijntjes) tonen in de terminal
# test het programma grondig. Maak daarvan printscreens . Sla het person.py + printscreens op in de map van-input-naar-output
# Als je dit gecommit hebt kan je deze lab afvinken.

import time

                                        # message prompts
print('Bedankt voor het bezoeken van onze website.')
time.sleep(1)                           # time delay before next function is executed

print('')                               # line spacer
                        
print('Vul hieronder uw gegevens in')
                                                                     
name = input('Naam: ')                  # inputs & variables
adress = input('Adres: ')
zipcode = input('Postcode: ')
city = input('Woonplaats: ')

print('')                               # line spacer

print('Gegevens worden verwerkt..')     # your data is being processed
time.sleep(1)

                                        # print data
print(f"""    
---------------------------                          
|  Naam      : {name}
|  Adres     : {adress}
|  Postcode  : {zipcode}
|  Woonplaats: {city}
---------------------------                           """)

print('')                               # line spacers

print('Uw bestelling is geplaatst!')    # your order has been placed

time.sleep(7)                           # time delay before script ends

