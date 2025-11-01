from configparser import ConfigParser
import os
from typing import TypeVar

from finances.core.consts import FILE_CONFIG

_T = TypeVar('_T')

class Configuration:

    def __init__(self):
        self.__config = ConfigParser()

        if os.path.exists(FILE_CONFIG):
            with open(FILE_CONFIG) as f:
                self.__config.read_file(f)

        if not self.__config.has_section('credentials'):
            self.__config.add_section('credentials')

    @property
    def parser(self):
        return self.__config
    
    def get(self, section:str, option:str, default:_T=None) -> str | _T:
        if self.__config.has_option(section, option):
            return self.__config[section][option]
        
        return default
    
    def removeOption(self, section:str, option:str):
        if not self.__config.has_option(section, option):
            return
        
        self.__config.remove_option(section, option)
        self.updateFile()

    def removeOptions(self, *args:tuple[str, str]):
        toUpdate = False

        for section, op in args:
            if self.__config.has_option(section, op):
                toUpdate = True
                self.__config.remove_option(section, op)
        
        if toUpdate:
            self.updateFile()
    
    def updateFile(self):
        with open(FILE_CONFIG, 'w') as f:
            self.__config.write(f)