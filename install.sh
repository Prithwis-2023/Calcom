sudo apt-get update
sudo apt-get install x11-xserver-utils
xhost +
docker run -t -i -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY calcom