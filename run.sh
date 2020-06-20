#!/bin/bash
./bin/server stop
pip install .
buildout
./bin/server start