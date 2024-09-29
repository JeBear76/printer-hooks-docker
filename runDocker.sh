docker build -t printer-webhooks .
docker image prune -f
docker run --rm -it -v ./audio:/usr/src/app/audio --mount type=bind,source=/mnt/wslg/PulseServer,target=/mnt/wslg/PulseServer -e PULSE_SERVER=unix:/mnt/wslg/PulseServer -e DEEPGRAM_API_KEY=$DEEPGRAM_API_KEY -p 80:5000 printer-webhooks  