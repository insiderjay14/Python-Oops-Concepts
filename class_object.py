# ### class & object example 

class Dog:
    animal = 'dog'
    def details(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color
max = Dog()
max.details("max", "leabra", "black")
print(max.name, max.breed, max.color, max.animal)
print(max.animal)
print(Dog.__dict__)


# ### Generic data example

class bike:
    wheels = 2
    steering = 1
    engine = 1
    hl = 1

bullet = bike()
harli = bike()
bullet.engine = 2
harli.hl = 3
bike.steering = 2

print("Details of bullet :", "wheels :",bullet.wheels, "steering :",bullet.steering, "engine :", bullet.engine, "had light :",bullet.hl)

print("Details of harli :", "wheels :",harli.wheels, "steering :",harli.steering, "engine :", harli.engine, "had light :",harli.hl)



# # ## specific data example

class hospital:
    hospital_name = "xyz"
    hospital_id = 123
    hospital_ad = "abc"
    staff_id = 456
    ward_id = 222

apollo = hospital()
apple = hospital()
orange = hospital()
apollo.staff_id = 227
apollo.hospital_name = 'apollo'
apple.ward_id = 674
apple.hospital_name = 'apple'
orange.hospital_ad = 'cba'
apple.docter_id = 124
apollo.docter_id = 546
orange.docter_id = 987

print("Details of apollo hospital :","hospital name :",apollo.hospital_name, "hospital id :",apollo.hospital_id, "hospital add :",apollo.hospital_ad, "staff id :",apollo.staff_id, "ward id :",apollo.ward_id, "docter id :",apollo.docter_id)

print("Details of apple hospital :","hospital name :",apple.hospital_name, apple.hospital_id, "hospital id :","hospital add :",apple.hospital_ad, "staff id :",apple.staff_id, "ward id :",apple.ward_id, "docter id :",apple.docter_id)

print("Details of orange hospital :","hospital name :",orange.hospital_name, "hospital id :",orange.hospital_id, "hospital add :",orange.hospital_ad, "staff id :",orange.staff_id, "ward id :",orange.ward_id, "docter id :",orange.docter_id)


class hotel:
    hotel_name = "abc"
    hotel_rooms = 250
    hotel_ad = "xyz"
    manager = 1

taj = hotel()
udupi = hotel()
laxmi = hotel()
taj.hotel_name = "Taj Hotel"
taj.manager = 2
udupi.hotel_ad = "abc"
udupi.hotel_rooms = 150
laxmi.hotel_name = "Laxmi"
taj.chefs = 25
taj.waiters = 125
udupi.chefs = 5
laxmi.waiters = 25
laxmi.gards = 3

print("Details of taj hotel :","hotel name :",taj.hotel_name, "hotel room :",taj.hotel_rooms, "hotel add :",taj.hotel_ad,"hotel manager :",taj.manager, "chefs :",taj.chefs, "waiters :",taj.waiters)

print("Details of udupi hotel :","hotel name :",udupi.hotel_name, "hotel room :",udupi.hotel_rooms, "hotel add :",udupi.hotel_ad,"hotel manager :",udupi.manager, "chefs :",udupi.chefs)

print("Details of laxmi hotel :","hotel name :",laxmi.hotel_name, "hotel room :",laxmi.hotel_rooms, "hotel add :",laxmi.hotel_ad,"hotel manager :",laxmi.manager, "waiters :",laxmi.waiters, "gards :",laxmi.gards)

# # ## constructer example 

class hospital:
    hospital_name = "xyz"
    hospital_id = 123
    hospital_ad = "abc"
    staff_id = 456
    ward_id = 222
    def __init__(self, docter_name, docter_id, phno, speciality, avalable_hours):
        self.docter_name = docter_name
        self.docter_id = docter_id
        self.phno = phno
        self.speciality = speciality
        self.avalable_hours = avalable_hours
apollo = hospital("raja", 123, 1234567890, "MD", 10)
apple = hospital("dinga", 225, 4561237899, "gestrologist", 12)
orange = hospital("dingi", 212, 9874561230, "heart specialist", 8)
apollo.staff_id = 227
apollo.hospital_name = 'apollo'
apple.ward_id = 674
apple.hospital_name = 'apple'
orange.hospital_ad = 'cba'
apple.docter_id = 124
apollo.docter_id = 546
orange.docter_id = 987
print("Details of apollo hospital :",apollo.hospital_name, apollo.hospital_id, apollo.hospital_ad,apollo.staff_id, apollo.ward_id, apollo.docter_id, "docter name :", apollo.docter_name, "docter id :", apollo.docter_id, "phno :", apollo.phno, "speciality :", apollo.speciality, "avalable hours :", apollo.avalable_hours)
print("Details of apple hospital :",apple.hospital_name, apple.hospital_id, apple.hospital_ad,apple.staff_id, apple.ward_id, apple.docter_id, "docter name :", apple.docter_name, "docter id :", apple.docter_id, "phno :", apple.phno, "speciality :", apple.speciality, "avalable hours :", apple.avalable_hours)
print("Details of orange hospital :",orange.hospital_name, orange.hospital_id, orange.hospital_ad,orange.staff_id, orange.ward_id, orange.docter_id, "docter name :", orange.docter_name, "docter id :", orange.docter_id, "phno :", orange.phno, "speciality :", orange.speciality, "avalable hours :", orange.avalable_hours)

class hotel:
    hotel_name = "abc"
    hotel_rooms = 250
    hotel_ad = "xyz"
    manager = 1
    def __init__(self, room_no, customer_name, chech_in_time, check_out_time, bill):
        self.room_no = room_no
        self.custeomer_name = customer_name
        self.check_in_time = chech_in_time
        self.check_out_time = check_out_time
        self.bill = bill
taj = hotel(22, "jay patel" ,"11:45", "2:30", 2500)
udupi = hotel(105, "man", "8:15", "9:50", 5000)
laxmi = hotel(25, "raja", "4:00", "5:30", 3500)
taj.hotel_name = "Taj Hotel"
taj.manager = 2
udupi.hotel_ad = "abc"
udupi.hotel_rooms = 150
laxmi.hotel_name = "Laxmi"
taj.chefs = 25
taj.waiters = 125
udupi.chefs = 5
laxmi.waiters = 25
laxmi.gards = 3
print("Details of taj hotel :",taj.hotel_name, taj.hotel_rooms, taj.hotel_ad,taj.manager, taj.chefs, taj.waiters, "room no :", taj.room_no, "customer_name :", taj.custeomer_name, "check in time :", taj.check_in_time, "check out time :", taj.check_out_time, "bill :", taj.bill)
print("Details of udupi hotel :",udupi.hotel_name, udupi.hotel_rooms, udupi.hotel_ad,udupi.manager, udupi.chefs, "room no :", udupi.room_no, "customer_name :", udupi.custeomer_name, "check in time :", udupi.check_in_time, "check out time :", udupi.check_out_time, "bill :", udupi.bill)
print("Details of laxmi hotel :",laxmi.hotel_name, laxmi.hotel_rooms, laxmi.hotel_ad,laxmi.manager, laxmi.waiters, laxmi.gards, "room no :", laxmi.room_no, "customer_name :", laxmi.custeomer_name, "check in time :", laxmi.check_in_time, "check out time :", laxmi.check_out_time, "bill :", laxmi.bill)


# # ## object method example 

class hospital:
    hospital_name = "xyz"
    hospital_id = 123       
    hospital_ad = "abc"
    staff_id = 456
    ward_id = 222
    def __init__(self, docter_name, docter_id, phno, speciality, avalable_hours):
        self.docter_name = docter_name
        self.docter_id = docter_id
        self.phno = phno
        self.speciality = speciality
        self.avalable_hours = avalable_hours

    def display(self):
        print("hospital name :",self.hospital_name)
        print("hospital id :",self.hospital_id)
        print("hospital add :",self.hospital_ad)
        print("staff id :",self.staff_id)
        print("ward id :",self.ward_id)
        print("docter name ;",self.docter_name)
        print("docter id :",self.docter_id)
        print("phno :",self.phno)
        print("speciality :",self.speciality)
        print("avalable hours :",self.avalable_hours)

    def change_hospital_name(self,new_name):
        self.hospital_name = new_name
    
    def change_hospital_ad(self,new_ad):
        self.hospital_ad = new_ad

    def change_phno(self,new_phno):
        self.phno = new_phno

apollo = hospital("raja", 123, 1234567890, "MD", 10)
apple = hospital("dinga", 225, 4561237899, "gestrologist", 12)
orange = hospital("dingi", 212, 9874561230, "heart specialist", 8)

print("Details of apple hospital :")
apple.display()
apple.change_hospital_name("pqr")
apollo.change_hospital_ad("cba")
orange.change_phno('0123456789')
print('#'*20)
apollo.display()
print('#'*20)
orange.display()


class hotel:
    hotel_name = "abc"
    hotel_rooms = 250
    hotel_ad = "xyz"
    manager = 1
    def __init__(self, room_no, customer_name, chech_in_time, check_out_time, bill):
        self.room_no = room_no
        self.customer_name = customer_name
        self.check_in_time = chech_in_time
        self.check_out_time = check_out_time
        self.bill = bill

    def display(self):
        print("hotel name :",self.hotel_name)
        print("hotel rooms :",self.hotel_rooms)
        print("hotel add :",self.hotel_ad)
        print("manager :",self.manager)
        print("room no :",self.room_no)
        print("customer name :",self.customer_name)
        print("check in time :",self.check_in_time)
        print("check out time :",self.check_out_time)
        print("bill :",self.bill)

    def change_hotel_name(self,new_name):
         self.hotel_name = new_name

    def change_bill(self,new_bill):
        self.bill = new_bill

taj = hotel(22, "jay patel" ,"11:45", "2:30", 2500)
udupi = hotel(105, "man", "8:15", "9:50", 5000)
laxmi = hotel(25, "raja", "4:00", "5:30", 3500)

print("Details of taj hotel :")
taj.display()
taj.change_hotel_name("jay")
udupi.change_bill(3000)
print('#'*20)
taj.display()
udupi.display()


# ### class method example

class MI:
    team_name = "mumbai indians"
    homeground = "wankhede"
    captain = "rohit sharma"
    coach = "johnty rosh"
    def __init__(self,name,role,country,price,jerse_no):
        self.name = name
        self.role = role
        self.country = country
        self.price = price
        self.jerse_no = jerse_no

    def display(self):
        print('team name :',self.team_name)
        print('homeground :',self.homeground)
        print('captain :',self.captain)
        print('coach :',self.coach)
        print('player name :',self.name)
        print('player role :',self.role)
        print('player country :',self.country)
        print('player price :',self.price)
        print('player jerse no :', self.jerse_no)

    @classmethod
    def change_team_name(cls,newteam):
        cls.team_name = newteam

    @classmethod
    def change_homeground(cls,newhome):
        cls.homeground = newhome

    @classmethod
    def change_captain(cls,newcaptain):
        cls.captain = newcaptain

    @classmethod
    def change_coach(cls,newcoach):
        cls.coach = newcoach

rohit = MI("rohit sharma","batsman","india","17cr",45)
bumrah = MI("jusprit bumrah","bowler","india","12cr",15)
bolt = MI("bolt","bowler","NZ","8cr",35)

rohit.display()
rohit.change_team_name("Delhi Cepital")
rohit.change_homeground("Mohali")
rohit.change_captain("KL Rahul")
rohit.change_coach("mike hussy")
print('#'*20)
bumrah.display()


class RCB:
    team_name = "Royal Challengers Benglore"
    homeground = "Channaswamy Banglore"
    captain = "virat kohli"
    coach = "Mike husson"
    def __init__(self,name,role,country,price,jerse_no):
        self.name = name
        self.role = role
        self.country = country
        self.price = price
        self.jerse_no = jerse_no

    def display(self):
        print('team name :',self.team_name)
        print('homeground :',self.homeground)
        print('captain :',self.captain)
        print('coach :',self.coach)
        print('player name :',self.name)
        print('player role :',self.role)
        print('player country :',self.country)
        print('player price :',self.price)
        print('player jerse no :', self.jerse_no)

    @classmethod
    def change_team_name(cls,newteam):
        cls.team_name = newteam

    @classmethod
    def change_homeground(cls,newhome):
        cls.homeground = newhome

    @classmethod
    def change_captain(cls,newcaptain):
        cls.captain = newcaptain

    @classmethod
    def change_coach(cls,newcoach):
        cls.coach = newcoach

virat = RCB("virat Kohli","batsman","india","17cr",18)
abd = RCB("AB D","batsman","SA","12cr",17)
maxi = RCB("maxwal","All rounder","AUS","8cr",35)

virat.display()
virat.change_team_name("Mumbai Indians")
virat.change_homeground("Wankhede")
abd.change_captain("AB d")
maxi.change_coach("Rahul Dravid")
print('#'*20)
abd.display()


class CSK:
    team_name = "Chennai Super King"
    homeground = "M. A. Chidambaram Stadium"
    captain = "M S Dhoni"
    coach = "Stephen Fleming"
    def __init__(self,name,role,country,price,jerse_no):
        self.name = name
        self.role = role
        self.country = country
        self.price = price
        self.jerse_no = jerse_no

    def display(self):
        print('team name :',self.team_name)
        print('homeground :',self.homeground)
        print('captain :',self.captain)
        print('coach :',self.coach)
        print('player name :',self.name)
        print('player role :',self.role)
        print('player country :',self.country)
        print('player price :',self.price)
        print('player jerse no :', self.jerse_no)

    @classmethod
    def change_team_name(cls,newteam):
        cls.team_name = newteam

    @classmethod
    def change_homeground(cls,newhome):
        cls.homeground = newhome

    @classmethod
    def change_captain(cls,newcaptain):
        cls.captain = newcaptain

    @classmethod
    def change_coach(cls,newcoach):
        cls.coach = newcoach

dhoni = CSK("M S Dhoni","batsman","india","17cr",7)
raina = CSK("Suresh Raina","batsman","india","15cr",3)
jaddu = CSK("jadeja","All Rounder","india","8cr",28)

dhoni.display()
jaddu.change_team_name("Punjab Kings")
jaddu.change_homeground("modhera")
print('#'*20)
raina.display()
dhoni.change_captain("Raina")
raina.change_coach("jhonty rozz")
print('#'*20)
jaddu.display()


class DC:
    team_name = "Delhi Capital"
    homeground = "Arun Jaitley Stadium"
    captain = "Rishabh Pant"
    coach = "Ricky Ponting"
    def __init__(self,name,role,country,price,jerse_no):
        self.name = name
        self.role = role
        self.country = country
        self.price = price
        self.jerse_no = jerse_no

    def display(self):
        print('team name :',self.team_name)
        print('homeground :',self.homeground)
        print('captain :',self.captain)
        print('coach :',self.coach)
        print('player name :',self.name)
        print('player role :',self.role)
        print('player country :',self.country)
        print('player price :',self.price)
        print('player jerse no :', self.jerse_no)

    @classmethod
    def change_team_name(cls,newteam):
        cls.team_name = newteam

    @classmethod
    def change_homeground(cls,newhome):
        cls.homeground = newhome

    @classmethod
    def change_captain(cls,newcaptain):
        cls.captain = newcaptain

    @classmethod
    def change_coach(cls,newcoach):
        cls.coach = newcoach

pant = DC("Rishab Pant","batsman","india","10cr",33)
dhavan = DC("Shikhar Dhavan","batsman","india","9cr",30)
show = DC("Pruthvi show","batsman","india","8cr",28)

pant.change_team_name("Rajasthan Royal")
pant.change_homeground("mohali")
print('#'*20)
dhavan.display()
show.change_captain("Miller")
show.change_coach("Anil Kumble")
print('#'*20)
dhavan.display()

class animal:
    animal_name = "Dog"
    tail = 1
    legs = 4
    eyes = 2
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

    def display(self):
        print('Animal name :', self.animal_name)
        print('tail :', self.tail)
        print('legs :', self.legs)
        print('eyes :', self.eyes)
        print('Dog name :',self.name)
        print('age :', self.age)
        print('breed :',self.breed)
        print('coler :', self.color)

    @classmethod
    def change_animal_name(cls,newanimal):
        cls.animal_name = newanimal

    @classmethod
    def change_legs(cls,newlegs):
        cls.legs = newlegs

    @classmethod
    def change_name(cls,newname):
        cls.name = newname

max = animal('Max', 8, 'Husky', 'white')
jeck = animal('jeck', 10, 'pit bull', 'broun')
coco = animal('coco',13, 'lebra', 'black')

max.display()
max.change_animal_name('cat')
max.change_legs('3')
max.change_name('Tom')
print('#'*20)
coco.display()


# # ## static method example

class animal:
    animal_name = "Dog"
    tail = 1
    legs = 4
    eyes = 2

    @staticmethod
    def set_name():
        return input("enter the name :")

    @staticmethod
    def set_age():
        return input("enter the age :")

    @staticmethod
    def set_breed():
        return input("enter the breed :")

    @staticmethod
    def set_color():
        return input("enter the color :")

    def __init__(self,name,age,breed,color):
        self.name = self.set_name()
        self.age = self.set_age()
        self.breed = self.set_breed()
        self.color = self.set_color()

    def display(self):
        print('Animal name :', self.animal_name)
        print('tail :', self.tail)
        print('legs :', self.legs)
        print('eyes :', self.eyes)
        print('Dog name :',self.name)
        print('age :', self.age)
        print('breed :',self.breed)
        print('coler :', self.color)

    @classmethod
    def change_animal_name(cls,newanimal):
        cls.animal_name = newanimal

    @classmethod
    def change_legs(cls,newlegs):
        cls.legs = newlegs

    @classmethod
    def change_name(cls,newname):
        cls.name = newname

max = animal('Max', 8, 'Husky', 'white')
jeck = animal('jeck', 10, 'pit bull', 'broun')
coco = animal('coco',13, 'lebra', 'black')

max.display()
max.change_animal_name('cat')
max.change_legs('3')
max.change_name('Tom')
print('#'*20)
coco.display()


# # ## single level inheritance example

class animal:
    animal_name = "Dog"
    tail = 1
    legs = 4
    eyes = 2

    @staticmethod
    def set_name():
        return input("enter the name :")

    @staticmethod
    def set_age():
        return input("enter the age :")

    @staticmethod
    def set_breed():
        return input("enter the breed :")

    @staticmethod
    def set_color():
        return input("enter the color :")

    def __init__(self,name,age,breed,color):
        self.name = self.set_name()
        self.age = self.set_age()
        self.breed = self.set_breed()
        self.color = self.set_color()

    def display(self):
        print('Animal name :', self.animal_name)
        print('tail :', self.tail)
        print('legs :', self.legs)
        print('eyes :', self.eyes)
        print('Dog name :',self.name)
        print('age :', self.age)
        print('breed :',self.breed)
        print('coler :', self.color)

    @classmethod
    def change_animal_name(cls,newanimal):
        cls.animal_name = newanimal

    @classmethod
    def change_legs(cls,newlegs):
        cls.legs = newlegs

    @classmethod
    def change_name(cls,newname):
        cls.name = newname

class cat(animal):
    def cat1(self):
        print("cat name is mini")

max = cat('Max', 8, 'Husky', 'white')
max.display()
print('#'*20)
max.cat1()
print("dog breed is :",max.breed)


# # ## multi level inheritance

class animal:
    animal_name = "Dog"
    tail = 1
    legs = 4
    eyes = 2
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

    def display(self):
        print('Animal name :', self.animal_name)
        print('tail :', self.tail)
        print('legs :', self.legs)
        print('eyes :', self.eyes)
        print('Dog name :',self.name)
        print('age :', self.age)
        print('breed :',self.breed)
        print('coler :', self.color)

    @classmethod
    def change_animal_name(cls,newanimal):
        cls.animal_name = newanimal

    @classmethod
    def change_legs(cls,newlegs):
        cls.legs = newlegs

    @classmethod
    def change_name(cls,newname):
        cls.name = newname

class cat(animal):
    def cat1(self):
        print("cat name is mini")

class horse(cat):
    def horse1(self):
        print("horse coler is white")

max = horse('Max', 8, 'Husky', 'white')
max.display()
print('#'*20)
max.cat1()
max.horse1()
print("dog breed is :",max.breed)


# ## Hierachical Inheritance

class IPL:
    ipl_season = 2021
    sponser = "vivo"
    
    def __init__(self,charman,organisers):
        self.charman = charman
        self.organisers = organisers

    def display(self):
        print('ipl season :',self.ipl_season)
        print('sponser :',self.sponser)
        print('charman :',self.charman)
        print('organisers :',self.organisers)

    @classmethod
    def change_sponser(cls,newsponser):
        cls.sponser = newsponser

class RCB(IPL):
    team_name = "Royal Challengers Benglore"
    homeground = "Channaswamy Banglore"
    captain = "virat kohli"
    coach = "Mike husson"
    def __init__(self,name,role,country,price,jerse_no):
        self.name = name
        self.role = role
        self.country = country
        self.price = price
        self.jerse_no = jerse_no

    def display(self):
        print('team name :',self.team_name)
        print('homeground :',self.homeground)
        print('captain :',self.captain)
        print('coach :',self.coach)
        print('player name :',self.name)
        print('player role :',self.role)
        print('player country :',self.country)
        print('player price :',self.price)
        print('player jerse no :', self.jerse_no)

    @classmethod
    def change_team_name(cls,newteam):
        cls.team_name = newteam

    @classmethod
    def change_homeground(cls,newhome):
        cls.homeground = newhome

    @classmethod
    def change_captain(cls,newcaptain):
        cls.captain = newcaptain

    @classmethod
    def change_coach(cls,newcoach):
        cls.coach = newcoach

class MI(IPL):
    team_name = "mumbai indians"
    homeground = "wankhede"
    captain = "rohit sharma"
    coach = "johnty rosh"
    def __init__(self,name,role,country,price,jerse_no):
        self.name = name
        self.role = role
        self.country = country
        self.price = price
        self.jerse_no = jerse_no

    def display(self):
        print('team name :',self.team_name)
        print('homeground :',self.homeground)
        print('captain :',self.captain)
        print('coach :',self.coach)
        print('player name :',self.name)
        print('player role :',self.role)
        print('player country :',self.country)
        print('player price :',self.price)
        print('player jerse no :', self.jerse_no)

    @classmethod
    def change_team_name(cls,newteam):
        cls.team_name = newteam

    @classmethod
    def change_homeground(cls,newhome):
        cls.homeground = newhome

    @classmethod
    def change_captain(cls,newcaptain):
        cls.captain = newcaptain

    @classmethod
    def change_coach(cls,newcoach):
        cls.coach = newcoach

virat = RCB("virat Kohli","batsman","india","17cr",18)
rohit = MI("rohit sharma","batsman","india","17cr",45)

rohit.display()
rohit.change_team_name("Delhi Cepital")
rohit.change_homeground("Mohali")
rohit.change_captain("KL Rahul")
rohit.change_coach("mike hussy")
print('#'*20)
rohit.display()

print('$'*30)

virat.display()
virat.change_team_name("Mumbai Indians")
virat.change_homeground("Wankhede")
virat.change_captain("AB d")
virat.change_coach("Rahul Dravid")
print('#'*20)
virat.display()




 