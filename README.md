# Message Flask App

This is an implementation of Flask Micro web-service which runs as a dockerized container


## Steps to Run

**NOTE** : Docker should be installed if using 

Build the image using `docker-compose build `

	> Building web
	Step 1/5 : FROM python:3.6.3
	 ---> a8f7167de312
	Step 2/5 : ADD . /code
	 ---> 7ac907330161
	Step 3/5 : WORKDIR /code
	 ---> Running in 70b017987134
	Removing intermediate container 70b017987134
	 ---> 3ccebed1bbff
	Step 4/5 : RUN pip install -r requirements.txt
	 ---> Running in 3d6ef5bedc27
	Collecting flask (from -r requirements.txt (line 1))
	  Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
	Collecting redis (from -r requirements.txt (line 2))
	  Downloading https://files.pythonhosted.org/packages/ac/a7/cff10cc5f1180834a3ed564d148fb4329c989cbb1f2e196fc9a10fa07072/redis-3.2.1-py2.py3-none-any.whl (65kB)
	Collecting Werkzeug>=0.14 (from flask->-r requirements.txt (line 1))
	  Downloading https://files.pythonhosted.org/packages/18/79/84f02539cc181cdbf5ff5a41b9f52cae870b6f632767e43ba6ac70132e92/Werkzeug-0.15.2-py2.py3-none-any.whl (328kB)
	Collecting Jinja2>=2.10 (from flask->-r requirements.txt (line 1))
	  Downloading https://files.pythonhosted.org/packages/1d/e7/fd8b501e7a6dfe492a433deb7b9d833d39ca74916fa8bc63dd1a4947a671/Jinja2-2.10.1-py2.py3-none-any.whl (124kB)
	Collecting itsdangerous>=0.24 (from flask->-r requirements.txt (line 1))
	  Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
	Collecting click>=5.1 (from flask->-r requirements.txt (line 1))
	  Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
	Collecting MarkupSafe>=0.23 (from Jinja2>=2.10->flask->-r requirements.txt (line 1))
	  Downloading https://files.pythonhosted.org/packages/b2/5f/23e0023be6bb885d00ffbefad2942bc51a620328ee910f64abe5a8d18dd1/MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl
	Installing collected packages: Werkzeug, MarkupSafe, Jinja2, itsdangerous, click, flask, redis
	Successfully installed Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.2 click-7.0 flask-1.0.2 itsdangerous-1.1.0 redis-3.2.1
	Removing intermediate container 3d6ef5bedc27
	 ---> 3b126041ba5d
	Step 5/5 : CMD python app.py
	 ---> Running in f04379609a10
	Removing intermediate container f04379609a10
	 ---> ace57a816f2a
	Successfully built ace57a816f2a
	Successfully tagged messagesappdocker_web:latest

Start the container for service using `docker-compose up`
	
	>Starting messagesappdocker_redis_1 ... done
	Starting messagesappdocker_web_1   ... done
	Starting messagesappdocker_nginx_1 ... done
	Attaching to messagesappdocker_redis_1, messagesappdocker_web_1, messagesappdocker_nginx_1
	web_1    |  * Serving Flask app "app" (lazy loading)
	web_1    |  * Environment: production
	web_1    |    WARNING: Do not use the development server in a production environment.
	redis_1  | 1:C 07 Apr 2019 02:47:59.090 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
	redis_1  | 1:C 07 Apr 2019 02:47:59.090 # Redis version=5.0.4, bits=64, commit=00000000, modified=0, pid=1, just started
	redis_1  | 1:C 07 Apr 2019 02:47:59.090 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
	redis_1  | 1:M 07 Apr 2019 02:47:59.091 * Running mode=standalone, port=6379.
	redis_1  | 1:M 07 Apr 2019 02:47:59.091 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
	redis_1  | 1:M 07 Apr 2019 02:47:59.091 # Server initialized
	redis_1  | 1:M 07 Apr 2019 02:47:59.091 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
	redis_1  | 1:M 07 Apr 2019 02:47:59.091 * DB loaded from disk: 0.000 seconds
	redis_1  | 1:M 07 Apr 2019 02:47:59.091 * Ready to accept connections
	web_1    |    Use a production WSGI server instead.
	web_1    |  * Debug mode: on
	web_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
	web_1    |  * Restarting with stat
	web_1    |  * Debugger is active!
	web_1    |  * Debugger PIN: 266-083-898

## Scaling

Detailed description given in Scaling.MD

Steps to run/increase containers

	docker-compose up --scale web=5

 
## API

POST : `curl -L -H "Content-type: application/json" \
-X POST http://0.0.0.0:4000/messages -d '{"message":"foo"}'`

Output:

    {
	    "digest": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
	}

GET: `curl http://0.0.0.0:4000/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae`

Output:

    {
	    "message" : "foo"
    }

GET: `curl http://0.0.0.0:4000/messages/11111`

    {
      "err_msg": "Message not found"
    }

POST (Non JSON): `curl -L -H "Content-type: application/aaaa" \
-X POST http://0.0.0.0:4000/messages -d '{"message":"foo"}'`

Output:

    {
      "error": "Unsupported Media Type"
    }
