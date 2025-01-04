import os

class Library: 
    list_student_account = []
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
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        
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
        account = Library(user_name, user_id)

        if user_role == "Admin":
           Library.list_employee_account.append(account)
        elif user_role == "Student":
           Library.list_student_account.append(account)
           

        
        

os.system("cls")
Library.position()