#!/bin/bash

for i in $(seq 1 5); do
  ./std/builddir/fluid_std ./input.$i.json ./ans.$i.hdf5 ./animation.$i.gif
done
