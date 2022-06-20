from abc import ABC, abstractmethod, ABCMeta

class CarSpecs(type, metaclass=ABCMeta):

    def __new__(classitself, classname, baseclasses, attributes):
        newattributes = {}
        for (attribute, value) in attributes.items():
            if attribute.startswith('__'):
                newattributes[attribute] = value
            elif type(value) == int or type(value) == float:
                newattributes[attribute] = {}
                newattributes[attribute]['feature'] = attribute.title().replace('_', ' ')
                newattributes[attribute]['info'] = str(value)
                newattributes[attribute]['type'] = 'NUMERIC'
            elif type(value) == str:
                newattributes[attribute] = {}
                newattributes[attribute]['feature'] = attribute.title().replace('_', ' ')
                newattributes[attribute]['info'] = value.title()
                newattributes[attribute]['type'] = 'VARCHAR'
            elif type(value) == bool:
                newattributes[attribute] = {}
                newattributes[attribute]['feature'] = attribute.title().replace('_', ' ')
                newattributes[attribute]['info'] = value.title()
                newattributes[attribute]['type'] = 'BOOLEAN'
            else:
                newattributes[attribute] = value
        return type.__new__(classitself, classname, baseclasses, newattributes)


class CarCatalogue(metaclass=CarSpecs):

    @abstractmethod
    def define_color(self):
        pass

    @abstractmethod
    def print_catalogue(self):
        pass


class CarMake(metaclass=CarSpecs):

    @abstractmethod
    def define_spec(self):
        pass


class BodyStyle(metaclass=CarSpecs):

    @abstractmethod
    def body_style_features(self):
        pass


class SaleType(metaclass=CarSpecs):

    @abstractmethod
    def calculate_price(self):
        pass


class New(SaleType, CarCatalogue, metaclass=CarSpecs):

    def calculate_price(self, classname):
        car = classname()
        price = float(car.price['info'])
        return price


class Resale(SaleType, CarCatalogue, metaclass=CarSpecs):

    def calculate_price(self, classname, years):
        car = classname()
        depreciation = years * 0.15
        price = float(car.price['info']) * (1 - depreciation)
        return price


