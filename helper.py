import pandas as pd 
# the below function converts csv to string 
def csv_to_string(file):
        df = pd.read_csv(file)
        combined_string = ""
        # Iterate over each row in the CSV file
        for index,row in df.iterrows():
            # Extract the values from the row
            time_start = row['start_time']
            time_end = row['end_time']
            text = row['speaker']
            action = row['text']

            # Concatenate the values in the desired format
            combined_string += f"{time_start}-{time_end} : {text} : {action}\n"
        return combined_string
