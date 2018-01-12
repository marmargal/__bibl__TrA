'''
Created on 11 ene. 2018

@author: inmam
'''
from Tkconstants import RIGHT, Y, END, LEFT, BOTH
from Tkinter import Toplevel, Scrollbar, Listbox, Tk, Button
import sqlite3

from src import Amazon


def imprimir_etiqueta(cursor):
    v = Toplevel()
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, width=150, yscrollcommand=sc.set)
    for row in cursor:
        lb.insert(END,row[0])
        lb.insert(END,row[1])
        lb.insert(END,row[2])
        lb.insert(END,'')
    lb.pack(side = LEFT, fill = BOTH)
    sc.config(command = lb.yview)


def almacenar_libros():
    conn = sqlite3.connect('books.db')
    conn.text_factory = str
    
    conn.execute("DROP TABLE IF EXISTS BOOKS")
    conn.execute(''' CREATE TABLE BOOKS
                (BOOK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                CATEGORIA TEXT,
                TITULO TEXT,
                AUTOR TEXT ); ''')
    libros = Amazon.obtener_libros_categoria()
    for l in libros:
        conn.execute(""" INSERT INTO BOOKS (CATEGORIA, TITULO, AUTOR) 
                        VALUES (?,?,?) """, (l[0],l[1],l[2]))
    conn.commit()
    cursor = conn.execute("SELECT CATEGORIA, TITULO, AUTOR FROM BOOKS")
    imprimir_etiqueta(cursor)
    conn.close()

def listar_bd():
    conn = sqlite3.connect('books.db')
    conn.text_factory = str  
    cursor = conn.execute("SELECT CATEGORIA, TITULO, AUTOR FROM BOOKS")
    imprimir_etiqueta(cursor)
    conn.close()    
    


def ventana():
    top = Tk()
    almacenar = Button(top, text="Almacenar libros", command=almacenar_libros)
    almacenar.pack(side=LEFT)
    listar = Button(top, text="Listar libros", command=listar_bd)
    listar.pack(side=LEFT)
    salir = Button(top,text="Salir", command=exit)
    salir.pack(side=LEFT)
    top.mainloop()    
    

ventana()
