class Car:
    def __init__(self, name, color='black', type='car'):
        self.name = name
        self.color = color
        self.type = type
        
    def drive(self):
        print("I can drive, and I'm a car!")
    def shape(self):
        print("I'm shape, and I'm a car!")

class Scooter(Car):
    def shape(self):
        print("I'm extanded shape, and I'm a scooter!")
    def ride(self):
        print("I can ride, and I'm scooter")

# Scooter繼承了Class Car，所以可以針對Class Car中的變數、function做修改，也可以自定其他function
mini = Scooter(name='mini', type='scooter', color='white')
print('car name:', mini.name, '\n', 'car_type:',  mini.type, '\n', 'color:',  mini.color)
mini.drive()
mini.shape()
mini.ride()

# Class Car並未繼承任何class，因此只能呼叫有定義的function
cooper = Car(name='cooper')
print('car name:', cooper.name, '\n', 'car_type:',  cooper.type, '\n', 'color:',  cooper.color)
cooper.drive()
cooper.shape()