# Testing an issue in Docker

Do requests made from one Docker container to another on a Docker Machine behave the same as requests made from one Docker container to a server on the host?

SO: https://stackoverflow.com/questions/37889960/moving-app-to-docker-from-host-increases-http-lag-by-5-seconds

## Setup

```
brew update
brew reinstall docker docker-machine docker-compose
docker-machine create default --driver virtualbox
```

## Testing within machine

You need to communicate to a server running in a separate container on the same host OS.

First, get the server up, since it takes time to start up.

```
docker-compose -f within-machine.yml build
docker-compose -f within-machine.yml up -d server
```

Then, run the emitter.

```
docker-compose -f within-machine.yml up emitter
```

Results:

```
dockerprob_server_1 is up-to-date
Recreating dockerprob_emitter_1
Attaching to dockerprob_emitter_1
emitter_1  |
emitter_1  | Total Time:  0.008154
dockerprob_emitter_1 exited with code 0
```

## Testing across machine

You need to communicate to a server running on the host OS from within a container on a Docker Machine.

In one terminal on the host machine,

```
pip3 install -r requirements.txt # `brew update && brew install python3` to get pip3
hug -f server.py -p 8002
```

In another terminal, first provide SERVER_URL. Here, I'm assuming you're on a mac, figure out how to provide `hostip` on your own machine if it's different.

```
alias hostip='ifconfig en0 | grep "inet\ " | cut -d: -f2 | cut -d" " -f2'
export SERVER_URL="http://`hostip`:8002"
```

Now, you're ready to build and run the emitter.


```
docker-compose -f across-machine.yml build
docker-compose -f across-machine.yml up emitter
```

Results:

```
Recreating dockerprob_emitter_1
Attaching to dockerprob_emitter_1
emitter_1  |
emitter_1  | Total Time:  0.017632
dockerprob_emitter_1 exited with code 0
```

## My system

```
OS X 10.11.5
VBoxManage version: 5.0.22r108108
Docker version 1.11.2, build b9f10c9
docker-compose version 1.7.1, build unknown
docker-machine version 0.7.0, build a650a40
```

