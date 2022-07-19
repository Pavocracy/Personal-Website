#!/usr/bin/env bash

date >> updated.txt

git fetch
git reset origin/master --hard
git pull

pip3 install -r requirements.txt
