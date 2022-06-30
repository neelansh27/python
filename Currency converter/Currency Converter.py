import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup

#CREATING OF TABLE OF FEW CURRENCIES
print('\nSome Common Currencies:-') 
table=PrettyTable()
table.add_column('CURRENCY',['Australia Dollar','Euro','Japan Yen','USA Dollar','Afghanistan Afghani','Canada Dollar','India Rupee','Indonesia Rupiah','Malaysia Ringgit','Nepal Rupee'])
table.add_column('ABBREVATION',['AUD','EUR','JPY','USD','AFN','CAD','INR','IDR','MYR','NPR'])
print(table)
#TAKING VALUES FROM USER
currency=input('\nPLEASE ENTER THE CURRENCY YOU WANT TO CONVERT(abbreviation): ').upper()
To=input('\nTHE CURRENCY YOU WANT TO COVERT {} TO(abbreviation): '.format(currency)).upper()
amount=input('\nPLEASE ENTER THE AMOUNT: ')
#FETCHING DATA
data=requests.get('https://www.xe.com/currencyconverter/convert/?Amount={}&From={}&To={}'.format(amount,currency,To))
#CHECKING IF THE CONNECTION WAS SUCCESSFUL OR NOT
if not data.ok:
    print('Please Check the data you have entered')
    raise Exception('SOMETHING WENT WRONG')
#FINDIND THE VALUES AND THEN DISPLAYING THEM
content=BeautifulSoup(data.content,'lxml')
finder=content.find('p',class_='result__BigRate-sc-1bsijpp-1 iGrAod')
print('\nThe value of {} {} is {}'.format(amount,currency,finder.get_text()))
