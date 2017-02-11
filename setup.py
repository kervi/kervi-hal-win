import distutils
from setuptools import setup
from kervi_hal_win.version import VERSION

try:
    distutils.dir_util.remove_tree("dist")
except:
    pass

setup(
    name='kervi-hal-win',
    version=VERSION,
    packages=[
        "kervi_hal_win",
    ],
    install_requires=[
        'psutil'
    ],

)