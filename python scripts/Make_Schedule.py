# Import required libraries
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Get the current document
doc = DocumentManager.Instance.CurrentDBDocument

# Start a transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# Access the MEP Fabrication Pipework category
categoryId = Category.GetCategory(doc, BuiltInCategory.OST_FabricationPipework).Id

# Create a new schedule for MEP Fabrication Pipework
schedule = ViewSchedule.CreateSchedule(doc, categoryId)

# Get ScheduleDefinition from ViewSchedule
scheduleDef = schedule.Definition

# Get all possible SchedulableFields
schedulableFields = scheduleDef.GetSchedulableFields()

# List of desired field names
fields = ["Assembly Name", "Item Number", "Family", "Size", "Count", "Length", "MN-FP Connector 1", "MN-FP Connector 2"]

# Create a dictionary for quick lookup of SchedulableFields by their name
fields_dict = {sf.GetName(doc): sf for sf in schedulableFields}

# A dictionary to store added fields' IDs
field_ids = {}

# Add fields to the schedule based on the order in the 'fields' list
for field_name in fields:
    if field_name in fields_dict:
        field = scheduleDef.AddField(fields_dict[field_name])
        field_ids[field_name] = field.FieldId

# Sorting setup using the field IDs
sortItemNumber = ScheduleSortGroupField(field_ids["Item Number"], ScheduleSortOrder.Ascending)
sortFamily = ScheduleSortGroupField(field_ids["Family"], ScheduleSortOrder.Ascending)

# Add the sorting criteria to the schedule
scheduleDef.AddSortGroupField(sortItemNumber)
scheduleDef.AddSortGroupField(sortFamily)

# Close the transaction
TransactionManager.Instance.TransactionTaskDone()

OUT = fields_dict
