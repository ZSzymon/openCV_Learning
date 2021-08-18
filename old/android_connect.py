import time
import numpy as np
import random
import os
import string
import glob
from ppadb.client import Client as AdbClient
from settings import BASE_DIR, IMAGES_ROOT

def getScreenShot(device):
    sc = device.screencap()
    return np.array(sc, np.uint8)

def removeAllFilesInDir(path):
    files = glob.glob(path+'/*')
    for f in files:
        os.remove(f)

def saveScreenShot(device):
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    filePath = os.path.join(IMAGES_ROOT, 'screenshots', id_generator() + '.png')

    with open(filePath, 'wb') as fp:
        fp.write(getScreenShot(device))

def connectDevice():
    client = AdbClient(host="127.0.0.1", port=5037)  # Default is "127.0.0.1" and 5037
    devices = client.devices()
    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]
    return device


if __name__ == '__main__':
    device = connectDevice()
    SCREENSHOTDIR = os.path.join(IMAGES_ROOT, 'screenshots')

    removeAllFilesInDir(SCREENSHOTDIR)
    before = time.time()
    for i in range(20):
        sc = saveScreenShot(device)

    after = time.time()

    print("Time: ", after - before)