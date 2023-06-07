from peewee import *

class User(Model):
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)

    class Meta:
        from entities.db import db
        database = db

    @classmethod
    def create_user(cls, username, password, email):
        from entities.db import db
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
