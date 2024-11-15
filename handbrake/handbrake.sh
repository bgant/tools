#!/usr/bin/bash
#
# Place .mkv files in the same directory as this script.
#     mkdir output
#     chmod go+w output
#     ./handbrake.sh
# Converted files placed in output/ with original <source>.mkv name
#

#==========================================
# Parallel or Sequential Conversions?
#==========================================
#STATE='parallel'
STATE='sequential'

#==========================================
# Is HandBrake CLI installed?
#==========================================
if [[ -f /usr/bin/HandBrakeCLI ]]; then
    COMMAND='/usr/bin/HandBrakeCLI'
elif [[ `flatpak list | grep -c HandBrakeCLI` -eq 1 ]]; then	
    COMMAND='flatpak run fr.handbrake.HandBrakeCLI'
else
    echo "No HandBrake CLI installed"
    exit 1
fi

#==========================================
# Create Array of Handbrake Commands to Run
#==========================================
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")  # Spaces in filenames
COMMAND_LIST=()

for input in *.mkv; do
extension="${input##*.}"
filename="${input%.*}"
output="output/${input}"
#taskset -c 1,3,5,7,9,11 \
COMMAND_LIST+=("$COMMAND \
--input \"$input\" \
--output \"$output\" \
--preset \"Roku 2160p60 4K HEVC Surround\" \
--crop-mode none \
--audio-lang-list eng \
--all-audio \
--aencoder aac \
--mixdown 5point1,stereo \
--aname \"Surround 5.1\",\"Stereo\",\"Commentary\" \
--native-language eng \
--subtitle \"scan\" \
--subtitle-forced")
# --start-at seconds:600 --stop-at seconds:120
done

#==========================================
# Run Handbrake Commands
#==========================================
#echo ${COMMAND_LIST[@]}  # List all elements in array
#echo ${COMMAND_LIST[20]} # List element 20 in array
if [[ $STATE == 'parallel' ]]; then
    # apt install parallel
    # --jobs # is the number of commands to run in parallel
    echo "Running Conversions in Parallel..."
    nice parallel --keep-order --progress --eta --jobs 8 ::: "${COMMAND_LIST[@]}"
elif [[ $STATE == 'sequential' ]]; then
    echo "Running Conversions Sequentially..."
    for COMMAND in ${COMMAND_LIST[@]}
    do
        echo "Command: $COMMAND"
	eval $COMMAND
    done
else
    echo "Something has broken"
    exit 1
fi

IFS=$SAVEIFS
# View output of any running Handbrake process with: tail -f /proc/<pid>/fd/1
