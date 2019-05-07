#!/bin/bash
echo reset
echo cd to djangodemo directory
cd djangodemo
echo installing twine
pip install twine
echo creating distribution
python setup.py sdist
echo upload archive to nexusRepo repository
twine upload -r nexusRepo dist/*.gz
