#!/bin/bash

set -euo pipefail

echo "${1:?}" > vinculum/VERSION

rm -rf dist
python setup.py bdist_wheel
rm -rf build
