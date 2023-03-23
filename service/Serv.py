import random
import string

from domain.entities import Person, Event
from domain.validators import ValidatorExceptions


class Serv:
    def __init__(self, repo, val):
        self.__repo = repo
        self.__val = val

    def getAllPersonsP(self):
        return self.__repo.getAllPersonsP()

    def getAllEventsE(self):
        return self.__repo.getAllEventsE()

    def addPerson(self, id_person, name, address):
        """
        validates and adds a person to list
        @params:
        id_person: int
        name, address: str
        person contains all @params
        return: person
        """
        self.__val.valInt(id_person)
        id_person = int(id_person)
        pers = Person(id_person, name, address, [])
        self.__val.validatePerson(pers)
        persons = self.__repo.getAllPersonsP()
        for i in range(0, len(persons)):
            if pers.get_id() == persons[i].get_id():
                raise ValidatorExceptions("There already is a person with this id")
        self.__repo.addPerson(pers)
        return pers

    def addEvent(self, id_event, date, time, desc):
        """
        validates and adds an event to list
        @params:
        id_event, time: int
        date, desc: str
        event contains all @params
        return: event
        """
        self.__val.valInt(id_event)
        id_event = int(id_event)
        self.__val.valInt(time)
        time = int(time)
        event = Event(id_event, date, time, desc, [])
        self.__val.validateEvent(event)
        events = self.__repo.getAllEventsE()
        for i in range(0, len(events)):
            if event.get_id() == events[i].get_id():
                raise ValidatorExceptions("There already is an event with this id")
        self.__repo.addEvent(event)
        return event

    def findPerson(self, id_person):
        """
        validates and searches in list a person with the id given
        @param: id_person: int = id by which we search
        returns: the person with the id given
        """
        self.__val.valInt(id_person)
        id_person = int(id_person)
        pers = self.__repo.findPerson(id_person)
        self.__val.validatePersonExists(pers)
        return pers

    def findEvent(self, id_event):
        """
        validates and searches in list an event with the id given
        @param: id_event: int = id by which we search
        returns: the event with the id given
        """
        self.__val.valInt(id_event)
        id_event = int(id_event)
        event = self.__repo.findEvent(id_event)
        self.__val.validateEventExists(event)
        return event

    def deletePerson(self, id_person):
        """
        validates and deletes from list a person with the id given
        @param: id_person: int = id by which we search and delete
        returns: the person that was deleted
        """
        self.__val.valInt(id_person)
        id_person = int(id_person)
        person = self.findPerson(id_person)
        pers = self.__val.validatePersonExists(person)
        self.__repo.deletePerson(id_person)
        return person

    def deleteEvent(self, id_event):
        """
        validates and deletes from list an event with the id given
        @param: id_event: int = id by which we search and delete
        returns: the event that was deleted
        """
        self.__val.valInt(id_event)
        id_event = int(id_event)
        event = self.findEvent(id_event)
        ev = self.__val.validateEventExists(event)
        self.__repo.deleteEvent(id_event)
        return event

    def modifyPerson(self, id_person, new_name, new_address):
        """
        modifies the person with the id given with a new name and address
        @params: id_person: int = id by which we search and modify
        new_name: string = a new value for name
        new_address: string = a new value for address
        returns: the modified person
        """
        self.__val.valInt(id_person)
        id_person = int(id_person)
        person = self.findPerson(id_person)
        return self.__repo.modifyPerson(person, new_name, new_address)

    def modifyEvent(self, id_event, new_date, new_time, new_desc):
        """
        modifies the event with the id given with a new date, time and description
        @params: id_event: int = id by which we search and modify
        new_date: string = a new value for date
        new_time: int = a new value for duration
        new_desc: string = a new value for description
        returns: the modified event
        """
        self.__val.valInt(id_event)
        id_event = int(id_event)
        event = self.findEvent(id_event)
        self.__repo.modifyEvent(event, new_date, new_time, new_desc)

    def populatePersons(self):
        """
        adds 2 persons to the list
        """
        self.addPerson(0, 'Dona Sur', 'Dambovitei89')
        self.addPerson(1, 'Radu Simu', 'Stefan cel Mare 34')

    def populateEvents(self):
        """
        adds 2 events to the list
        """
        self.addEvent(0, '11.11.2022', 120, 'Teatru')
        self.addEvent(1, '22.11.2022', 150, 'Opera')
        self.addEvent(2, '11.11.2022', 150, 'Balet')
        self.addEvent(3, '11.11.2022', 150, 'Polo')
        self.addEvent(4, '11.11.2022', 150, 'Baschet')

    def signToEvent(self, id_pers, id_event):
        """
        validates and signs a person found by id to an event found by id
        """
        self.__val.valInt(id_pers)
        id_pers = int(id_pers)
        self.__val.valInt(id_event)
        id_event = int(id_event)
        person = self.findPerson(id_pers)
        event = self.findEvent(id_event)
        for e in person.get_events():
            if e['id_event'] == id_event:
                raise ValidatorExceptions("Person is already signed to this event")
        return self.__repo.signToEvent(person, event)

    def getAllPersonEvents(self, id_person):
        """
        validates and returns all events for a person searched by id
        """
        self.__val.valInt(id_person)
        id_person = int(id_person)
        pers = self.findPerson(id_person)
        if pers is not None:
            return self.__repo.getAllEventsForPerson(pers)
        else:
            raise ValidatorExceptions("Person doesn't exist")

    def getAllEventPersons(self, id_event):
        """
        validates and returns all persons for an event searched by id
        """
        self.__val.valInt(id_event)
        id_event = int(id_event)
        event = self.findEvent(id_event)
        if event is not None:
            return self.__repo.getAllPersonsForEvent(event)
        else:
            raise ValidatorExceptions("Event doesn't exist")

    @staticmethod
    def randomString(length=None):
        """
        generates random string
        """
        length = length if length is not None else random.randint(1, 20)
        lit = string.ascii_letters
        str_list = [random.choice(lit) for _ in range(length)]
        random_str = "".join(str_list)
        return random_str

    def generatePersons(self, number):
        """
        generates random person entities
        """
        self.__val.valInt(number)
        number = int(number)
        for i in range(0, number):
            nr = string.digits
            digit_list = [random.choice(nr) for _ in range(2)]
            ID = "".join(digit_list)
            ID = int(ID)
            name = self.randomString(random.randint(1, 20))
            address = self.randomString(random.randint(1, 20))
            pers = Person(ID, name, address, [])
            self.__val.validatePerson(pers)
            persons = self.__repo.getAllPersonsP()
            for j in range(0, len(persons)):
                if pers.get_id() == persons[j].get_id():
                    raise ValidatorExceptions("There already is a person with this id")
            self.__repo.addPerson(pers)

    def generateEvents(self, number):
        """
        generates random event entities
        """
        self.__val.valInt(number)
        number = int(number)
        for i in range(0, number):
            nr = string.digits
            digit_list = [random.choice(nr) for _ in range(2)]
            ID = "".join(digit_list)
            ID = int(ID)
            day = "".join(digit_list)
            month = "".join(digit_list)
            year_list = [random.choice(nr) for _ in range(4)]
            year = "".join(year_list)
            date1 = day + "." + month + "." + year
            time = [random.choice(nr) for _ in range(3)]
            time1 = "".join(time)
            time1 = int(time1)
            desc = self.randomString(random.randint(1, 20))
            event = Event(ID, date1, time1, desc, [])
            self.__val.validateEvent(event)
            events = self.getAllEventsE()
            for k in range(0, len(events)):
                if event.get_id() == events[k].get_id():
                    raise ValidatorExceptions("There already is an event with this id")
            self.__repo.addEvent(event)

    def topEvents(self):
        """
        events top
        """
        eventsStats = {}
        all_pers = self.getAllPersonsP()
        for pr in all_pers:
            persID = pr.get_id()
            all_events = self.getAllPersonEvents(persID)
            for ev in all_events:
                if ev['id_event'] not in eventsStats:
                    eventsStats[ev['id_event']] = 1
                else:
                    eventsStats[ev['id_event']] += 1
        res = []
        for statsKey in eventsStats:
            eventName = self.findEvent(statsKey).get_desc()
            personsNumber = eventsStats[statsKey]
            eventToBeWritten = {'event': eventName, 'nr_of_persons': personsNumber}
            res.append(eventToBeWritten)
        for i in range(len(res) - 1):
            for j in range(i + 1, len(res)):
                if res[i]['nr_of_persons'] < res[j]['nr_of_persons']:
                    aux = res[i]
                    res[i] = res[j]
                    res[j] = aux
        return res

    def top20Events(self):
        """
        first 20% events with the most people
        """
        res = self.topEvents()
        if len(res) >= 5:
            return res[:len(res) // 5]
        else:
            return res

    def topPersons(self):
        """
        persons top
        """
        persStats = {}
        all_ev = self.getAllEventsE()
        for ev in all_ev:
            evID = ev.get_id()
            all_pers = self.getAllEventPersons(evID)
            for pers in all_pers:
                if pers['id_person'] not in persStats:
                    persStats[pers['id_person']] = 1
                else:
                    persStats[pers['id_person']] += 1
        res = []
        for statsKey in persStats:
            persName = self.findPerson(statsKey).get_name()
            eventsNumber = persStats[statsKey]
            persToBeWritten = {'pers': persName, 'nr_of_events': eventsNumber}
            res.append(persToBeWritten)
        for i in range(len(res)-1):
            for j in range(i+1, len(res)):
                if res[i]['nr_of_events'] < res[j]['nr_of_events']:
                    aux = res[i]
                    res[i] = res[j]
                    res[j] = aux
        return res

    def sortEventsForPerson(self, id_person):
        """
        sorts the events a person is signed to by date, and if the date is equal than it is sorted alphabetically
        """
        self.__val.valInt(id_person)
        id_person = int(id_person)
        pers = self.findPerson(id_person)
        persEvents = self.getAllPersonEvents(id_person)
        for i in range(0, len(persEvents)-1):
            if persEvents[i]['desc'] > persEvents[i+1]['desc']:
                aux = persEvents[i]
                persEvents[i] = persEvents[i+1]
                persEvents[i+1] = aux
        for i in range(0, len(persEvents)-1):
            ev1 = self.findEvent(persEvents[i]['id_event'])
            ev2 = self.findEvent(persEvents[i+1]['id_event'])
            date1 = ev1.get_date()
            date2 = ev2.get_date()
            day1, month1, year1 = str(date1).split(".")
            day2, month2, year2 = str(date2).split(".")
            if year1 > year2:
                aux = persEvents[i]
                persEvents[i] = persEvents[i + 1]
                persEvents[i + 1] = aux
            elif year1 == year2 and month1 > month2:
                aux = persEvents[i]
                persEvents[i] = persEvents[i + 1]
                persEvents[i + 1] = aux
            elif year1 == year2 and month1 == month2 and day1 > day2:
                aux = persEvents[i]
                persEvents[i] = persEvents[i + 1]
                persEvents[i + 1] = aux
        return persEvents

    def leastPopularEvent(self):
        """
        shows the event with the lowest number of persons signed to it, at least one person has to be signed
        if 2 events have the same number of persons, the program will return the one that has been added first in the
        events list
        """
        res = self.topEvents()
        return res[len(res)-1]

