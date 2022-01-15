sudo apt update
sudo apt install docker.io
sudo systemctl start docker.service
sudo systemctl enable docker.service
sudo docker pull pycalcx/calcom:latest
sudo apt-get update
sudo apt-get install x11-xserver-utils
xhost +
clear
sudo docker run -t -i -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY calcom


