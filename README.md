# Assignment-3
Extracting and structuring information using file I/O operations into a dictionary which will be used as a lookup table. 

The text file "books.txt" includes 72 books from the list: "Goodreads: 100 Books You Should Read in a Lifetime". This list was published in Time magazine a couple of years ago. Please take a look at the content of the file before starting your code. The data for each book is (in order): book title, author, language, type (genre) and number of copies sold (int). You will use one of the file reading methods seen to read the contents of the file and structure the information in a nested dictionary. The unique key for each book is its title, a string. The other information associated with each book will be in the inner dictionary with the keys as shown.

1- How many different languages are there? Print a numbered list of languages.
2- What language has the most books? (Hint: create a new small dictionary to count books in each language)
3- Display all the books in a language. (Ask user to enter a language and Print book title, author, type and copies sold)
4- How many different types of books are there? Print a numbered list of the types? Which type has most copies sold?
(Hint: create a new small dictionary)
5- List all authors who have more than one book on the list. (show result as author: number of books)
6- List the top 10 authors based on the number of books they have authored (on the list)
7- For a given author, what is the total number of books sold? (Ask user to enter an author name)
8- List all books of a given type. (When selected, display list of types from option 4 then ask user to input a type)
9- What are the top 5 types of books based on total sold? (Hint: create a new small dictionary)
10- Display a pie chart plot to show the distribution of books among the top 5 types of books (from option 8).
