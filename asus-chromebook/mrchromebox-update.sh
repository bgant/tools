#!/usr/bin/zsh
# Source: https://mrchromebox.tech/#fwscript
# sudo vi /etc/default/grub
#    Add iomem=relaxed to GRUB_CMDLINE_LINUX_DEFAULT
# sudo update-grub

curl -L mrchromebox.tech/firmware-util.sh > /tmp/firmware-util.sh
sudo bash /tmp/firmware-util.sh
