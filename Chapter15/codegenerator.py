class CodeGenerator:
 
    def generate_meta(self):
        ast = __import__('ast')
        meta_template = '''
from abc import ABC, abstractmethod, ABCMeta
class CarSpecs(type, metaclass = ABCMeta):
    def __new__(classitself, classname, baseclasses, attributes):  
        newattributes = {}
        for attribute, value in attributes.items():
            if attribute.startswith("__"):
                newattributes[attribute] = value
            elif type(value)==int or type(value)==float:
                newattributes[attribute] = {}
                newattributes[attribute]['feature'] = attribute.title().replace('_', ' ')
                newattributes[attribute]['info'] = str(value)
                newattributes[attribute]['type'] = 'NUMERIC'
            elif type(value)==str:
                newattributes[attribute] = {}
                newattributes[attribute]['feature'] = attribute.title().replace('_', ' ')
                newattributes[attribute]['info'] = value.title()
                newattributes[attribute]['type'] = 'VARCHAR'
            elif type(value)==bool:
                newattributes[attribute] = {}
                newattributes[attribute]['feature'] = attribute.title().replace('_', ' ')
                newattributes[attribute]['info'] = value.title()
                newattributes[attribute]['type'] = 'BOOLEAN'

            else:
                newattributes[attribute] = value                
        return type.__new__(classitself, classname, baseclasses, newattributes)
'''
        meta_tree = ast.parse(meta_template)
        print(ast.unparse(meta_tree))
        print('\n')
        
    def generate_car_catalogue(self):
        ast = __import__('ast')
        catalogue_template = '''
class CarCatalogue(metaclass = CarSpecs):
    @abstractmethod
    def define_color(self):
        pass
    
    @abstractmethod
    def print_catalogue(self):
        pass
        '''
        catalogue_tree = ast.parse(catalogue_template)
        print(ast.unparse(catalogue_tree))
        print('\n')
        
    def generate_carmake_code(self):
        ast = __import__('ast')
        carmake_template = '''
class CarMake(metaclass = CarSpecs):   
    @abstractmethod
    def define_spec(self):
        pass     
        '''
        carmake_tree = ast.parse(carmake_template)
        print(ast.unparse(carmake_tree))
        print('\n')
        
    def generate_bodystyle_parent(self):
        ast = __import__('ast')
        bodystyle_parent_template = '''
class BodyStyle(metaclass = CarSpecs):
    @abstractmethod
    def body_style_features(self):
        pass  
        '''
        bodystyle_parent_tree = ast.parse(bodystyle_parent_template)
        print(ast.unparse(bodystyle_parent_tree))
        print('\n')
        
    def generate_salestype_code(self):
        ast = __import__('ast')
        saletype_template = '''
class SaleType(metaclass = CarSpecs):
    @abstractmethod
    def calculate_price(self):
        pass
        '''
        salestype_tree = ast.parse(saletype_template)
        print(ast.unparse(salestype_tree))
        print('\n')
    
    def generate_newsale_code(self):
        ast = __import__('ast')
        newsale_template = '''
class New(SaleType, CarCatalogue,  metaclass = CarSpecs):
    def calculate_price(self, classname):
        car = classname()
        price = float(car.price['info'])
        return price
        '''
        newsale_tree = ast.parse(newsale_template)
        print(ast.unparse(newsale_tree))
        print('\n')
        
    def generate_resale_code(self):
        ast = __import__('ast')
        resale_template = '''
class Resale(SaleType, CarCatalogue,  metaclass = CarSpecs):
    def calculate_price(self, classname, years):
        car = classname()
        depreciation = years * 0.15
        price = float(car.price['info']) * (1 - depreciation)
        return price
        '''
        resale_tree = ast.parse(resale_template)
        print(ast.unparse(resale_tree))
        print('\n')
        
    def generate_car_code(self, classname, carspecs):
        self.classname = classname
        self.carspecs = carspecs
        ast = __import__('ast')
        car_template = '''
class '''+self.classname+'''(CarMake, CarCatalogue, metaclass = CarSpecs):
    fuel_type = '''+"'"+self.carspecs['fuel_type']+"'"+'''
    aspiration = '''+"'"+self.carspecs['aspiration']+"'"+'''
    num_of_door = '''+"'"+self.carspecs['num_of_door']+"'"+'''
    drive_wheels = '''+"'"+self.carspecs['drive_wheels']+"'"+'''
    wheel_base = '''+"'"+self.carspecs['wheel_base']+"'"+'''
    length = '''+"'"+self.carspecs['length']+"'"+'''
    width = '''+"'"+self.carspecs['width']+"'"+'''
    height = '''+"'"+self.carspecs['height']+"'"+'''
    curb_weight = '''+"'"+self.carspecs['curb_weight']+"'"+'''
    fuel_system = '''+"'"+self.carspecs['fuel_system']+"'"+'''
    city_mpg = '''+"'"+self.carspecs['city_mpg']+"'"+'''
    highway_mpg = '''+"'"+self.carspecs['highway_mpg']+"'"+'''
    price = '''+"'"+self.carspecs['price']+"'"+'''

    def define_color(self):
            BOLD = '\33[5m'
            BLUE = '\033[94m'
            return BOLD + BLUE

    def define_spec(self):
            specs = [self.fuel_type, self.aspiration, self.num_of_door, self.drive_wheels, 
                     self.wheel_base, self.length, self.width, self.height, self.curb_weight,
                    self.fuel_system, self.city_mpg, self.highway_mpg]
            return specs

    def print_catalogue(self):
            for i in self.define_spec():
                print(self.define_color() + i['feature'], ": ", self.define_color() + i['info'])   
                '''

        car_tree = ast.parse(car_template)
        print(ast.unparse(car_tree))
        print('\n')
        
    def generate_bodystyle_code(self, classname, carfeatures):
        self.classname = classname
        self.carfeatures = carfeatures
        ast = __import__('ast')
        bodystyle_template = '''
class '''+self.classname+'''(BodyStyle, CarCatalogue,  metaclass = CarSpecs):
    engine_location = '''+"'"+self.carfeatures['engine_location']+"'"+'''
    engine_type = '''+"'"+self.carfeatures['engine_type']+"'"+'''
    num_of_cylinders = '''+"'"+self.carfeatures['num_of_cylinders']+"'"+''' 
    engine_size = '''+"'"+self.carfeatures['engine_size']+"'"+'''
    bore = '''+"'"+self.carfeatures['bore']+"'"+'''
    stroke = '''+"'"+self.carfeatures['stroke']+"'"+'''
    compression_ratio = '''+"'"+self.carfeatures['compression_ratio']+"'"+'''
    horse_power = '''+"'"+self.carfeatures['horse_power']+"'"+'''
    peak_rpm = '''+"'"+self.carfeatures['peak_rpm']+"'"+'''

    def body_style_features(self):
            features = [self.engine_location, self.engine_type, self.num_of_cylinders, self.engine_size,
                     self.bore, self.stroke, self.compression_ratio, self.horse_power, self.peak_rpm]
            return features  

    def define_color(self):
            BOLD = '\33[5m'
            RED = '\033[31m'
            return BOLD + RED

    def print_catalogue(self):
            for i in self.body_style_features():
                print(self.define_color() + i['feature'], ": ", self.define_color() + i['info'])  
                '''
        bodystyle_tree = ast.parse(bodystyle_template)
        print(ast.unparse(bodystyle_tree))
        print('\n')