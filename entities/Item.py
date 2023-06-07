from peewee import *

class Item(Model):
    # 商品，包含: id, 名字，价格，备注，供应商
    # id 自增 1 而且是主键
    name = CharField()
    price = FloatField()
    note = TextField(null=True)
    supplier = CharField(null=True)
    id = AutoField(primary_key=True)

    class Meta:
        from entities.db import db
        database = db
    
    # 一个创建条目的方法
    @classmethod
    def create_item(cls, name, price, note, supplier):
        from entities.db import db
        try:
            with db.transaction():
                cls.create(
                    name=name,
                    price=price,
                    note=note,
                    supplier=supplier
                )
        except IntegrityError:
            raise ValueError("Item already exists")
        
    # 查询所有条目
    @classmethod
    def get_all_items(cls):
        try:
            items = cls.select()
        except:
            raise ValueError("No items")
        return items
