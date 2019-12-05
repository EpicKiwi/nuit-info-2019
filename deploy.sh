#!/bin/bash
set -e

echo "checking out latest version"
git pull origin master

VERSION=$(./get_version.sh)
export VERSION
echo "DEPLOYING version $VERSION"

docker build . -t epickiwi/nopls-django
docker build proxy -t epickiwi/nopls-proxy

echo "Starting stack"
docker stack deploy --compose-file docker-compose.yml no-pls

echo "Cleaning old containers"
docker ps | grep "no-pls_" | grep -v "_db" | cut -d' ' -f1 | xargs docker rm -f