class AlfaRomero0(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '88.6'
    length = '168.8'
    width = '64.1'
    height = '48.8'
    curb_weight = '2548'
    fuel_system = 'mpfi'
    city_mpg = '21'
    highway_mpg = '27'
    price = '13495'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class AlfaRomero1(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '94.5'
    length = '171.2'
    width = '65.5'
    height = '52.4'
    curb_weight = '2823'
    fuel_system = 'mpfi'
    city_mpg = '19'
    highway_mpg = '26'
    price = '16500'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Audi2(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '99.8'
    length = '176.6'
    width = '66.2'
    height = '54.3'
    curb_weight = '2337'
    fuel_system = 'mpfi'
    city_mpg = '24'
    highway_mpg = '30'
    price = '13950'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Audi3(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '105.8'
    length = '192.7'
    width = '71.4'
    height = '55.7'
    curb_weight = '2954'
    fuel_system = 'mpfi'
    city_mpg = '19'
    highway_mpg = '25'
    price = '18920'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Audi4(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'turbo'
    num_of_door = 'two'
    drive_wheels = '4wd'
    wheel_base = '99.5'
    length = '178.2'
    width = '67.9'
    height = '52.0'
    curb_weight = '3053'
    fuel_system = 'mpfi'
    city_mpg = '16'
    highway_mpg = '22'
    price = '?'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Bmw5(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '101.2'
    length = '176.8'
    width = '64.8'
    height = '54.3'
    curb_weight = '2395'
    fuel_system = 'mpfi'
    city_mpg = '23'
    highway_mpg = '29'
    price = '16430'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Chevrolet6(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '88.4'
    length = '141.1'
    width = '60.3'
    height = '53.2'
    curb_weight = '1488'
    fuel_system = '2bbl'
    city_mpg = '47'
    highway_mpg = '53'
    price = '5151'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Chevrolet7(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '94.5'
    length = '158.8'
    width = '63.6'
    height = '52.0'
    curb_weight = '1909'
    fuel_system = '2bbl'
    city_mpg = '38'
    highway_mpg = '43'
    price = '6575'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Dodge8(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '93.7'
    length = '157.3'
    width = '63.8'
    height = '50.8'
    curb_weight = '1876'
    fuel_system = '2bbl'
    city_mpg = '37'
    highway_mpg = '41'
    price = '5572'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Dodge9(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '93.7'
    length = '157.3'
    width = '63.8'
    height = '50.6'
    curb_weight = '1989'
    fuel_system = '2bbl'
    city_mpg = '31'
    highway_mpg = '38'
    price = '6692'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Dodge10(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '103.3'
    length = '174.6'
    width = '64.6'
    height = '59.8'
    curb_weight = '2535'
    fuel_system = '2bbl'
    city_mpg = '24'
    highway_mpg = '30'
    price = '8921'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Honda11(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '86.6'
    length = '144.6'
    width = '63.9'
    height = '50.8'
    curb_weight = '1713'
    fuel_system = '1bbl'
    city_mpg = '49'
    highway_mpg = '54'
    price = '6479'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Honda12(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '96.5'
    length = '163.4'
    width = '64.0'
    height = '54.5'
    curb_weight = '2010'
    fuel_system = '1bbl'
    city_mpg = '30'
    highway_mpg = '34'
    price = '7295'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Honda13(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '96.5'
    length = '157.1'
    width = '63.9'
    height = '58.3'
    curb_weight = '2024'
    fuel_system = '1bbl'
    city_mpg = '30'
    highway_mpg = '34'
    price = '7295'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Isuzu14(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'rwd'
    wheel_base = '94.3'
    length = '170.7'
    width = '61.8'
    height = '53.5'
    curb_weight = '2337'
    fuel_system = '2bbl'
    city_mpg = '24'
    highway_mpg = '29'
    price = '6785'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Isuzu15(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '96.0'
    length = '172.6'
    width = '65.2'
    height = '51.4'
    curb_weight = '2734'
    fuel_system = 'spfi'
    city_mpg = '24'
    highway_mpg = '29'
    price = '11048'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Jaguar16(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'rwd'
    wheel_base = '113.0'
    length = '199.6'
    width = '69.6'
    height = '52.8'
    curb_weight = '4066'
    fuel_system = 'mpfi'
    city_mpg = '15'
    highway_mpg = '19'
    price = '32250'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Mazda17(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '93.1'
    length = '159.1'
    width = '64.2'
    height = '54.1'
    curb_weight = '1890'
    fuel_system = '2bbl'
    city_mpg = '30'
    highway_mpg = '31'
    price = '5195'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Mazda18(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '93.1'
    length = '166.8'
    width = '64.2'
    height = '54.1'
    curb_weight = '1945'
    fuel_system = '2bbl'
    city_mpg = '31'
    highway_mpg = '38'
    price = '6695'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class MercedesBenz19(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'diesel'
    aspiration = 'turbo'
    num_of_door = 'four'
    drive_wheels = 'rwd'
    wheel_base = '110.0'
    length = '190.9'
    width = '70.3'
    height = '56.5'
    curb_weight = '3515'
    fuel_system = 'idi'
    city_mpg = '22'
    highway_mpg = '25'
    price = '25552'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class MercedesBenz20(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'diesel'
    aspiration = 'turbo'
    num_of_door = 'four'
    drive_wheels = 'rwd'
    wheel_base = '110.0'
    length = '190.9'
    width = '70.3'
    height = '58.7'
    curb_weight = '3750'
    fuel_system = 'idi'
    city_mpg = '22'
    highway_mpg = '25'
    price = '28248'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class MercedesBenz21(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'diesel'
    aspiration = 'turbo'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '106.7'
    length = '187.5'
    width = '70.3'
    height = '54.9'
    curb_weight = '3495'
    fuel_system = 'idi'
    city_mpg = '22'
    highway_mpg = '25'
    price = '28176'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class MercedesBenz22(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '96.6'
    length = '180.3'
    width = '70.5'
    height = '50.8'
    curb_weight = '3685'
    fuel_system = 'mpfi'
    city_mpg = '16'
    highway_mpg = '18'
    price = '35056'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Mercury23(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'turbo'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '102.7'
    length = '178.4'
    width = '68.0'
    height = '54.8'
    curb_weight = '2910'
    fuel_system = 'mpfi'
    city_mpg = '19'
    highway_mpg = '24'
    price = '16503'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Mitsubishi24(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '93.7'
    length = '157.3'
    width = '64.4'
    height = '50.8'
    curb_weight = '1918'
    fuel_system = '2bbl'
    city_mpg = '37'
    highway_mpg = '41'
    price = '5389'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Mitsubishi25(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '96.3'
    length = '172.4'
    width = '65.4'
    height = '51.6'
    curb_weight = '2365'
    fuel_system = '2bbl'
    city_mpg = '25'
    highway_mpg = '32'
    price = '6989'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Nissan26(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '94.5'
    length = '165.3'
    width = '63.8'
    height = '54.5'
    curb_weight = '1889'
    fuel_system = '2bbl'
    city_mpg = '31'
    highway_mpg = '37'
    price = '5499'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Nissan27(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '94.5'
    length = '170.2'
    width = '63.8'
    height = '53.5'
    curb_weight = '2024'
    fuel_system = '2bbl'
    city_mpg = '31'
    highway_mpg = '37'
    price = '7349'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Nissan28(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '94.5'
    length = '165.6'
    width = '63.8'
    height = '53.3'
    curb_weight = '2028'
    fuel_system = '2bbl'
    city_mpg = '31'
    highway_mpg = '37'
    price = '7799'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Nissan29(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '95.1'
    length = '162.4'
    width = '63.8'
    height = '53.3'
    curb_weight = '2008'
    fuel_system = '2bbl'
    city_mpg = '31'
    highway_mpg = '37'
    price = '8249'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Peugot30(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'rwd'
    wheel_base = '107.9'
    length = '186.7'
    width = '68.4'
    height = '56.7'
    curb_weight = '3020'
    fuel_system = 'mpfi'
    city_mpg = '19'
    highway_mpg = '24'
    price = '11900'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Peugot31(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'rwd'
    wheel_base = '114.2'
    length = '198.9'
    width = '68.4'
    height = '58.7'
    curb_weight = '3230'
    fuel_system = 'mpfi'
    city_mpg = '19'
    highway_mpg = '24'
    price = '12440'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Plymouth32(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '93.7'
    length = '157.3'
    width = '63.8'
    height = '50.8'
    curb_weight = '1918'
    fuel_system = '2bbl'
    city_mpg = '37'
    highway_mpg = '41'
    price = '5572'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Plymouth33(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '93.7'
    length = '167.3'
    width = '63.8'
    height = '50.8'
    curb_weight = '1989'
    fuel_system = '2bbl'
    city_mpg = '31'
    highway_mpg = '38'
    price = '6692'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Plymouth34(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '103.3'
    length = '174.6'
    width = '64.6'
    height = '59.8'
    curb_weight = '2535'
    fuel_system = '2bbl'
    city_mpg = '24'
    highway_mpg = '30'
    price = '8921'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Porsche35(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '94.5'
    length = '168.9'
    width = '68.3'
    height = '50.2'
    curb_weight = '2778'
    fuel_system = 'mpfi'
    city_mpg = '19'
    highway_mpg = '27'
    price = '22018'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Porsche36(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '89.5'
    length = '168.9'
    width = '65.0'
    height = '51.6'
    curb_weight = '2756'
    fuel_system = 'mpfi'
    city_mpg = '17'
    highway_mpg = '25'
    price = '32528'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Porsche37(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '89.5'
    length = '168.9'
    width = '65.0'
    height = '51.6'
    curb_weight = '2800'
    fuel_system = 'mpfi'
    city_mpg = '17'
    highway_mpg = '25'
    price = '37028'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Renault38(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '96.1'
    length = '181.5'
    width = '66.5'
    height = '55.2'
    curb_weight = '2579'
    fuel_system = 'mpfi'
    city_mpg = '23'
    highway_mpg = '31'
    price = '9295'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Renault39(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '96.1'
    length = '176.8'
    width = '66.6'
    height = '50.5'
    curb_weight = '2460'
    fuel_system = 'mpfi'
    city_mpg = '23'
    highway_mpg = '31'
    price = '9895'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Saab40(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '99.1'
    length = '186.6'
    width = '66.5'
    height = '56.1'
    curb_weight = '2658'
    fuel_system = 'mpfi'
    city_mpg = '21'
    highway_mpg = '28'
    price = '11850'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Saab41(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '99.1'
    length = '186.6'
    width = '66.5'
    height = '56.1'
    curb_weight = '2695'
    fuel_system = 'mpfi'
    city_mpg = '21'
    highway_mpg = '28'
    price = '12170'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Subaru42(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '93.7'
    length = '156.9'
    width = '63.4'
    height = '53.7'
    curb_weight = '2050'
    fuel_system = '2bbl'
    city_mpg = '31'
    highway_mpg = '36'
    price = '5118'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Subaru43(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '97.2'
    length = '172.0'
    width = '65.4'
    height = '52.5'
    curb_weight = '2145'
    fuel_system = '2bbl'
    city_mpg = '32'
    highway_mpg = '37'
    price = '7126'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Subaru44(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '97.0'
    length = '173.5'
    width = '65.4'
    height = '53.0'
    curb_weight = '2290'
    fuel_system = '2bbl'
    city_mpg = '28'
    highway_mpg = '32'
    price = '7463'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Toyota45(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '95.7'
    length = '158.7'
    width = '63.6'
    height = '54.5'
    curb_weight = '1985'
    fuel_system = '2bbl'
    city_mpg = '35'
    highway_mpg = '39'
    price = '5348'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Toyota46(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '95.7'
    length = '169.7'
    width = '63.6'
    height = '59.1'
    curb_weight = '2280'
    fuel_system = '2bbl'
    city_mpg = '31'
    highway_mpg = '37'
    price = '6918'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Toyota47(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '95.7'
    length = '166.3'
    width = '64.4'
    height = '53.0'
    curb_weight = '2081'
    fuel_system = '2bbl'
    city_mpg = '30'
    highway_mpg = '37'
    price = '6938'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Toyota48(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '98.4'
    length = '176.2'
    width = '65.6'
    height = '52.0'
    curb_weight = '2540'
    fuel_system = 'mpfi'
    city_mpg = '24'
    highway_mpg = '30'
    price = '8449'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Toyota49(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'rwd'
    wheel_base = '98.4'
    length = '176.2'
    width = '65.6'
    height = '53.0'
    curb_weight = '2975'
    fuel_system = 'mpfi'
    city_mpg = '24'
    highway_mpg = '30'
    price = '17669'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Volkswagen50(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'diesel'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '97.3'
    length = '171.7'
    width = '65.5'
    height = '55.7'
    curb_weight = '2261'
    fuel_system = 'idi'
    city_mpg = '37'
    highway_mpg = '46'
    price = '7775'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Volkswagen51(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '94.5'
    length = '159.3'
    width = '64.2'
    height = '55.6'
    curb_weight = '2254'
    fuel_system = 'mpfi'
    city_mpg = '24'
    highway_mpg = '29'
    price = '11595'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Volkswagen52(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'two'
    drive_wheels = 'fwd'
    wheel_base = '94.5'
    length = '165.7'
    width = '64.0'
    height = '51.4'
    curb_weight = '2221'
    fuel_system = 'mpfi'
    city_mpg = '24'
    highway_mpg = '29'
    price = '9980'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Volkswagen53(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'fwd'
    wheel_base = '100.4'
    length = '183.1'
    width = '66.9'
    height = '55.1'
    curb_weight = '2563'
    fuel_system = 'mpfi'
    city_mpg = '25'
    highway_mpg = '31'
    price = '12290'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Volvo54(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'rwd'
    wheel_base = '104.3'
    length = '188.8'
    width = '67.2'
    height = '56.2'
    curb_weight = '2912'
    fuel_system = 'mpfi'
    city_mpg = '23'
    highway_mpg = '28'
    price = '12940'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Volvo55(CarMake, CarCatalogue, metaclass=CarSpecs):
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_door = 'four'
    drive_wheels = 'rwd'
    wheel_base = '104.3'
    length = '188.8'
    width = '67.2'
    height = '57.5'
    curb_weight = '3034'
    fuel_system = 'mpfi'
    city_mpg = '23'
    highway_mpg = '28'
    price = '13415'

    def define_color(self):
        BOLD = '\x1b[5m'
        BLUE = '\x1b[94m'
        return BOLD + BLUE

    def define_spec(self):
        specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, self.wheel_base, self.length, self.width, self.height, self.curb_weight, self.fuel_system, self.city_mpg, self.highway_mpg]
        return specs

    def print_catalogue(self):
        for i in self.define_spec():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Convertible0(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'dohc'
    num_of_cylinders = 'four'
    engine_size = '130'
    bore = '3.47'
    stroke = '2.68'
    compression_ratio = '9.0'
    horse_power = '111'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback1(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohcv'
    num_of_cylinders = 'six'
    engine_size = '152'
    bore = '2.68'
    stroke = '3.47'
    compression_ratio = '9.0'
    horse_power = '154'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan2(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '109'
    bore = '3.19'
    stroke = '3.4'
    compression_ratio = '10.0'
    horse_power = '102'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon3(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'five'
    engine_size = '136'
    bore = '3.19'
    stroke = '3.4'
    compression_ratio = '8.5'
    horse_power = '110'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback4(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'five'
    engine_size = '131'
    bore = '3.13'
    stroke = '3.4'
    compression_ratio = '7.0'
    horse_power = '160'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan5(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '108'
    bore = '3.5'
    stroke = '2.8'
    compression_ratio = '8.8'
    horse_power = '101'
    peak_rpm = '5800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback6(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'l'
    num_of_cylinders = 'three'
    engine_size = '61'
    bore = '2.91'
    stroke = '3.03'
    compression_ratio = '9.5'
    horse_power = '48'
    peak_rpm = '5100'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan7(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '90'
    bore = '3.03'
    stroke = '3.11'
    compression_ratio = '9.6'
    horse_power = '70'
    peak_rpm = '5400'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback8(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '90'
    bore = '2.97'
    stroke = '3.23'
    compression_ratio = '9.41'
    horse_power = '68'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan9(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '90'
    bore = '2.97'
    stroke = '3.23'
    compression_ratio = '9.4'
    horse_power = '68'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon10(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '122'
    bore = '3.34'
    stroke = '3.46'
    compression_ratio = '8.5'
    horse_power = '88'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback11(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '92'
    bore = '2.91'
    stroke = '3.41'
    compression_ratio = '9.6'
    horse_power = '58'
    peak_rpm = '4800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan12(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '92'
    bore = '2.91'
    stroke = '3.41'
    compression_ratio = '9.2'
    horse_power = '76'
    peak_rpm = '6000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon13(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '92'
    bore = '2.92'
    stroke = '3.41'
    compression_ratio = '9.2'
    horse_power = '76'
    peak_rpm = '6000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan14(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '111'
    bore = '3.31'
    stroke = '3.23'
    compression_ratio = '8.5'
    horse_power = '78'
    peak_rpm = '4800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback15(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '119'
    bore = '3.43'
    stroke = '3.23'
    compression_ratio = '9.2'
    horse_power = '90'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan16(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'dohc'
    num_of_cylinders = 'six'
    engine_size = '258'
    bore = '3.63'
    stroke = '4.17'
    compression_ratio = '8.1'
    horse_power = '176'
    peak_rpm = '4750'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback17(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '91'
    bore = '3.03'
    stroke = '3.15'
    compression_ratio = '9.0'
    horse_power = '68'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan18(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '91'
    bore = '3.03'
    stroke = '3.15'
    compression_ratio = '9.0'
    horse_power = '68'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan19(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'five'
    engine_size = '183'
    bore = '3.58'
    stroke = '3.64'
    compression_ratio = '21.5'
    horse_power = '123'
    peak_rpm = '4350'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon20(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'five'
    engine_size = '183'
    bore = '3.58'
    stroke = '3.64'
    compression_ratio = '21.5'
    horse_power = '123'
    peak_rpm = '4350'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hardtop21(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'five'
    engine_size = '183'
    bore = '3.58'
    stroke = '3.64'
    compression_ratio = '21.5'
    horse_power = '123'
    peak_rpm = '4350'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Convertible22(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohcv'
    num_of_cylinders = 'eight'
    engine_size = '234'
    bore = '3.46'
    stroke = '3.1'
    compression_ratio = '8.3'
    horse_power = '155'
    peak_rpm = '4750'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback23(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '140'
    bore = '3.78'
    stroke = '3.12'
    compression_ratio = '8.0'
    horse_power = '175'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback24(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '92'
    bore = '2.97'
    stroke = '3.23'
    compression_ratio = '9.4'
    horse_power = '68'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan25(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '122'
    bore = '3.35'
    stroke = '3.46'
    compression_ratio = '8.5'
    horse_power = '88'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan26(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '97'
    bore = '3.15'
    stroke = '3.29'
    compression_ratio = '9.4'
    horse_power = '69'
    peak_rpm = '5200'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon27(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '97'
    bore = '3.15'
    stroke = '3.29'
    compression_ratio = '9.4'
    horse_power = '69'
    peak_rpm = '5200'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback28(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '97'
    bore = '3.15'
    stroke = '3.29'
    compression_ratio = '9.4'
    horse_power = '69'
    peak_rpm = '5200'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hardtop29(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '97'
    bore = '3.15'
    stroke = '3.29'
    compression_ratio = '9.4'
    horse_power = '69'
    peak_rpm = '5200'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan30(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'l'
    num_of_cylinders = 'four'
    engine_size = '120'
    bore = '3.46'
    stroke = '3.19'
    compression_ratio = '8.4'
    horse_power = '97'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon31(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'l'
    num_of_cylinders = 'four'
    engine_size = '120'
    bore = '3.46'
    stroke = '3.19'
    compression_ratio = '8.4'
    horse_power = '97'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback32(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '90'
    bore = '2.97'
    stroke = '3.23'
    compression_ratio = '9.4'
    horse_power = '68'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan33(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '90'
    bore = '2.97'
    stroke = '3.23'
    compression_ratio = '9.4'
    horse_power = '68'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon34(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '122'
    bore = '3.35'
    stroke = '3.46'
    compression_ratio = '8.5'
    horse_power = '88'
    peak_rpm = '5000'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback35(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '151'
    bore = '3.94'
    stroke = '3.11'
    compression_ratio = '9.5'
    horse_power = '143'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hardtop36(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'rear'
    engine_type = 'ohcf'
    num_of_cylinders = 'six'
    engine_size = '194'
    bore = '3.74'
    stroke = '2.9'
    compression_ratio = '9.5'
    horse_power = '207'
    peak_rpm = '5900'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Convertible37(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'rear'
    engine_type = 'ohcf'
    num_of_cylinders = 'six'
    engine_size = '194'
    bore = '3.74'
    stroke = '2.9'
    compression_ratio = '9.5'
    horse_power = '207'
    peak_rpm = '5900'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon38(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '132'
    bore = '3.46'
    stroke = '3.9'
    compression_ratio = '8.7'
    horse_power = '?'
    peak_rpm = '?'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback39(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '132'
    bore = '3.46'
    stroke = '3.9'
    compression_ratio = '8.7'
    horse_power = '?'
    peak_rpm = '?'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback40(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '121'
    bore = '3.54'
    stroke = '3.07'
    compression_ratio = '9.31'
    horse_power = '110'
    peak_rpm = '5250'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan41(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '121'
    bore = '3.54'
    stroke = '3.07'
    compression_ratio = '9.3'
    horse_power = '110'
    peak_rpm = '5250'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback42(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohcf'
    num_of_cylinders = 'four'
    engine_size = '97'
    bore = '3.62'
    stroke = '2.36'
    compression_ratio = '9.0'
    horse_power = '69'
    peak_rpm = '4900'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan43(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohcf'
    num_of_cylinders = 'four'
    engine_size = '108'
    bore = '3.62'
    stroke = '2.64'
    compression_ratio = '9.5'
    horse_power = '82'
    peak_rpm = '4800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon44(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohcf'
    num_of_cylinders = 'four'
    engine_size = '108'
    bore = '3.62'
    stroke = '2.64'
    compression_ratio = '9.0'
    horse_power = '82'
    peak_rpm = '4800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback45(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '92'
    bore = '3.05'
    stroke = '3.03'
    compression_ratio = '9.0'
    horse_power = '62'
    peak_rpm = '4800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon46(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '92'
    bore = '3.05'
    stroke = '3.03'
    compression_ratio = '9.0'
    horse_power = '62'
    peak_rpm = '4800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan47(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '98'
    bore = '3.19'
    stroke = '3.03'
    compression_ratio = '9.0'
    horse_power = '70'
    peak_rpm = '4800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hardtop48(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '146'
    bore = '3.62'
    stroke = '3.5'
    compression_ratio = '9.3'
    horse_power = '116'
    peak_rpm = '4800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Convertible49(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '146'
    bore = '3.62'
    stroke = '3.5'
    compression_ratio = '9.3'
    horse_power = '116'
    peak_rpm = '4800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan50(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '97'
    bore = '3.01'
    stroke = '3.4'
    compression_ratio = '23.0'
    horse_power = '52'
    peak_rpm = '4800'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Convertible51(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '109'
    bore = '3.19'
    stroke = '3.4'
    compression_ratio = '8.5'
    horse_power = '90'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Hatchback52(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '109'
    bore = '3.19'
    stroke = '3.4'
    compression_ratio = '8.5'
    horse_power = '90'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon53(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '109'
    bore = '3.19'
    stroke = '3.4'
    compression_ratio = '9.0'
    horse_power = '88'
    peak_rpm = '5500'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Sedan54(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '141'
    bore = '3.78'
    stroke = '3.15'
    compression_ratio = '9.5'
    horse_power = '114'
    peak_rpm = '5400'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


class Wagon55(BodyStyle, CarCatalogue, metaclass=CarSpecs):
    engine_location = 'front'
    engine_type = 'ohc'
    num_of_cylinders = 'four'
    engine_size = '141'
    bore = '3.78'
    stroke = '3.15'
    compression_ratio = '9.5'
    horse_power = '114'
    peak_rpm = '5400'

    def body_style_features(self):
        features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size, self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
        return features

    def define_color(self):
        BOLD = '\x1b[5m'
        RED = '\x1b[31m'
        return BOLD + RED

    def print_catalogue(self):
        for i in self.body_style_features():
            print(self.define_color() + i['feature'], ': ', self.define_color() + i['info'])


