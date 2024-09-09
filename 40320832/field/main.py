import data
import field
import sys
import numpy as np

np.set_printoptions(floatmode='unique')


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


EPSILON = 1e-6

f = data.field()
q = data.queries()
d = data.dist()
rho, dBdt = field.compute(f, q, d)
if rho is None or dBdt is None:
    eprint("Error: Not implemented")
    sys.exit(1)

rhoRef, dBdtRef = data.ans()

if rho.shape != rhoRef.shape or dBdt.shape != dBdtRef.shape:
    eprint(
        f"Error: Wrong result shape. Expected {rhoRef.shape}, {dBdtRef.shape}, got {rho.shape}, {dBdt.shape}")
    sys.exit(1)

rhoDiff = np.max(np.abs(rho - rhoRef))
dBdtDiff = np.max(np.abs(dBdt - dBdtRef))

if rhoDiff > np.mean(np.abs(rhoRef) + EPSILON) * EPSILON or dBdtDiff > np.mean(np.abs(dBdtRef) + EPSILON) * EPSILON:
    eprint(f"Error: Significant numerical error: {rhoDiff}, {dBdtDiff}")
    eprint(f"==== Expected result ====")
    eprint(f"> rho")
    eprint(repr(rhoRef))
    eprint(f"> dB/dt ")
    eprint(repr(dBdtRef))

    eprint(f"==== Your result ====")
    eprint(f"> rho")
    eprint(repr(rho))
    eprint(f"> dB/dt ")
    eprint(repr(dBdt))

    sys.exit(1)

else:
    sys.exit(0)
