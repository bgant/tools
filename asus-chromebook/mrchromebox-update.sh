#!/usr/bin/zsh
# Source: https://mrchromebox.tech/#fwscript
# sudo vi /etc/default/grub
#    Add iomem=relaxed to GRUB_CMDLINE_LINUX_DEFAULT
# sudo update-grub

curl -LO mrchromebox.tech/firmware-util.sh && sudo bash firmware-util.sh
