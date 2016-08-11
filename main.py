import argparse


class Application(object):

    def __init__(self):
        self.reader = Reader()
        employee = Employee()
        employee.set_first_name('Jared')
        employee.set_last_name('Hooper')
        employee.add_pick(1)
        employee.add_pick(2)
        employee.add_pick(3)
        employee.add_pick(4)
        employee.add_pick(5)
        employee.pick_powerball(5)
        print(employee)


class Reader(object):
    pass


class Employee(object):
    """
    Holds Employee first name, last name & picks.
    """

    def __init__(self):
        self.__picks = []

    def set_first_name(self, _name):
        self.__fname = _name

    def set_last_name(self, _name):
        self.__lname = _name

    def add_pick(self, _pick):
        # returns True on success
        if self.validate_pick(_pick):
            self.__picks.append(str(_pick))
            self.__picks.sort()
            return True

    def validate_pick(self, _pick):
        return str(_pick) not in self.__picks and isinstance(_pick, int)

    def pick_powerball(self, _pb):
        if isinstance(_pb, int):
            self.__pball = str(_pb)

    def __str__(self):
        return " ".join([self.__fname, self.__lname] + self.__picks + ['Powerball:', self.__pball])

if __name__ == '__main__':
    application = Application()
