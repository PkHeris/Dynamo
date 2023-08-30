# Import necessary libraries
import clr

# Import Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

# Input assigned to the IN variable
nested_views = IN[0]

# Recursive function to duplicate views
def duplicate_nested_views(input_list):
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.append(duplicate_nested_views(item))
        else:
            try:
                # Unwrap the Dynamo element to get the Revit element
                revit_element = UnwrapElement(item)
                
                if isinstance(revit_element, View):  
                    duplicated_id = revit_element.Duplicate(ViewDuplicateOption.Duplicate)
                    duplicated_view = revit_element.Document.GetElement(duplicated_id)
                    result.append(duplicated_view)  # Append the duplicated view object itself
                else:
                    result.append("Not a valid view for duplication.")
            except Exception as e:
                result.append(str(e))  # Return the error message
    return result


# Call the recursive function
OUT = duplicate_nested_views(nested_views)
