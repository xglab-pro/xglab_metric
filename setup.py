from setuptools import setup, find_packages

setup(name='xglab_metric',
      version='1.0.1',
      description='Abstractions library for 3rd party metrics development at xglab.pro',
      url='https://github.com/xglab-pro/xglab_metric',
      author='Egor Gumin',
      author_email='',
      license='Unlicensed',
      packages=find_packages(),
      install_requires=['StrEnum==0.4.9'],
      zip_safe=False,
      include_package_data=True
      )
