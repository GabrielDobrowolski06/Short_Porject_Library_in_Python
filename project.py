import sys

library = []

def main():
    while True:
        print("\nMenu")
        print("Choose 1 to Add book")
        print("Choose 2 to Show list of books")
        print("Choose 3 to Borrow book")
        print("Choose 4 to Return book")
        print("Choose 5 to Remove book")
        print("Choose 6 to Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title, author, year = get_new_book_informations()
            add_new_book(title, author, year)
        elif choice == "2":
            list_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            remove_book()
        elif choice == "6":
            for book in library:
                if book['status'] == "borrowed":
                    print("\nSee you soon, erudite")
                    sys.exit(0)
            print("\nOkay, you are unlettered man, bye\n")
            sys.exit(0)
        else:
            print("\nThis is a serious facility, don't joke around")


def get_new_book_informations():
    title = input("\ntitle: ")
    author = input("author: ")
    year = input("year of release: ")
    return title, author, year

def add_new_book(title, author, year):
    global library
    book = {
        "title": title,
        "author": author,
        "year": year,
        "status": "available"
    }
    library.append(book)

def list_books():
    global library
    if not library:
        print("\nThere are not books in the library lol")
    else:
        for book in library:
            print(f"\n{book['title']} was written by {book['author']} and released in {book['year']}, status: {book['status']}")

def borrow_book():
    global library
    title_borrow = input("Enter title of the book to borrow: ")
    for book in library:
        if title_borrow.lower() == book['title'].lower():
            if book['status'] == "available":
                book['status'] = "borrowed"
                print(f"\n{book['title']} has just been borrowed")
                return
            elif book['status'] == "borrowed":
                print(f"\n{book['title']} is already borrowed")
                return
    print("\nThe book is not available in the library.")

def return_book():
    global library
    title_return = input("Enter title of the book to return: ")
    for book in library:
        if title_return.lower() == book['title'].lower():
            if book['status'] == "borrowed":
                book['status'] = "available"
                print(f"\n{book['title']} has just been returned")
                return
            else:
                print(f"\n{book['title']} was not borrowed.")
                return
    print("\nThe book is not available in the library.")

def remove_book():
    title_remove = input("Enter title of the book to remove: ")
    for book in library:
        if title_remove.lower() == book['title'].lower():
            library.remove(book)
            print(f"\n'{book['title']}' has just been removed from the library.")
            return
    print("\nYou have just removed book, but please Stop it!")


if __name__ == "__main__":
    main()
