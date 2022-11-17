#!/bin/bash
rsync --archive --itemize-changes --exclude=nfs-backup ~/rke-flatcar/ ~/rke-flatcar/nfs-backup/`date --utc +rke-flatcar-%Y-%m-%dT%H:%M:%SZ`/
