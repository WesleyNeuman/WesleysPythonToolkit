from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'My personal Python toolkit'
LONG_DESCRIPTION = "Contains functions I've developed to simplify common tasks for myself"

# Setting up
setup(
    name="WesleysPythonToolkit",
    version=VERSION,
    author="Wesley Neuman",
    author_email="<wgeorgeneuman@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)