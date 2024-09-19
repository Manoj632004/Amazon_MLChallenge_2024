import pandas as pd
import re



"""

pd1 = pd.read_csv('part1_pred_cleaned.csv')
pd2 = pd.read_csv('part2_pred_cleaned.csv')
pd3 = pd.read_csv('part3_pred_cleaned.csv')
pd4 = pd.read_csv('part4_pred_cleaned.csv')
frames = [pd1,pd2,pd3,pd4]
final_sub = pd.concat(frames)
final_sub.to_csv('sub_final.csv', index = False)

"""
# Define valid units
valid_units = {
    'cubic foot', 'millilitre', 'kilovolt', 'ounce', 'microlitre', 'pound', 'fluid ounce', 'microgram',
    'milligram', 'kilogram', 'millivolt', 'watt', 'volt', 'yard', 'quart', 'imperial gallon', 'centimetre',
    'litre', 'ton', 'centilitre', 'decilitre', 'gallon', 'kilowatt', 'millimetre', 'foot', 'inch', 'pint',
    'gram', 'cubic inch', 'metre', 'cup'
}

def clean_predicted_value(value):
    # Convert non-string values to string
    if not isinstance(value, str):
        return ''
    
    # Remove special characters and handle invalid formats
    value = re.sub(r'Error: Invalid format in \d+', '', value)
    value = re.sub(r'[^0-9a-zA-Z\s\.\-]', '', value)
    
    # Extract numbers and units, ensuring only one unit and one value
    match = re.match(r'(\d+\.?\d*)\s*(\w+)', value)
    if match:
        num, unit = match.groups()
        unit = re.sub(r'[^a-zA-Z]', '', unit)
        if unit in ['cubicfoot', 'millilitre', 'kilovolt', 'ounce', 'microlitre', 'pound', 'fluidounce', 'microgram', 'milligram', 'kilogram', 'millivolt', 'watt', 'volt', 'yard', 'quart', 'imperialgallon', 'centimetre', 'litre', 'ton', 'centilitre', 'decilitre', 'gallon', 'kilowatt', 'millimetre', 'foot', 'inch', 'pint', 'gram', 'cubicinch', 'metre', 'cup']:
            return f'{num} {unit}'
    return ''
def clean_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    
    if 'prediction' not in df.columns:
        raise ValueError("CSV file must contain a 'prediction' column.")
    
    df['prediction'] = df['prediction'].apply(clean_predicted_value)
    
    # Save the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)

# Specify your input and output files here
input_file = 'sub_final.csv'  # Replace with your actual input file name
output_file = 'final_sub.csv'  # Replace with your desired output file name

# Call the cleaning function
clean_csv(input_file, output_file)

