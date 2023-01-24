import subprocess
import sys
import os

from leaf import Leaf

class GenerateBoilerPlate (Leaf):
    def __handler__ (self, message):
        if ('in' == message.port):
            bdir = os.path.realpath ('')
            nullsupport=f'{bdir}/nullsupport.js'
            src = message.data
            cmd = [f'{bdir}/fab/fab', f'{bdir}/bred.ohm', f'{bdir}/bredohm1.fab', nullsupport]
            print ('BOILERPLATE')
            print (cmd)
            p = subprocess.run (cmd,input=src,capture_output=True,universal_newlines=True)
            if ('' != p.stderr):
                print ('INTERNAL ERROR 1')
                sys.exit (p.stderr)
            self.send (xfrom=self, portname='out', data=p.stdout, cause=message)
            self.send (xfrom=self, portname='next', data=True, cause=message)
        else:
            self.unhandledPort (message)
                
        
