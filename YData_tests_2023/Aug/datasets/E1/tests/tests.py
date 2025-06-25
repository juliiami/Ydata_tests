import numpy as np
import os
import pandas as pd

def get_data():
    data_path = os.path.dirname(__file__)
    input_file = os.path.join(data_path,'vehicles.csv')
    output_file = os.path.join(data_path,'E1_result.csv')
    data_in = pd.read_csv(input_file)
    data_out = pd.read_csv(output_file)
    return data_in, data_out