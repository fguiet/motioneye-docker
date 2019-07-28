# Getting motioneye work with a Raspberry Pi Zero, a Raspberry Cam and Docker

## Download a HypriotOS image and burn it on a SD card

* [HypriotOS](https://blog.hypriot.com/downloads/)
* [Some FAQ to help](https://blog.hypriot.com/faq/)

Don't forget to enable the raspberry camera

```bash
sudo raspi-config
````

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
cd /home/fred/applications/motioneye
```

2. Git clone this repository

```bash
git clone https://github.com/fguiet/motioneye-docker.git
```

2. Git clone ccrisan motioneye repository

```bash
git clone -b dev https://github.com/ccrisan/motioneye.git
```

3. Enter project folder, build the docker image and have a cup of coffe (or two..or three...)

```
cd motioneye
docker build --build-arg VCS_REF=$(git rev-parse HEAD)  --build-arg BUILD_DATE=$(date +"%Y-%m-%dT%H:%M:%SZ") -t guiet/motioneye:v1 -f  /home/fred/applications/motioneye/motioneye-docker/Docker/motioneye_dockerfile .
```

4. Run docker motioneye

```bash
cd /home/fred/applications/motioneye/motioneye-docker/Docker
chmod u+x motioneye_dockerrun
./motioneye_dockerrun
```

5. Open your favorite browser...wait for motioneye to be ready and enjoy !

```
http://your_raspberry_zero_ip:8765/
```


