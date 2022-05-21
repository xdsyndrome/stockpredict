from unittest import TestCase
import pytest
import pandas as pd
import numpy as np
from utils import generate_time_sequence, get_mean

class Test_Preprocessing:
    def test_generate_time_sequence(self):
        test_data = pd.DataFrame(
            data=[x for x in range(10)],
            columns=['data']
            )
        
        output_data = generate_time_sequence(test_data, 'data', 3)
        
        assert output_data == [
            [[0, 1, 2], 3], 
            [[1, 2, 3], 4], 
            [[2, 3, 4], 5], 
            [[3, 4, 5], 6], 
            [[4, 5, 6], 7], 
            [[5, 6, 7], 8]
            ]
        
    def test_get_mean(self):
        test_data = pd.DataFrame(
            data=[[x*5,x] for x in range(4)],
            columns=['high','low']
        )
        
        output_data = get_mean(test_data, 'high', 'low', 'mean')
        
        assert output_data['mean'].to_list() == [0.0, 2.0, 4.0, 6.0]
     
