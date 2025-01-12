nested_dict = {
    "fictions": {
        "Harper Lee": "To Kill a Mockingbird",
        "George Orwell": "1984"
    },
    "non-fiction": {
        "Yuval Noah Harari": "Sapiens",
        "Michelle Obama": "Becoming"
    }
}

all_keys = []

range_of_books = int(input("Enter how many books you want to borrow: "))

for num in range (range_of_books):
    genere_of_book = input("Enter the genre of the book: ")
    if genere_of_book in nested_dict:
        book_finder = input("Enter the author of the book: ")
        
        if book_finder in nested_dict[genere_of_book]:
            value = nested_dict[genere_of_book][book_finder]
            all_keys.append(value)
        else:
            print ("The book is not here")
    else:
        print ("The genre of book is not here")

print(all_keys)

