all: data/tvE100.h5

clean:
	rm -f data/tvE10.h5 
	rm -f data/tvE100.h5 

# MCMC sampling
data/tvE100.h5: data/Entries100.h5 data/PE.h5 data/Time.h5 data/PMT.txt
	time python3 main.py -i $< -o $@ --pe $(word 2, $^) --time $(word 3, $^) --pmt $(word 4, $^)

# test on small dataset
data/tvE10.h5: data/Entries10.h5 data/PE.h5 data/Time.h5 data/PMT.txt
	time python3 main.py -i $< -o $@ --pe $(word 2, $^) --time $(word 3, $^) --pmt $(word 4, $^)

# Check sampling results for correctness, code execution timing
check: 
	python3 check.py

.DELETE_ON_ERROR:
.SECONDARY:
