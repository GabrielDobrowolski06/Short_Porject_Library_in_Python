# Short_Porject_Library_in_Python
Mine project in python (project.py -> code, test_project.py -> code which can check the correctness of the actuall project code)

### BOOK LIBRARY IN PYTHON
#### Description:

##### Project Goal
The goal of this project is to create a simple console application to manage a book library. The application allows users to add new books to the library, display the list of available books, borrow and return books, remove books from the library, and exit the program.


Code Structure
The project is based on several functions that perform specific tasks related to managing the book library. Throughout the code, a global variable library is used to store the list of books in the library. Each book is represented as a dictionary containing information such as title, author, year of publication, and availability status.


Importing Modules
At the beginning of the code, the sys module is imported, which is used to exit the program.


main Function
The main function is the main function that controls the program flow. In an infinite loop, it displays a menu from which the user can choose one of the options: add a book, display the list of books, borrow a book, return a book, remove a book, or exit the program. After choosing the appropriate option, the main function calls the corresponding helper function.


get_new_book_informations Function
The get_new_book_informations function is used to collect information about a new book from the user. The user is asked to provide the title, author, and year of publication of the book. The collected data is returned as a tuple.


add_new_book Function
The add_new_book function adds a new book to the library. It takes the title, author, and year of publication of the book as arguments. It creates a dictionary with this information and an additional status field, which is set to "available" by default. This dictionary is then added to the global library list.


list_books Function
The list_books function displays the list of all books in the library. If the library is empty, an appropriate message is displayed. Otherwise, for each book in the library, its details are displayed: title, author, year of publication, and status (available or borrowed).


borrow_book Function
The borrow_book function allows the user to borrow a book from the library. The user is asked to provide the title of the book they want to borrow. If a book with the given title is in the library and is available, its status is changed to "borrowed" and the user receives a confirmation message. If the book is already borrowed, the user also receives a corresponding message. If a book with the given title is not in the library, a message is displayed informing the user that the book is not available.


return_book Function
The return_book function allows the user to return a previously borrowed book. The user is asked to provide the title of the book they want to return. If a book with the given title is in the library and is borrowed, its status is changed to "available" and the user receives a confirmation message. If the book was not borrowed, the user receives information about this fact. If a book with the given title is not in the library, a message is displayed informing the user that the book is not available.


remove_book Function
The remove_book function allows the user to remove a book from the library. The user is asked to provide the title of the book they want to remove. If a book with the given title is in the library, it is removed from the library list and the user receives a confirmation message. If a book with the given title is not in the library, a message is displayed informing the user that the book is not available.


main Function - Exiting the Program
The main function also contains logic for exiting the program. If the user chooses to exit the program, the function checks if all books have been returned. If any book is still borrowed, an appropriate message is displayed and the program exits. If all books are available, a different message is displayed and the program also exits.

Summary
This project illustrates basic techniques for managing data in Python, such as using lists and dictionaries, and basic input-output operations. The application allows users to interact with the book library through the console, which is useful for learning the basics of programming and data management. The code is modular and easy to understand, which makes it easier to further develop

TODO
