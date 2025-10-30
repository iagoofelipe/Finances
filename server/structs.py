from dataclasses import dataclass

@dataclass
class AbstractTable:
    __table__ = None
    __encryptedFields__ = None

@dataclass
class User(AbstractTable):
    id: str
    name: str
    email: str
    username: str
    password: str
    __table__ = 'user'
    __encryptedFields__ = ['password']

@dataclass
class Profile(AbstractTable):
    id: str
    name: str
    user_id: str
    __table__ = 'profile'

@dataclass
class ProfileRole(AbstractTable):
    id: str
    edit: bool
    view: bool
    pending: bool
    profile_id: str
    user_id: str
    is_default: bool
    __table__ = 'profile_role'

# @dataclass
# class Category(AbstractTable):
#     id: str
#     name: str
#     type: int
#     description: str = ''
#     userId: str = None
#     __table__ = 'category'

# @dataclass
# class Card(AbstractTable):
#     id: str
#     name: str
#     userId: str = None
#     __table__ = 'card'

# @dataclass
# class Third(AbstractTable):
#     id: str
#     name: str
#     userId: str = None
#     __table__ = 'third'

# @dataclass
# class Registry(AbstractTable):
#     id: str
#     type: int
#     title: str
#     value: float
#     datetime: dt.datetime
#     description: str = ''
#     userId: str = None
#     cardId: str | None = None
#     categoryId: str | None = None
#     thirdId: str | None = None
#     __table__ = 'registry'