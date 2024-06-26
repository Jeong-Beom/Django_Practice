# mysite01
### 코드 변경시 적용 기본 사항
1. git push
2. git pull
3. sudo systemctl restart mysite01.service
4. sudo systemctl restart nginx

### 시작 가이드(로컬서버)
0. Change Time standard and git clone
>```bash
>sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
>git clone https://github.com/Jeong-Beom/Django_Practice.git
>```  
1. Create virtual environment and reboot.
>```bash
>pyenv install 3.12.4
>pyenv virtualenv 3.12.4 venv_mysite01
>```
2. Activate Virtual Environment after move to project directory(~/Django_Practice/mysite01) as command.
>```bash
>. Activate_server_local.sh
>```
3. Install packages
>```python
>pip install -r requirements.txt
>```
4. Create logs folder and .env file that is created for storing important informantions like SECRET KEY.(+ migrate)
>```bash
>mkdir logs
>sudo nano .env
>```
>```
># .env info
>SECRET_KEY={적용할 SECRET 값 정보}
>DEBUG={적용할 DEBUG값}
>{...}
>```
>```bash
>python manage.py migrate
>```

### 시작 가이드(운영서버)
0. Change Time standard and git clone
>```bash
>sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
>git clone https://github.com/Jeong-Beom/Django_Practice.git
>```  
1. Create virtual environment and reboot.
>```bash
>pyenv install 3.12.4
>pyenv virtualenv 3.12.4 venv_mysite01
>```
2. Activate Virtual Environment after move to project directory(~/Django_Practice/mysite01) as command.
>```bash
>. Activate_server.sh
>```
3. Install packages
>```python
>pip install wheel==0.43.0
>pip install -r requirements.txt
>pip install gunicorn==22.0.0
>```
>```bash
>sudo apt install nginx
>```
4. Create logs folder and .env file that is created for storing important informantions like SECRET KEY.(+ migrate)
>```bash
>mkdir logs
>sudo nano .env
>```
>```
># .env info
>SECRET_KEY={적용할 SECRET 값 정보}
>IP={적용할 IP정보}
>DEBUG={적용할 DEBUG값}
>DOMAIN={적용할 도메인}
>DJANGO_SETTINGS_MODULE=config.settings.prod
>{...}
>```
>```bash
>python manage.py migrate
>```
5. Move to '/etc/systemd/system/' and create service file.
>- check user, group info
>```bash
>id
>```
>```bash
>sudo nano mysite01.service
>```
>```
># mysite01.service - it is needed to change as environment.
>[Unit]
>Description=gunicorn daemon
>After=network.target
>
>[Service]
>User=azureuser
>Group=azureuser
>WorkingDirectory=/home/azureuser/Django_Practice/mysite01
>EnvironmentFile=/home/azureuser/Django_Practice/mysite01/.env
>ExecStart=/home/azureuser/.pyenv/versions/3.12.4/envs/venv_mysite01/bin/gunicorn \
>        --workers 2 \
>        --bind unix:/tmp/gunicorn.sock \
>        config.wsgi:application
>
>[Install]
>WantedBy=multi-user.target
>```
>- execute mysite01.service and check error.
>```bash
>sudo systemctl start mysite01.service
>sudo systemctl status mysite01.service
>sudo systemctl enable mysite01.service
>```
6. Move to '/etc/nginx/sites-available/' and create file for nginx. 
>- create mysite01 file
>```bash
>sudo nano mysite01
>```
>```
># mysite01 - if it doesn't exist domain. it is needed to open 80 port. it is needed to change as environment.
>server {
>        listen 80;
>        server_name {IP 주소};
>
>        location = /favicon.ico { access_log off; log_not_found off; }
>
>        location /static {
>                alias /home/azureuser/Django_Practice/mysite01/static;
>        }
>
>        location / {
>                include proxy_params;
>                proxy_pass http://unix:/tmp/gunicorn.sock;
>        }
>}
>
># mysite01 - if it exists domain. it is needed to open 80, 443 port. it is needed to change as environment.
>server {
>        listen 80;
>        server_name {도메인 명칭};
>        rewrite ^https://$server_name$request_uri? permanent;
>}
>
>server {
>        listen 443 ssl;
>        server_name {도메인 명칭};
>
>        ssl_certificate /etc/letsencrypt/live/{도메인 명칭}/fullchain.pem; # managed by Certbot
>        ssl_certificate_key /etc/letsencrypt/live/{도메인 명칭}/privkey.pem; # managed by Certbot
>        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
>
>        location = /favicon.ico { access_log off; log_not_found off; }
>
>        location /static {
>                alias /home/azureuser/Django_Practice/mysite01/static;
>        }
>
>        location / {
>                include proxy_params;
>                proxy_pass http://unix:/tmp/gunicorn.sock;
>        }
>}
>```
>- move to '/etc/nginx/sites-enabled/' and delete default. create mysite(link)
>```bash
>sudo rm default
>sudo ln -s /etc/nginx/sites-available/mysite01
>```
>- check error and restart nginx
>```bash
>sudo nginx -t
>sudo systemctl restart nginx
>```
7. Move to project directory(~/Django_Practice/mysite01/) and execute commands.
>```
>python manage.py collectstatic
>sudo systemctl restart mysite01.service
>```
