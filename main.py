import argparse

from collections import Counter
import random

BOTTOM_RANGE = 1
TOP_RANGE_REGULAR = 69
TOP_RANGE_POWERBALL = 26


class Application(object):

    def __init__(self):
        self.employees = []
        self.winning_numbers = Counter()
        self.powerball = Counter()
        pass

    def run(self):
        position = 0
        NUMBER_START = 3  # after fname lname
        employee = Employee()  # first employee
        while(position < NUMBER_START + 6):

            if position == 0:  # first name
                first_name = input('First Name: ')
                success = employee.set_first_name(first_name)

            elif position == 1:  # last name
                last_name = input('Last Name: ')
                success = employee.set_last_name(last_name)

            elif position >= NUMBER_START \
                    and position < NUMBER_START + 5:
                pick = input('Select ' + str(position - 2) + ': ')
                success = employee.add_pick(pick)
                if success:
                    self.winning_numbers[pick] += 1

            elif position == NUMBER_START + 5:
                pick = input('Select Powerball Number: ')
                success = employee.pick_powerball(pick)
                if success:
                    self.powerball[pick] += 1

            if success:
                position += 1

        self.employees.append(employee)

        if self.prompt_done():
            self.end()
        else:
            self.run()

    def prompt_done(self):
        """
        Return true if we're done.
        """
        done = input('Finished? (Y/N)')
        try:
            done = str(done)
            done = done.lower()
        except Exception as e:
            print('please pick yY or nN.')
            return False
        if done != 'y':
            return False
        return True

    def end(self):
        """
        Decide winner.
        """

        print('-' * 20)
        print('Employees:')
        for employee in self.employees:
            print(employee)

        print('-' * 20)
        print('Picks:')
        print(self.winning_numbers)

        print('-' * 20)
        print('Powerball:')
        print(self.powerball)

        print('-' * 20)
        self.decide_winner()

    def decide_winner(self):
        winners = []

        for i in self.winning_numbers.most_common(5):
            if i[1] > 1:
                winners.append(i[0])

        for i in range(len(winners), 5):
            winners.append(
                str(random.randint(BOTTOM_RANGE, TOP_RANGE_REGULAR))
            )

        top_2 = self.powerball.most_common(2)
        if top_2[0][1] > top_2[1][1]:
            powerball_winner = top_2[0][1]
        else:
            powerball_winner = str(random.randint(
                BOTTOM_RANGE, TOP_RANGE_POWERBALL))

        print(winners)
        print(powerball_winner)


class Employee(object):
    """
    Holds Employee first name, last name & picks.
    """

    def __init__(self):
        self.__picks = []
        self.__powerball = None

    def has_first_name(self):
        return hasattr(self, '__fname')

    def set_first_name(self, _name):
        self.__fname = _name
        return True

    def set_last_name(self, _name):
        self.__lname = _name
        return True

    def add_pick(self, _pick):
        # returns True on success
        try:
            _pick = int(_pick)
            if self.validate_pick(_pick):
                self.__picks.append(_pick)
                self.__picks.sort()
                return True
            else:
                print('Picks must be unique, and between 1 and 69.')
        except Exception as e:
            print(e)

    def validate_pick(self, _pick):
        return _pick not in self.__picks \
            and isinstance(int(_pick), int) \
            and len(self.__picks) < 5   \
            and _pick >= BOTTOM_RANGE and _pick <= TOP_RANGE_REGULAR

    def validate_powerball(self, _pb):
        return _pb >= BOTTOM_RANGE and _pb <= TOP_RANGE_POWERBALL \
            and self.__powerball is None

    def pick_powerball(self, _pb):
        try:
            _pb = int(_pb)
            if self.validate_powerball(_pb):
                self.__powerball = _pb
                return True
            else:
                print('Powerball value must be between 1 and 26.')
        except Exception as e:  # can't cast to int
            print(e)

    def __str__(self):
        return " ".join([self.__fname, self.__lname] + list(map(str, self.__picks)) + ['Powerball:', str(self.__powerball)])

if __name__ == '__main__':
    application = Application()
    application.run()
