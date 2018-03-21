from mrjob.job import MRJob

class MRWordCounter(MRJob):
    data=[]
    length=[]
    val=[]
    def mapper(self, key, line):
            line=line.split(',')
            numline=list(map(int, line))
            self.data.append(sum(numline))
            self.length.append(len(numline))
            yield sum(self.data),sum(self.length)

    def reducer(self, num, values):
            values=float(max(values))
            self.val.append(float(num / values))
            yield "The mean is ",max(self.val)



if __name__ == '__main__':
    MRWordCounter.run()