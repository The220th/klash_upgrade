# coding: utf-8

"""
pip3 install cx_freeze
pip3 install -r requirements.txt
python3 setup.py build
"""

from cx_Freeze import setup, Executable
from klash_upgrade import __version__ as klash_upgrade_version

executables = [Executable('run_klash_upgrade.py')]

zip_include_packages = ['tqdm', "numpy"]

options = {
    'build_exe': {
        'zip_include_packages': zip_include_packages,
        "optimize": 2,
    }
}

setup(name='konciliation',
      version=klash_upgrade_version,
      description='Helps you to upgrade your klash of the driver of needed device by its id ',
      executables=executables,
      options=options)
