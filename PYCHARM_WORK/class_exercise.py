class Dog:
    """用于简单模拟小狗的类"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到坐下命令"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到打滚命令"""
        print(f"{self.name} rolled over!\n")


my_dog = Dog('bob', 100)
your_dog = Dog('pop', 101)
print(f"This is my dog {my_dog.name}, he is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
print(f"This is your dog {your_dog.name}, he is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def greet_user(self):
        print(f"\nHello, {self.first_name} {self.last_name}")

    def describe_user(self):
        name = self.first_name + ' ' + self.last_name
        print(f"name: {self.first_name} {self.last_name}, {self.age} years old")
        print(f"name: {name.title()}")

    def increment_login_attempts(self):
        """用户尝试登陆次数+1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置用户尝试登陆的次数"""
        self.login_attempts = 0

    def get_logi_attempts(self):
        """返回用户尝试登陆的次数"""
        return self.login_attempts


user1 = User('li', 'peiyang', 20)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
print(user1.get_logi_attempts())

user1.increment_login_attempts()
print(user1.get_logi_attempts())

user1.increment_login_attempts()
print(user1.get_logi_attempts())

user1.increment_login_attempts()
print(user1.get_logi_attempts())

user1.reset_login_attempts()
print(user1.get_logi_attempts())


class Car:
    """简单模拟一辆汽车的信息"""
    def __init__(self, make, model, year):
        """初始化汽车的一些属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 100

    def get_descriptive_name(self):
        """返回规范格式的描述信息"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        """打印一条显示汽车行驶里程的信息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表增加指定的值"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        self.gas_tank = 100
        print(f"Now gas tank is {self.gas_tank}")


my_new_car1 = Car('audi', 'a4', 2077)
print(f"\n{my_new_car1.get_descriptive_name()}")
my_new_car1.read_odometer()
my_new_car1.update_odometer(666888)
my_new_car1.read_odometer()
my_new_car1.update_odometer(23)
my_new_car1.read_odometer()
my_new_car1.increment_odometer(888666)
my_new_car1.read_odometer()
my_new_car1.increment_odometer(-10000)
my_new_car1.fill_gas_tank()


class ElectricCar(Car):
    """电动汽车的简单模拟（继承汽车Car类）"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        """将子类的make, model, year,传入父类的__init__"""
        self.battery_size = 40
        """保留一个问题：Car 中的属性 gas_tank 要如何处理？？？"""

    def describe_battery(self):
        """打印有关电池容量的信息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("This car done not have a gas tank!")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(f"\n{my_leaf.get_descriptive_name()}")
my_leaf.describe_battery()
my_leaf.fill_gas_tank()
print(my_leaf.gas_tank)


class Battery:
    """模拟电动汽车的电池"""

    def __init__(self, battery_size=40):
        """初始化电池属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池信息的信息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条信息，指出电池的续航里程"""
        car_range = 0
        if self.battery_size == 40:
            car_range = 150
        elif self.battery_size == 62:
            car_range = 225
        print(f"This car can go about {car_range} miles on a full charge.")


class NewElectricCar(Car):
    """新的模拟电动汽车的类"""
    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_new_leaf = NewElectricCar('nissan', 'leaf', 2024)
print(f"\n{my_new_leaf.get_descriptive_name()}")
my_new_leaf.battery.describe_battery()
my_new_leaf.battery.get_range()




























