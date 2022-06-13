class BranchMetaclass(type):
    '''
    This is a meta class for ABC Megamart branch that adds an additional 
    quality to the attributes of branch classes. 
    Add this as only a meta class.
    There are no methods to inherit this class as a parent class or super class.    
    '''
    def __new__(classitself, classname, baseclasses, attributes):
        import inspect
        newattributes = {}
        for attribute, value in attributes.items():
            if attribute.startswith("__"):
                newattributes[attribute] = value
            elif inspect.isfunction(value):
                newattributes['branch' + attribute.title()] = value
            else:
                newattributes[attribute] = value
        return type.__new__(classitself, classname, baseclasses, newattributes)