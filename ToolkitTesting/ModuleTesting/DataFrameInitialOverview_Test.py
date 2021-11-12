# Import Component's Modules
import pandas as pd

import logging, sys, os

# Import Component
import WesleysPythonToolkit.PandasWrappers as pw

# Test Functions
def test_df_initialoverview(visualize_output: bool):
    pd.set_option('display.max_columns', None)

    test_df = pd.DataFrame({'RandomNumber': [7, 8, 3],
                            'TestSplitString': ['Chicken, Beef', 'Beef, Pork, Chicken', 'Chicken']})
    if visualize_output == False:
        sys.stdout = open(os.devnull, 'w')

    try:
        pw.df_initialoverview(test_df)
        logging.info('test_df_initialoverview has successfully evaluated with no columnlist argument')
    except Exception as inst:
        logging.error('test_df_initialoverview has failed with no columnlist argument')
        logging.error(inst)

    try:
        pw.df_initialoverview(test_df, columnlist=['RandomNumber'])
        logging.info('test_df_initialoverview has successfully evaluated with a column list argument')
    except Exception as inst:
        logging.error('test_df_initialoverview has failed with a columnlist argument')
        logging.error(inst)

    if visualize_output == False:
        sys.stdout = sys.__stdout__