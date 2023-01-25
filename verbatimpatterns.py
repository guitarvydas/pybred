import subprocess
import sys
import os

from leaf import Leaf

class VerbatimPatterns (Leaf):
    def __handler__ (self, message):
        if ('in' == message.port):
            bdir = os.path.realpath ('')
            ohmfilename = f'{bdir}/pattern.ohm'
            fabfilename = f'{bdir}/pattern.fab'
            self.send (xfrom=self, portname='ohm', data=ohmfilename, cause=message)
            self.send (xfrom=self, portname='fab', data=fabfilename, cause=message)
        else:
            self.unhandledPort (message)
