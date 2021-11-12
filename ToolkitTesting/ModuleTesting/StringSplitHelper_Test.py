# Import Component's Modules
import pandas as pd

import logging, sys, os

# Import Component
import WesleysPythonToolkit.PandasWrappers as ssh

# Test Functions
def test_df_stringsplit(visualize_output: bool):
    pd.set_option('display.max_columns', None)

    test_df = pd.DataFrame({'RandomNumber' : [7, 8, 3],
                            'TestSplitString' : ['Chicken, Beef', 'Beef, Pork, Chicken', 'Chicken']})
    try:
        test_df = ssh.df_stringsplit(test_df, 'TestSplitString', ',')
        if visualize_output==True:
            print(test_df)
        logging.info('test_df_stringsplit has successfully evaluated')
    except Exception as inst:
        logging.error('test_df_stringsplit has failed')
        logging.error(inst)
