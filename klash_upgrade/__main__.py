# -*- coding: utf-8 -*-

import os
import sys

base_dir = os.path.dirname(__file__)
sys.path.insert(0, base_dir)

from . import main


if __name__ == "__main__":
    main()
