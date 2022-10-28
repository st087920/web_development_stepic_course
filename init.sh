sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

cd /home/box/web
sudo gunicorn -b 0.0.0.0:8080 hello:wsgi_aplication &

sudo ln -sf /home/box/web/etc/ask_conf.py /etc/gunicorn.d/ask_conf.py
sudo gunicorn -c /etc/gunicorn.d/ask_conf.py ask.wsgi:application &
sudo /etc/init.d/mysql start
sudo /ask/manage.py syncdb

