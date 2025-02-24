# Training Project For Sircles
---
## Lab Building
To download ** sorint-X.X-el9.noarch.rpm ** Packages you can use this [link](https://github.com/DeyAgrO/Linux101/releases/download/Sorint-1.4-rpm/sorint-1.4-el9.noarch.rpm) or From release page [here](https://github.com/DeyAgrO/Linux101/releases).

To download **RunMe.sh** you can use this [link](https://github.com/DeyAgrO/Linux101/releases/download/Sorint-1.4-rpm/RunMe.sh) or From release page [here](https://github.com/DeyAgrO/Linux101/releases).

Or you can run the next command **Inside the newly Created Template VM** To Download and Lunch the **RunMe.sh** script
#### Using **wget** command
```bash
wget -q -O - https://raw.githubusercontent.com/DeyAgrO/Linux101/refs/heads/main/RunMe/RunMe.sh | bash
```
#### Using **curl** command
```bash
curl -s https://raw.githubusercontent.com/DeyAgrO/Linux101/refs/heads/main/RunMe/RunMe.sh | bash
```
---

## Course 101 - First Chapter Lab Exercise

***__REQUIRED:__***

- For this lab exercise, you have to create **__one__** almalinux 9.X virtual marchine (Clone **__One__** Machine).

INFO

- username : sorint / password : sorint
- to start course you should enter the command ` sorint start course101`
- After you finish the exercise you should enter the command `sorint grade course101`
- If all the question has been answered correctly then it should output finished.

#### 

### Exercise 101

Start the course :

```
sorint start course101
```

**Exercises**
1. Create a folder called `exam` in the home directory and create 3 folders inside it `txt` `mp3` `mp4`
2. Redirect the first 10 lines of the file `days.txt` which exist in the home directory to the file `/home/sorint/exam/txt/head.txt` Redirect the last 7 lines of the file `days.txt` which does exist in the home directory to the file `/home/sorint/exam/txt/tail.txt`
3. Redirect the value of the `$HOME` and `$PATH` environment variables to the file `/home/sorint/exam/txt/env.txt`
4. Create the file `/home/sorint/exam/txt/whoami.txt` and edit it using your favourite editor (nano, vim) and put inside it you name and email in this same context. **It is only local at your PC**

```java
name: <XXXX XXXXX>
email: <XXXXX@XXXXX.XXXX>
```

5. Inside the folder `/home/sorint/random` there are plenty of random files
   - Move all `.mp4` files to `/home/sorint/exam/mp4/` directory *that you have created before*
   - Move all `.mp3` files to `/home/sorint/exam/mp3/` directory *that you have created before*
   - Delete all `.wav` files from the `/home/sorint/random` directory
6. Check the content of the file `/home/sorint/code.txt` for the code `ansible-api-token=XXXXXXXXXXX` copy **__only__** the code `XXXXXXXXX` to the file `/home/sorint/exam/txt/token.txt`
7. Create two groups : `devops` `testers`
8. Create the users: `developer1` `tester1` Create a password for the users, the password is `sorint`
9. Append (*add*) the user `developer1` to the group `devops` Append (*add*) the user `tester1` to the group `testers`
10. Create the directory `/partage` Change the ownership of the directory to user `tester1` and the group `sorint` using the `chown` command `tester1:sorint` Create symbolic link for the folder `/partage` to the folder `/tmp/shared`
11. Create the alias `ipa="ip --color a"` And the alias must stay persistent after reboot

Evaluate your answers:

```
sorint grade course101
```

---

---

## Course 102 - Second Chapter Lab Exercise

***__REQUIRED:__***

- For this lab exercise, you have to create **__two__** almalinux 9.X virtual marchine (Clone **__two__** Machines) .

INFO:

- username : sorint / password : sorint
- to start course you should enter the command ` sorint start course102`
- After you finish the exercise you should enter the command `sorint grade course102`
- If all the question has been answered correctly then it should output finished.

### Exercise 102

Start the course :

```
sorint start course102
```

**Exercises**
1. Check all the sleep processes that are running in the background deactivate them all
2. Enable `sshd.service` Disable `chronyd.service` Stop `httpd.service`
3. There is a failed ssh login attempt used by the user `bernard` and you need to find the **IP address** associated with the failed login and copy it to the file `/home/sorint/exam/txt/ip.txt`
4. For this exercise you need to generate two ssh keys one default and use it to ssh to the second machine you created before ( ssh to the remote host without using the password) and **only** generate the second one called `sorintKey`


Evaluate your answers:

```
sorint grade course102
```

---

---

## Course 103 - Second Chapter Lab Exercise

***__REQUIRED:__***

- For this lab exercise, you have to create **__one__** almalinux 9.X virtual marchine (Clone **__One__** Machine).
- You should attach external Hard Drive of X GB to the VM.
- You Should add a second network interface card (NIC) to the VM.

INFO

- username : sorint / password : sorint


- to start course you should enter the command ` sorint start course103`
- After you finish the exercise you should enter the command `sorint grade course103`
- If all the question has been answered correctly then it should output finished green.

### Exercise 103

Start the course :

```
sorint start course103
```

**Exercises**
1. There is a need to set the hostname to `alma9.sorint.exam.com`
2. The second interface with the connection name `sorint` needs to have these info:

   Mode : Manual  
   IP Address: 172.168.1.200/24  
   Gateway: 172.168.1.1  
   DNS Server 1 : 172.168.1.1  
   DNS Server 2 : 1.1.1.1
3. There is an important information about the RPM package `sorint-1.X-X.noarch` and there is a code in the summery must be copied to the file `/home/sorint/exam/txt/rpmcode.txt`
4. We need to install the package `httpd` and then **enable**, **start** it.
5. Add the services `http` and `https` to the firewall.
6. Add the `librewolf` Browser Repo to your system using these info: It should be `enabled` and `GPG` check is active
```java
name: LibreWolf

baseurl: https://rpm.librewolf.net

gpgkey: https://rpm.librewolf.net/pubkey.gpg#
```

   **then check if you can download `librewolf` package**

7. Create the folder `/external` and mount the disk `/dev/sdX` to it The folder `/external` should be owned by the user and the group `sorint`
8. You have a folder called `random-d3` in the home directory We have to `find` all the files end with `.txt` extensions and redirect the output to the file `/home/sorint/exam/txt/texts.txt` We have to `find` all the files that contains the word `sorint` in their names and redirect the output to the file `/home/sorint/exam/txt/sorint.txt`
9. We have to allow all the users in the group `sorint` to use the `sudo` privilege without using the password

Evaluate your answers:

```
sorint grade course103
```
