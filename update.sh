#!/bin/bash

date > updated.txt

git fetch
git reset origin/master --hard
git pull