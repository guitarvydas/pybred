import subprocess
import sys
import os

from leaf import Leaf

class GenerateFabSpec (Leaf):
    def __handler__ (self, message):
        if ('go' == message.port):
            bdir = '.'
            support=f'{bdir}/support.js'
            cmd = [f'{bdir}/fab/fab', f'{bdir}/bred.ohm', f'{bdir}/bredfab.fab', support]
            p = subprocess.run (cmd,input=self.src,capture_output=True,universal_newlines=True)
            if ('' != p.stderr):
                print ('INTERNAL ERROR 4')
                sys.exit (p.stderr)
            self.send (xfrom=self, portname='out', data=p.stdout, cause=message)
            self.send (xfrom=self, portname='next', data=True, cause=message)
        elif ('in' == message.port):
            self.src = message.data
        else:
            self.unhandledPort (message)
