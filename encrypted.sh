#!/bin/bash

TARGET=~/Documents/git_space/TD_Cronjob/cryptoProject/toCrypt/
PROCESSED=~/Documents/git_space/TD_Cronjob/cryptoProject/crypted/

inotifywait -m -e create -e moved_to --format "%f" $TARGET \
        | while read FILENAME
                do
                        echo Detected $FILENAME, moving and crypting
                        mv "$TARGET/$FILENAME" "$PROCESSED/$FILENAME"
                        python3 ~/Documents/git_space/TD_Cronjob/encrypt.py "$PROCESSED/$FILENAME"
                done
