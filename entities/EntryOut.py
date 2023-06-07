from peewee import *



class EntriesOut(Model):
    # 包含: id, 创建的用户， 时间，名字，金额，数量，备注
    # 一个用户可以创建多个条目
    # id 自增 1 而且是主键
    from entities.Item import Item
    from entities.User import User
    user = ForeignKeyField(User, backref='entries_out')
    time = DateTimeField()
    item = ForeignKeyField(Item, backref='entries_out')
    amount = FloatField()
    quantity = IntegerField(default=1)
    from entities.Customer import Customer
    customer = ForeignKeyField(Customer)
    note = TextField(null=True)
    id = AutoField(primary_key=True)

    class Meta:
        from entities.db import db
        database = db
    
    # 一个创建条目的方法
    @classmethod
    def create_entry(cls, user, time, item, amount, quantity, customer,note=""):
        from entities.db import db
        try:
            with db.transaction():
                cls.create(
                    user=user,
                    time=time,
                    item=item,
                    amount=amount,
                    quantity=quantity,
                    customer=customer,
                    note=note,
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
