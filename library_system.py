import os

class Library: 
    list_student_account = []
    account_number = 0
    list_employee_account = []
    list_of_book = {
        "fictions": {
            "Harper Lee": "To kill a mocking bird",
            "George Orwell": "1984",
            "Jane Austen": "Pride and Prejudice",
            "Scott Fitzgerald": "The Great Gatsby",
        },
        "non-fiction": {
            "Yuval Noah Harari": "Sapiens",
            "Michelle Obama": "Becoming",
            "Rebecca Skloot": "The immortal life of Henrietta",
            "Tara Westover": "Educated",
            "Stephen Hawking": "A Brief history of time",
        },
        "science-fiction": {
            "Frank Herbert": "Dune",
            "J.R.R Tolkien": "The lord of rings",
            "Suzzane Collins": "The hunger games",
            "Orson Scott Card": "Ender's game",
        }

    }
    def __init__(self, user_name, user_id, user_role):
        self.user_name = user_name
        self.user_id = user_id
        self.user_role = user_role
        self.borrowed_books = []
        Library.account_number += 1
   
    def show_books ():
      while True:
         os.system("cls")
         print ("1. Fictions")
         print ("2. Non-fictions")
         print ("3. Science Fiction")
         print ("4. Exit")
         choice = input("Enter what type of genre do you want: ")
         
         if choice == "4":
            break

         match choice:
            case "1":
               os.system("cls")
               print (Library.list_of_book["fictions"])
               input()
            case "2":
               os.system("cls")
               print (Library.list_of_book["non-fiction"])
               input()
            case "3":
               os.system("cls")
               print (Library.list_of_book["science-fiction"])
               input()
            case _:
               print ("Invalid choice")

    def position ():
       try: 
        user_role = input("Enter your position: ")
        if any(char.isdigit() for char in user_role):
           raise ValueError ("Username should not contain a number")
       except ValueError as message:
          print (f"Error: {message}")
          return
       
       if user_role == "Admin":
          print ("Welcome admin")
          Library.register_account(user_role)
       elif user_role == "Student":
          print ("Welcome student")
          Library.register_account(user_role)
       else:
          print ("Invalid role")
          return   

    def register_account (user_role):
        try: 
         user_name = input("Enter your user name: ")
         if any(char.isdigit() for char in user_name):
            raise ValueError ("Username should not contain a number")
        except ValueError as message:
           print (f"Error: {message}")
           return
        try: 
         user_id = input ("Enter your user id: ")
         if any(user_id.isalpha () for char in user_id):
            raise ValueError ("Pin should not contain a letter. ")
        except ValueError as message:
           print (f"Error: {message}")
           return
        account = Library(user_name, user_id,user_role)

        if user_role == "Admin":
           Library.list_employee_account.append(account)
           print (f"Your account number: {account.account_number}")
        elif user_role == "Student":
           Library.list_student_account.append(account)
           print (f"Your account number is: {account.account_number}")
      
    def show_information (self):
         print (f"Your name is: {self.user_name}")
         print (f"Your user id is: {self.user_id}")
         print (f"Your accounter number is: {self.account_number}")
         print (f"Your role is: {self.user_role}")
         print(f"Borrowed Books: {self.borrowed_books if self.borrowed_books else 'None'}")

    def show_seperate_information (self):
         try:
          account_number = int(input("Enter your account number: "))
         except ValueError:
            print ("Enter a valid account number")
            return

         if user_role == "Admin":
             # access the list of employee
            if 0 <= account_number < len(Library.list_employee_account):
               account = Library.list_employee_account[account_number]
               account.show_information()
            else:
               print ("No account number")

         elif user_role == "Student":
             #access the list of student
            if 0 <= account_number < len(Library.list_student_account):
               account = Library.list_student_account[account_number]
               account.show_information()
            else:
               print ("No account number")
      
    def borrowing_books (self):
      try:
         num_of_books = int(input("Enter the number of books: "))
      except ValueError:
         print ("Should not contain a alpha")
             
      for num in range (num_of_books):
         genre_of_books = input("Enter the genre of the books: ")
         if genre_of_books in Library.list_of_book:
            author_of_books = input("Enter the author of the book: ")

            if author_of_books in Library.list_of_book[genre_of_books]:
               value = Library.list_of_book[genre_of_books][author_of_books]
               self.borrowed_books.append(value)

               print (self.borrowed_books)
            else:
               print ("The author of the book is not here")

         else:
            print ("There's no genre of book you are looking for")

    def display_borrowed_books (self):
      try:
         account_number = int(input("Enter your account number: "))
      except ValueError:
         print ("Enter a valid account number")
         return
      if user_role == "Admin":
            # access the list of employee
         if 0 <= account_number < len(Library.list_employee_account):
            account = Library.list_employee_account[account_number]
            account.borrowing_books()
         else:
            print ("No account number")

      elif user_role == "Student":
            #access the list of student
         if 0 <= account_number < len(Library.list_student_account):
            account = Library.list_student_account[account_number]
            account.borrowing_books()
         else:
            print ("No account number")
   
while True:
   os.system("cls")
   print ("1. Check all books available")
   print ("2. Create a account")
   print ("3. Show information of account")
   print ("4. Borrow a book")
   print ("5. Return Book")
   print ("5. Exit")

   user_choice = input("Enter your choice: ")

   if user_choice == "5":
      break

   match user_choice:
      case "1":
         os.system("cls")
         Library.show_books()
         input()
      case "2":
         os.system("cls")
         Library.position()
         input()
      case "3":
         os.system("cls")
         user_role = input ("Are you a admin or student ?: ")
         Library.show_seperate_information(user_role)
         input()
      case "4":
         os.system("cls")
         user_role = input ("Are you a admin or student ?: ")
         Library.display_borrowed_books(user_role)
         input()
      case "5":
         os.system("cls")
         pass
      case _:
         print ("Invalid choice")