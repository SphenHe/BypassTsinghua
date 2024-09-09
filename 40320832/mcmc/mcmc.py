import tables
from config import *
import accept
import numpy as np

# Reconstruction data_type
class data_type(tables.IsDescription):
    EventID = tables.Int32Col(pos=0)
    step = tables.Int32Col(pos=1)
    x = tables.Float32Col(pos=2)
    y = tables.Float32Col(pos=3)
    z = tables.Float32Col(pos=4)
    E = tables.Float32Col(pos=5)
    t = tables.Float32Col(pos=6)
    Likelihood = tables.Float32Col(pos=7)
    acceptr = tables.Float32Col(pos=8)
    acceptE = tables.Float32Col(pos=9)
    acceptt = tables.Float32Col(pos=10)

def sample(eids, chs, PEts, probe, output):
    # create output table
    h5file = tables.open_file(output, mode="w", title="JNE", filters = tables.Filters(complevel=9))
    group = "/"
    ReconTable = h5file.create_table(group, "Recon", data_type, "Recon")
    recon = ReconTable.row

    for eid, ch, PEt in zip(eids, chs, PEts):
        # convert to np.array
        ch = np.array(ch)
        PEt = np.array(PEt)

        # init vertex
        vertex = np.zeros(vertex_dim)
        vertex[3] = 1
        likelihood_vertex = accept.likelihood(vertex, ch, PEt, probe)

        # generate random number
        np.random.seed(eid)
        u_perturb = np.random.uniform(-1, 1, (mc_step, vertex_dim))
        u_accept = np.random.uniform(0, 1, (mc_step, gibbs_dim))

        # Gibbs iteration
        for step in range(mc_step):
            # record step
            recon['EventID'] = eid
            recon['step'] = step

            # r iteration
            perturbation = np.zeros(vertex_dim)
            perturbation[:3] = r_step * u_perturb[step, :3]
            vertex_r = np.add(vertex, perturbation)
            # geometric boundary
            if np.sum(vertex_r[:3] ** 2) < 1:
                likelihood_r = accept.likelihood(vertex_r, ch, PEt, probe)
                if likelihood_r - likelihood_vertex > np.log(u_accept[step, 0]):
                    vertex = vertex_r
                    likelihood_vertex = likelihood_r
                    recon['acceptr'] = 1

            # E iteration
            perturbation = np.zeros(vertex_dim)
            perturbation[3] = E_step * u_perturb[step, 3]
            vertex_E = np.add(vertex, perturbation)
            # positive E
            if vertex_E[3] > 0:
                likelihood_E = accept.likelihood(vertex_E, ch, PEt, probe)
                if likelihood_E - likelihood_vertex > np.log(u_accept[step, 1]):
                    vertex = vertex_E
                    likelihood_vertex = likelihood_E
                    recon['acceptE'] = 1

            # t iteration
            perturbation = np.zeros(vertex_dim)
            perturbation[4] = t_step * u_perturb[step, 4]
            vertex_t = np.add(vertex, perturbation)
            likelihood_t = accept.likelihood(vertex_t, ch, PEt, probe)
            if likelihood_t - likelihood_vertex > np.log(u_accept[step, 2]):
                vertex = vertex_t
                likelihood_vertex = likelihood_t
                recon['acceptt'] = 1

            # record sampling
            recon['x'], recon['y'], recon['z'], recon['E'], recon['t'] = vertex
            recon['Likelihood'] = likelihood_vertex
            recon.append()

    # close table
    ReconTable.flush()
    h5file.close()


