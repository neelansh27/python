#Importing modules
import requests
import bs4
def meaning(soup,word):
    defination= soup.find_all(class_="dtText")
    example=soup.find_all(class_="ex-sent first-child t no-aq sents")
    print("\nMeaning of "+word.title()+'\n')
    for i in defination:
        print(i.text)
    print("\nExamples:")
    for i in example:
        print(i.text.title().strip())
def synonyms(soup,word):
    syn=soup.find(class_="mw-list")
    if syn==None:
       return  syn
    syn=syn.text.strip()
    print("\n\nSynonyms Of {} Are:".format(word.title()),end=" ")
    for i in syn.split():
        print(i.capitalize(),end=' ')
    print()
def owd(soup):
    a=soup.find(id="other-words-anchor")
    print("\n\n"+a.h2.text)
    for i in a.find_all(class_="uro"):
        print(i.find(class_="ure").text+' : '+i.find(class_="fl").text)

head={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
word=input('\n\nEnter The Word:')
url = 'https://www.merriam-webster.com/dictionary/'+word
res = requests.get(url,headers=head)
if not res.ok:
    raise Exception("connection error")

soup = bs4.BeautifulSoup(res.text, "lxml")
try:
    meaning(soup, word)
    synonyms(soup, word)
    owd(soup)
except AttributeError:
    pass 
