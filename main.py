import argparse


class Application(object):

    def __init__(self):
        pass

    def prompt_done(self):
        pass

    def decide_winner(self):
        pass

    def update_winning_numbers(self):
        pass

    def prompt_picks(self, position):
        pass

    def run(self):
        while(self.position < 6):
            if success:
                self.position += 1
        if self.prompt_done():
            self.end()


class Counter(object):

    def __init__(self):
        self.count = 0


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
        return str(_pick) not in self.__picks \
            and isinstance(_pick, int) \
            and len(self.__picks) < 5 \
            and _pick >= 1 and _pick <= 69

    def validate_powerball(self, _pb):
        return isinstance(_pb, int) \
            and _pb >= 1 and _pb <= 26 \
            and not self.hasattr(self.__powerball)

    def pick_powerball(self, _pb):
        if self.validate_powerball(_pb):
            self.__pball = str(_pb)

    def __str__(self):
        return " ".join([self.__fname, self.__lname] + self.__picks + ['Powerball:', self.__pball])


class Test(object):

    def __init__(self):
        pass

    def success_1(self):
        pass

    def fail_case_1(self):
        pass

if __name__ == '__main__':
    application = Application()
