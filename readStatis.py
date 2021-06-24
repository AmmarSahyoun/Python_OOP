import os, math

class Statistics:
    def __init__(self, path):
        self.path = path
        self._newData = []
        self._separator = ''
        self._mu = 0
        self.separator()

    def read(self):
        with open(self.path, 'r') as file:
            myData = [line.rstrip().split(self._separator) for line in file.readlines()]
            for x in myData:
                for y in x:
                    self._newData.append(float(y))
        self.mean()

    def count_different(self):
        _ = set(self._newData)
        print(f"The count of unduplicated intgers are: {len(_)}")

    def count_occurrences(self):
        D = {}
        {int(_): 1 if int(_) not in D and not D.update({int(_): 1})
        else D[int(_)] + 1 if not D.update({int(_): D[int(_)] + 1}) else 1 for _ in self._newData}
        print("The frequency of the numbers: \n", D)

    def mean(self):
        self.count_different()
        self._mu = sum(self._newData) / len(self._newData)
        print("The mean: ", round(self._mu, 4))
        self.std()

    def std(self):
        w = [(i - self._mu) ** 2 for i in self._newData]
        variance = (1 / len(self._newData)) * sum(w)
        print("std: ", round(math.sqrt(variance), 4), '\n')
        self.count_occurrences()

    def separator(self):
        if os.path.exists(self.path):
            file = open(self.path)
            if ',' in file.read():
                self._separator = ','
            else:
                self._separator = ':'
            file.close()
            self.read()
        else:
            print('No file Found!')

letsGo_A = Statistics('file_10000integers_A.txt')
# https://www.mathsisfun.com/data/standard-deviation-formulas.html