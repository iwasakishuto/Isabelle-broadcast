#!/bin/zsh
# chmod +x main.sh
# zsh ./main.sh

ISABEL_BASE_DIR=$(cd $(dirname $0); pwd)
python3 ${ISABEL_BASE_DIR}/main.py
imgcat ${ISABEL_BASE_DIR}/Isabelle-broadcast.png
rm ${ISABEL_BASE_DIR}/Isabelle-broadcast.png
