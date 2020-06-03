import numpy as np

CACHE_SIZE = 50
PHASE_SIZE = 5000
NUM_PHASES = 5
UNIVERSE_SIZE = 2000
WORKING_SET_SIZE = 30
WS_DELTA = 0.90

if __name__ == "__main__" :
    np.random.seed(123)
    other = np.arange(0,UNIVERSE_SIZE, dtype=np.int32)
    workingSet = np.array([], dtype=np.int32)
    
    eps = 0.5
    for i in range(0, NUM_PHASES) :
        
        ## Remove a proportion WS_DELTA from the workingSet
        workingSet = np.random.choice(UNIVERSE_SIZE, WORKING_SET_SIZE, replace=False)
                
        for _ in range(0, PHASE_SIZE) :
        
            if np.random.rand() < WS_DELTA :
                q = np.random.choice(workingSet, 1)
            else:
                q = np.random.choice(UNIVERSE_SIZE, 1)
            print (int(q)) 
