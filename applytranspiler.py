from leaf import Leaf

class GenerateFabSpec (Leaf):
    def __handler__ (self, message):
        if ('go' == data.port):
            bdir = '.'
            nullsupport=f'{bdir}/nullsupport.js'
            fname='pattern'
            # # apply matcher/replacer to source
            # #${bdir}/bred-apply.bash ${fname} ${bdir}
            # # run the nano-transpiler
            # ${bdir}/fab/fab - NestingGrammar ${fname}.ohm ${fname}.fab
            srcHardWired='hard-wired: f (int x) { a = b; }'
            ## note: fab requires filenames not text
            ohmFname = fname + '.ohm'
            fabFname = fname + '.fab'
            with open (ohmFname, 'w') as f:
                f.write (generatedOhm)
            with open (fabFname, 'w') as f:
                f.write (generatedFab)
            cmd = [f'{bdir}/fab/fab', '-', f'{ohmFname}', f'{fabFname}', nullsupport]
            p = subprocess.run (cmd,input=self.src,capture_output=True,universal_newlines=True)
            if ('' != p.stderr):
                print ('INTERNAL ERROR 5')
                sys.exit (p.stderr)
            self.send (xfrom=self, portname='out', data=p.stdout, cause=message)
            self.send (xfrom=self, portname='next', data=True, cause=message)
        elif ('in' == data.port):
            self.src = data.message
        else:
            self.unhandledPort (message)
