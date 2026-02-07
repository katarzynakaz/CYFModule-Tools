#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt with one change:
# If a line starts with a number and a space, make the line instead end with a space and the number.
# So line 6 which currently reads "37 Alisha" should instead read "Alisha 37".
# The output should contain 11 lines.

# --regexp-extended for less slashes
sed '/^[0-9]\+ / s/^\([0-9]\+\) \(.*\)/\2 \1/' input.txt

sed 's|^\([0-9]*\) \(.*\)|\2 \1|' input.txt
sed 's#^\([0-9][0-9]*\) \(.*\)#\2 \1#' input.txt

# s/ pattern / replacement / if global
# so

# [^ ] match any not spaces
# ^start of line
# \([0-9]*\ all occurances at start of line
# \2 \1 swap order
sed -E 's/^([0-9]+) (.*)$/\2 \1/' input.txt
# -E to avoid escape and use +