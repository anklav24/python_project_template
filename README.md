# Project name

### What the project is for:

### Why we need it:

### Configuration

- Check config `configs/config.py`
- Add environment variables like `NAME="VALUE"`

### Installing and running

- Add all your environment variables into `/etc/environment`.

```bash
sudo echo "YOUR_VARIABLE_NAME="YOUR_VARIABLE_VALUE"" >> /etc/environment && source /etc/environment
source /etc/environment
# Do the same under "sudo su":
sudo su
source /etc/environment
# Check your environment variables you should see them:
echo $NAME_OF_YOUR_VARIABLE
sudo echo $NAME_OF_YOUR_VARIABLE
```

- Install / Download Python, Project, Requirements:

```bash
sudo apt install python3.X  # Install Python 3.8 or above where X is your version (e.g. python3.8)
git clone REPOSITORY_URL  # Clone repository from git.
cd YOUR_PROJECT_FOLDER_PATH  # Go into the repository folder.
python3.X -m venv venv  # Create virtual environment.
source venv/bin/activate  # Activate virtual environment.
pip install -U pip  # Update pip.
pip install -r requirements.txt  # Install requirements.
# Make sure you use LF line separators in your start file.
python RUN_YOUR_SCRIPT_NAME.py  # Try to run manually.
```

- Check the `RUN_YOUR_SCRIPT_NAME.sh` file in the project folder and change paths and names if necessary.

`RUN_YOUR_SCRIPT_NAME.sh`

```bash
#!/usr/bin/env bash
cd /PATH/TO/YOUR/PROJECT/FOLDER
source venv/bin/activate
python RUN_YOUR_SCRIPT_NAME.py
```

```bash
chmod +x RUN_YOUR_SCRIPT_NAME.sh  # Make it executable.
sudo /PATH/TO/YOUR/PROJECT/FOLDER/RUN_YOUR_SCRIPT_NAME.sh  # Try to run manually.
sudo vim /etc/crontab  # Add it to cron.
```

`/etc/crontab`

```bash
00 3    * * *   root    /PATH/TO/YOUR/PROJECT/FOLDER/RUN_YOUR_SCRIPT_NAME.sh
```

### Environment

- Ubuntu 18.04.4 LTS
- Python3.X
- Tested YYYY-MM-DD

### Abbreviations

### References

### Source code
