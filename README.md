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

### Test
![20241209_030617](https://github.com/user-attachments/assets/4b11e66b-eee4-4e2a-b7a5-c7186a8aa948)
![20241209_030702](https://github.com/user-attachments/assets/9632f865-b41d-4c35-8a71-d4b3644fd599)
![20241209_030711](https://github.com/user-attachments/assets/f60406c5-b431-4dce-9fa2-db016f21a6bd)
