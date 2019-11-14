

class Book:

    def __init__(self,bnm,anm,pub,qty,pri,bid=0):
        self.book_name=bnm
        self.author_name = anm
        self.book_publication = pub
        self.book_qty = qty
        self.book_price = pri
        self.id=bid

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)