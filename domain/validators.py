from domain.entities import Person, Event
from exceptions.exceptions import ValidatorExceptions


class Validator(Exception):
    @staticmethod
    def valInt(a):
        """
        Validation of an entity to be int
        """
        try:
            a = int(a)
        except ValueError:
            raise ValidatorExceptions("Id must be a number")
        return a

    @staticmethod
    def validatePerson(person):
        """
        Validation of a Person etity:
        positive id
        first/lastnames can't be null
        address can't be null
        """

        errorsP = []

        if int(person.get_id()) < 0:
            errorsP.append("ID has to be a positive number")
        if person.get_id() == "":
            errorsP.append("ID can't be null")
        if person.get_name() == "":
            errorsP.append("Name can't be null")
        if person.get_address() == "":
            errorsP.append("Address can't be null")
        if len(errorsP) > 0:
            errorsP_str = '\n'.join(errorsP)
            raise ValidatorExceptions(errorsP_str)

    @staticmethod
    def validatePersonExists(person):
        errorsP = []
        if person is None:
            errorsP.append("Person doesn't exist")
        if len(errorsP) > 0:
            raise ValidatorExceptions(errorsP)

    @staticmethod
    def validateEvent(event):
        """
        Validation of Event entity:
        positive id
        date can't be null
        time can't be negative
        description can't be null
        """

        errorsE = []
        if int(event.get_id()) < 0:
            errorsE.append("ID has to be a positive number")
        if event.get_date() == "":
            errorsE.append("Date can't be null")
        if int(event.get_time()) < 0:
            errorsE.append("Time has to be a positive number")
        if event.get_desc() == "":
            errorsE.append("Description can't be null")
        if len(errorsE) > 0:
            errorsE_str = '\n'.join(errorsE)
            raise ValidatorExceptions(errorsE_str)

    @staticmethod
    def validateEventExists(event):
        errorsE = []
        if event is None:
            errorsE.append("Event doesn't exist")
        if len(errorsE) > 0:
            raise ValidatorExceptions(errorsE)


def test_validatePerson():
    val = Validator()
    p1 = Person(1, 'Dona Sur', 'Dambovitei89', [])
    p2 = Person(-1, 'Dona Sur', 'Dambovitei89', [])
    p3 = Person(1, '', 'Dambovitei89', [])
    p4 = Person(1, 'Dona Sur', '', [])
    p5 = Person(-1, 'Dona Sur', '', [])
    try:
        val.validatePerson(p1)
        val.validatePerson(p2)
        val.validatePerson(p3)
        val.validatePerson(p4)
        val.validatePerson(p5)
        assert False
    except ValueError:
        assert True


def test_validateEvent():
    val = Validator()
    e1 = Event(1, '11.11.2022', 120, 'Teatru', [])
    e2 = Event(-1, '11.11.2022', 120, 'Teatru', [])
    e3 = Event(1, '', 120, 'Teatru', [])
    e4 = Event(1, '11.11.2022', -120, 'Teatru', [])
    e5 = Event(1, '11.11.2022', 120, '', [])
    e6 = Event(1, '11.11.2022', -120, '', [])
    try:
        val.validateEvent(e1)
        val.validateEvent(e2)
        val.validateEvent(e3)
        val.validateEvent(e4)
        val.validateEvent(e5)
        val.validateEvent(e6)
        assert False
    except ValueError:
        assert True
