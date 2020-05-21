#!/bin/bash
set -e

VENV_PATH=env

command -v python3 > /dev/null 2>&1 || { echo >&2 "Python3 is required but it isn't available. Aborting..."; exit 1; }

python3 -m venv "${VENV_PATH}"
source "${VENV_PATH}"/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
deactivate


echo ""
echo ""
echo "Setup finished! To activate the new Python venv type:"
echo ""
echo -e "    $ source ${VENV_PATH}/bin/activate"
echo ""