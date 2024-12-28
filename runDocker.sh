docker build -t printer-webhooks .
docker image prune -f
docker run --rm -it -v ./audio:/usr/src/app/audio --mount type=bind,source=${XDG_RUNTIME_DIR}/pulse/native,target=${XDG_RUNTIME_DIR}/pulse/native -e HOST_NAME=$(hostname) -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -e DEEPGRAM_API_KEY=$DEEPGRAM_API_KEY -p 80:5000 printer-webhooks