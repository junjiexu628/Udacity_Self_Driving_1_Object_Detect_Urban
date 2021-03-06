import argparse
import glob
import os
import random
import shutil

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    ls_data = os.listdir(data_dir)
    num_data = len(ls_data)
    rate = 0.1
    num_val = int(num_data*rate)
    
    #random 10% data for validation
    val_data = random.sample(ls_data,num_val)
    for name in val_data:
        shutil.move(data_dir + name, '/home/workspace/data/waymo/val/')
        
    #left 90% data for training    
    left_data = os.listdir(data_dir)
    for left in left_data:
        shutil.move(data_dir + left,'/home/workspace/data/waymo/train/')
    
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)