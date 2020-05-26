# Why Use Selenium with Docker?
One of the reasons to use Selenium with Docker include:
- It’s much quicker to get up and running using the pre-made containers than to try and set Selenium up from scratch.
- You don’t need to install all the necessary browsers. Perhaps you don’t want to install Firefox or want to test with a specific older build of Chrome or one with specific plugin or capabilities.
- Selenium can (and likely will) crash on you. It’s not really something you can simply set and forget. Using containers means you can spin up a new Selenium instance when you need it, discard and then start fresh. Alternatively, if you do plan on leaving it running for extended periods of time, if/when it crashes you can just set to reboot.
- Team members can use the same container regardless of what operating system they use so there are fewer discrepancies between environments.
 
# Installing Docker
The first thing you’ll want to do is install Docker. I will be using Ubuntu for example.

## Step 1: Update Software Repositories
As usual, it’s a good idea to update the local database of software to make sure you’ve got access to the latest revisions. Therefore, open a terminal window and type:

```bash
$ sudo apt-get update
```

## Step 2: Uninstall old version of Docker
Use the command-

```bash
$ sudo apt-get remove docker docker-engine docker.io
```

## Step 3: Install Docker
Use the command-

```bash
$ sudo apt install docker.io
```

## Step 4:  Start and automate Docker
The Docker service needs to be setup to run at startup. To do so, type in each command followed by enter:

```bash
$ sudo systemctl start docker
$ sudo systemctl enable docker
```

## Step 5:  Check the version of Docker
To verify the installed Docker version number, enter:

```bash
$ docker --version
```
# Using Docker with Selenium
Once you’ve got Docker up and running, SeleniumHQ maintains a whole range of Docker images that you can pull down and start using right away.
The list of images is available at Docker Hub or you can browse the project repository on GitHub. The GitHub repository also provides some resources, and you can submit issues if you come across anything.
The images are roughly split into:
- Standalone – Images that create a standalone Selenium server. You’ll only be able to run one of these at a time on your local machine or the port (4444) will conflict.
- Hub – Image that creates a central Selenium server in grid configuration.
- Node – Images that are used in conjunction with the “Hub” image to create a Selenium grid. You can start multiple node containers that connect to your Hub image.
- Base – Images that you can you use to build your own images

Getting a Standalone Server Up and Running
To get a standalone selenium server working, run the following command in your terminal:
```bash
$ docker run -d -p 4444:4444 selenium/standalone-chrome:3.4.0
```
-d runs the container in the background (detached)
-p 4444:4444 maps the local port 4444 to the port 4444 used by the Selenium Server in the container
:latest is tag/version of the image to use

The above will get the latest released image for the Chrome Standalone Server. Alternatively, you can specify a specific version by using the relevant tag. For example:
```bash
$ docker run -d -p 4444:4444 selenium/standalone-chrome:3.4.0
```

Firefox, instead use:
```bash
$ docker run -d -p 4444:4444 selenium/standalone-firefox:3.4.0
```
Once you run the command, Docker will download the image and run the container straight away.
You can then use  docker ps to check the container is running.

# Running a Grid
Setting up a Selenium Grid only requires a few different steps.
To start a small grid with 1 Chrome and 1 Firefox node you can run the following commands:

```bash
$ docker run -d -p 4444:4444 --name selenium-hub selenium/hub:3.4.0
$ docker run -d --link selenium-hub:hub selenium/node-chrome:3.4.0
$ docker run -d --link selenium-hub:hub selenium/node-firefox:3.4.0
```

- --name assigns a specific name, “selenium-hub”, to the Hub container
- --link links one container to another

Once you have run the above commands and the images have been downloaded and started. You can check the status of the images using command: 

```bash
$ docker ps-a
```