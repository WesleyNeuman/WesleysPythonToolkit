# Import Component's Modules
import pandas as pd

import logging, traceback

# Import Component
import WesleysPythonToolkit as ssh


# Test Functions
def test_df_stringsplit(visualize_output: bool):
    pd.set_option('display.max_columns', None)

    test_df = pd.DataFrame({'RandomNumber' : [7, 8, 3, 6, 6],
                            'TestSplitString' : ['Chicken, Beef', 'Beef, Pork, Chicken', 'Chicken', r'Fish/Ham', r'Beef, Lamb/Sausage']})
    try:
        test_df2 = ssh.df_stringsplit(test_df, 'TestSplitString', ',')
        if visualize_output==True:
            print('Comma Test')
            print(test_df2)

        test_df2 = ssh.df_stringsplit(test_df, 'TestSplitString', r'/')
        if visualize_output==True:
            print('Backslash Test')
            print(test_df2)

        test_df2 = ssh.df_stringsplit(test_df, 'TestSplitString', r'[,/]')
        if visualize_output==True:
            print('Multisplit Test')
            print(test_df2)

        logging.info('test_df_stringsplit has successfully evaluated')
    except Exception as inst:
        logging.error('test_df_stringsplit has failed')
        logging.error(inst)
        logging.error(traceback.format_exc())
