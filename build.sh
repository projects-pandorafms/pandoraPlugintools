python3 -m pip install --upgrade pip
python3 setup.py sdist
pip3 install twine
twine upload dist/*

