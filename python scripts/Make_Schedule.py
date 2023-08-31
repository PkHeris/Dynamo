# Import required libraries
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Function to rename field titles
def rename_field(schedule_definition, field_ids, old_name, new_name):
    field = schedule_definition.GetField(field_ids[old_name].IntegerValue)
    field.ColumnHeading = new_name

# Get the current document
doc = DocumentManager.Instance.CurrentDBDocument

# Start a transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# Access the MEP Fabrication Pipework category
categoryId = Category.GetCategory(doc, BuiltInCategory.OST_FabricationPipework).Id

# Create a new schedule for MEP Fabrication Pipework
schedule = ViewSchedule.CreateSchedule(doc, categoryId)

# Rename the schedule's view name to the desired assembly name
schedule.Name = "NSB-P4-SUBS5-STM-55"

# Get ScheduleDefinition from ViewSchedule
scheduleDef = schedule.Definition

# Get all possible SchedulableFields
schedulableFields = scheduleDef.GetSchedulableFields()

# List of desired field names
fields = ["Assembly Name", "Item Number", "Family", "Size", "Count", "Length", "MN-FP_Connector 1", "MN-FP_Connector 2"]

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

# Rename the necessary fields
rename_field(scheduleDef, field_ids, "Family", "Description")
rename_field(scheduleDef, field_ids, "Count", "Qty")
rename_field(scheduleDef, field_ids, "Length", "Length (mm)")
rename_field(scheduleDef, field_ids, "MN-FP_Connector 1", "End Prep 1")
rename_field(scheduleDef, field_ids, "MN-FP_Connector 2", "End Prep 2")

# Add filter for the Assembly Name
filter = ScheduleFilter(field_ids["Assembly Name"], ScheduleFilterType.Equal, "NSB-P4-SUBS5-STM-55")
scheduleDef.AddFilter(filter)

# Close the transaction
TransactionManager.Instance.TransactionTaskDone()

OUT = schedule
