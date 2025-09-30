from enum import Enum, auto
from dataclasses import dataclass
from PySide6.QtCore import QDate, QDateTime
from typing import TypeVar, Iterable, Generic

T = TypeVar('T')

class RegType(Enum):
    OUT = 0
    IN = 1

@dataclass
class User:
    id: str
    name: str
    username: str
    password: str

@dataclass
class Category:
    id: str
    name: str
    type: RegType
    description: str = ''

@dataclass
class Card:
    id: str
    name: str

@dataclass
class Registry:
    id: str
    type: RegType
    title: str
    value: float
    datetime: QDateTime
    description: str = ''
    card: Card | None = None
    category: Category | None = None

@dataclass
class DashParams:
    start: QDate
    end: QDate
    regType: RegType
    # allCategories: bool
    # categories: set[Category] | None

@dataclass
class TableParams:
    orderByColumn: str
    alphabetically: bool = True

@dataclass
class RegTableParams(TableParams):
    titleContains: str = ''
    type: RegType | None = None

class NavigableData(Generic[T]):
    def __init__(self, data:Iterable[T], maxLen:int):
        if maxLen < 1:
            raise ValueError('maxLen must be bigger than 0')
        
        self.__max = maxLen
        self.setData(data)

    def setData(self, data:Iterable[T]):
        self.__data = data
        self.__len = len(data)
        self.__numIntervals = self.__len // self.__max + bool(self.__len % self.__max)
        self.__splitted = [[] for _ in range(self.__numIntervals)]
        self.__index = 0

        count = 0
        index = 0
        for d in data:
            self.__splitted[index].append(d)
            count += 1

            if count == self.__max:
                count = 0
                index += 1

        if self.__len:
            self.__start = 1
            self.__end = len(self.__splitted[0])

        else:
            self.__start = 0
            self.__end = 0

        # convertendo em tuple
        self.__splitted = [tuple(v) for v in self.__splitted]

    @property
    def numIntervals(self) -> int: return self.__numIntervals

    def __len__(self): return self.__len

    @property
    def all(self): return self.__data

    @property
    def start(self) -> int:
        return self.__start

    @property
    def end(self) -> int:
        return self.__end

    def hasNext(self) -> bool:
        return self.__index < self.__numIntervals - 1

    def hasPrevious(self) -> bool:
        return self.__index > 0

    def previous(self) -> tuple[T] | None:
        if not self.hasPrevious():
            return
        
        self.__index -= 1
        return self.__updateStartEnd(self.__splitted[self.__index])
    
    def next(self) -> tuple[T] | None:
        if not self.hasNext():
            return
        
        self.__index += 1
        return self.__updateStartEnd(self.__splitted[self.__index])

    def currentIndex(self) -> int:
        return self.__index

    def currentInterval(self) -> tuple[T] | None:
        if 0 <= self.__index < self.__numIntervals:
            return self.__splitted[self.__index]
        
    def __updateStartEnd(self, d):
        self.__start = self.__index * self.__max + 1
        self.__end = self.__start + len(d) - 1
        return d