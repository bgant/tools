#!/usr/bin/python3
#
# Brandon Gant
# Created: 2021-03-04
# Updated: 2021-12-14
#
# Check to see if NFS for Longhorn Backups is mounted properly on each server
# by looking for a check-longhorn-nfs.txt file on the NFS mount point
#
# NFS Volume must have 'relatime' set in /etc/fstab or ZFS or you will
# or you get "Invalid Date" errors on backups
#    EXT4: UUID=26345b2f-f310-4ab2-a08d-c30d87a2c0d8       /nfs    ext4    rw,relatime 0 2
#     ZFS: zfs set relatime=on mypool
#

########################################################
# Custom Variables
########################################################

IP='192.168.7.119'
NFS='/var/lib/longhorn-backupstore-mounts/192_168_7_119'
KUBECONFIG='export KUBECONFIG=kube_config_cluster.yml;'


########################################################
# Main Script
########################################################

from subprocess import run

# The awk gsub command converts repeating whitespaces into a single whitespace character
command = KUBECONFIG + \
          ' kubectl get -n longhorn-system pods -o wide | egrep \"longhorn-manager-|instance-manager-r-\" | \
          awk \'{ gsub(/[ ]+/,\" \"); print }\' | awk \'{print $1\":\"$7}\''

output = run(command, shell=True, capture_output=True, text=True)
#print(output.stdout)

# Create key:value pairs for pod:host
result = {}
for row in output.stdout.split('\n'):
    if ':' in row:
        key, value = row.split(':')
        result[key.strip(' .')] = value.strip()
#print(result)

for key in result:
    # Does the /var/lib/longhorn-backupstore-mounts/<server>/ folder exist?
    command = KUBECONFIG + \
              ' kubectl exec -it -n longhorn-system ' + key + \
              ' -- stat ' + NFS
    output = run(command, shell=True, capture_output=True, text=True)
    folder = True if output.returncode == 0 else False

    # Is it reporting a "Stale" NFS mount when you look in the directory?
    command = KUBECONFIG + \
              ' kubectl exec -it -n longhorn-system ' + key + \
              ' -- ls -l ' + NFS + '/'
    output = run(command, shell=True, capture_output=True, text=True)
    fresh = True if output.returncode == 0 else False

    # Is it actually NFS mounted right now?
    command = KUBECONFIG + \
              ' kubectl exec -it -n longhorn-system ' + key + \
              ' -- stat ' + NFS + '/backupstore'
    output = run(command, shell=True, capture_output=True, text=True)
    mounted = True if output.returncode == 0 else False

    if not folder:
        print(f"FAILED:  {key} on {result[key]} is missing /var/lib/longhorn-backupstore-mounts folder...")
        status = False
    elif not fresh:
        print(f"FAILED:  {key} on {result[key]} is a stale NFS mount...")
        status = False
    elif not mounted:
        print(f"FAILED:  {key} on {result[key]} is not mounted to NFS {IP}...")
        status = False
    else:
        print(f"SUCCESS: {key} on {result[key]} is mounted to NFS")
        status = True

    # Try to fix FAILED state by remounting volume
    if not status:
        command = KUBECONFIG + \
                  ' kubectl exec -it -n longhorn-system ' + key + \
                  ' -- umount --force ' + NFS + '; \
                  mkdir -p ' + NFS + ';\
                  chmod 777 ' + NFS + ';\
                  kubectl exec -it -n longhorn-system ' + key + \
                  ' -- mount -t nfs4 -o nfsvers=4.2 ' + IP + ':/ ' + NFS
        remount = run(command, shell=True, capture_output=True, text=True)
        print("    Attempted to fix problem... Run this script again to see if it is working now...")
        print(command)

# Show example of last command run
#print(command)
