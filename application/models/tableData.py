from typing import Iterable, Any

class NavigableTableData:
    def __init__(self, maxLen:int, data:dict[Any, Iterable]=None):
        self.__maxLen = maxLen
        self.__lenData = 0
        self.__index = 0
        self.__numIntervals = 0
        self.__intervals = []
        self.__data = {}
        if data: self.setData(data)

    def setData(self, data:dict[Any, Iterable]):
        maxLen = self.__maxLen
        self.__lenData = len(data)
        self.__data = data
        self.__index = 0
        self.__numIntervals = self.__lenData // maxLen + bool(self.__lenData % maxLen)
        self.__intervals = [[] for _ in range(self.__numIntervals)]

        count = 0
        intervalIndex = 0
        for k, v in data.items():
            self.__intervals[intervalIndex].append([k] + list(v))

            count += 1
            if count == maxLen:
                intervalIndex += 1
                count = 0

    def getData(self) -> dict[Any, Iterable]: return self.__data

    @property
    def maxLen(self): return self.__maxLen

    @property
    def start(self):
        return (self.__index * self.__maxLen + 1) if self.__lenData else 0
    
    @property
    def end(self): return (self.__index * self.__maxLen + len(self.currentInterval())) if self.__lenData else 0
    
    @property
    def total(self): return self.__lenData

    @property
    def index(self): return self.__index
    
    def hasNext(self) -> bool:
        return self.__index < self.__numIntervals - 1
    
    def hasPrevious(self) -> bool:
        return self.__index > 0

    def next(self) -> list | None:
        if not self.hasNext(): return
        self.__index += 1
        return self.__intervals[self.__index]

    def previous(self) -> list | None:
        if not self.hasPrevious(): return
        self.__index -= 1
        return self.__intervals[self.__index]
    
    def currentInterval(self) -> list | None:
        if self.__lenData:
            return self.__intervals[self.__index]
    
if __name__ == '__main__':
    data = NavigableTableData(2, {'row1': [1, 2, 3], 'row2': [4, 5, 6], 'row3': [7, 8, 9]})

    print('current', data.index, data.currentInterval())
    while data.hasNext():
        d = data.next()
        print(data.index, d)
    
    print('current', data.index, data.currentInterval())
    while data.hasPrevious():
        d = data.previous()
        print(data.index, d)

    print('current', data.index, data.currentInterval())