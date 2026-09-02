from collections import defaultdict
books = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "read": False}
]
def add_book(books,title, author, year,read) -> None:
    new_dict = {"title": title, "author": author, "year": year, "read": read}
    books.append(new_dict) # No need to make it like this books = books.append(new_dict)

def mark_as_read(books, title) -> bool: # this function only marks the book as read
    for book in books:
        if book["title"].upper() == title.upper():
            book["read"] = True
            return True

def search_by_author(books, author):
    basket = [] # create an empty list because the author maybe wrote more than one book
    for book in books: # book here is a dictionary from the dictionaries in the list
        if book["author"].upper() == author.upper():
            basket.append(book['title']) #adding every book this author wrote
    return basket
def remove_book(books, title) -> bool:
    for book in books:
        if book["title"].upper() == title.upper():
            books.remove(book) #This actually removes the dictionary from the books list , as if we made "del book" it will delete the dictionary but in local scope not global
            return True

def average_year(books) -> float | int :
    number_of_books = 0
    sum_of_year = 0
    for book in books:
        sum_of_year += book["year"]
        number_of_books += 1
    return sum_of_year / number_of_books

def books_by_decade(books) -> dict:
    dict_of_lists = defaultdict(list)
    for book in books:
        decade = (book["year"] // 10) * 10
        dict_of_lists[decade].append(book["title"])
    return dict(dict_of_lists)

ans = 'YES'
while ans.upper() == 'YES':
    try:
        choice = int(input("1-add new book\n"
                           "2-mark the book\n"
                           "3-search of author\n"
                           "4-remove book\n"
                           "5-show current books available\n"
                           "6-average year\n"
                           "7-books by decade\n"))
    except ValueError:
        print(f"cannot enter any type except integer and from 1 to 5")
        continue
    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        try:
            year = int(input("Enter the year of the book: "))
        except ValueError:
            print(f"year value can be integer only!(Not a decimal/word/sentense)")
            continue
        read = input("Did you read this book before(yes/no): ").upper() == "YES"
        add_book(books,title,author,year,read)
    elif choice == 2:
        title = input("Enter book title: ")
        check_book_presence = mark_as_read(books,title)
        if check_book_presence != True:
            print(f"{title} isnot in our library to be marked as read")

    elif choice == 3:
        author = input("Enter the author name: ")
        book_title= search_by_author(books,author)
        if book_title: # if the author name is found , it returns all the books he wrote
            print(f"{author} is found in the list and he made the {book_title}")
        else:
            print(f"{author} isnot found in the list!")

    elif choice == 4:
        title = input("Enter the book u want to remove: ")
        check_book_presence= remove_book(books,title)
        if check_book_presence != True:
            print(f"{title} isnot found in the booklist to remove it!")
    elif choice == 5:
        print(books)
    elif choice == 6:
        try:
            average_of_years = average_year(books)
            print(f"The average year of all the books in the list is: {average_of_years}")
        except ZeroDivisionError:
            print("Cannot divide by zero(error)!")
            continue
    elif choice == 7:
        books_grouped=books_by_decade(books)
        print(books_grouped)
    else:
        print(f"{choice} option is not available at the moment!")
        continue
    ans = input("do u want to repeat(yes/no): ")


