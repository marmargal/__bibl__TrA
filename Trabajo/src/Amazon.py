'''
Created on 10 ene. 2018

@author: inmam
'''


from bs4 import BeautifulSoup
from pip._vendor import requests

def obtener_categorias():
    req = requests.get("https://www.amazon.es/Libros-Categorias/b/ref=sv_b_0?ie=UTF8&node=599365031")
    data = req.text
    soup = BeautifulSoup(data, 'html.parser')
    
    categorias = []
    
    for c in soup.find_all(class_= "vxd-brandfarm-row"):#"vxd-brand-tile-links"):
        for i in c.find_all('a'): 
            #print (i.text, i.get('href'))
            cat = i.text
            enlace = i.get('href')
            if (len(cat)>2):
                
        
                categorias.append([cat, "https://www.amazon.es"+enlace])
        
        
    return categorias

            
#soup.find_all("h2", attrs={"class":"a-size-medium s-inline s-access-title a-text-normal"})
#<span class="a-size-small a-color-secondary">Alex Ross y </span>

def obtener_libros_categoria():
    
    Libros_categoria = []
    res = []
    
    
    for c in obtener_categorias():
        req = requests.get(c[1])
        data = req.text
        soup = BeautifulSoup(data, 'html.parser')
        Libros = []
        Autores = []
        for libro in soup.find_all("h2", attrs={"class":"a-size-medium s-inline s-access-title a-text-normal"}):
            #print libro.text
            Libros.append(libro.text)
            Libros_categoria.append([c[0], Libros])
            
        for a in soup.find_all("div", attrs={"class":"a-row a-spacing-none"}):
            au= a.find_all("span", attrs={"class":"a-size-small a-color-secondary"})
            if(len(au)>1):
                autor = au[1].text
                if (autor[len(autor)-2]=="y"):
                    autor = au[1].text[0:(len(au[1].text)-2)]
            
                Autores.append(autor)
                
        for i in zip(Libros, Autores):
            if [c[0],i] not in res:  res.append([c[0], i])
            
        #for r in res: print r
        
    return res

   

 