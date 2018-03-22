from mrjob.job import MRJob

class MRWordCounter(MRJob):
    def mapper(self, key, line):
            line=line.split(',')
            numline=list(map(int, line))
            yield 0,max(numline)

    def reducer(self, num, values):
            numline = list(map(int, values))
            maxline=list(numline)
            yield "The max value is ", max(maxline)



if __name__ == '__main__':
    MRWordCounter.run()