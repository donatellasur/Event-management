from termcolor import colored


class Person:

    def __init__(self, id_person, name, address, events):
        self.__id = id_person
        self.__name = name
        self.__address = address
        self.__events = events

    # getters

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_events(self):
        return self.__events

    # setters

    def set_id(self, value):
        self.__id = value

    def set_name(self, value):
        self.__name = value

    def set_address(self, value):
        self.__address = value

    def set_events(self, value):
        self.__events = value

    # others

    def __eq__(self, other):
        if self.get_id() == other.get_id():
            return True
        return False

    def __str__(self):
        return colored('ID:' + str(self.__id) + '\nName:' + self.__name + '\nAdaress:' +
                       self.__address + '\n', 'magenta')


class Event:
    def __init__(self, id_event, date, time, description, persons):
        self.__id = id_event
        self.__date = date
        self.__time = time
        self.__desc = description
        self.__persons = persons

    # getters

    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_desc(self):
        return self.__desc

    def get_persons(self):
        return self.__persons

    # setters

    def set_id(self, value):
        self.__id = value

    def set_date(self, value):
        self.__date = value

    def set_time(self, value):
        self.__time = value

    def set_desc(self, value):
        self.__desc = value

    def set_persons(self, value):
        self.__persons = value

    # others

    def __eq__(self, other):
        if self.get_id() == other.get_id():
            return True
        return False

    def __str__(self):
        return colored('ID: ' + str(self.__id) + '\nDate: ' + self.__date + '\nTime: ' + str(self.__time) +
                       '\nDescription: ' + self.__desc + '\n', 'magenta')
