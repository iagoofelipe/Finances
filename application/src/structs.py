from dataclasses import dataclass

@dataclass
class LoginData:
    username: str
    password: str
    remember: bool

@dataclass
class User:
    id: str
    username: str
    name: str
    email: str
    password: str