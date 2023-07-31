from django.shortcuts import render
from .models import Book
from datetime import datetime
from django.core.paginator import Paginator


class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
   format = "%Y-%m-%d"

   def to_python(self, value: str) -> datetime:
       return datetime.strptime(value, self.format)

   def to_url(self, value: datetime.date) -> str:
       return value.strftime(self.format)

from django.urls import register_converter
register_converter(DateConverter, 'date')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    
    #date = request.Get.get('pub_date')

    context = {"books":books}
    return render(request, template, context)


def books_date(request, date:datetime.date):
    template = 'books/books_list.html'
    books_all = Book.objects.all()
    books, previous_books, next_books = [], [], []
    
    for book in books_all:
        if DateConverter.to_url(DateConverter,book.pub_date) == DateConverter.to_url(DateConverter,date):
            books.append(book)

        elif DateConverter.to_url(DateConverter,book.pub_date) < DateConverter.to_url(DateConverter,date):
            previous_books.append(book)

        elif DateConverter.to_url(DateConverter,book.pub_date) > DateConverter.to_url(DateConverter,date):
            next_books.append(book)


    if previous_books:
        previous = previous_books[0]

        for book in previous_books:
            if book.pub_date > previous.pub_date:
                previous = book
    else:
        previous = ''


    if next_books:
        next = next_books[0]

        for book in next_books:
            if book.pub_date > next.pub_date:
                next = book
    else:
        next = ''


    context = {
        "books":books,
        "previous":previous,
        "next":next
        }

    print(context['books'])
    print(context['previous'])
    print(context['next'])

    return render(request, template, context)
