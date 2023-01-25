import subprocess
import sys
import os

from leaf import Leaf

def fetchFromFile (filename):
  with open (filename, 'r') as f:
    r = f.read ()
    return r

class VerbatimPatterns (Leaf):
    def __handler__ (self, message):
        if ('in' == message.port):
            bdir = os.path.realpath ('')
            ohmfilename = f'{bdir}/pattern.ohm'
            fabfilename = f'{bdir}/pattern.fab'
            ohmspec = fetchFromFile (ohmfilename)
            fabspec = fetchFromFile (fabfilename)
            self.send (xfrom=self, portname='ohm', data=ohmspec, cause=message)
            self.send (xfrom=self, portname='fab', data=fabspec, cause=message)
        else:
            self.unhandledPort (message)
