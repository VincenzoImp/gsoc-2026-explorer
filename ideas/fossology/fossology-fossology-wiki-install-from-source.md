# https://github.com/fossology/fossology/wiki/Install-from-Source

**Parent:** FOSSology — Project Ideas
**Source:** https://github.com/fossology/fossology/wiki/Install-from-Source
**Scraped:** 2026-02-22T23:28:47.598412

---

## Source Install

This document is designed to help you get FOSSology configured and ready to use. Its intended audience is the system administrator who wants to quickly get a local FOSSology instance up and running from source, or a distribution developer looking to create packages.

For other system administrator documentation, including where to download the source, see our [Sysadmin Documentation](http://www.fossology.org/projects/fossology/wiki/Sysadmin_Documentation).

(In examples, # is as root, $ is mortal) 

### Instructional Video

We have also recorded a screen-cast installing FOSSology from Source on an Ubuntu machine. It is available at https://youtu.be/q12KwmPYZG4

### Short Installation Instructions

If you have any old FOSSology installs you want to remove from the system you can run the fo-cleanold script

```console
# utils/fo-cleanold
```

If you have an existing install that you want to transition, be sure to back up your repository, database, and config files before proceeding.

#### 1. Install dependencies

Install latest version of CMake (preferred >= 3.19.0) from https://www.cmake.org/download

##### 1.a Install build dependencies

```console
# utils/fo-installdeps
```

**NOTE**:This program requires the lsb_release command. On Debian based systems this is probably in the lsb-release package, on Fedora/RedHat systems it is probably the redhat-lsb package. For example for centos7:

```console
# yum install redhat-lsb
```

#### 2. Build FOSSology

Configure CMake in `./build` folder, keeping it separate from source.

```console
$ cmake -S. -B./build -G Ninja
```

To enable testing, cmake requires additional flag.
```console
$ cmake -S. -B./build -DTESTING=ON -G Ninja
```
If you want to do a non-standard build, see [[HACKING]]

On centos7 the fo-installdeps script does not (yet) install the development tools, including the c++ compiler which is needed for the copyright agent for example (most of the original agents are written in c and php, but the copyright agent for example is written in c++). Thus you might want to install the gnu c++ compiler tools

```console
# yum groupinstall 'Development Tools'
```

##### 2.a Install Composer (optional, some versions prior 3.1-RC3)

Composer is a PHP package management tool which is not installable as package on some Linux distros, therefore we need to install it at some versions of the fossology master (the composer installation needed some adjustments over some time):

```console
# ./utils/install_composer.sh
```

#### 3. Build and install FOSSology

To install (finally) FOSSology

```console
$ cmake --build ./build --parallel
# cmake --install ./build
```

##### 3.a Install FOSSology offline (without access to composer)

The build steps of FOSSology has a separate target called `composer_install` which is used at the end of build target to download the composer dependencies. However, if you are behind a corporate network and do not have access to internet, FOSSology can be installed without downloading the composer dependencies and shipping the composer's vendor from a separate machine.

To do so, download the composer dependencies on a computer with internet access and tar them.

```console
$ composer --working-dir=src install && composer --working-dir=src dump-autoload
$ tar -czvf php-vendor.tar.gz -C src vendor
```

Ship this tar to the destination system and perform offline install

```console
$ cmake -S. -B./build -G Ninja -DOFFLINE=ON
$ cmake --build ./build --parallel
# cmake --install ./build
```

Untar the composer dependencies

```console
# tar -xzvf php-vendor.tar.gz --directory=/usr/local/share/fossology/
# chown fossy:fossy /usr/local/share/fossology/
$ rm -f php-vendor.tar.gz
```

#### 4. Run the postinstall script

```console
# /usr/local/lib/fossology/fo-postinstall
```

#### 5. Login to FOSSology with the default fossy/fossy user and password and:
 1. Create yourself a user with administrative privileges
 1. Change the default password for user fossy

#### 6. Test that things are installed correctly

```console
# /usr/local/etc/fossology/mods-enabled/scheduler/agent/fo_scheduler -t
```

#### 7. Start the fossology scheduler daemon

On new systems with **systemd**

```console
# systemctl enable --now fossology
```

On old systems with **SysV**

```console
# /etc/init.d/fossology start
```

You're done, point your web browser at the new install (http://yourhostname/repo/) and start using FOSSology! If the browser returns a not found, pls check if the fossology apache httpd configuration is actually loaded by the apache httpd. The installation places the original file at `/usr/local/etc/fossology/conf/src-install-apache-example.conf` from which a soft link is created during `# make install`.

#### 8. [[Configure and tune the system|Configuration and Tuning]]

#### Dependencies

We provide a script, fo-installdeps (see above), to install needed dependencies. FOSSology uses lots of different existing tools and software and expects to find them installed on the system.

* For Debian nearly all packages can be found in main, unless you want the non-free version of unrar
* For Ubuntu you will need a universe apt source setup
* For RHEL you can find needed packages from EPEL
    (http://fedoraproject.org/wiki/EPEL) or rpm.pbone.net.

If `fo-installdeps` doesn't support the distro you are running (or fails to install everything that's needed) please [report a bug](https://github.com/fossology/fossology/issues/new?labels=bug&template=bug_report.md).

The `fo-installdeps` command provides output that can be helpful in 
figuring out what dependent packages you will have to install either 
from your distro or some other location.

The script, `fo-installdeps` itself will install the fossology core dependencies. Then every module, like scheduler, www, nomos, pkgagent, etc., will install any specific dependencies that they require with a script called `mod_deps`.  For example, [fossology/src/scheduler/mod_deps](https://github.com/fossology/fossology/blob/master/src/scheduler/mod_deps).

#### fo-postinstall 

It is highly recommended that you run the `fo-postinstall` script. However,
you may want to know the details of what the script is doing. This may be out
of academic curiosity, or more likely because you may have to troubleshoot
something gone wrong.

#### Setting up Users and Groups

You are expected to already have a "postgres" user as part of the
system postgresql install, and a "www-data" user as part of the
apache2 install. Note that some versions of Apache (like the one
shipped with RHEL) use the user apache, not www-data. Whichever user
your Apache uses, make sure that the user (www-data or apache) gets
added to the "fossy" group.

FOSSology requires a system user and a system group both named
"fossy".

The /etc/passwd entries for these user should look
something like (Note: your uid & gid values may be different):

```
fossy:x:107:1002:fossology,,,:/srv/fossology:/bin/bash
```

and the /etc/group entry

```
fossy:x:1001:fossy,www-data
```

On a system with the useradd and groupadd commands (all LSB systems
including Debian, Fedora, etc) you can create the above system user
and group with the following commands as root:

```console
# groupadd fossy
# useradd -c FOSSology -d /srv/fossology -g fossy -s /bin/false fossy
```

Alternatively, you can use the adduser command:

```console
# adduser --gecos "FOSSology" --home /srv/fossology --system --group fossy
```

You can see the rest of what fo-postinstall does in [fossology/install/fo-postinstall](https://github.com/fossology/fossology/blob/master/install/fo-postinstall.in).

### Install for WSL2(OPTIONAL)

NOTE :" FOSSology does not officially support WSL "

Follow all the steps from "Install From Source Section" 
Also you can refer to the instructional video "https://youtu.be/q12KwmPYZG4"

Most Probable errors you can face while installing with WSL2 :

1. Apache server not running , To overcome this run :

```console 
# sudo service apache2 start
```

2. psql : error(Postgresql isn't running) , To overcome this run the following commands :

 Step 1 : Running "pg_lsclusters" will list all the Postgres Clusters running on your device 

```console
# Ver  Cluster Port  Status  Owner     Data directory               Log file
  12   main    5432   down   postgres  /var/lib/postgresql/12/main  /var/log/postgresql/postgresql-12-main.log
```

 Step 2 : Restart the "pg_ctlcluster"

NOTE : VER is different in different systems , 12 here is used for examples only .

```console
# sudo pg_ctlcluster 12 main start

```

 Run the postinstall script , as mentioned as instructions in "Install From Source "

```console
# /usr/local/lib/fossology/fo-postinstall
```

 Login to FOSSology with the default fossy/fossy user and password and:
 1. Create yourself a user with administrative privileges
 1. Change the default password for user fossy

[Then follow from step 6](https://github.com/fossology/fossology/wiki/Install-from-Source#6-test-that-things-are-installed-correctly)
