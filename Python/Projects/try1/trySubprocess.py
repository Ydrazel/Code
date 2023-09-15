#-*- code: utf-8 -*-
import subprocess, time

booksPath = "/home/ydrazel/Belgeler/Books/Python/Think Python-cropped.pdf"
subprocess.run(["tmux", "-c", "attach"], shell=True)
#time.sleep(3)
#subprocess.run("exit 1", shell=True, check=True)
subprocess.run(["zathura", f"{booksPath}"])
