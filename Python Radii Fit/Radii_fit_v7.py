# @Author: Giovanni G. Baez Flores
# @Date:   2020-011-12T13:25:14-05:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2020-07-03T13:08:34-05:00

from time import process_time
import pandas as pd
import numpy as np
import os
import sys
################################################################################
#### Setting directories
################################################################################
cwd=os.getcwd()
os.chdir(cwd)
def lmgf_check(layer):
    if os.path.exists(cwd+'/'+str(layer)+'_l')
