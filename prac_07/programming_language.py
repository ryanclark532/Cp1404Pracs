class ProgrammingLanguage() :
    def __init__(self, name, typing, reflection, year):
        self.name=name
        self.typing=typing
        self.reflection=reflection
        self.year=year


    def is_dynamic(self):
         return bool(self.reflection)

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name,self.typing,self.reflection,self.year)

CURRENT_YEAR = 2017
VINTAGE_AGE = 50
class myguitar():
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name,self.year,self.cost)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year


