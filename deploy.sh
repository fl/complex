#!/usr/bin/env bash
#
BOARDS="0 1"
FILELIST="main.py"

for BLINKI in $BOARDS; do
  AMPY_PORT="/dev/ttyS$BLINKI"
  echo "working on $AMPY_PORT ..."

  for FILE in $FILELIST; do
    echo ampy -p AMPY_PORT put $FILE
  done
done
