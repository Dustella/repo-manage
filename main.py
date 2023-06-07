

from entities.EntryIn import EntriesIn
from entities.EntryOut import EntriesOut
from entities.User import User
from entities.db import db
from views.Login import LoginWindow


db.connect()
db.create_tables([User ,EntriesIn, EntriesOut])


LoginWindow()
