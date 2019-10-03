class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.species = 'homo sapiens'
        self.isMale = None
        if gender == 'M':
            self.isMale = True
        elif gender == 'F':
            self.isMale = False
        else:
            print('Gender not recognised ')

    def greetingInformal(self):
        print('HI, ', self.name)

    def greetingFormal(self):
        if self.isMale:
            print('welcome , Mr ', self.name)
        else:
            print('welcome , Ms', self.name)

    def greetingAgedBased(self):
        if self.age < 18:
            print('welcome , young ', self.name)
        elif self.age > 60:
            print('welcome , old ', self.name)
        else:
            self.greetingFormal()


p1 = Person('Harry', 12, 'm')
p2 = Person('Hermione', 12, 'f')
p1.greetingInformal()
p1.greetingFormal()
p2.greetingFormal()

# python myCode.py -w -t 0.5 -d data1.txt -r results1.txt
# with options to specify the input data file (-d), the results file (-r), and a threshold value (-t) affecting the process

# and a boolean option -w to direct some aspect of behaviour

# Help option: good practice to include a boolean help option -h
# if present, code just prints help message and then quits
# help message says how to call program, lists options, etc

