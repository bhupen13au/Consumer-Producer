import requests
from consumerapp.BookInfo import Book

BOOK_API_BASE_URI = "http://localhost:8000/v1/books/"
BOOK_API_BASE_URI1 = "http://localhost:8000/tokeng/"

def actual_conversion(bookjson):
    if bookjson.get('detail') == 'Not found.':
        return None
    elif bookjson:
        return Book(bid=bookjson.get('id'),
                    bnm=bookjson.get('book_name'),
                    anm=bookjson.get('author_name'),
                    pub=bookjson.get('book_publication'),
                    qty=bookjson.get('book_qty'),
                    pri=bookjson.get('book_price'))
    return bookjson


def deseriaze_bookjson_bookinstace(bookjson,type):
    bookList = []
    if type=='S':
        return actual_conversion(bookjson)
    elif type =='M':
        for book in bookjson:
            bookList.append(actual_conversion(book))
        return bookList


class ConsumeProducers:

    @staticmethod
    def fetch_book(bookId):
        response =requests.get(BOOK_API_BASE_URI+str(bookId))
        bookjson = response.json()
        return deseriaze_bookjson_bookinstace(bookjson,'S')

    @staticmethod
    def fetch_all_books():
        response = requests.get(BOOK_API_BASE_URI,headers={'Authorization': 'Token cb95920cfddab1807c4aa0bed70eedc98288be97'})
        print(response.status_code)
        bookjson=response.json()
        print(bookjson)
        return deseriaze_bookjson_bookinstace(bookjson,'M')

    @staticmethod
    def add_book(p_book):
        if type(p_book)==Book:
            if p_book.id==0:
                p_book.__dict__.pop('id')
            response =requests.post(url=BOOK_API_BASE_URI,json=p_book.__dict__)
            print(response.status_code)
            print(response.json())
            print('Data inserted successfully...')

    @staticmethod
    def update_book(p_book):
        if type(p_book)==Book and p_book.id>0:
            dbbook = ConsumeProducers.fetch_book(p_book.id)
            if dbbook:
                dbbook.book_name=p_book.book_name
                dbbook.author_name=p_book.author_name
                dbbook.book_publication=p_book.book_publication
                dbbook.book_qty=p_book.book_qty
                dbbook.book_price=p_book.book_price
                response =requests.put(url=BOOK_API_BASE_URI+str(p_book.id)+"/",json=dbbook.__dict__)
                print(response.status_code)
                print(response.json())
                print('Data updated successfully...')
            else:
                 print('cannot update as book not avbl ..with given id')
        else:
            print('invalid book or no Id specified...!')

    @staticmethod
    def remove_book(bid):
        if bid>0:
            dbbook = ConsumeProducers.fetch_book(bid)
            #print('DBBook',dbbook)
            if dbbook:
                response =requests.delete(url=BOOK_API_BASE_URI+str(bid)+"/")
                print(response.status_code)
                print('Data deleted successfully...')
            else:
                print('cannot delete as book not avbl ..with given id')
        else:
            print('Invalid Id specified...!')

    @staticmethod
    def get_token_from_producer():
        response = requests.post(BOOK_API_BASE_URI1,
                                 data={"username":"yogymax"})
        if response.status_code==200:
            print(response.text)
        else:
            print(response.status_code)

if __name__ == '__main__':
    #binstance = Book(bnm="IOT",anm='YYY',pub='AATT',qty=25,pri=55223.33)
    #ConsumeProducers.remove_book(7)
    ConsumeProducers.get_token_from_producer()
