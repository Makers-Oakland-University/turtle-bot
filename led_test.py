import subprocess
from time import sleep
import os

subprocess.call(["xboxdrv","--led 1"])
sleep(1)
subprocess.call(["xboxdrv","--led 6"])
sleep(1)
subprocess.call(["xboxdrv","--led 8"])
sleep(1)
subprocess.call(["xboxdrv","--led 8"])
sleep(1)
subprocess.call(["xboxdrv","--led 9"])
sleep(1)
subprocess.call(["xboxdrv","--led 10"])
sleep(5)
os.system('pkill xboxdrv')

#subprocess.call(["xboxdrv","--led 10", "--quit"])
#https://pingus.seul.org/~grumbel/xboxdrv/xboxdrv.html