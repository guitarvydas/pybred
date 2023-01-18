import subprocess
#p = subprocess.run(["ls", "-l", "/dev/null"], capture_output=True, universal_newlines=True)
p = subprocess.run(["ls", "--noname", "/dev/null"], capture_output=True, universal_newlines=True)
if (0 == p.returncode):
    print (p.stdout)
else:
    print (f'ERROR: {p.returncode}')
    print (p.stderr)
