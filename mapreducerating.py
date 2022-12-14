# -*- coding: utf-8 -*-
"""mapreducerating.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15y3nUKvdUOa5MA6m4O0GC5GGmKdm2DT4
"""

from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings)
        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('::')
        yield movieID, 1
 def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('::')
        yield rating, 1

        
    def reducer_count_ratings(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    RatingsBreakdown.run()
    
  
