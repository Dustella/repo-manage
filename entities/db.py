from peewee import *

db = SqliteDatabase('data.db')


def add_test_data():
    # test add
    from entities.EntryIn import EntriesIn
    from entities.EntryOut import EntriesOut

    from entities.User import User
    User.create_user(username="1", password="1",
                     email="admin@localhost", role="超级管理员")
    User.create_user(username="user1", password="password",
                     email="user@localhost", role="采购员")
    User.create_user(username="user2", password="password",
                     email="user@localhost", role="仓库管理员")
    User.create_user(username="user3", password="password",
                     email="user@localhost", role="销售员")
    from entities.Customer import Customer
    Customer.create_customer(name="test", phone="123456789", address="test")
    from entities.Item import Item
    ite = Item(name="test", price=100, )
    ite.save()

    entri1 = EntriesOut.create_entry(
        user=1, time="2019-01-01 00:00:00", item=1, amount=100, quantity=1, note="test", customer=1)
    entri2 = EntriesOut.create_entry(
        user=1, time="2019-01-01 00:00:00", item=1, amount=100, quantity=1, note="test", customer=1)


if __name__ == "__main__":
    from entities.EntryIn import EntriesIn
    from entities.EntryOut import EntriesOut

    from entities.User import User

    db.connect()
    db.create_tables([User, EntriesIn, EntriesOut])
    # test add
    User.create_user(username="admin", password="password",
                     email="admin@localhost")
    # test authenticate
    user = User.authenticate(username="admin", password="password")
    print(user.username)
