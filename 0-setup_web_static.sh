#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config_file="/etc/nginx/sites-available/default"
sudo sed -i '/location \/hbnb_static {/a alias /data/web_static/current/;' "$nginx_config_file"

# Restart Nginx
sudo service nginx restart

exit 0
