# SNS Platform API

SNS is a platform where users can safly save those very cherised messages from your loved ones in a easy to use, friendly, and clean way.
Lets just say that your messages will be "Said In Stone"!
## Local Setup

1. Clone this repository and change to the directory in the terminal.
2. Run `pipenv shell`
3. Run `pipenv install`
4. Run migrations and make migrations
5. Seed database with python3 manage.py loaddata {table name}
###LoadData Order
1.users
2.tokens
3.app_user
4.tags
5.contacts
6.messages
7.message_tags
Now that your database is set up all you have to do is run the command:

```
python3 manage.py runserver
```

## SNS ERD

Here is the ERD for the models in the api: https://drawsql.app/nashville-software-school/diagrams/capstone

## Documentation

Register a new User then begin by adding a contact and start saving messages.
You can add/edit/delete contacts and messages
### Texting Functionality
Texting functionality only enabled on demo day.
Behavior of texting
1. Text "New" to the provided phone number
2. Respond with the appropriate number assigned to the contact that you want to save the message under
3. Respond with the body of the message
4. Respond with the date of the message
5. Check website for the updated message list
