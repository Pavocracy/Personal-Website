#!/bin/bash

while getopts 'dp' flag; do
  case "${flag}" in
    d)
        export FLASK_ENV=development
        echo "FLASK_ENV set to" $FLASK_ENV
        python3 app.py ;;
    p)
        export FLASK_ENV=production
        echo "FLASK_ENV set to" $FLASK_ENV
        uwsgi uwsgi.ini ;;
  esac
done
