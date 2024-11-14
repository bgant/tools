#!/usr/bin/bash
#
# Place .mkv files in the same directory as this script.
#     mkdir output
#     chmod go+w output
#     ./handbrake.sh
# Converted files placed in output/ with original <source>.mkv name
#

# Is HandBrake CLI installed?
if [[ -f /usr/bin/HandBrakeCLI ]]; then
    COMMAND='/usr/bin/HandBrakeCLI'
elif [[ `flatpak list | grep -c HandBrakeCLI` -eq 1 ]]; then	
    COMMAND='flatpak run fr.handbrake.HandBrakeCLI'
else
    echo "No HandBrake CLI installed"
    exit 1
fi


SAVEIFS=$IFS
IFS=$(echo -en "\n\b")  # Spaces in filenames
for input in *.mkv; do

echo "############################################################"
echo "$input"
extension="${input##*.}"
filename="${input%.*}"
output="output/${input}"
#taskset -c 1,3,5,7,9,11 \
$COMMAND \
--input $input \
--output $output \
--preset "Roku 2160p60 4K HEVC Surround" \
--crop-mode none \
--audio-lang-list eng \
--all-audio \
--aencoder aac \
--mixdown 5point1,stereo \
--aname "Surround 5.1","Stereo","Commentary" \
--native-language eng \
--subtitle "scan" \
--subtitle-forced

done
IFS=$SAVEIFS

# --start-at seconds:600 --stop-at seconds:120
