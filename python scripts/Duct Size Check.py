import clr

# Add references for Revit's API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

import math

def check_duct_sizes(element):
    # Constants (mixed SI and imperial units)
    AIR_DENSITY = 1.225  # kg/m³, at standard conditions
    GRAVITY = 9.81  # m/s²
    MAX_VELOCITY_FPM = 1500  # fpm
    MAX_FRICTION_LOSS = 0.08  # in. w.g./100ft
    CFM_TO_CUBICMPS = 0.00047194745  # Conversion factor from cfm to m³/s

    # Extract parameters from the duct element
    width_mm = float(element.LookupParameter("Main Primary Width").AsValueString()) if element.LookupParameter("Main Primary Width") else 0.0
    height_mm = float(element.LookupParameter("Main Primary Depth").AsValueString()) if element.LookupParameter("Main Primary Depth") else 0.0
    diameter_mm = float(element.LookupParameter("Main Primary Diameter").AsValueString()) if element.LookupParameter("Main Primary Diameter") else 0.0
    length_mm = float(element.LookupParameter("Length").AsValueString()) if element.LookupParameter("Length") else 0.0
    
    # "Flow Maximum" is stored as an integer
    cfm = element.LookupParameter("Flow Maximum").AsInteger() if element.LookupParameter("Flow Maximum") else 0 #Should be defined by user

    # Convert mm to m
    width = width_mm / 1000
    height = height_mm / 1000
    diameter = diameter_mm / 1000
    length = length_mm / 1000

    # Check if duct is rectangular or round
    if diameter != 0:
        duct_type = "round"
    else:
        duct_type = "rectangular"

    # Convert CFM to m³/s
    flow_rate = cfm * CFM_TO_CUBICMPS

    # Calculate area and perimeter based on duct type
    if duct_type == 'rectangular':
        area = width * height  # m²
        perimeter = 2 * (width + height)  # m
    else:  # round
        area = math.pi * (diameter / 2) ** 2  # m²
        perimeter = math.pi * diameter  # m

    # Calculate velocity in m/s
    velocity_mps = flow_rate / area
    velocity_fpm = velocity_mps * 196.85  # Conversion factor from m/s to fpm

    # Calculate friction loss (using the previously provided formula)
    hydraulic_diameter = (4 * area) / perimeter  # m
    f = (MAX_FRICTION_LOSS / 100) * (hydraulic_diameter / (GRAVITY * velocity_mps**2 / 2))
    friction_loss = f * (100 / hydraulic_diameter) * (velocity_mps**2 / (2 * GRAVITY))

    # Return the results for the element using .format()
    if velocity_fpm > MAX_VELOCITY_FPM or friction_loss > MAX_FRICTION_LOSS:
        return {
            "ElementId": element.Id,
            "Status": "Not Sized Correctly",
            "Velocity": "{:.2f} fpm".format(velocity_fpm),
            "Friction Loss": "{:.4f} in. w.g./100ft".format(friction_loss),
            "Length": "{:.2f} m".format(length)
        }
    else:
        return {
            "ElementId": element.Id,
            "Status": "Sized Correctly",
            "Velocity": "{:.2f} fpm".format(velocity_fpm),
            "Friction Loss": "{:.4f} in. w.g./100ft".format(friction_loss),
            "Length": "{:.2f} m".format(length)
        }

# The input to this node will be a list of duct elements from Dynamo
elements = IN[0]

# Check sizes for each duct and return results
results = [check_duct_sizes(el) for el in elements]
OUT = results
