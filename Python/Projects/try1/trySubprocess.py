#-*- code: utf-8 -*-
import subprocess, time

booksPath = "/home/ydrazel/Belgeler/Books/Python/Think Python-cropped.pdf"
p1 = subprocess.Popen(["tmux", "-c", "attach"], shell=True)
#time.sleep(3)
#subprocess.Popen("exit 1", shell=True, check=True)
p2 = subprocess.Popen(["zathura", f"{booksPath}"])

p1.wait()
p2.wait()
