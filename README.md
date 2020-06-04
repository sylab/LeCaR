#### Driving Cache Replacement with ML-based LeCaR

LeCaR is ML-based algorithm that uses reinforcement learning and regret minimization to model the cache replacement problem. LeCaR relies only on two fundamental policies: recency-based and frequency-based evictions. Each policy has an assigned weight (probability distribution) that is learned based on wrong decisions. LeCaR achieves good performance when cache sizes are small relative to the working set.

More details about this work can be found in the link to the paper:
[LeCaR HotStorage'18 (PDF)](https://www.usenix.org/system/files/conference/hotstorage18/hotstorage18-paper-vietri.pdf)

Citation:

    @inproceedings {216890,
    author = {Giuseppe Vietri and Liana V. Rodriguez and Wendy A. Martinez and Steven Lyons and Jason Liu and Raju Rangaswami and Ming Zhao and Giri Narasimhan},
    title = {Driving Cache Replacement with ML-based LeCaR},
    booktitle = {10th {USENIX} Workshop on Hot Topics in Storage and File Systems (HotStorage 18)},
    year = {2018},
    address = {Boston, MA},
    url = {https://www.usenix.org/conference/hotstorage18/presentation/vietri},
    publisher = {{USENIX} Association},
    month = jul,
    }

#### Code source

The LRU, LFU, ARC and LeCaR implementations can be found in the code/alg folder.
Additional code for data structure implementations are in the code/alg/lib folder. 

To run experiments, the arguments can be modified appropriately with the specific parameters such as cache size, input trace and algorithm name.
Executing the following command inside the code directory will produce the results: 

```python3 run.py <cache_size> <algorithm> <trace_name>```

For instance, running the commands 

```python3 run.py 4 lru data.txt```\
```python3 run.py 4 lfu data.txt```\
```python3 run.py 4 arc data.txt```\
```python3 run.py 4 lecar data.txt```

will produce the following outputs

```Results: lru        size=4        hits=181, misses=319, ios=500, hitrate=36.2%, data.txt```\
```Results: lfu        size=4        hits=132, misses=368, ios=500, hitrate=26.4%, data.txt```\
```Results: arc        size=4        hits=176, misses=324, ios=500, hitrate=35.2%, data.txt```\
```Results: lecar      size=4        hits=183, misses=317, ios=500, hitrate=36.6%, data.txt```

#### Traces

The synthetic trace with 4 phase changes and the source code to generate phase changes in the working set can be found in the /synth-traces folder.

The FIU workloads (day 3) are publicly available on the [SNIA Website](http://iotta.snia.org/tracetypes/3).  
