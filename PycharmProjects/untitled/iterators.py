
def x():
    i = range(10)
    for x in i:
        print x
        yield x

it = iter(x())

for r in it:
    print r


class Emp:

    def __init__(self, sal):
        self.salary = sal
        self.name = ['s', 'd', 'v']
        self.state = 0

    def __eq__(self, other):
        if other.salary == self.salary:
            print("Yay")
            return True
        return False

    def __add__(self, other):
        print other.salary + self.salary

    def __iter__(self):
        return self

    def next(self):
        try:
            r = self.name[self.state]
            self.state = self.state + 1
        except:
            raise StopIteration

tt = Emp(3)

for d in tt:
    print(d)


 class Emp(models.Model):
     name =  CharField()