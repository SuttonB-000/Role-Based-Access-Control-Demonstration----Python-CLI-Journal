from datetime import date


# hard coded example users, intentionally insecure
users = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user1": {
        "password":"pass123",
        "role":"user"
    },
    "user2": {
        "password":"pass456",
        "role":"user"
    },
    "user3": {
        "password":"pass246",
        "role":"user"
    }
}

#journal entries
journal_entries = [
    {
        'id': 1,
        'owner': 'user1',
        'title': 'My First Day',
        'content': "today I cleaned the house, and made some ramen",
        'date': '2026-10-31'
    },
    {
        'id': 2,
        'owner': 'user2',
        'title': 'list of dictionaries',
        'content': 'what is the difference between a list of dictionaries and an object?',
        'date':'2026-8-27'
    },
    {
        'id': 3,
        'owner':'user2',
        'title':'methods & dictionaries',
        'content':'I assume the defining differance between a dictionary and an object are methods, or methods attatched to objects',
        'date':'2026-9-14'
    },
    {
        'id':4,
        'owner':'user1',
        'title':'Python Practice',
        'content':'I learned about access control systems with python today',
        'date':'2026-10-29'

    }
]


print('Application Started Successfully')

def main():
    current_user = None

    while current_user is None:
        current_user = login()

    current_role = users[current_user]["role"]

    #print(f'\nWelcome, {current_user}!')
    #print(f'Your role is: {role}')

    print('=' * 36)
    #TODO automate this so that it fills the full width
    print(' ' * 9 + 'CLI JOURNAL')
    print('=' * 36)
    print("Your secure cli journal is ready")


    while True:
        print('\n---Main Menu ---')
        print('1. View Journal')
        print('2. Create Entry')
        print('3. Exit')
        print('4. About This Application')
        if current_role == 'admin':
            print('5. Admin Dashboard')

        choice = input('Choose an option: ')

        #TODO implement a view journal feature
        if choice == "1":
            view_entries(current_user, current_role)

            read_choice = input(
                'Would you like to read an entry?'
            )

            if read_choice.lower() == 'yes':
                read_entry(current_user, current_role)


        elif  choice == '2':
            create_entry(current_user, current_role)
            #print('Create New Journal Entry feature coming soon!')
        elif choice == '3':
            print('Goodbye')
            break
        elif choice == '4':
            #TODO create separate function for this
            print('This is a Python CLI Journal Application to provide an example for RBAC and demonstrate understanding of the CIA triad')
        elif  choice == '5':
            admin_menu(current_role)
        else:
            print('Invalid option. Please try again')

#user dictionary test
def userDictTest():
    print('testing user dictionary: ')
    print(users['admin']['role'])
    print(users['user1']['role'])
    print(users['user3']['password'])

    print('output should be: "admin", "user", "pass246" ')
#userDictTest()

#login funtion
def login():
    print('\n--- LOGIN ---')

    username = input('Username: ')
    password = input('Password: ')

    if username in users:
        if password == users[username]['password']:
            print(f'Login Succesful, welcome {username}')
            return username

    print('Invalid username or password')
    return None

#display journal entries for user
def view_entries(current_user, current_role):
    if current_role != 'user':
        print("Access Denied")
        return
        

    print('\n---Journal Entries---')

    print(f"{'ID':<5}{'owner':12}{'title':<25}{'date':<12}")
    print('_'* 52)

    for entry in journal_entries:
        if entry['owner'] == current_user:
            print(
                f"{entry['id']:<5}"
                f"{entry['owner']:<12}"
                f"{entry['title']:<25}"
                f"{entry['date']:<12}"

            )

#Function to read entry filtered by user
def read_entry(current_user, current_role):
    if current_role != 'user':
        print('Access Denied')
        return 

    entry_id = input('Enter Entry ID to read: ')

    for entry in journal_entries:
        if str(entry['id']) == entry_id:
            if entry['owner'] != current_user:
                print('Access Denied')
                return 
            
            print(f"\nTitle: {entry['title']}")
            print(f"\nDate: {entry['date']}")
            print(f"\nContent: {entry['content']}")
            return
        print('Entry not found.')

def create_entry(current_user, current_role):
    if current_role != 'user':
        print('Access Denied')
        return 

    print('\n---create new entry---')

    title = input('Entry title: ')

    if title == '':
        print('title cannot be empty')
        return 

    content = input('Entry Content: ')

    new_id = 1

    for entry in journal_entries:
        if entry['id'] >= new_id:
            new_id = entry['id'] + 1

    new_entry = {
        'id': new_id,
        'owner': current_user,
        'title': title,
        'content': content,
        'date': date.today().isoformat()
    }

    journal_entries.append(new_entry)

    print('Journal entry created successfully')

def admin_view_entries(current_role):
    if current_role != 'admin':
        print('Access Denied')
        return
    
    print('\n--- All Journal Entries ---')

    print(f"{'id':<5}{'owner':<12}{'title':<25}{'Date':<12}")
    print('-' * 54)

    for entry in journal_entries:
        print(
            f"{entry['id']:<5}"
            f"{entry['owner']:<12}"
            f"{entry['title']:<25}"
                f"{entry['date']:<12}"
        )

def admin_delete_entry(current_role):
    if current_role != 'admin':
        print('Access Denied')
    print("\n --- Delete Journal Entry ---")

    entry_id = input('Entry ID to delete: ')

    for entry in journal_entries:
        if str(entry['id']) == entry_id:
            confirm  = input('Delete this enty? yes/no: ')

            if confirm.lower() == 'yes':
                journal_entries.remove(entry)
                print(f'Entry {entry} deleted successfully')
            else:
                print('Deletion cancelled')
            return
    print("Entry not found.")

#admin board
def admin_menu(current_role):
    if current_role != 'admin':
        print("access denied")
        return

    while True:
        print('\n---Admin Dashboard---')
        print('1. View all journal enntries')
        print('2. Delete journal Entry')
        print('3. Return to main menu')

        choice = input('Choose an option: ')
    
        if choice == '1':
            admin_view_entries(current_role)

        elif choice == '2':
            admin_delete_entry(current_role)

        elif choice == '3':
            break

        else:
            print('Invalid option. Please try again')


def admin_view_entries(current_role):
    if current_role != 'admin':
        print('Access Denied')
        return
    print(f"/n --- All Journal Entries ---")
    
    print(f"{'ID':<5}{'Owner':<12}{'Title':<25}{'Date':<12}")
    print("-" * 54)

    for entry in journal_entries:
        print(
            f"{entry['id']:<5}"
            f"{entry['owner']:<12}"
            f"{entry['title']:<25}"
            f"{entry['date']:<12}"
        )


def admin_delete_entry(current_role):
    if current_role != "admin":
        print('Access Denied')
        return

    admin_view_entries(current_role)

    print('\n --- Delete Journal Entries ---')

    entry_id = input('Enter Entry ID to delete: ')
    
    for entry in journal_entries:
        if st(entry['id']) == entry_id:
            confirm = input('Delete this entry? (yes/no): ')

            if confirm.lower() == 'yes':
                journal_entries.remove(entry)
                print('Entry deleted!')
            else:
                print('Deletetion cancelled')
            return
        print('Entry not found')


# Security Test
def rbac_test():
    print('\n--- RBAC SECURITY TEST ---')
    
    print('Testing user access to admin function')
    admin_view_entries('user')

    print('Testing admin access to user functions')
    view_entries('user1', 'admin')

    print('---END OF SECURITY TEST--- \n')

rbac_test()


main()
