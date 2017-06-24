# to package
# run $ python setup.py sdist
from distutils.core import setup

setup(
    name='ExpenseManager',
    version='0.1dev',
    packages=['expensemanager',],
    license='MIT Open Licence',
    long_description=open('README.md').read(),
)
