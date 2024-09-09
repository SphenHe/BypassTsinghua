#!/usr/bin/env python3

import numpy as np
import pandas as pd
import h5py
from config import mc_step
import sys
import time
import subprocess

def check(recon_file, truth_file):
    shell = 645

    # reading recon data
    recon = pd.read_hdf(recon_file, "Recon")
    # burning
    recon = recon[recon['step'] > (mc_step / 5 * 3)]
    # average
    recon = recon.groupby('EventID').mean().reset_index()
    recon['x'] = recon['x'].apply(lambda x: x * shell)
    recon['y'] = recon['y'].apply(lambda x: x * shell)
    recon['z'] = recon['z'].apply(lambda x: x * shell)
    recon['r'] = np.sqrt(recon['x'].values**2 + recon['y'].values**2 + recon['z'].values**2)

    # reading truth from simulation
    with h5py.File(truth_file) as h:
        # event id
        eids = h['truth']['eid'][:]
        x = h['truth']['x'][:]
        y = h['truth']['y'][:]
        z = h['truth']['z'][:]
        r = h['truth']['r'][:]
        truth = pd.DataFrame({"EventID":eids, "x":x, "y":y, "z":z, "r":r})

    # sort
    recon = recon.sort_values(by=['EventID'])
    truth = truth.sort_values(by=['EventID'])

    # r check
    if np.abs(recon['r'].mean() - truth['r'].mean()) > 15 or max(np.abs(recon['r'].values - truth['r'].values)) > 150:
        print("r-bias is too large.")
        return False

    # E check
    if np.abs(recon['E'].mean() - 1) > 0.1:
        print("E-bias is too large.")
        return False

    # t check
    if np.abs(recon['t'].mean()) > 1:
        print("t-bias is too large.")
        return False
    
    return True

if __name__ == '__main__':
    if sys.version_info[0] != 3:
        print("Please use Python 3")
        sys.exit()

    start_time = time.time()

    # 执行命令
    command = [sys.executable, 'main.py', '-i', 'data/Entries100.h5', '-o', 'data/tvE100.h5', '--pe', 'data/PE.h5', '--time', 'data/Time.h5', '--pmt', 'data/PMT.txt']
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.communicate()

    end_time = time.time()
    execution_time = end_time - start_time

    if check("data/tvE100.h5", "data/Entries100.h5"):
        print(f"Command executed in {execution_time:.2f} seconds")
    else:
        print("Please check the code for changes")



