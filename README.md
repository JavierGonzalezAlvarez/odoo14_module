# instalar Odoo 14.0 (Versión Community) en linux 20.04 and VMwarePlayer y crear modulo odoo

usuarios:
-javier
-odoo

teclado idioma: sudo setxkbmap -layout 'es,es' -model pc105

-con un usuario no rot con permisos root
$ sudo apt update && upgrade

## con oddo 14 instalamos python3
$ sudo apt-get install -y python3 python3-pip

## paquetes que necesita odoo14
$ sudo apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev \
libldap2-dev libssl-dev python-dev python3-dev build-essential libffi-dev \
zlib1g-dev gcc

## paquetes que necesita python3
$ sudo apt-get install -y python-pypdf2 python-dateutil python-feedparser \
python-ldap python-libxslt1 python-lxml python-mako python-openid \
python-psycopg2 python-babel python-pychart python-pydot python-pyparsing \
python-reportlab python-simplejson python-tz python-vatnumber python-vobject \
python-webdav python-werkzeug python-xlwt python-yaml python-zsi \
python-docutils python-psutil python-mock python-unittest2 python-jinja2 \
python-decorator python-requests python-passlib python-pil

$ sudo pip3 install PyPDF2 Werkzeug==0.11.15 python-dateutil reportlab \
psycopg2-binary

sudo apt-get install -y npm

## link simbolico, posiblemente ya lo crea npm
$ sudo ln -s /usr/bin/nodejs /usr/bin/node

$ sudo npm install -g less less-plugin-clean-css
$ sudo apt-get install -y node-less

## instalacion de odoo 14
## añadir un usuario
$ sudo adduser --system --home=/opt/odoo --group odoo
$ sudo apt-get install postgresql

$ sudo apt install git

# entrar en postgres, crear el usuairo de oddo en BD. Se va relacionar el usuario con odoo
$ sudo su postgres
## crear un usuario
user: odoo
pss: odoo14
$ createuser --createdb --username postgres --no-createrole --no-superuser --pwprompt odoo
# entrar en psql
psql
ALTER USER odoo WITH SUPERUSER;
\q
## salimos de postgres
exit

## entrar en usuario odoo desde linux
me envia a la home opt/odoo
$ sudo su - odoo -s /bin/bash

# descarga del paqute odoo 14 desde el repositorio de odoo 14
$ mkdir opt/odoo
$ cd /opt/odoo
$ git clone https://www.github.com/odoo/odoo --depth 1 --branch 14.0 --single-branch .

# salir del usuario odoo
$ exit
# el archico reqirements.txt me indica las depdencias de odoo
$ sudo pip3 install -r requirements.txt
exit

$ usuario javier => /opt/odoo/sudo -Hu odoo ./odoo-bin

si error => PermissionError: [Errno 13] Permission denied: '/opt/odoo/.local'
$ sudo chmod 777 opt/odoo

# run odoo
$ usuario javier => /opt/odoo/sudo -Hu odoo ./odoo-bin

message when run odoo => You need Wkhtmltopdf to print a pdf version of the reports
sirve par imprimir las versiones de pdf de un html. Convierte texto en hmtl en pdf

# install Wkhtmltopdf
desde usuario javier
https://github.com/wkhtmltopdf/packaging/releases
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/0.12.3/
copy enlace:

$ wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz

-descomprimir
$ tar vxf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
-copiar
$ cp wkhtmltox/bin/wk* /usr/local/bin/
-comprobar version
$ wkhtmltopdf --version
    wkhtmltopdf 0.12.3 (with patched qt)

# run odoo 14 in browser
http://localhost:8069

Create database
--------------------
Master Password: rmrz-tazj-4n5v
Databasename: odoo14
email: javier@email.com
password: 12qweD34
Phone number: 7878787878
Language: Spanish
Country: Spain
Demo data: yes

install apps:
    - ventas
    - facturación
    - inventario etc

# crear modulo odoo
podría crear un directorio nuevo para nuevos modulos desde
$ odoo/debian $ sudo nano odoo.conf
permite recupear los addons personalizados en caso de reinstalacion

-desde usuario javier, en directorio, usamos odoo-bin:
/opt/odoo/oddo-bin

-en la carpeta adons. mejor carpeta customizada

## comando: crear modulo
desde usuario javier: /opt/odoo
nombre modulo: modulo_personalizado
directorio destino: addons
$ sudo ./odoo-bin scaffold modulo_personalizado addons

-en adons tenemos creado la carpeta "modulo_personalizado" con todas las carpetas y ficheros
-entrar en modo desarrollador y "actualizar lista de aplicaciones"
veremos el modulo creado e instalar





