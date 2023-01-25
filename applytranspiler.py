import subprocess
import sys
import os

from leaf import Leaf

class ApplyTranspiler (Leaf):
    def __handler__ (self, message):
        if ('in' == message.port):
            self.src = message.data
            bdir = os.path.realpath ('')
            nullsupport=f'{bdir}/nullsupport.js'
            fname='pattern'
            # # apply matcher/replacer to source
            # #${bdir}/bred-apply.bash ${fname} ${bdir}
            # # run the nano-transpiler
            # ${bdir}/fab/fab - NestingGrammar ${fname}.ohm ${fname}.fab
            ## note: fab requires filenames not text
            ohmFname = fname + '.ohm'
            fabFname = fname + '.fab'
            with open (ohmFname, 'w') as f:
                f.write (self.generatedOhm)
            with open (fabFname, 'w') as f:
                f.write (self.generatedFab)
            cmd = [f'{bdir}/fab/fab', f'{ohmFname}', f'{fabFname}', nullsupport]
            p = subprocess.run (cmd,input=self.src,capture_output=True,universal_newlines=True)
            if ('' != p.stderr):
                print ('INTERNAL ERROR 5')
                sys.exit (p.stderr)
            s = p.stdout.rstrip ()
            self.send (xfrom=self, portname='out', data=s, cause=message)
            self.send (xfrom=self, portname='next', data=True, cause=message)
        elif ('ohm' == message.port):
            try:
                self.generatedOhm = self.generatedOhm + message.data
            except:
                self.generatedOhm = message.data
        elif ('fab' == message.port):
            try:
                self.generatedFab = self.generatedFab + message.data
            except:
                self.generatedFab = message.data
        else:
            self.unhandledPort (message)
