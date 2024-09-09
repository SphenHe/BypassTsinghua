import numpy as np
from config import tau, ts, chnum

def legval(x, n):
    res = np.zeros((n,) + x.shape)
    res[0] = 1
    res[1] = x
    res[2:n] = ((2 * np.arange(2, n) - 1) * x * res[1:n-1] - (np.arange(2, n) - 1) * res[0:n-2]) / np.arange(2, n)
    return res

class probe:
    def __init__(self, coeff_pe, coeff_time, pmt_pos):
        self.coeff_pe = coeff_pe
        self.coeff_time = coeff_time
        self.base_r = None
        self.base_t = None
        self.pmt_pos = pmt_pos

    def calc_basis(self, rho, cos_theta, len1, len2):
        # Generating Base
        base_t = legval(cos_theta, len1)
        base_r = legval(np.array([rho,]), len2).flatten()
        return base_r, base_t

    def get_base(self, vertex):
        # Boundary
        v = vertex[:3]
        rho = np.linalg.norm(v)
        rho = np.clip(rho, 0, 1)
        # Calculate cos theta
        cos_theta = np.cos(np.arctan2(np.linalg.norm(np.cross(v, self.pmt_pos), axis=1), np.dot(v,self.pmt_pos.T)))
        self.base_r, self.base_t = self.calc_basis(rho, cos_theta, 
            np.max([self.coeff_pe.shape[0], self.coeff_time.shape[0]]),
            np.max([self.coeff_pe.shape[1], self.coeff_time.shape[1]]))

    def call_PE(self, vertex):
        # Calculate NPE
        self.get_base(vertex)
        NPE = np.exp(self.base_t[:self.coeff_pe.shape[0]].T @ self.coeff_pe @ self.base_r[:self.coeff_pe.shape[1]])
        return NPE

    def call_Ti(self, vertex, firedPMT):
        # Calculate Ti
        self.get_base(vertex)
        Ti = self.base_t[:self.coeff_time.shape[0], firedPMT].T @ self.coeff_time @ self.base_r[:self.coeff_time.shape[1]]
        return Ti

def likelihood_PE(E, PE_array, expect):
    # Calculate the PE part of the log-likelihood function
    ln_likelihood = PE_array * np.log(expect * E) - expect * E
    return np.sum(ln_likelihood)

def likelihood_Ti(T_i, fired, PE_array, PEt):
    # Calculate the timing part of the log-likelihood function
    ln_likelihood = 0
    NPE = 0
    ln_likelihood += np.sum(likelihood_quantile(PEt[NPE : NPE + PE_array[j]], T_i[i]) for i, j in enumerate(fired))
    NPE += np.sum(PE_array[fired])
    return ln_likelihood

def likelihood_quantile(y, T_i):
    L = (T_i-y) * (y<T_i) * (1-tau) + (y-T_i) * (y>=T_i) * tau
    return - L/ts

def likelihood(vertex, ch, PEt, probe):
    expect = probe.call_PE(vertex)
    PE_array = np.bincount(ch, minlength = chnum)
    PE_part = likelihood_PE(vertex[3], PE_array, expect)
    fired = np.unique(ch)
    Ti = probe.call_Ti(vertex, fired)
    timing_part = likelihood_Ti(Ti + vertex[-1], fired, PE_array, PEt)
    return PE_part + timing_part