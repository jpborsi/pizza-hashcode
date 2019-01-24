'''
Created on Jan 24, 2019

@author: john.borsi
'''
from abc import ABCMeta, abstractmethod

class Solver(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_solution(self, problem):
        raise NotImplementedError