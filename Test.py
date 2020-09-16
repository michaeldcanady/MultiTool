import glob
import os
results = glob.glob('Options/**/*.exe', recursive=True)
options = {k.split(".")[0].lower():False for k in results}
print("\n".join(["[x] "+name if bool == True else "[ ] "+name for name,bool in options.items()]))
