import pandas as pd

# Define the column headers
columns = [
    'branch', 'item_id', 'category', 'supplier', 'current_stock', 'max_daily_demand', 
    'avg_daily_demand', 'max_lead_time_days', 'avg_lead_time_days', 'unit_cost', 
    'last_restock_date', 'safety_stock', 'min_level', 'max_level', 'total_value', 
    'stock_status', 'reorder_quantity'
]

# Create an empty DataFrame with the specified column headers
df = pd.DataFrame(columns=columns)
print(df)

# import usage data
# usage = pd.read_csv('usage.csv')
# print(usage.head())

# manipulate the data
df['branch'] = 'Mobile Tool Truck'

print(df.head())
#