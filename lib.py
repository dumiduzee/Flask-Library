class Library:
    def __init__(self,con):
        self.__con = con


    def addBook(self,bookName,book_isbn,book_author,book_publisher,book_year):
        if bookName and book_isbn and book_author and book_publisher and book_year:
            try:
                querry = f'INSERT INTO books(bookname,bookIsbn,bookAuthor,bookPublisher,bookyear) VALUES ("{bookName}","{book_isbn}","{book_author}","{book_publisher}","{book_year}")'
                cursor = self.__con.Database().cursor()
                cursor.execute(querry)
                self.__con.Database().commit()
                return "Data added successfull"
            except Exception as e:
                return f"Something went wrong"
        else:
            return "Fields cannot be empty!!"
        
    def removeBook(self,book_isbn):
        if book_isbn:
            try:
                cursor = self.__con.Database().cursor()
                querry = f'DELETE FROM books WHERE bookIsbn="{book_isbn}"'
                cursor.execute(querry)
                self.__con.Database().commit()
                return f"Deleted success"
            except Exception as e:
                return f'Something went wrong {e}'
        else:
            return "Field cant be empty"


