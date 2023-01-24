from leaf import Leaf

class GenerateLiterals (Leaf):
    def __handler__ (self, message):
        if ('go' == data.port):
            bdir = '.'
            nullsupport=f'{bdir}/nullsupport.js'
            cmd = [f'{bdir}/fab/fab', f'{bdir}/bred.ohm', f'{bdir}/bredohm3.fab', nullsupport]
            p = subprocess.run (cmd,input=src,capture_output=True,universal_newlines=True)
            if ('' != p.stderr):
                print ('INTERNAL ERROR 3')
                sys.exit (p.stderr)
            self.send (xfrom=self, portname='out', data=p.stdout, cause=message)
            self.send (xfrom=self, portname='next', data=True, cause=message)
    elif ('in' == data.port):
            self.src = data.message
        else:
            self.unhandledPort (message)
