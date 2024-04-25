# Execute given commands one by one to install Odoo

### Fetch the updates:
```bash
sudo apt-get update
```

### Run the following commands to install the main dependencies:
```bash
sudo apt install openssh-server fail2ban python3-pip python3-dev libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential libssl-dev libffi-dev libmysqlclient-dev libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev git curl -y
```

### Download and install wkhtmltopdf:

```bash
wget  https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
```

```bash
sudo dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb
```

If you find errors in previous command, force install the dependencies with given command.

```bash
sudo apt-get install -f
```

### Now, install and configure PostgreSQL database:
```bash
sudo apt install postgresql -y
```

```bash
sudo -u postgres createuser --superuser
```

```bash
sudo su postgres
```

```bash
psql
```

```bash
alter user user_name with password 'your_password';
```


```bash
\q
```

```bash
exit
```

### Configure git:

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email youremail@example.com
```

### Clone the Odoo code base:

```bash
mkdir ~/odoo-dev
```

```bash
cd ~/odoo-dev
```

```bash
git clone -b 16.0 --single-branch --depth 1 https://github.com/odoo/odoo.git
```

### Create an venv-oodoo-16.0 virtual environment and activate it:
```bash
python3 -m venv ~/venv-odoo-16.0
```

```bash
source ~/venv-odoo-16.0/bin/activate
```

### Install the Python dependencies of Odoo in venv:

```bash
cd ~/odoo-dev/odoo/
```

```bash
pip3 install wheel
```

```bash
pip3 install -r requirements.txt
```

### Create and start your first Odoo instances:

```bash
createdb odoo-test
```

```bash
python3 odoo-bin -d odoo-test –i base --addons-path=addons --db-filter=odoo-test$
```
