.PHONY: all

all: figures.pdf

.PHONY: test

test: figures.pdf test.pdf

.PHONY: clean

clean:
	rm -f data.h5
	rm -f figures.pdf
	rm -f test.pdf

data.h5: geo.h5
	python3 simulate.py -n 400 -g $^ -o $@

figures.pdf: data.h5 geo.h5
	python3 draw.py $< -g $(word 2,$^) -o $@

test.pdf: data.h5 geo.h5
	python3 test.py $< -g $(word 2,$^) -o $@

.SECONDARY:
