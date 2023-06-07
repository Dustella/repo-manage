
from peewee import *


class EntriesIn(Model):
    # 包含: id, 创建的用户， 时间，名字，金额，数量，备注
    # 一个用户可以创建多个条目
    # id 自增 1 而且是主键
    from entities.User import User
    user = ForeignKeyField(User, backref='entries')
    time = DateTimeField()
    name = CharField()
    amount = FloatField()
    quantity = IntegerField()
    note = TextField()
    id = AutoField(primary_key=True)

    class Meta:
        from entities.db import db
        database = db
    
    # 一个创建条目的方法
    @classmethod
    def create_entry(cls, user, time, name, amount, quantity, note):
        from entities.db import db
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