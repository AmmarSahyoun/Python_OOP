class Statistics:
    def __init__(self, newlist):
        self._newlist = newlist
        self._mu = 0.
        self._variance = 0.
        self.mean()
        self.std()
 