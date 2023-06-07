from peewee import *

db = SqliteDatabase('data.db')

    

if __name__ == "__main__":
    from entities.EntryIn import EntriesIn
    from entities.EntryOut import EntriesOut

    from entities.User import User

    db.connect()
    db.create_tables([User ,EntriesIn, EntriesOut])
    # test add
    User.create_user(username="admin", password="password", email="admin@localhost")
    # test authenticate
    user = User.authenticate(username="admin", password="password")
    print(user.username)

