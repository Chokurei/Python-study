# Python
---------------------
## numpy


## list

## dictionary

## pandas


## others


# Command
---------------------

## SSH
    $ ssh name@domain # log in
    $ scp <source> <distination> # download and upload
        e.g: Download: $ scp -r hadoop@152.xx.xxx.xx:home/hadoop/data /path/to/file
               Upload: $ scp /path/to/file username@a:/path/to/destination
    $ ssh localhost 
    
## Compress
    $ unzip /path/to/file/ # zip
    $ unrar e -r file.rar # unrar
    $ gunzip file.gz # gz
    $ tar -czvf newname.gz file # compress

## install
    $ apt-get install #autoremove/upgrade/update
    $ sudo dpkg -i xx.deb
    $ sudo bash xx.sh

## Others
    $ wget URL -O path
    $ sudo cp -r path1 path2 # between different users
    $ sudo chmod 777 -R /path/to/file/
    $ conda list | grep *
    $ pip freeze | grep * 
    $ gksudo gedit /sourse.list # change sourse
    $ ls -l /use/bin/python  
    $ ln -s /usr/bin/python2.6 /usr/bin/python  # soft like
    $ sudo find / -name 'name'


# Docker
---------------------
    $ docker images
    $ docker ps -a  #-a means check all containers
    $ docker pull
    $ docker run -t -i image:Tag /bin/bash # /bin/bash means start from this path, -t: terminal, -i interactive
    $ docker exit
    $ docker commit -m "comment" image_id image_name:Tag # the way to make new images, image_id is given by checking docker images
    $ docker login 
    $ docker tag image_old_name image_new_name
    $ docker push image_name # name need to be docker_bub_name/image_name
    $ docker rmi image_name
    $ docker rm contrainer_name

# Hadoop
----------------------
