# Importing required libraries for Dynamo & Revit API
import clr

# Adding references for Revit API
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *

# Adding references for DynamoRevit interop
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

def get_item_custom_id(element):
    """Retrieve the ItemCustomId of an element if it exists."""
    try:
        return element.ItemCustomId
    except AttributeError:
        return None

def flatten(input_list):
    """Flatten a list of lists."""
    if isinstance(input_list, list):
        return [a for i in input_list for a in flatten(i)]
    else:
        return [input_list]

# Assuming the input elements are provided as IN[0]
unwrapped_elements = [UnwrapElement(element) for element in flatten(IN[0])]
cids = [get_item_custom_id(element) for element in unwrapped_elements]

# Pairing elements with their CID for sorting
paired_elements = zip(unwrapped_elements, cids)

# Sorting function based on CID priority
def sort_key(pair):
    _, cid = pair
    if cid == 2041:
        return 1
    elif cid == 2523:
        return 2
    else:
        return 3

sorted_pairs = sorted(paired_elements, key=sort_key)

# Assigning item numbers and collecting elements with CID 2041
elements_with_cid_2041 = []
for index, (fabPart, cid) in enumerate(sorted_pairs):
    # Use the Revit API to get and set the "Item Number" parameter using the method fabPart.LookupParameter()
    item_number_param = fabPart.LookupParameter("Item Number")
    if item_number_param:
        item_number_param.Set(str(index + 1))
    if cid == 2041:
        elements_with_cid_2041.append(fabPart)

OUT = elements_with_cid_2041
