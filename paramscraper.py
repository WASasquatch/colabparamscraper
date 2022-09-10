import copy

class paramScraper():

    def __init__(self, template, globals):
        self.updateGlobals(globals)
        self.reset(template)

    @classmethod
    def clear(cls, params=False, template=False):
        if not template:
            try:
                if cls.template and len(cls.template) > 0:
                    cls.template.clear()
            except AttributeError:
                cls.template = {}; pass
        if not params:
            try:
                if cls.params and len(cls.params) > 0:
                    cls.params.clear()
            except AttributeError:
                cls.params = {}; pass
    
    @classmethod
    def reset(cls, template=None):
        if template and type(template) is dict and len(template) > 0:
            cls.clear()
            for k in template.keys():
                cls.template[k] = copy.deepcopy(template[k])
                cls.params[k] = copy.deepcopy(template[k])
        else:
            try: 
                if cls.template and len(cls.template) > 0:
                    cls.clear(False, True)
                    for k in cls.template.keys():
                        cls.template[k] = copy.deepcopy(cls.template[k])
                        cls.params[k] = copy.deepcopy(cls.template[k])
            except AttributeError:
                raise AttributeError("Unable to load template from memory! paramScraper template needs to be re-initialized!")

    @classmethod
    def updateParams(cls, param, value, settingsType=None):
        try:
            if cls.template and len(cls.template) <= 0:
                raise AttributeError("The template dictionary is empty!")
        except AttributeError:
            raise AttributeError("The template dictionary is not initiated!")
        try:
            if cls.params: pass
        except AttributeError:
            raise AttributeError("The settings dictionary is not initiated!")
        if settingsType:
            if cls.template.__contains__(settingsType):
                if cls.template[settingsType].__contains__(param):
                    cls.params[settingsType][param] = copy.deepcopy(value)
        else:
            if cls.template.__contains__(param):
                cls.params[param] = copy.deepcopy(value)
                
    @classmethod
    def updateGlobals(cls, globals):
        if globals and type(globals) is dict:
            if len(globals) > 0:
                cls.globals = globals

    def scrape(self, settingsType=None):
        if settingsType is not None and self.template:
            for k in self.template[settingsType].keys():
                if cls.globals.__contains__(k):
                    self.updateParams(k, cls.globals[k], settingsType)
        else:
            for k in self.template.keys():
                if cls.globals.__contains__(k):
                    self.updateParams(k, cls.globals[k])
