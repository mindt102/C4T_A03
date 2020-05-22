class Animal:
    def __init__(self,name):
        self.name = name
        self.weight = 5
        self.skills = []
    
    def feed(self):
        self.weight += 1
    def teach(self,skill):
        self.skills.append(skill)

class Dog(Animal):
    def bark(self):
        print("Meow meow")

class Timer:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours   = 0
    
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
        
    def reset(self):
        self.__init__()
        # self.seconds = 0
        # self.minutes = 0
        # self.hours   = 0

def get_number_of_second(hours,minutes,seconds):
    return 3600*hours + 60*minutes + seconds

number_of_seconds = get_number_of_second(25,60,1)
print("Number of seconds: {}".format(number_of_seconds))
time = Timer()

for i in range(number_of_seconds):
    time.tick()

print(time.hours,time.minutes,time.seconds)
time.reset()
print(time.hours,time.minutes,time.seconds)