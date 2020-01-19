#!/bin/bash
SRC_DIR="/opt/Everest"
DEST_DIR="/opt/everest_backup/eve_backup"
FILENAME=_$(date +%-Y%-b%-d)-$(date +%-T).tgz
tar --create --gzip --file=$DEST_DIR$FILENAME $SRC_DIR


# SRC_DIR="/opt/Everest/otn"
# DEST_DIR="/opt/otn_backup/otn_backup"
# FILENAME=_$(date +%-Y%-b%-d)-$(date +%-T).tgz
# tar --create --gzip --file=$DEST_DIR$FILENAME $SRC_DIR


# SRC_DIR="/Sattu/coding"
# DEST_DIR="/sattu_backup"
# FILENAME=_$(date +%-Y%-b%-d)-$(date +%-T).tgz
# tar --create --gzip --file=$DEST_DIR$FILENAME $SRC_DIR
