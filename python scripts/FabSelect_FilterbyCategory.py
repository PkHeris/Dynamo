# Copyright(c) 2016, Dimitar Venkov
# @5devene, dimitar.venkov@gmail.com
# Enhanced by Pooriya Kazemzadeh Heris - added Filtering and removed the ToDSType
# @PkHeris, pkazemzadehheris@uwaterloo.ca

# Define a boolean variable named refresh and set it to True; making Dynamo re-evaluate the script every time.
refresh = True  

# clr is a module that provides a bridge between Python and .NET Common Language Runtime (CLR)
import clr  

# Add a reference to the RevitNodes library, which allows to interact with Revit's API using Python
clr.AddReference("RevitNodes")

import Revit  # Import the Revit module from RevitNodes
clr.ImportExtensions(Revit.Elements)  # Import Revit elements module to work with Revit Elements

# Add a reference to RevitServices which includes utilities for interacting with Revit
clr.AddReference("RevitServices")

import RevitServices  # Import RevitServices module
from RevitServices.Persistence import DocumentManager  # Import DocumentManager from RevitServices which provides access to the current Revit document

doc = DocumentManager.Instance.CurrentDBDocument  # Get the current database document (i.e., the current open Revit document)
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument  # Get the current UI document (i.e., the document currently visible in the Revit interface)

def filter_by_category(element):
    """Check if an element's category is 'MEP Fabrication Ductwork' and not 'Tags'."""
    return element.Category.Name == "MEP Fabrication Ductwork" and element.Category.Name != "Tags"

def output1(l1):
    """Return a list of elements that pass the filter, or a single element if there is only one."""
    filtered_elements = [element for element in l1 if filter_by_category(element)]
    return filtered_elements[0] if len(filtered_elements) == 1 else filtered_elements

selid = uidoc.Selection.GetElementIds()  # Get the IDs of the currently selected elements in the Revit interface

OUT = output1([doc.GetElement(id) for id in selid])  # Convert the selected elements and pass them to the output1 function

