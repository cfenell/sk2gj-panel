from distutils.core import setup

setup(name='SK2GJ-panel',
      version='0.1',
      description='Antenna control panel with webcam display for rotor controller',
      author='Carl-Fredrik Enell SM2YHP',
      author_email='fredrik@kyla.kiruna.se',
      url='https://www.sk2gj.se',
      py_modules = ['webcam.py'],
      scripts = ['panel.py']
     )
