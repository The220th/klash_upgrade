# -*- coding: utf-8 -*-

import time
import random
import numpy as np
from colorama import Fore, Back, Style, init
from tqdm import tqdm
import os
import sys

base_dir = os.path.dirname(__file__)
sys.path.insert(0, base_dir)

from .process import *


init(autoreset=True)

def main():
    input("Input device what you need to upgrade (check it by typing \"lspci\" for example): ")

    print("\n\n\tAny interruption of the process could result in a non-functional system!!!\n"
          "\tMake sure the connection is stable and the electricity does not turn off during the process. \n\n")

    input("Press \"Enter\" to continue...")

    print("Getting blobs...")
    for _ in tqdm(range(random.randint(50, 1000))):
        if random.randint(1, 500) <= 3:
            time.sleep(random.randint(1000, 5000)/1000)
            print(f"HTTP requests failed (return status={random.randint(396, 440)})! Are your internet connection is established?")
        time.sleep(random.randint(1, 15)/1000)

    print("Flashing... It may take some time. Please wait and do not interrupt the process. ")
    flashing_process()


if __name__ == "__main__":
    main()
