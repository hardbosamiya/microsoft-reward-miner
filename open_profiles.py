import subprocess
import time

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

profiles = ["Default"]

for p in profiles:
    subprocess.Popen([
        edge_path,
        f"--profile-directory={p}",
        "https://www.bing.com"
    ])
    
    print(f"Opened Edge with {p}")
    
    time.sleep(8)   # VERY IMPORTANT → wait for profile to load