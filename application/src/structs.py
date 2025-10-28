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
    username: str
    profile: Profile
    shareType: int