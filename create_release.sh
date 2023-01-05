#!/bin/bash

RELEASE_VERSION=$1

if test "$RELEASE_VERSION" == ""; then
    echo "Usage: create_release.sh [release_version]"
    echo "Missing [release_version] argument..."
    exit 1
fi

SOURCE_BRANCH="develop"
RELEASE_BRANCH="release-${RELEASE_VERSION}"

git checkout -b $RELEASE_BRANCH $SOURCE_BRANCH
echo $RELEASE_VERSION > VERSION
git commit -a -m "Bumped version number to ${RELEASE_VERSION}"
git push -u origin $RELEASE_BRANCH