#! /usr/bin/python3
# Interface/API

from .lens import SwapLens

class Swap(object):

    def __init__(self):
        self = self
        self.lens = SwapLens()
    #end

    def total(self):
        """
        Total swap space available to the kernel.
        """
        return format(self.lens.get_swap_total(), '.2f')
    #end

    def free(self):
        """
        Unused/free swap space unused by the kernel.
        """
        return format(self.lens.get_swap_free(), '.2f')
    #end

    def used(self):
        """
        Used swap space.
        """
        return format(self.lens.get_swap_used(), '.2f')
    #end
#end
