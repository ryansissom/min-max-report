import pandas as pd

# build dataframe
data = {
    'branch': ['North', 'South', 'East', 'West'],
    'item_id': ['A001', 'A002', 'A003', 'A004'],
    'category': ['Electronics', 'Furniture', 'Clothing', 'Food'],
    'supplier': ['Supplier1', 'Supplier2', 'Supplier3', 'Supplier4'],
    'current_stock': [150, 200, 300, 400],
    'max_daily_demand': [10, 20, 15, 25],
    'avg_daily_demand': [5, 10, 8, 12],
    'max_lead_time_days': [30, 45, 60, 90],
    'avg_lead_time_days': [20, 30, 40, 50],
    'unit_cost': [100, 200, 150, 50],
    'last_restock_date': ['2025-01-01', '2025-01-15', '2025-02-01', '2025-02-15'],
    'safety_stock': [50, 60, 70, 80],
    'min_level': [30, 40, 50, 60],
    'max_level': [200, 250, 350, 450],
    'stock_status': ['In Stock', 'In Stock', 'Low Stock', 'Out of Stock'],
    'reorder_quantity': [100, 150, 200, 250]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculated column for total_value
df
df['total_value'] = df['current_stock'] * df['unit_cost']

# Reorder columns to place total_value in the desired spot
df = df[[
    'branch', 'item_id', 'category', 'supplier', 'current_stock', 'max_daily_demand', 
    'avg_daily_demand', 'max_lead_time_days', 'avg_lead_time_days', 'unit_cost', 
    'last_restock_date', 'safety_stock', 'min_level', 'max_level', 'total_value', 
    'stock_status', 'reorder_quantity'
]]

# importing data with looker api

#