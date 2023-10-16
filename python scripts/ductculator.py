import math

def equivalent_diameter(L1, L2_or_shape):
    """
    Calculate equivalent diameter based on given dimensions and shape.
    
    L1: Length or one dimension of the duct (in mm)
    L2_or_shape: If round, input should be "RND". Otherwise, provide the second dimension (in mm).
    """
    
    if L2_or_shape == "RND":
        return L1 / 25
    else:
        L2 = L2_or_shape
        return 1.3 * (L1 * L2 / 645.16)**0.625 / (L1/25.4 + L2/25.4)**0.25

def fpm(airflow_rate, area_ft2):
    """
    Calculate the air velocity in the duct (FPM).
    
    airflow_rate: Airflow rate in CFM.
    area_ft2: Cross-sectional area in square feet.
    """
    
    return airflow_rate / area_ft2

def pressure_drop(airflow_rate, equivalent_diameter):
    """
    Calculate the pressure drop within the duct.
    
    airflow_rate: Airflow rate in CFM.
    equivalent_diameter: Equivalent diameter of the duct.
    """
    
    return (0.109136 * (airflow_rate ** 1.9)) / (equivalent_diameter ** 5.02)

def area_ft2(L1, L2_or_shape):
    """
    Calculate the duct's cross-sectional area in square feet.
    
    L1: Length or one dimension of the duct (in mm).
    L2_or_shape: If round, input should be "RND". Otherwise, provide the second dimension (in mm).
    """
    
    L_in_inches = L1 / 25.4
    
    if L2_or_shape == "RND":
        return (L_in_inches / 2)**2 * math.pi / 144
    else:
        M_in_inches = L2_or_shape / 25.4
        return L_in_inches * M_in_inches / 144

def main():
    # Sample user inputs
    airflow_rate = float(input("Enter Airflow Rate (CFM): "))
    L1 = float(input("Enter Length or Dimension (mm): "))
    L2_or_shape = input("Enter Shape (e.g., 'RND') or Second Dimension (mm): ")
    
    try:
        L2_or_shape = float(L2_or_shape)
    except ValueError:
        pass
    
    # Calculations
    eq_diameter = equivalent_diameter(L1, L2_or_shape)
    duct_area_ft2 = area_ft2(L1, L2_or_shape)
    air_velocity = fpm(airflow_rate, duct_area_ft2)
    p_drop = pressure_drop(airflow_rate, eq_diameter)
    
    # Output results
    print(f"\nEquivalent Diameter: {eq_diameter} inches")
    print(f"Air Velocity (FPM): {air_velocity}")
    print(f"Pressure Drop: {p_drop}")

if __name__ == "__main__":
    main()
