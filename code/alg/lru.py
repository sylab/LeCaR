from .lib.dequedict import DequeDict


class LRU:
    class LRU_Entry:
        def __init__(self, oblock):
            self.oblock = oblock

        def __repr__(self):
            return "(o={})".format(self.oblock)

    def __init__(self, cache_size, **kwargs):
        self.cache_size = cache_size
        self.lru = DequeDict()

        self.time = 0

    def __contains__(self, oblock):
        return oblock in self.lru

    def cacheFull(self):
        return len(self.lru) == self.cache_size

    def addToCache(self, oblock):
        x = self.LRU_Entry(oblock)
        self.lru[oblock] = x

    def hit(self, oblock):
        x = self.lru[oblock]
        self.lru[oblock] = x

    def evict(self):
        lru = self.lru.popFirst()
        return lru.oblock

    def miss(self, oblock):
        evicted = None

        if len(self.lru) == self.cache_size:
            evicted = self.evict()
        self.addToCache(oblock)

        return evicted

    def request(self, oblock):
        miss = True
        evicted = None

        self.time += 1

        if oblock in self:
            miss = False
            self.hit(oblock)
        else:
            evicted = self.miss(oblock)

        return miss, evicted
