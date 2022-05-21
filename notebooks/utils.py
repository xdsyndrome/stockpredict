import pandas as pd
import numpy as np

# Test Cases should be parked under tests folder in future
def get_mean(df, high, low, mean):
    df[mean] = (df[high] - df[low]) / 2
    return df

def generate_time_sequence(df, col, seq_length):
    '''
    Get rolling sequence of length = seq_length, if remaining duration >= seq_length.
    Outputs a list of sequences. Each sequence is a list of [[x1,x2,x3],y4]
    '''
    df = df.reset_index()
    output = []
    for index in df.index:
        # Check if remaining sequence is of sufficient length
        if index + seq_length + 1 < df.index.stop:
            mini_seq = df[col].iloc[index:index+seq_length].to_list()
            output.append([mini_seq, df[col].iloc[index+seq_length]])
    return output
