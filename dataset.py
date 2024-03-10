import os
import pandas as pd
from numpy import vstack


def import_from_files():
    """
        Read .csv files and store data into an array
    """
    rootdir = './dataset/'
    output_arr = []
    first = 1
    columns_name = None

    columns_to_remove = ['#<Time(ms)>', '<Successes#>', '<Burst#>', '<Std dev(m)>', '<Ch-MHz>', '<AP-SSID>', '<RTT AP?>']
    columns_to_rename = {'<True Range(m)>': 'True Range', '<Est. Range(m)>': 'RTT', '<RSSI(dBm)>': 'RSSI'}
    
    scenario_mapping = {'LOS': 0, 'Glass': 1, 'Metal': 2, 'Wall': 3}
    
    for dirpath, dirnames, filenames in os.walk(rootdir):
        for file in filenames:
            if file.endswith('.csv'):
                filename = os.path.join(dirpath, file)
                print(filename)
                output_data = [] 

                # read data from file
                df = pd.read_csv(filename)

                # Remove specified columns
                df.drop(columns=columns_to_remove, inplace=True, errors='ignore')
                
                # Rename specified columns
                df.rename(columns=columns_to_rename, inplace=True)
                
                # Add a new column for scenarios based on the original folder name
                scenario = os.path.basename(os.path.dirname(filename))
                df['Scenario'] = scenario_mapping.get(scenario, -1)  # Assign -1 if scenario not found
                
                if columns_name is None:
                    columns_name = df.columns.values
    
                input_data = df.values
                
                # append to array
                if first > 0:
                    first = 0
                    output_arr = input_data

                else:
                    output_arr = vstack((output_arr, input_data))
    
    return columns_name, output_arr

if __name__ == '__main__':

    # import raw data from folder with dataset
    print("Importing dataset to numpy array")
    print("-------------------------------")
    columns, data = import_from_files()
    print("-------------------------------")
    # print dimensions and data
    print("Number of samples in dataset: %d" % len(data))
    print("Number of features: %d" % len(columns))
    print("-------------------------------")
    print("Dataset columns:")
    print(columns)
    print("-------------------------------")
    print("Dataset:")
    print(data)
