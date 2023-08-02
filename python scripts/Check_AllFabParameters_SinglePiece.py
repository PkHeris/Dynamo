# Import RevitAPI
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

# Import DocumentManager and TransactionManager
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Get the current document and fabrication part from input(IN[0])
doc = DocumentManager.Instance.CurrentDBDocument
fabPart = UnwrapElement(IN[0])

# Start a new transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# Create a dictionary to hold parameter names and values
paramDict = {}

# Get all parameters and add them to the dictionary
params = fabPart.Parameters
for p in params:
    # Store parameter names and values in the dictionary
    paramDict[p.Definition.Name] = p.AsValueString() if p.StorageType == StorageType.String else p.AsDouble() if p.StorageType == StorageType.Double else p.AsInteger() if p.StorageType == StorageType.Integer else None

# End the transaction
TransactionManager.Instance.TransactionTaskDone()

# Set the output
OUT = paramDict
