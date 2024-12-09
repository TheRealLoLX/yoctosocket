### MIT Checksum
# md5sum /home/thereallol/yocto/sources/poky/meta/files/common-licenses/Proprietary
### Initialize build folder
# source sources/poky/oe-init-build-env
### Bitbake commands
# bitbake -c clean tfsocket
# bitbake tfsocket
## Clean image layer
# bitbake -c cleansstate
# bitbake -c cleanall
### Build image
# bitbake core-image-minimal
### Image path
# ls tmp/deploy/images/raspberrypi5/*wic*
### Copy image to
# sudo bmaptool copy <source file path .bz2>  <destination file path .bmap>
### Wifi interface config
# vi /etc/network/interfaces
## ssid and psk
# vi /etc/wpa_supplicant.conf
# wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
