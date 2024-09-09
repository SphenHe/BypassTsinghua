#!/usr/bin/env python3

import argparse
import numpy as np
import accept
import mcmc
import h5py

parser = argparse.ArgumentParser()
parser.add_argument("--pe", dest="pe", type=str, help="probe pe coeff")
parser.add_argument("--time", dest="time", type=str, help="probe time coeff")
parser.add_argument("--pmt", dest="pmt", type=str, help="pmt position file")
parser.add_argument("-i", dest="ipt", type=str, help="input PEt file")
parser.add_argument("-o", dest="opt", type=str, help="output recon file")
args = parser.parse_args()

# Loading Probe
with h5py.File(args.pe, 'r') as h:
    coeff_pe = h['coeff'][:]
with h5py.File(args.time, 'r') as h:
    coeff_time = h['coeff'][:]
pmt_pos = np.loadtxt(args.pmt)
probe = accept.probe(coeff_pe, coeff_time, pmt_pos)

# Reading Data
with h5py.File(args.ipt) as h:
    # event id
    eids = h['truth']['eid'][:]
    # NPE
    NPE = h['truth']['NPE'][:]
    # channel id
    chs_flatten = h['ch'][:]
    # the timing of PEs
    PEts_flatten = h['PEt'][:]
    # split
    chs = []
    PEts = []
    PE_count = 0
    for i, NPE_i in enumerate(NPE):
        chs.append(chs_flatten[PE_count : NPE_i + PE_count])
        PEts.append(PEts_flatten[PE_count : NPE_i + PE_count])
        PE_count += NPE_i

# MCMC Sampling
mcmc.sample(eids, chs, PEts, probe, args.opt)







