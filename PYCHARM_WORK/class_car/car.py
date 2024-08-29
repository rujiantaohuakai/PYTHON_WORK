"""一个用于表示汽车的类"""

class Car:
    """模拟汽车"""

    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self. model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """打印汽车的行驶路程"""
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


"""一组用于表示燃油汽车和电动汽车的类"""


class Battery:
    """模拟电动汽车电瓶"""

    def __init__(self, battery_size=40):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印电池容量"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """打印一条描述电池续航里程的消息"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """模拟电动汽车"""

    def __init__(self, make, model, year):
        """先初始化父类属性，再初始化电动汽车特有属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

