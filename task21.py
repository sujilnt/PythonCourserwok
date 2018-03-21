from mrjob.job import MRJob

class MRWordCounter(MRJob):
    def mapper(self, key, line):
            yield 0,max(line)

    def reducer(self, num, values):
        yield 0, max(values)


if __name__ == '__main__':
    MRWordCounter.run()