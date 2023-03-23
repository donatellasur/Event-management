from repository.Repo import Repo
from service.Serv import Serv
from domain.validators import Validator
from domain.entities import Event, Person
from termcolor import colored


# Repo tests
def testCreatePerson():
    pers = Person(1, "Dona Sur", "Dambovitei89", [])
    assert pers.get_id() == 1
    assert pers.get_name() == "Dona Sur"
    assert pers.get_address() == "Dambovitei89"


def testCreateEvent():
    event = Event(1, "11.11.2022", 120, "Teatru", [])
    assert event.get_id() == 1
    assert event.get_date() == "11.11.2022"
    assert event.get_time() == 120
    assert event.get_desc() == "Teatru"


def testAddPersonRepo():
    repo = Repo()
    pers1 = Person(1, "Dona Sur", "Dambovitei89", [])
    repo.addPerson(pers1)
    assert len(repo.getAllPersonsP()) == 1
    pers2 = Person(2, "Dona Sur", "Dambovitei89", [])
    pers3 = Person(3, "Dona Sur", "Dambovitei89", [])
    pers4 = Person(4, "Dona Sur", "Dambovitei89", [])
    repo.addPerson(pers2)
    repo.addPerson(pers3)
    repo.addPerson(pers4)
    assert len(repo.getAllPersonsP()) == 4


def testAddEventRepo():
    repo = Repo()
    event1 = Event(1, "11.11.2022", 120, "Teatru", [])
    repo.addEvent(event1)
    assert len(repo.getAllEventsE()) == 1
    event2 = Event(2, "11.11.2022", 120, "Teatru", [])
    event3 = Event(3, "11.11.2022", 120, "Teatru", [])
    event4 = Event(4, "11.11.2022", 120, "Teatru", [])
    repo.addEvent(event2)
    repo.addEvent(event3)
    repo.addEvent(event4)
    assert len(repo.getAllEventsE()) == 4


def testFindPersonRepo():
    repo = Repo()
    pers1 = Person(1, "Dona Sur", "Dambovitei89", [])
    repo.addPerson(pers1)
    assert repo.findPerson(1) == pers1
    try:
        repo.findPerson(2)
    except ValueError:
        raise ValueError("Person does not exist")


def testFindEventRepo():
    repo = Repo()
    event1 = Event(1, "11.11.2022", 120, "Teatru", [])
    repo.addEvent(event1)
    assert repo.findEvent(1) == event1
    try:
        repo.findEvent(2)
    except ValueError:
        raise ValueError("Event does not exist")


def testDeletePersonRepo():
    repo = Repo()
    pers1 = Person(1, "Dona Sur", "Dambovitei89", [])
    repo.addPerson(pers1)
    assert len(repo.getAllPersonsP()) == 1
    repo.deletePerson(1)
    assert len(repo.getAllPersonsP()) == 0
    try:
        repo.deletePerson(1)
    except ValueError:
        return


def testDeleteEventRepo():
    repo = Repo()
    event1 = Event(1, "11.11.2022", 120, "Teatru", [])
    repo.addEvent(event1)
    assert len(repo.getAllEventsE()) == 1
    repo.deleteEvent(1)
    assert len(repo.getAllEventsE()) == 0
    try:
        repo.deleteEvent(1)
    except ValueError:
        return


def testModifyPersonRepo():
    repo = Repo()
    pers1 = Person(1, "Dona Sur", "Dambovitei89", [])
    repo.addPerson(pers1)
    assert pers1.get_name() == "Dona Sur"
    repo.modifyPerson(pers1, "Sur", "undeva")
    assert pers1.get_name() == "Sur"


def testModifyEventRepo():
    repo = Repo()
    event1 = Event(1, "11.11.2022", 120, "Teatru", [])
    repo.addEvent(event1)
    assert event1.get_desc() == "Teatru"
    repo.modifyEvent(event1, "11.11.2022", 150, "Opera")
    assert event1.get_desc() == "Opera"


def testSignToEventRepo():
    repo = Repo()
    pers1 = Person(1, "Dona Sur", "Dambovitei89", [])
    repo.addPerson(pers1)
    event1 = Event(1, "11.11.2022", 120, "Teatru", [])
    repo.addEvent(event1)
    assert len(pers1.get_events()) == 0
    repo.signToEvent(pers1, event1)
    assert len(pers1.get_events()) == 1


# Serv tests
def testAddPersonServ():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addPerson(1, "Dona Sur", "Dambovitei89")
    assert len(serv.getAllPersonsP()) == 1
    serv.addPerson(2, "Dona Sur", "Dambovitei89")
    serv.addPerson(3, "Dona Sur", "Dambovitei89")
    serv.addPerson(4, "Dona Sur", "Dambovitei89")
    assert len(repo.getAllPersonsP()) == 4
    try:
        serv.addPerson(1, "", "Dambovitei89")
    except:
        return


def testAddEventServ():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addEvent(1, "11.11.2022", 120, "Teatru")
    assert len(serv.getAllEventsE()) == 1
    serv.addEvent(2, "11.11.2022", 120, "Teatru",)
    serv.addEvent(3, "11.11.2022", 120, "Teatru")
    serv.addEvent(4, "11.11.2022", 120, "Teatru")
    assert len(repo.getAllEventsE()) == 4
    try:
        serv.addEvent(1, "", 120, "Teatru")
    except:
        return


