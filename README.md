# Python CLI Journaling App

*This is an intentionally insecure app, usernames and passwords are hardcoded*

## Purpose

This app was built in python and is meant to demonstrate Role Based Access Contol (**RBAC**), 
and to identify its relationship to the CIA Triad. 
There a 3 example users with passwords and roles defined in a dictionary. As well as 3
different Journal entries related to 2 users. As well as users there is one Admin account with
specified admin access. 


## How RBAC is implemented

When the program is started, a user is prompted for a login, a username and password. After login, 
they are presented with a short dashboard that allows viewing and creating journal entires. 
Each user is assigned the role 'user', and thier inidividual journal entries are only visible 
to that user. This is checked against their username and role.

Journal entries are given a unique searchable id and assigned an owner. When a user selects 'View Entries', 
only the entries by the user are presented. Even if the user enters an ID of another users journal entry.

The admin can view all entires by all users, and can delete any entry. To accomplish this there are several 
checks in palce to ensure if the user is an Admin. Each function that is admin specific runs a check against
current_user != 'admin', an 'Access Denied' message appears and a break is incurred.

## How this demonstrates the CIA Triad

### Confindentiality 
When a user views or searches entries, that user can **only** see thier posts. Each function that relates to
viewing entries run's a check for 'username', 'role' and compares that to what is in the dictionary

### Integrity
Users to no have the function to edit or delete posts. Preventing tampering of owned posts and if unathorized is 
obtained, an attacker cannot alter or delete what is there. The admin account can view only the titles and owners
of entries and can read the contents.


