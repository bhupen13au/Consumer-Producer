from django.shortcuts import render
from consumerapp.BookInfo import Book
from consumerapp.REST_API import ConsumeProducers

def home_page_book(request):
    return render(request, 'book.html',{"books":ConsumeProducers.fetch_all_books()})


def save_book_info(request):
    print(request.POST)
    bookdict=request.POST
    binstance = Book(bnm=bookdict['book_name'],
                     anm=bookdict['author_name'],
                     pub=bookdict['book_publication'],
                     qty=bookdict['book_qty'],
                     pri=bookdict['book_price'])
    ConsumeProducers.add_book(binstance)

    return render(request, 'book.html',{"msg":"Book Saved Successfully..!"})
