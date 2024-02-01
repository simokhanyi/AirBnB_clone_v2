#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static.
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary folders
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively to root user and group
chown -R root:root /data/

# Update Nginx configuration
echo -e "location /hbnb_static {\n\talias /data/web_static/current/;\n}\n" | tee -a /etc/nginx/sites-available/default > /dev/null

# Restart Nginx
service nginx restart

# Exit successfully
exit 0
