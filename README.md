
Check that the ollama serves only on localhost:11434 with commands like:

```
$OLLAMA_HOST=127.0.0.1 OLLAMA_PORT=11434 ollama serve
$sudo nano /etc/systemd/system/ollama.service
$sudo nano /etc/nginx/sites-available/ollama.conf
```

Create a self-signed SSL certificate for the nginx server using OpenSSL:

```
$sudo apt-get install nginx openssl
$sudo mkdir -p /etc/nginx/ssl
$sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/selfsigned.key -out /etc/nginx/ssl/selfsigned.crt
$sudo openssl dhparam -out /etc/nginx/dhparam.pem 4096
```

Create the encrypted auth header file and default debugging hello index.html:

```
$sudo mkdir -p /etc/nginx/secrets/
$sudo touch /etc/nginx/secrets/ollama_token.conf
$sudo chmod 600 /etc/nginx/secrets/ollama_token.conf
$sudo sh -c "python3 api-key.py > /etc/nginx/secrets/ollama_token.conf"
$sudo sh -c "echo hello > /var/www/html/index.html"
```


Replace the configuration files:

```
$sudo cp nginx.conf /etc/nginx/nginx.conf
$sudo systemctl daemon-reload
$sudo systemctl restart nginx
```

test:

```
$ export HEADER=$(sudo cat /etc/nginx/secrets/ollama_token.conf | cut -d '"' -f 2)
$ HEADER="Authorization: $HEADER"
$ curl -k -v https://localhost/ -H "$HEADER"
```

should say something like 'hello'