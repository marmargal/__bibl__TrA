from .models import Book
from datetime import datetime
from django.db.transaction import commit_on_success

path = "ml-100k"
    
@commit_on_success
def populateBooks():
    print("Loading books...")
    Book.objects.all().delete()
    
    fileobj=open(path+"\\u.BOOKS", "r")
    line=fileobj.readline()
    while line:
        data = line.split(',')
        if len(data)>1:
            ide = data[0].strip()
            category = data[1].strip()
            title = data[2].strip()
            autor = data[3].strip().decode('utf-8', 'replace')
            Book.objects.create(category=category, title=title, autor=autor)   
        line=fileobj.readline()
    fileobj.close()
    
    print("Books inserted: " + str(Book.objects.count()))
    print("---------------------------------------------------------")
    

    
    
def populateDatabase():
    populateBooks()
    print("Finished database population")
    
if __name__ == '__main__':
    populateDatabase()