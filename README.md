## MIT Checksum
#### md5sum /home/thereallol/yocto/sources/poky/meta/files/common-licenses/Proprietary
## Initialize build folder
#### source sources/poky/oe-init-build-env
## Bitbake commands
#### bitbake -c clean tfsocket
#### bitbake tfsocket
### Clean image layer
#### bitbake -c cleansstate
#### bitbake -c cleanall
## Build image
#### bitbake core-image-minimal
## Image path
#### ls tmp/deploy/images/raspberrypi5/*wic*
## Copy image to
#### sudo bmaptool copy <source file path .bz2>  <destination file path .bmap>
## Wifi interface config
#### vi /etc/network/interfaces
### ssid and psk
#### vi /etc/wpa_supplicant.conf
#### wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

## Hotspot
### don't forget to disable firewall of PC

## Test
#### Open Palm
![20241209_130129](https://github.com/user-attachments/assets/781a0f70-8e30-4802-8f32-dd87f1b6a0ac)

#### Thumb up
![20241209_130132](https://github.com/user-attachments/assets/95ade000-c609-4d99-ab15-8d4b5f210e56)

#### Fist
![20241209_130137](https://github.com/user-attachments/assets/f603be26-d238-4217-bc06-26cf1381132d)

