class Statistics:
    def __init__(self, newlist):
        self._newlist = newlist
        self._mu = 0.
        self._variance = 0.
        self.mean()
        self.std()
    def mean(self):
        self._mu = sum(self._newlist)/len(self._newlist)
        print("mean: ", self._mu)
        return self._mu
    def std(self):
        w = [(i-self._mu)**2 for i in self._newlist]
        self._variance = (1/len(self._newlist))*sum(w)
        print("std: ", round(math.sqrt(self._variance),4))


letsGo = Statistics(mydata)