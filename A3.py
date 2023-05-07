#Justin Sciortino

fp = open('books.txt')
Books = {}

for line in fp.readlines():
    line=line.strip('\n')
    book_record = line.split(",")
    book_dict = {}
    book_dict['author'] = book_record[1]
    book_dict['language'] = book_record[2]
    book_dict['type'] = book_record[3]
    book_dict['sold'] = int(book_record[4])
    Books[book_record[0]] = book_dict
    book_title = book_record[0]
    Books.setdefault((book_title), book_dict)
fp.close()
print(Books)

menu = """1- How many different languages are there? Print a numbered list of languages.
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
11- Exit
Select an option:"""


book_types = {}           #Dictionary for types(key) and the total amount sold per type(value)
for k in Books.values():
    types_books = k['type']
    copies = int(k['sold'])
    if types_books in book_types:
        book_types[types_books] += copies
    else:
        book_types[types_books] = copies

dict_authors = {}      #Dictionary for authors(key) and the amount of books authored(value)
for k in Books.values():
    author = k['author']
    count5 = 1
    if author not in dict_authors:
        dict_authors[author] = count5
    else:
        dict_authors[author] += count5

author_sold = {}         #Dictionary for authors(key) and the total amount of copies sold(value)
for k in Books.values():
    author = k['author']
    copies = int(k['sold'])
    if author in author_sold:
        author_sold[author] += copies
    else:
        author_sold[author] = copies

dict_lang = {}          #Dictionary for languages(key) and the amount of languages in the top 100 (value)
for k in Books.values():
    lang = k['language']
    count2 = 1
    if lang not in dict_lang:
        dict_lang[lang] = count2
    else:
        dict_lang[lang] += count2


option = 0
while option != 11:
    option = int(input(menu))

#OPTION 1
    if option == 1:
        f = 1      #f is used for the numbered list
        for title in dict_lang:
            print('{} {} {}'.format(f,')',title))
            f+=1
#OPTION 2
    elif option == 2:
        num_of_mostlang = max(dict_lang.values())         #The most amount of books for a language
        most_lang = max(dict_lang, key=dict_lang.get)     #The language with the most amount of books
        print('{}{}{}{}{}'.format('The language ',most_lang,' has the most books with ',num_of_mostlang, ' books'))
#OPTION 3
    elif option == 3:
        display_books = input('Enter a language:')      #User input to enter a language
        for key in Books:
            if display_books in Books[key]['language']:   #Finds the user input in the Books dictionary and prints the relavent information
                print('{:50s} {:30s} {:30s} {:20d}'.format(key, Books[key]['author'],Books[key]['type'], Books[key]['sold']))

#OPTION 4
    elif option == 4:
        i = 1   #i is used for the numbered list
        for k in book_types:
            print('{} {} {}'.format(i, ')', k))       #Print a numbered list of the types
            i+=1
        most_copies_sold = max(book_types.values())
        type_of_mostsold = max(book_types, key = book_types.get )
        print('The type',type_of_mostsold, 'has the most copies sold with', most_copies_sold, 'copies sold')

#OPTION 5
    elif option == 5:
        i = 1       #i is used for the numbered list
        for author in dict_authors:
            if dict_authors[author] >1:     #narrows it for authors who have more than one book
                print(('{} {} {}:{} '.format(i,')',author, dict_authors[author])))
                i += 1
#OPTION 6
    elif option == 6:
        count6 = 0
        p = 1     #p is used for the numbered list
        for numbook in sorted(dict_authors, key = dict_authors.get, reverse = True):   #gets the author and the number of books they have
            if count6 <10:                                                             #reverse = True part will make it in decreasing order (highest number of books sold to lowest)
                print(('{} {} {}:{} '.format(p, ')', numbook, dict_authors[numbook])))
                count6 += 1
                p +=1

#OPTION 7
    elif option == 7:
        given_author = input('Enter an author:')    #User input to enter an author
        if given_author in author_sold:
            print("The total number of books sold by", given_author, 'is:', author_sold[given_author])   #print the given author and the total copies sold

#OPTION 8
    elif option == 8:
        print('The types of books are:')
        i=1     #i is used for the numbered list
        for type in book_types:
            print('{} {} {}'.format(i,')',type))   #Lists all the types of books
            i+=1

        input_typebook = input('Input a type of book:')   #user input to enter a book type
        u = 1      #u is used for the numbered list
        print('The books of the given type', input_typebook, 'are:')
        for k in Books:
            if Books[k]['type'] == input_typebook:      #print the title of book if the user input is in the master dictionary Books
                print('{} {} {}'.format(u, ')', k))
                u +=1
#OPTION 9
    elif option == 9:
        count9 = 0
        u = 1     #u is used for the numbered list
        for booktype in sorted(book_types, key=book_types.get, reverse=True):     
            if count9 < 5:    #Limits the amount printed to only 5 things
                print('{} {} {}:{}'.format(u,')',booktype,book_types[booktype]))
                count9 += 1    #Limits the amount printed to only 5 things
                u += 1
#OPTION 10
    elif option == 10:
        count10 = 0
        top5dict = {}
        for booktype in sorted(book_types, key = book_types.get, reverse = True):    
            if len(top5dict) !=5:   #checks to make sure that they are only 5 types of books, the len function will count the amount of keys
                top5dict[booktype] = book_types[booktype]   #dictionary of the top 5 books in decreasing order (highest to lowest)

        import matplotlib
        import matplotlib.pyplot as pl

        typesofBook = []    #list for the top 5 types
        totalsold =[]     #list for the total amount sold
        totalbooks_sold = 0
        for k, v in top5dict.items():
            typesofBook.append(k)
            totalbooks_sold +=v
        for k,v in top5dict.items():
            i = (v/totalbooks_sold)*100
            totalsold.append(i)

        colors = ["blue", 'yellow', 'green', 'orange', 'red', 'purple', 'grey']
        pl.pie(totalsold, labels=typesofBook, colors=colors, startangle=90, autopct='%1.1f%%')
        pl.axis('equal')
        pl.title('Distribution of books among the top 5 types of books')
        pl.show()

    elif option == 11:
        print('Exiting...')


