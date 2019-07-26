# A little repository to get motioneye work with a Raspberry Pi Zero, a Raspberry Cam and Docker

## Download a HypriotOS image and burn it on a SD card

* [HypriotOS](https://blog.hypriot.com/downloads/)
* [Some FAQ to help](https://blog.hypriot.com/faq/)

## Installation

This tutorial is using a modified version of Calin Crisan docker file :

* [Calin Crison MotionEye GitHub](https://github.com/ccrisan/motioneye)
* [Initial docker file](https://github.com/ccrisan/motioneye/blob/dev/extra/Dockerfile.armv7-armhf)

I recommend you to read his Wiki about how to configure MotionEye for more information

* [MotionEye Wiki](https://github.com/ccrisan/motioneye/wiki)

### How to :

1.  Create the following folder (adapt with your linux home)

```bash
mkdir -p /home/fred/applications/motioneye
mkdir -p /home/fred/applications/motioneye/conf
mkdir -p /home/fred/applications/motioneye/data
```

2. Git clone ccrisan motioneye repository

```bash
git clone -b dev https://github.com/ccrisan/motioneye.git
```

3. Enter project folder

```
 cd motioneye
```
     
 # If you would like build docker image from official project
 docker build --build-arg VCS_REF=$(git rev-parse HEAD) --build-arg BUILD_DATE=$(date +"%Y-%m-%dT%H:%M:%SZ") -t ccrisan/motioneye:master-amd64 -f extra/Dockerfile .