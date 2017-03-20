# Python
---------------------
## basic
    str.split()
    
    n = 0
    if n == 0:
        output = merge1
        n += 1
    else:
        output = pd.concat([output, merge1]) 
        
    for a in data_name:
        no_pon = ''.join(e for e in a if e.isalnum())
        name_no_pun.append(no_pon)
    
## numpy


## list
    list(str()) # split sentence

## dictionary
    data_list = list(data)
    new_dict = {}
    for idx in range(0,len(data_list)):
        address = data_list[idx][5]
        address_ = address.split(' ')
        if len(address_) > 2:
            address_ = "".join([address_[0],address_[1]])
        else:
            citycode = str(int(data_list[idx][13]))
            if citycode in city_dict:
                address_ = city_dict[citycode]
            else:
                address_ = "other"
        new_dict.setdefault(address_, []).append(data_list[idx])
    return new_dict


## pandas
    build_old = build_old.rename(columns={'所在地':'所在地_地番', '延べ面積':'総延べ面積'})
    build_old = pd.read_csv(build_old_name, usecols=[0,1,4])
    merge1 = merge1.reindex(columns=['Uniq_ID','ID2','住宅地図ID','ユーザーID'])
    dff2=pd.concat([build_new_clean, build_old_clean, dff],axis=0)
    merge1 = pd.concat([dff2,reinforcement],1)
    build_old_clean = build_old_clean.drop_duplicates(['マッチ用物件名'], keep='last')
    dff = pd.merge(build_old_clean, build_new_clean, on=['マッチ用物件名'],how='inner')
    data = data.sort(['マッチ用物件名'])
    

## csv
    data = {}
    with open(filepath,"r") as f:
        reader = csv.reader(f)
    for row in reader:
        citycode = str(row[0])
        data[citycode] = cityname

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
