# ------ Import necessary packages ----
#import networkx as nx
#from collections import defaultdict
#from itertools import combinations
#import math
from dwave.system import DWaveSampler, EmbeddingComposite
sampler_auto = EmbeddingComposite(DWaveSampler(solver={'topology__type': 'chimera'}))

# Set Q matrix
linear = {('a', 'a'): -1, ('b', 'b'): -1, ('c', 'c'): -1}
quadratic = {('a', 'b'): 2, ('b', 'c'): 2, ('a', 'c'): 2}
Q = {**linear, **quadratic}

#Run QUBO on QPU
sampleset = sampler_auto.sample_qubo(Q, num_reads=1000)

#Solution
print(sampleset)

