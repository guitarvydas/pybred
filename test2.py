import subprocess
s='test 2a from string'
p = subprocess.run(["cat"], input=s,capture_output=True, text=True)
if (0 == p.returncode):
    print (p.stdout)
else:
    print (f'ERROR: {p.returncode}')
    print (p.stderr)
