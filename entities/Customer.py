from peewee import *

class Customer(Model):
    # 客户，包含: id, 名字，电话，地址，备注
    # id 自增 1 而且是主键
    name = CharField()
    phone = CharField()
    address = CharField(null=True)
    note = TextField(null=True)
    id = AutoField(primary_key=True)

    class Meta:
        from entities.db import db
        database = db

    # 一个创建条目的方法
    @classmethod
    def create_customer(cls, name, phone, address, note=""):
        from entities.db import db
        try:
            with db.transaction():
                cls.create(
                    name=name,
                    phone=phone,
                    address=address,
                    note=note
                )
        except IntegrityError:
            raise ValueError("Customer already exists")
    
    # 查询所有条目
    @classmethod
    def get_all_customers(cls):
        try:
            customers = cls.select()
        except:
            raise ValueError("No customers")
        return customers
