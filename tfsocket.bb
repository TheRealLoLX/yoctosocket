#fuck this shit
DESCRIPTION = "Python client for receiving and displaying images"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://tfsocket.py"

# The package depends on Python and required libraries
RDEPENDS:${PN} = " \
    python3-core \
    python3-pickle \
    python3-json \
    python3-numpy \
    python3-opencv \
"

# Destination for installation
do_install() {
    install -d ${D}${bindir}/tfsocket
    install -m 0755 ${WORKDIR}/tfsocket.py ${D}${bindir}/tfsocket/tfsocket.py
}


# Mark the file as executable
FILES:${PN} += "${bindir}/tfsocket/tfsocket.py"
IMAGE_INSTALL += "tfsocket"