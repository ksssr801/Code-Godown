#!/bin/bash
SRC_DIR="path/to/source"
DEST_DIR="path/to/destination"
FILENAME=_$(date +%-Y%-b%-d)-$(date +%-T).tgz
tar --create --gzip --file=$DEST_DIR$FILENAME $SRC_DIR


# SRC_DIR="/Sattu/coding"
# DEST_DIR="/sattu_backup"
# FILENAME=_$(date +%-Y%-b%-d)-$(date +%-T).tgz
# tar --create --gzip --file=$DEST_DIR$FILENAME $SRC_DIR
