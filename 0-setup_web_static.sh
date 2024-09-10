#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
printf % "
!DOCTYPE html
<html>
	<head>
		<title>Holberton Deploy Static</title>
	</head>
	<body>
		<p>Holberton School</p>
	</body?
</html>
" > /data/web_static/releases/test/index.html

sudo ln --symbolic --force /data/web_static/releases/test/ /data/web_static/current
sudo chown --recursive -L ubuntu:ubuntu /data/

new_location="server_name _;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
replace="server_name _;"
sudo sed -i "s/$replace/$new_location/" /etc/nginx/sites-available/default

sudo service nginx restart
