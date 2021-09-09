# F1.2.03.O2 - Pizzacalculator
# Amar Nagim
# opdracht: Pizza Calculator

import time
import sys

small = '€8,-'                                                             # variables
medium = '€10,-'
large = '€12,-'

small_digit = 8
medium_digit = 10
large_digit = 12

total_order = []
seperator = """ 
                      """
total_price = []                   

print('Welkom bij Dominos!')
print('')

def order():                                                              # function of the script

   global total_order                                                     # bringing the global variables into the function
   global seperator
   global total_price
   global small
   global medium
   global large
   global small_digit
   global medium_digit 
   global large_digit
   
   
   print('Kies hieronder de opties van uw pizza:')
   time.sleep(1)

   size = input('Small, medium of large: ').lower()
   print('')
                                                                        # choice of pizza sizes and lists
   if size == 'small':  
    print(f'U heeft pizza small gekozen. Dit kost {small}')
    total_order.append(f'Pizza small {small}')
    total_price.append(small_digit)
   elif size == 'medium':
    print(f'U heeft pizza medium gekozen. Dit kost {medium}')
    total_order.append(f'Pizza medium {medium}') 
    total_price.append(medium_digit)
   elif size == 'large':
    print(f'U heeft pizza large gekozen. Dit kost {large}')
    total_order.append(f'Pizza large {large}')
    total_price.append(large_digit)
   else:
       order()
       print('We hebben u niet begrepen. Probeer het opnieuw.')
   
   order_again = {'j':True,'n':False}.get(input('Wilt u nog een pizza bestellen? J/N: ').lower())  # order again option 
   
   if order_again == True:
       print('')
       print('U word over enkele ogenblikken doorgestuurd naar ons pizza keuzemenu.')
       time.sleep(1)
       order()
   else:
       print('')
       print('')
       print(f"Uw totale bestelling: {(seperator.join(total_order))} ")                            # order overview
       total_price_sum = sum(total_price)
       print (f'                      De totaalprijs is: €{total_price_sum},-')
       time.sleep(10)
       sys.exit



order()


