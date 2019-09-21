import sqlite3
# Database name
db = sqlite3.connect('records2.db')
db.row_factory = sqlite3.Row
cur = db.cursor()

# Menu for choice
menu = ["1 Add ",
        "2 Search ",
        "3 Update ",
        "4 Delete ",
        "5 Quit"]
# check if the required number is choice for menu
def main():
    choice = 1
    create_table()
    add_record()
    while choice is not 5:
        display_menu()
        choice = int(input('Enter a menu choice'))
        while choice < 0 or choice > 5:
            print('\nEnter a number between 1 and 5')
            choice = int(input('Enter a menu choice'))
        get_menu_option(choice)



def get_menu_option(choice):
    if choice == 1:
        add_new_record()
    elif choice == 2:
        search_records()
    elif choice == 3:
        update_record()
    elif choice == 4:
        delete_record()
 # Create table and check if is exists or not
def create_table():
    cur.execute('create table if not exists records (name text, country text, catches int)')
 # Add required record
def add_record():
    cur.execute('insert into records values("Janne Mustonen","Finland",98)')
    cur.execute('insert into records values ("Ian Stewart", "Canada", 94)')
    cur.execute('insert into records values ("Aaron Gregg", "Canada", 88)')
    cur.execute('insert into records values ("Chad Taylor", "USA", 78)')

# Menu display
def display_menu():
    print('***MENU***')
    for i in menu:
        print('\n' + i)
# Add a new record
def add_new_record():
    try:
        name = input('Enter a new record holder name: ')
        country = input("Enter record holder's country: ")
        catches = int(input('Enter a number of catches: '))
        cur.execute('insert into records values(?, ?, ?)', (name, country, catches))
    except sqlite3.Error as e:
        print(e)
    except ValueError:
        print('numbers are required!!')
# search record by name
def search_records():
    name = input('Enter the name of the record holder to retrieve: ')
    try:
        if name == "":
            query = 'select * from records'
            for row in cur.execute(query):
                print('name: ' + row['name'])
                print('country: ' + row['country'])
                print('catches: ' + str(row['catches']))
        else:
            for row in cur.execute('select * from records where name = ?', (name,)):
                print('name: ' + row['name'])
                print('country: ' + row['country'])
                print('catches: ' + str(row['catches']))
    except sqlite3.Error as e:
        print(e)

def update_record():
    try:
        name = input('Please Enter the name of the record holder to be update: ')
        catches = int(input('Enter amount of catches: '))
        cur.execute('update records set catches = ? where name = ?', (catches, name))
        print('\nrecord updated')
    except sqlite3.Error as e:
        print(e)
    except ValueError:
        print('Please enter the required input')
def delete_record():
    name = input('Enter the name of the record holder you wish to delete: ')
    try:
        cur.execute('delete from records where record_holder = ?', (name,))
        print('\nrecord holder is deleted')
    except sqlite3.Error as e:
        print(e)


main()

db.commit()
db.close()