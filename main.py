

from entities.Customer import Customer
from entities.EntryIn import EntriesIn
from entities.EntryOut import EntriesOut
from entities.Item import Item
from entities.User import User
from entities.db import add_test_data, db
from views.Login import LoginWindow


db.connect()
db.create_tables([User ,EntriesIn, EntriesOut,Customer,Item])
add_test_data()

LoginWindow()
