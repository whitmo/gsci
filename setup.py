from setuptools import setup

version = '0.1'

setup(name='gsci',
      version=version,
      description="A script to git svn clone and install a package in one cmd",
      long_description=open("README.rst").read(),
      classifiers=[], 
      keywords='',
      author='whit',
      author_email='',
      url='',
      license='',
      py_modules=['gsci'],
      include_package_data=True,
      zip_safe=True,
      install_requires=['fabric',
                        'path.py',
                        ],
      entry_points="""
      [console_scripts]
      gsci=gsci:main
      """,
      )
