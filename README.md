# Printer Hooks Docker

This project sets up a Docker environment for managing printer hooks. It allows you to easily deploy and manage printer hooks using Docker containers.

This project requires Docker Desktop running on WSL2.  
A WSL2 Ubuntu 24.04 VM. I use the Microsoft Store one.  
OctoPrint and the OctoPrint-Webhooks plugin.  
I use DeepGram to generate the audio. If you don't provide the image with a DEEPGRAM_API_KEY, it'll use default wav files. Otherwise, it'll build a new text based on the DEVICE IDENTIFIER and topic is receives, send that to DeepGram and save the file in the _audio_ folder.  This only happens once.

## Table of Contents
- [Installation](#installation)
- [Installing PulseAudio on Windows](#Installing%20PulseAudio%20on%20Windows)
- [Usage](#usage)
- [License](#license)

## Installing PulseAudio on Windows
[follow these instructions](https://gist.github.com/Stormwind99/e5ffc026a44ec2374f92864652d94854)  

## Installation

### Using DockerHub
1. Pull the image.
```
docker push jerepondumie/printer-webhooks:latest
```
2. Create an empty _audio_ folder somewhere.

3. Run the container.  
```
# Windows WSL2 (Example)
docker run \
    -d \
    -v ./audio:/usr/src/app/audio \
    --mount type=bind,source=/mnt/wslg/PulseServer,target=/mnt/wslg/PulseServer \
    -e HOST_NAME=$(hostname) \
    -e PULSE_SERVER=unix:/mnt/wslg/PulseServer \
    -e DEEPGRAM_API_KEY=$DEEPGRAM_API_KEY \
    -p 80:5000 \
    jerepondumie/printer-webhooks
```

```
# Ubuntu 24.04 (Example)
docker run \
    -d \
    --restart=always \
    -v ./audio:/usr/src/app/audio \
    --mount type=bind,source=/run/user/1000/pulse/native,target=/run/user/1000/pulse/native \
    -e HOST_NAME=$(hostname) \
    -e PULSE_SERVER=unix:/run/user/1000/pulse/native \
    -e DEEPGRAM_API_KEY=<YOUR_DEEPGRAM_KEY> \
    -p 80:5000 \
    jerepondumie/printer-webhooks
```

### Manual
1. Clone the repository:
    ```sh
    git clone https://github.com/jebear76/printer-hooks-docker.git
    cd printer-hooks-docker
    ```  
2. Create an empty _audio_ folder in the solution.  

3. Setup your DeepGram API Key (optional)  
    ```
        echo DEEPGRAM_API_KEY=<YOUR_DEEPGRAM_KEY> > .env
        source .env
    ```  

3. Run the docker run script:
    ```sh
    . ./runDocker.sh
    ```  

By default, the _runDocker.sh_ script exposes the api on port 80 of the host.
You can go to http://localhost

## Usage

Configure your Octopi Webhooks.  
For this, the writer of the [OctoPrint-Webhooks](https://github.com/derekantrican/OctoPrint-Webhooks) wrote a README.

You can add a specific voice for the printer in the DATA json under _Advanced_.
For example.  
```
{
  "deviceIdentifier":"@deviceIdentifier",
  "apiSecret":"@apiSecret",
  "topic":"@topic",
  "message":"@message",
  "extra":"@extra",
  "voice":"aura-asteria-en"
}
```

A full list of the deepGram voice models is available [here](https://developers.deepgram.com/docs/tts-models)

## DeepGram Config

You can change the default voice for the DeepGram API in the config.json.  
I created the class for another project. The other 2 config settings are useless in this one.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.