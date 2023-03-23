class Repo:
    def __init__(self):
        self.__persons = []
        self.__events = []

    def getAllPersonsP(self):
        """
        returns all persons
        """
        return self.__persons

    def getAllEventsE(self):
        """
        returns all the events
        """
        return self.__events

    @staticmethod
    def getAllEventsForPerson(person):
        """
        returns the parameter events of entity person
        """
        return person.get_events()

    @staticmethod
    def getAllPersonsForEvent(event):
        """
        returns the parameter persons of entity event
        """
        return event.get_persons()

    def addPerson(self, person):
        """
        adds a person to list
        @param: person = the entity that has to be added
        @raises: ValueError if the entity already exists in list
        """
        self.__persons.append(person)

    def addEvent(self, event):
        """
        adds an event to list
        @param: event = the entity that has to be added
        @raises: ValueError if the entity already exists in list
        """
        self.__events.append(event)

    def findPerson(self, id_person):
        """
        finds a person with the id given
        @param: id_person = the id by which we search
        return: the entity that was searched for
        """
        for i in range(0, len(self.__persons)):
            if id_person == self.__persons[i].get_id():
                return self.__persons[i]

    def findEvent(self, id_event):
        """
        finds an event with the id given
        @param: id_event = the id by which we search
        return: the entity that was searched for
        """
        for i in range(0, len(self.__events)):
            if id_event == self.__events[i].get_id():
                return self.__events[i]

    def deletePerson(self, id_person):
        """
        deletes an entity from list
        @param: id_person = the id of the entity we want to delete
        @raises: ValueError if no entity was found by the id given
        """
        for i in range(id_person, len(self.__persons)-1):
            self.__persons[i] = self.__persons[i+1]
        if len(self.__persons) > 0:
            del self.__persons[len(self.__persons)-1]
        else:
            return

    def deleteEvent(self, id_event):
        """
        deletes an entity from list
        @param: id_event = the id of the entity we want to delete
        @raises: ValueError if no entity was found by the id given
        """
        for i in range(id_event, len(self.__events)-1):
            self.__events[i] = self.__events[i + 1]
        if len(self.__events) > 0:
            del self.__events[len(self.__events) - 1]
        else:
            return

    @staticmethod
    def modifyPerson(person, nn, addr):
        """
        sets new values to name and address
        @param: person: Person
        nn: string = new name
        addr: string = new address
        returns: the modified entity
        """
        person.set_name(nn)
        person.set_address(addr)
        return person

    @staticmethod
    def modifyEvent(event, ndate, ntime, ndesc):
        """
        sets new values for date, time and description
        @params: event = Event
        ndate: string = new date
        ntime: int = new time
        ndesc: string = new desc
        returns: the modified entity
        """
        event.set_date(ndate)
        event.set_time(ntime)
        event.set_desc(ndesc)
        return event

    @staticmethod
    def signToEvent(person, event):
        """
        signs a person to an event
        adds the person to persons list of the event
        adds the event to events list of the person
        @params: person: Person
        event: Event
        returns: the event the person was signed to
        """
        persEvent = {'id_event': event.get_id(), 'desc': event.get_desc()}
        eventPerson = {'id_person': person.get_id(), 'name': person.get_name()}
        person.get_events().append(persEvent)
        event.get_persons().append(eventPerson)
        return person.get_events()[len(person.get_events())-1]
        # return persEvent
