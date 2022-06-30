import requests as req
from bs4 import BeautifulSoup as bs
from prettytable import PrettyTable
def get_data(url):
    #Establishing Connection
    head = { 
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.54', 
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip', 
    'DNT' : '1', 
    'Connection' : 'close'
    }    
    if  url[0:22]!='https://www.amazon.in/':
        raise Exception('INCORRECT URL')
    r=req.get(url,headers=head)
    data=bs(r.text,'lxml')
    product=data.find_all(id='centerCol')
    title=product[0].find(id="productTitle").get_text().strip()
    print('\n\nTitle:',title)
    f=data.find(id="twister-plus-price-data-price")
    price=f.get('value')
    print('\nPrice:',price)
    global choice
    if choice==1:
        name=input('\n\nGive a name to this product: ')
        add([name,title,price,url])
        exit()
def get_price(url):
    head = { 
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.54', 
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip', 
    'DNT' : '1', 
    'Connection' : 'close'
    }    
    r=req.get(url,headers=head)
    data=bs(r.text,'lxml')
    f=data.find(id="twister-plus-price-data-price")
    price=f.get('value')
    return price
def add(l):
    f=open('prices.txt','r+')
    r=f.readlines()
    f.write(f'{l}\n')
    f.close()
def show():
    f=open('prices.txt','r')
    table=PrettyTable(['Name'])
    data=f.readlines()
    for i in data:
        d=eval(i)
        table.add_row([d[0]])
    print(table)
    n=input('\nEnter the name: ').lower()
    for i in data:
        d=eval(i)
        if d[0].lower()==n:
            print(f'\nTitle: {d[1]}',f'\nPrice:{d[2]}')
            res=check(d)
            break

    if change==0:
        return res
    else:
        print('New Price:',int(d[2])+change)
        data.remove(i)
        d[2]=int(d[2])+change
        data.append(str(d)+'\n')
        f=open('prices.txt','w')
        f.writelines(data)
        f.close()
        return res
def check(d):
    p=get_price(d[3])
    f=open('prices.txt','r')
    global change
    change=eval(p)-int(d[2])
    if change==0:
        return 'price has remained same'.title()
    elif change>0:
        return 'Prince Has Gone Up by:' +str(change)
    else: 
       return 'Prince Has Gone Down by:'+str(abs(change))

choice=int(input("\n1->Add Tracking For A New Product\n2->Check Current Price Of An Old Entry\nEnter Your Choice:"))
if choice==1:
    url=input('\nEnter The URL OF Product:')
    p=get_data(url)
if choice==2:
    print(show())
else:
    print('Invalid Input')
