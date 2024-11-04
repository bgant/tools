#!/usr/bin/bash

for input in *.mkv; do
if [ -f "$input" ]; then

echo "############################################################"
echo "$input"
extension="${input##*.}"
filename="${input%.*}"
output="output/${input}"
#taskset -c 1,3,5,7,9,11 \
flatpak run fr.handbrake.HandBrakeCLI \
--input $input \
--output $output \
--preset "Roku 2160p60 4K HEVC Surround" \
--crop-mode none \
--audio-lang-list eng \
--all-audio \
--aencoder aac \
--mixdown 5point1,stereo \
--aname "Surround 5.1","Stereo","Commentary" \
--subtitle-lang-list eng \
--all-subtitles \
--subtitle-default="none" \
--subtitle-burned="none"

fi
done

# --start-at seconds:600 --stop-at seconds:120
