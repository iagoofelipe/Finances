from dataclasses import dataclass
from PySide6.QtCore import QDate

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

@dataclass
class Profile:
    id: str
    roleId: str
    name: str
    isOwner: bool
    ownerName: str
    editPermission: str
    viewPermission: str
    pendingShare: bool
    accessType: str

@dataclass
class ProfileThirdAccess:
    id: str
    userId: str
    userName: str
    profileId: str
    profileName: str
    editPermission: str
    viewPermission: str
    pendingShare: bool
    status: str

@dataclass
class ShareProfile:
    email: str
    profile: Profile
    shareType: int

@dataclass
class Registry:
    id: str
    title: str
    pending: bool
    value: float
    date: QDate
    category: str
    operation: int
    description: str
    accountId: str = None
    destinyAccountId: str = None
    cardId: str = None
    installments: int = None

@dataclass
class Account:
    id: str
    name: str

@dataclass
class Card:
    id: str
    name: str
    dueDay: int
    limit: int