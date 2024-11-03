#!/usr/bin/bash

#echo -n "Enter Filename (without .mkv): "
#read filename
#INPUT=$filename.mkv
#OUTPUT=$filename-output.mkv

for input in *.mkv; do
if [ -f "$input" ]; then

echo "############################################################"
echo "$input"
extension="${input##*.}"
filename="${input%.*}"
#output="${filename}-handbrake.${extension}"
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
--all-subtitles

fi
done

# --ab 448K
# --mixdown 5point1
# --arate auto
