class CodeGenerator:
    def __init__(self, classname, attribute):
        self.classname = classname
        self.attribute = attribute
        
    def generatecode(self):
        classtemplate = '''class ''' +self.classname+ ''':'''+'''\n    def __init__(self):''' + '\n    '+'''    self._'''+self.attribute+''' = None\n\n    @property
    def test'''+self.attribute+'''(self):\n        return self.test'''+self.attribute+'''\n\n    @test'''+self.attribute+'''.getter
    def test'''+self.attribute+'''(self):\n        print("get test'''+self.attribute+'''")\n        return self._test'''+self.attribute+'''

    @test'''+self.attribute+'''.setter
    def test'''+self.attribute+'''(self, value):
        print("set test'''+self.attribute+'''")
        self._test'''+self.attribute+''' = value

    @test'''+self.attribute+'''.deleter
    def test'''+self.attribute+'''(self):
        print("del test'''+self.attribute+'''")
        del self._test'''+self.attribute+'''
        '''
        import ast
        class_tree = ast.parse(classtemplate)

        actualclass = compile(class_tree, 'class_tree', 'exec')

        print(ast.unparse(class_tree))
        print('\n')