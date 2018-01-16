from django.contrib import admin
from principal.models import Book
from principal.models import Comment
from principal.models import Reader

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Reader)