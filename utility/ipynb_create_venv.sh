#!/usr/bin/env bash

VENVNAME=cv101 

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

pip install ipython
pip install jupyter

python -m ipykernel install --user --name=$VENVNAME

test -f requirements.txt && pip install requirements.txt

deactivate
echo "build $VENVNAME"