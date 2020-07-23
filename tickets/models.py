from django.db import models


# Create your models here.


class CarProblems:
    def __init__(self):
        self.car_problems = {
            "change_oil": [],
            "inflate_tires": [],
            "diagnostic": [],
            "cards": []
        }
        self.priorities = {
            "change_oil": 1,
            "inflate_tires": 2,
            "diagnostic": 3
        }
        self.last = None
        self.processing = False

    def solve_time(self, problem_n, card_n):
        if problem_n == "change_oil":
            time = ((self.get_oil_length() - 1) * 2)
            return time
        time = (self.get_oil_length() * 2)
        if problem_n == "inflate_tires":
            time += ((self.get_tires_length() - 1) * 5)
            return time
        time += (self.get_tires_length() * 5)
        return time + ((self.get_diagnostic_length() - 1) * 30)

    def get_time(self, card_n):
        if self.get_maintained() is None:
            return 0
        for problem_n in self.car_problems:
            if problem_n != "card":
                for card in self.car_problems[problem_n]:
                    if card_n == card:
                        return self.solve_time(problem_n, card_n)
        return None

    def get_card(self, name):
        if name in self.car_problems:
            card_n = self.get_new_card()
            self.car_problems[name].append(card_n)
            return card_n
        return None

    def get_new_card(self):
        for _e in range(len(self.car_problems["cards"]) + 1):
            if (_e + 1) not in self.car_problems["cards"]:
                self.car_problems["cards"].append(_e + 1)
                return _e + 1
        return None

    def get_maintained(self):
        if self.car_problems["change_oil"]:
            return self.car_problems["change_oil"][0]
        elif self.car_problems["inflate_tires"]:
            return self.car_problems["inflate_tires"][0]
        elif self.car_problems["diagnostic"]:
            return self.car_problems["diagnostic"][0]
        return None

    def get_oil_length(self):
        return len(self.car_problems["change_oil"])

    def get_tires_length(self):
        return len(self.car_problems["inflate_tires"])

    def get_diagnostic_length(self):
        return len(self.car_problems["diagnostic"])

    def get_next(self):
        if self.processing:
            for problem in self.car_problems:
                if problem != "card" and self.car_problems[problem]:
                    return self.car_problems[problem][0]
        return None

    def process_next(self):
        self.processing = True
        self.last = self.get_next()
        for problem in self.car_problems:
            if self.last in self.car_problems[problem]:
                self.car_problems[problem].remove(self.last)
        # self.processing = True
        return None

    def get_last_added(self, problem):
        if self.car_problems[problem]:
            return self.car_problems[problem][-1]
        return 0
