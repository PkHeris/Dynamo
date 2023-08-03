# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import System
from System import Array
from System.Collections.Generic import *

# The inputs to this node will be stored as a list in the IN variables.
FirstList = IN[0]
SecondList = IN[1]

# Flatten list function
def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

# Combine the two lists
combined_list = FirstList + SecondList

# Use the function with the combined list
flat_list = flatten_list(combined_list)

# Count the elements in the final list
element_count = len(flat_list)

# Assign your output to the OUT variable.
OUT = element_count
