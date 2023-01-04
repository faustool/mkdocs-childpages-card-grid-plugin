#!/bin/bash

RELEASE_VERSION=$1

if test "$RELEASE_VERSION" == ""; then
    echo "Usage: create_release.sh [release_version]"
    echo "Missing [release_version] argument..."
    exit 1
fi

CHANGE_COUNT=$(git status --porcelain | wc -l)

if test $CHANGE_COUNT -gt 0; then
    echo "There are pending changes that need to be commited"
    exit 1
fi



echo $RELEASE_VERSION > VERSION