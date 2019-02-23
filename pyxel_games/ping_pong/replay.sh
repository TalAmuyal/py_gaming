#! /bin/bash

fswatch -or . | xargs -n1 pipenv run python ./src

