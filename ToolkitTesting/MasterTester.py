# Import All Testing Modules
import ToolkitTesting.ModuleTesting.StringSplitHelper_Test

#Import Logging
import logging
import os
if os.path.exists('MasterTestingDebug.log'):
    os.remove('MasterTestingDebug.log')
logging.basicConfig(filename='MasterTestingDebug.log', level=logging.INFO)

# Call Every Test Function
def test_all(visout):
    ToolkitTesting.ModuleTesting.StringSplitHelper_Test.test_df_stringsplit(visout)



# Call Test All
test_all(True)