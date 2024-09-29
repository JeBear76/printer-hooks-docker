# Printer Hooks Docker

This project sets up a Docker environment for managing printer hooks. It allows you to easily deploy and manage printer hooks using Docker containers.

## Table of Contents
- [Installation](#installation)
- [Installing PulseAudio on Windows](#Installing%20PulseAudio%20on%20Windows)
- [Usage](#usage)
- [License](#license)

## Installing PulseAudio on Windows
[follow these instructions](https://gist.github.com/Stormwind99/e5ffc026a44ec2374f92864652d94854)  

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/jebear76/printer-hooks-docker.git
    cd printer-hooks-docker
    ```  

3. Setup your DeepGram API Key (optional)  
    ```
        echo DEEPGRAM_API_KEY=<your key> > .env
        source .env
    ```  

3. Run the docker run script:
    ```sh
    . ./runDocker.sh
    ```  

## Usage

Configure your Octopi Webhooks

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.