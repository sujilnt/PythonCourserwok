from mrjob.job import MRJob

class MRWordCounter(MRJob):
    def mapper(self, key, line):
            line=line.split(',')
            numline=list(map(int, line))
            print sum(numline), len(numline)
            yield sum(numline),len(numline)

    def reducer(self, num, values):
            print num,values, num/values
            pass
            yield 0, max(maxline)



if __name__ == '__main__':
    MRWordCounter.run()