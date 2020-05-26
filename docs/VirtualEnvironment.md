## Step 1: Installing pip

pip is the reference Python package manager. It’s used to install and update packages. You’ll need to make sure you have the latest version of pip installed.
Use the command:

```bash
$ sudo apt install python3-pip
```

## Step 2: Install Virtual environment

Use the command:

```bash
$ sudo pip3 install virtualenv
```

## Step 3: Create a virtual environment

```bash
$ virtualenv venv
```

## Step 4: Activate your virtual environment

```bash
$ source venv/bin/activate
```
## Step 5: Install required python modules

```bash
$ pip install -r requirements.txt
```