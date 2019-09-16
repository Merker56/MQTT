FROM ubuntu

ARG URL=http://169.44.201.108:7002/jetpacks/4.2

RUN apt-get update && apt install -y git pkg-config wget build-essential cmake unzip python python3-pip

WORKDIR /tmp
# RUN rm *.deb

RUN curl $URL/libopencv_3.3.1-2-g31ccdfe11_arm64.deb  -so libopencv_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb

RUN apt install -y  libtbb-dev libavcodec-dev libavformat-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgtk2.0-dev
RUN apt install -y libswscale-dev libv4l-dev
RUN dpkg -i *.deb

RUN apt install -y libcanberra-gtk-module libcanberra-gtk3-module libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 

RUN pip3 install paho-mqtt
