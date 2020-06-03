from alg.get_algorithm import get_algorithm
import os
import sys
import math

if __name__ == '__main__':
    
    hits = 0
    requests = 0
    
    cache_size = int(sys.argv[1])
    algorithm = sys.argv[2]
    trace_file = sys.argv[3]
    
    if cache_size <= 0:
        print("Cache_size should be greater than 0")
        exit(1)

    alg = get_algorithm(algorithm)(cache_size)
     
    with open(trace_file, 'r') as f:
        for line in f:
            lba = int(line)
            if lba < 0:
                continue
            requests += 1

            miss, evicted = alg.request(lba)

            if not miss:
                hits += 1

        misses = requests - hits
        print("Results: {:<10} size={:<8} hits={}, misses={}, ios={}, hitrate={:4}%, {}"
                .format(algorithm, cache_size, hits, misses, requests,
                round(100 * hits / requests, 2), trace_file))
