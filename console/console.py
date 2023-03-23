import random
from termcolor import colored
from domain.validators import ValidatorExceptions


class Console:
    def __init__(self, srv):
        self.__srv = srv

    def showAllPersons(self):
        pers = self.__srv.getAllPersonsP()
        for i in range(0, len(pers)):
            print(pers[i])

    def showAllEvents(self):
        events = self.__srv.getAllEventsE()
        for i in range(0, len(events)):
            print(events[i])

    def showAllPersonEvents(self):
        Id = input("Person id: ")
        persEvents = self.__srv.getAllPersonEvents(Id)
        print(persEvents)

    def showAllEventPersons(self):
        Id = input("Event id: ")
        eventPersons = self.__srv.getAllEventPersons(Id)
        print(eventPersons)

    def addPerson(self):
        ID = input("Id: ")
        n = input("Name: ")
        adr = input("Address: ")
        try:
            pers = self.__srv.addPerson(ID, n, adr)
            print(colored("Person:\n", "green") + str(pers) + colored("was added succesfully", "green"))
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def addEvent(self):
        ID = input("Id: ")
        date = input("Date: ")
        time = input("Duration: ")
        desc = input("Description: ")
        try:
            event = self.__srv.addEvent(ID, date, time, desc)
            print(colored("Event:\n", "green") + str(event) + colored("was added succesfully", "green"))
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def findPerson(self):
        ID = input("Id: ")
        try:
            pers = self.__srv.findPerson(ID)
            print(colored(str(pers), "magenta"))
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def findEvent(self):
        ID = input("Id: ")
        try:
            event = self.__srv.findEvent(ID)
            print(colored(str(event), "magenta"))
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def deletePerson(self):
        ID = input("Id: ")
        try:
            pers = self.__srv.deletePerson(ID)
            print(colored("Person:\n", "green") + str(pers) + colored("was deleted succesfully", "green"))
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def deleteEvent(self):
        ID = input("Id: ")
        try:
            event = self.__srv.deleteEvent(ID)
            print(colored("Event:\n", "green") + str(event) + colored("was deleted succesfully", "green"))
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def modifyPerson(self):
        ID = input("Id: ")
        try:
            pers = self.__srv.findPerson(ID)
            newName = input("New name: ")
            newAddress = input("New address: ")
            print(colored("Person:\n", "green") + str(pers) + colored("was modified successfully to", "green"))
            pers1 = self.__srv.modifyPerson(ID, newName, newAddress)
            print(str(pers1))
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def modifyEvent(self):
        ID = input("Id: ")
        try:
            event = self.__srv.findEvent(ID)
            newDate = input("New date: ")
            newTime = input("New duration: ")
            newDesc = input("New description: ")
            print(colored("Event:\n", "green") + str(event) + colored("was modified successfully to", "green"))
            event1 = self.__srv.modifyEvent(ID, newDate, newTime, newDesc)
            print(str(event1))
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def signPersToEvent(self):
        IDPers = input("Person id: ")
        IDEvent = input("Event id: ")
        try:
            pers = self.__srv.findPerson(IDPers)
            event = self.__srv.findEvent(IDEvent)
            self.__srv.signToEvent(IDPers, IDEvent)
            print(colored("Person:\n", "green") + str(pers) + colored("was signed to:\n", "green") + str(event))
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def randomPersons(self):
        try:
            # nr = random.randint(10, 100)
            nr = input("Enter a number: ")
            self.__srv.generatePersons(nr)
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))
        self.showAllPersons()

    def randomEvents(self):
        try:
            nr = random.randint(1, 20)
            self.__srv.generateEvents(nr)
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))
        self.showAllEvents()

    def topEvents(self):
        print("Events NrPersons:")
        try:
            aux = self.__srv.top20Events()
            for i in aux:
                print(i['event'], "   ", i['nr_of_persons'], end="\n")
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def topPersons(self):
        print("Persons    NrEvents:")
        try:
            aux = self.__srv.topPersons()
            for i in aux:
                print(i['pers'], "   ", i['nr_of_events'], end="\n")
        except ValidatorExceptions as ve:
            print(colored(str(ve)), "red")

    def sortEvents(self):
        ID = input("Enter person id: ")
        try:
            print("Events    Dates:")
            aux = self.__srv.sortEventsForPerson(ID)
            for i in aux:
                evI = self.__srv.findEvent(i['id_event'])
                print(i['desc'], "   ", evI.get_date())
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def leastPopularEvent(self):
        try:
            print("Events NrPersons:")
            aux = self.__srv.leastPopularEvent()
            print(aux['event'], "   ", aux['nr_of_persons'])
        except ValidatorExceptions as ve:
            print(colored(str(ve), "red"))

    def showUI(self):
        self.__srv.populatePersons()
        self.__srv.populateEvents()
        while True:
            menu = """
Meniu:
0. Exit
1. Add:
2. Delete:
3. Modify:
4. Find:
5. Sign to event
6. Sort a persons events list by desc and date
7. Top persons
8. Top 20% most popular events
9. Least popular event
10. Show all:
11. Show events a person is signed to
12. Show persons signed to an event
13. Random:
            """
            menu2 = """
0. Return
1. Person
2. Event
            """
            print(colored(menu, "blue"))
            cmd = input("Enter your command: ")

            if cmd == '0':
                break

            elif cmd == '1':
                print(colored(menu2, "yellow"))
                cmd1 = input("Enter your command: ")
                while cmd1 != '0':
                    if cmd1 == '1':
                        self.addPerson()
                        break
                    elif cmd1 == '2':
                        self.addEvent()
                        break
                    else:
                        print(colored("Ivalid command", "red"))
                        print(colored(menu2, "yellow"))
                        cmd1 = input("Enter your command: ")

            elif cmd == '2':
                print(colored(menu2, "yellow"))
                cmd2 = input("Enter your command: ")
                while cmd2 != '0':
                    if cmd2 == '1':
                        self.deletePerson()
                        break
                    elif cmd2 == '2':
                        self.deleteEvent()
                        break
                    else:
                        print(colored("Ivalid command", "red"))
                        print(colored(menu2, "yellow"))
                        cmd2 = input("Enter your command: ")

            elif cmd == '3':
                print(colored(menu2, "yellow"))
                cmd4 = input("Enter your command: ")
                while cmd4 != '0':
                    if cmd4 == '1':
                        self.modifyPerson()
                        break
                    elif cmd4 == '2':
                        self.modifyEvent()
                        break
                    else:
                        print(colored("Ivalid command", "red"))
                        print(colored(menu2, "yellow"))
                        cmd4 = input("Enter your command: ")

            elif cmd == '4':
                print(colored(menu2, "yellow"))
                cmd3 = input("Enter your command: ")
                while cmd3 != '0':
                    if cmd3 == '1':
                        self.findPerson()
                        break
                    elif cmd3 == '2':
                        self.findEvent()
                        break
                    else:
                        print(colored("Ivalid command", "red"))
                        print(colored(menu2, "yellow"))
                        cmd3 = input("Enter your command: ")

            elif cmd == '5':
                self.signPersToEvent()

            elif cmd == '6':
                self.sortEvents()

            elif cmd == '7':
                self.topPersons()

            elif cmd == '8':
                self.topEvents()

            elif cmd == '9':
                self.leastPopularEvent()

            elif cmd == '10':
                print(colored(menu2, "yellow"))
                cmd10 = input("Enter your command: ")
                while cmd10 != '0':
                    if cmd10 == '1':
                        self.showAllPersons()
                        break
                    elif cmd10 == '2':
                        self.showAllEvents()
                        break
                    else:
                        print(colored("Ivalid command", "red"))
                        print(colored(menu2, "yellow"))
                        cmd10 = input("Enter your command: ")

            elif cmd == '11':
                self.showAllPersonEvents()

            elif cmd == '12':
                self.showAllEventPersons()

            elif cmd == '13':
                print(colored(menu2, "yellow"))
                cmd13 = input("Enter your command: ")
                while cmd13 != '0':
                    if cmd13 == '1':
                        self.randomPersons()
                        break
                    elif cmd13 == '2':
                        self.randomEvents()
                        break
                    else:
                        print(colored("Ivalid command", "red"))
                        print(colored(menu2, "yellow"))
                        cmd13 = input("Enter your command: ")

            else:
                print(colored("Ivalid command", "red"))

