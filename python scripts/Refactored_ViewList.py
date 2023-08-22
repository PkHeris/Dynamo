#Copyright (c) mostafa el ayoubi ,  2016
#Data-Shapes www.data-shapes.net , elayoubi.mostafa@gmail.com
# Pooriya Kazemzadeh Heris - Refactored the code to combine multiple classes into a single Python script node.

class listview():
    def __init__(self, inputname, height, highlight, display_mode, element_count, default_values, _sorted, showId):
        self.inputname = inputname
        self.height = height
        self.highlight = highlight
        self.display_mode = display_mode
        self.element_count = element_count
        self.default_values = default_values
        self.sorted = _sorted
        self.showId = showId

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def values(self):
        return self.__dict__.values()

    def keys(self):
        return self.__dict__.keys()

    def __repr__(self):
        return 'UI.ListView input'

def process_listview(inputname, keys, values, height, highlight, display_mode, element_count_condition, default_values, _sorted, showId):
    element_count = len(keys) if element_count_condition else 0
    list_instance = listview(inputname, height, highlight, display_mode, element_count, default_values, _sorted, showId)
    
    for k, v in zip(keys, values):
        key_representation = str(k) + '  -  id: ' + str(v.Id) if list_instance.showId else str(k)
        list_instance[key_representation] = v
    
    return list_instance

# Example of usage:
OUT = process_listview(IN[0], IN[1], IN[2], IN[3], IN[4], IN[5], IN[6], IN[7], IN[8], IN[9])