def testFindPersonServ():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addPerson(1, "Dona Sur", "Dambovitei89")
    pers1 = Person(1, "Dona Sur", "Dambovitei89", [])
    assert serv.findPerson(1) == pers1
    try:
        repo.findPerson(2)
    except ValueError:
        raise ValueError("Person does not exist")


def testFindEventServ():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addEvent(1, "11.11.2022", 120, "Teatru")
    event1 = Event(1, "11.11.2022", 120, "Teatru", [])
    assert serv.findEvent(1) == event1
    try:
        repo.findEvent(2)
    except ValueError:
        raise ValueError("Person does not exist")


def testDeletePersonServ():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addPerson(1, "Dona Sur", "Dambovitei89")
    assert len(serv.getAllPersonsP()) == 1
    serv.deletePerson(1)
    assert len(serv.getAllPersonsP()) == 0
    try:
        serv.deletePerson(1)
    except:
        return


def testDeleteEventServ():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addEvent(1, "11.11.2022", 120, "Teatru")
    assert len(serv.getAllEventsE()) == 1
    serv.deleteEvent(1)
    assert len(serv.getAllEventsE()) == 0
    try:
        serv.deleteEvent(1)
    except:
        return


def testModifyPersonServ():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addPerson(1, "Dona Sur", "Dambovitei89")
    pers1 = serv.findPerson(1)
    assert pers1.get_name() == "Dona Sur"
    serv.modifyPerson(1, "Sur", "undeva")
    assert pers1.get_name() == "Sur"


def testModifyEventServ():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addEvent(1, "11.11.2022", 120, "Teatru")
    ev1 = serv.findEvent(1)
    assert ev1.get_desc() == "Teatru"
    serv.modifyEvent(1, "11.11.2022", 150, "Opera")
    assert ev1.get_desc() == "Opera"


def testSignToEventServ():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addPerson(1, "Dona Sur", "Dambovitei89")
    pers1 = serv.findPerson(1)
    serv.addEvent(1, "11.11.2022", 120, "Teatru")
    event1 = serv.findEvent(1)
    assert len(pers1.get_events()) == 0
    serv.signToEvent(1, 1)
    assert len(pers1.get_events()) == 1
    try:
        serv.signToEvent(1, 1)
    except:
        return


def testTopEvents():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addPerson(0, "Dona Sur", "Dambovitei89")
    serv.addPerson(1, "Radu Simu", "Dambovitei 89")
    serv.addEvent(0, "11.11.2022", 120, "Teatru")
    serv.addEvent(1, "22.11.2022", 120, "Opera")
    serv.signToEvent(0, 0)
    serv.signToEvent(1, 1)
    assert serv.topEvents()[1] == {'event': 'Opera', 'nr_of_persons': 1}


def testTopPersons():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addPerson(0, "Dona Sur", "Dambovitei89")
    serv.addPerson(1, "Radu Simu", "Dambovitei 89")
    serv.addEvent(0, "11.11.2022", 120, "Teatru")
    serv.addEvent(1, "22.11.2022", 120, "Opera")
    serv.signToEvent(0, 0)
    serv.signToEvent(1, 1)
    assert serv.topPersons()[1] == {'pers': 'Radu Simu', 'nr_of_events': 1}


def testSortEvents():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addPerson(0, "Dona Sur", "Dambovitei89")
    serv.addEvent(0, "11.11.2022", 120, "Teatru")
    serv.addEvent(1, "22.11.2022", 120, "Opera")
    serv.addEvent(2, "11.11.2022", 120, "Polo")
    serv.signToEvent(0, 0)
    serv.signToEvent(0, 1)
    serv.signToEvent(0, 2)
    assert serv.sortEventsForPerson(0) == [{'id_event': 2, 'desc': 'Polo'}, {'id_event': 0, 'desc': 'Teatru'},
                                           {'id_event': 1, 'desc': 'Opera'}]


def testLeastPopularEvent():
    repo = Repo()
    val = Validator()
    serv = Serv(repo, val)
    serv.addPerson(0, "Dona Sur", "Dambovitei89")
    serv.addEvent(0, "11.11.2022", 120, "Teatru")
    serv.addEvent(1, "22.11.2022", 120, "Opera")
    serv.addEvent(2, "11.11.2022", 120, "Polo")
    serv.signToEvent(0, 0)
    serv.signToEvent(0, 1)
    assert serv.leastPopularEvent() == {'event': 'Opera', 'nr_of_persons': 1}


def runTests():
    testCreatePerson()
    testCreateEvent()
    # Repo test
    testAddPersonRepo()
    testAddEventRepo()
    testFindPersonRepo()
    testFindEventRepo()
    testDeletePersonRepo()
    testDeleteEventRepo()
    testModifyPersonRepo()
    testModifyEventRepo()
    testSignToEventRepo()
    # Serv test
    testAddPersonServ()
    testAddEventServ()
    testFindPersonServ()
    testFindEventServ()
    testDeletePersonServ()
    testDeleteEventServ()
    testModifyPersonServ()
    testModifyEventServ()
    testSignToEventServ()
    testTopEvents()
    testTopPersons()
    testSortEvents()
    testLeastPopularEvent()
    print(colored("Tests PASSED", "magenta"))
