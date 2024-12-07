#!/bin/bash
docker run -d --name qualitycontrol -e LOGIN="mahanairlines.com@gmail.com" --device=/dev/net/tun --cap-add=NET_ADMIN --cap-add=NET_RAW --cap-add=SYS_ADMIN --log-opt max-size=10m --log-opt max-file=3 --restart=always ghcr.io/org004/qc:latest
sleep 20
docker run --detach \
    --name watchtower \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower
