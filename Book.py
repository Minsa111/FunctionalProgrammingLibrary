# emptypush

currentUser = None

users = {
    "admin" : "12345",
    "user1" : "1",
    "user2" : "2"
}
users_book= {}
user_role = {
    "admin" : True,
    "user1" : False,
    "user2" : False
}

book={
    "J.K Rowling":"Harry Potter",
    "Finn the Human":"Adventure Time"
}

def addBook():
    author = input("Input author name: ")
    title = input("Input title name: ")
    book[author] = title
    print("Succesfully added a book!")
    print(book)
    input("Press enter to continue...")
    adminUser()

def checkBorrowedBook():
    print(users_book)
    adminUser()
    
def checkData():
    print(book)
    input("Press enter to continue...")
    adminUser()

def borrowBook():
    for author, title in book.items():
        print(f"{author}: {title}")
    ans = input("Enter the book title to borrow: ")

    for author, title in book.items():
        if ans == title:
            for (b_author, b_title), borrower in users_book.items():
                if b_author == author and b_title == title:
                    print("Book already borrowed by", borrower)
                    input("Press enter to continue...")
                    break
            else:
                users_book[(author, title)] = currentUser
                borrowedBook()
                break
    normUser()


def borrowedBook():
    print(f"Books that are borrowed by {currentUser}:\n")
    for (author, title), borrower in users_book.items():
        if borrower==currentUser:
            print(f"{author} : {title}")
    input("Press enter to continue")
    normUser()

def returnBook():
    print("Books borrowed by", currentUser + ":")
    for (author, title), borrower in users_book.items():
        if borrower == currentUser:
            print(f"{author} : {title}")

    book_to_return = input("Enter the book title to return: ")
    for (author, title), borrower in users_book.items():
        if borrower == currentUser and title == book_to_return:
            del users_book[(author, title)]
            print(f"You've returned the book: {author} : {title}")
            input("Press enter to continue...")
            normUser()
            return

    print("You don't have a book with that title.")
    input("Press enter to continue...")
    normUser()

def adminUser():
    global currentUser
    print(f"Welcome {currentUser}!")
    print("1. Input Book")
    print("2. Check Data")
    print("3. Log Out")
    ans = int(input("Please Choose one of the option: "))
    if ans == 1:
        addBook()
    elif ans == 2:
        checkBorrowedBook()
    elif ans == 3:
        currentUser = ""
        login()
    else:
        print("Please enter valid answer")


def normUser():
    global currentUser
    print(f"Welcome {currentUser}!")
    print("1. Borrow Book")
    print("2. Check Borrowed Book")
    print("3. Return Book")
    print("4. Log Out")
    ans = int(input("Please Choose one of the option: "))
    if ans == 1:
        borrowBook()
    elif ans == 2:
        borrowedBook()
    elif ans == 3:
        returnBook()
    elif ans == 4:
        currentUser = ""
        login()
    else:
        print("Please enter valid answer")
        normUser()

def login():
    global currentUser
    print("\n--- Welcome to this Humble Library ---\n\n")
    username = input("Username: ")
    password = input("Password: ")
    role = checkAcc(username, password)

    if username and password:  # Check if both username and password are provided
        role = checkAcc(username, password)
        if role == "admin":
            currentUser = username
            adminUser()
        elif role == "user":
            currentUser = username
            normUser()
        else:
            print("Wrong username or password.")
    else:
        print("Please enter a valid username and password.")

def checkAcc(username, password):
    if username in users and user_role[username] and password == users[username]:
        return "admin"
    elif username in users and not user_role[username] and password == users[username]:
        return "user"
    else:
        return "Wrong username or Password"


def main():
    login()


if __name__=="__main__":
    main()