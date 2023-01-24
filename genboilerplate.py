from leaf import Leaf

class GenerateBoilerPlate (Leaf):
    def __handler__ (self, message):
        if ('in' == data.port):
            bdir = '.'
            nullsupport=f'{bdir}/nullsupport.js'
            src = message.data
            cmd = [f'{bdir}/fab/fab', f'{bdir}/bred.ohm', f'{bdir}/bredohm1.fab', nullsupport]
            p = subprocess.run (cmd,input=src,capture_output=True,universal_newlines=True)
            if ('' != p.stderr):
                print ('INTERNAL ERROR 1')
                sys.exit (p.stderr)
            self.send (xfrom=self, portname='out', data=p.stdout, cause=message)
            self.send (xfrom=self, portname='next', data=True, cause=message)
        else:
            self.unhandledPort (message)
                
        
