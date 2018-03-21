from mrjob.job import MRJob

class MRWordCounter(MRJob):
    def mapper(self, key, line):
            listing=[]
            line=line.split(',')
            numline=list(map(int, line))
            listing.append(sum(numline))
            yield sum(numline),len(numline)

    def reducer(self, num, values):
            yield num,sum(values)



if __name__ == '__main__':
    MRWordCounter.run()