from peewee import *

db = SqliteDatabase('data.db')

class User(Model):
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)

    class Meta:
        database = db

    @classmethod
    def create_user(cls, username, password, email):
        try:
            with db.transaction():
                cls.create(
                    username=username,
                    password=password,
                    email=email
                )
        except IntegrityError:
            raise ValueError("User already exists")

    @classmethod
    def authenticate(cls, username, password):
        try:
            user = cls.get(cls.username == username)
        except cls.DoesNotExist:
            return ValueError("User does not exist")
        if user.password != password:
            return ValueError("Incorrect password")
        return True

class EntriesIn(Model):
    # 包含: id, 创建的用户， 时间，名字，金额，数量，备注
    # 一个用户可以创建多个条目
    # id 自增 1 而且是主键
    user = ForeignKeyField(User, backref='entries')
    time = DateTimeField()
    name = CharField()
    amount = FloatField()
    quantity = IntegerField()
    note = TextField()
    id = AutoField(primary_key=True)

    class Meta:
        database = db
    
    # 一个创建条目的方法
    @classmethod
    def create_entry(cls, user, time, name, amount, quantity, note):
        try:
            with db.transaction():
                cls.create(
                    user=user,
                    time=time,
                    name=name,
                    amount=amount,
                    quantity=quantity,
                    note=note
                )
        except IntegrityError:
            raise ValueError("Entry already exists")
    
    # 查询所有条目
    @classmethod
    def get_all_entries(cls):
        try:
            entries = cls.select()
        except cls.DoesNotExist:
            raise ValueError("No entries")
        return entries
    
class EntriesOut(Model):
    # 包含: id, 创建的用户， 时间，名字，金额，数量，备注
    # 一个用户可以创建多个条目
    # id 自增 1 而且是主键
    user = ForeignKeyField(User, backref='entries')
    time = DateTimeField()
    name = CharField()
    amount = FloatField()
    quantity = IntegerField()
    note = TextField()
    id = AutoField(primary_key=True)

    class Meta:
        database = db
    
    # 一个创建条目的方法
    @classmethod
    def create_entry(cls, user, time, name, amount, quantity, note):
        try:
            with db.transaction():
                cls.create(
                    user=user,
                    time=time,
                    name=name,
                    amount=amount,
                    quantity=quantity,
                    note=note
                )
        except IntegrityError:
            raise ValueError("Entry already exists")
    
    # 查询所有条目
    @classmethod
    def get_all_entries(cls):
        try:
            entries = cls.select()
        except cls.DoesNotExist:
            raise ValueError("No entries")
        return entries


if __name__ == "__main__":

    db.connect()
    db.create_tables([User ,EntriesIn, EntriesOut])
    # test add
    User.create_user(username="admin", password="password", email="admin@localhost")
    # test authenticate
    user = User.authenticate(username="admin", password="password")
    print(user.username)

