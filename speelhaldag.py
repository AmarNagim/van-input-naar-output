# berekening feestlunch
# info: Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag. Jullie willen ook met zijn 
# allen voor 45 minuten in de VIP-VR-GameSeat. De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten. 
# Jij trakteert dus betaal je alles. Laat Python dat uitrekenen. Hoe duur wordt jouw speelhal-dag?
# dagticket_pp = 7.45, vip_per_5_min = 0.37, aantal_mensen = 4

print('Voer hieronder de gevraagde waardes in')                                                                         

dagticket_pp = int(input('Prijs dagticket per persoon: '))                                                            # alle waardes
vip_tijd = int(input('Hoeveel minuten VIP VR (stappen van 5): '))
aantal_mensen = int(input('Aantal mensen: '))

prijs_dagtickets = dagticket_pp*aantal_mensen                                                                         # berekeningen
prijs_vip_pp = vip_tijd*7.4
prijs_vip = prijs_vip_pp*aantal_mensen

prijs_totaal = prijs_dagtickets + prijs_vip
prijs_totaal_afgerond = round(prijs_totaal)
prijs_totaal_afgerond_int = int(prijs_totaal_afgerond)

print(f'De totaalprijs in eurocent is {prijs_totaal_afgerond_int}. En in euro\'s €{prijs_totaal_afgerond_int/100},-') # resultaat in euro's




