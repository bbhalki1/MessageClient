BottleNeck:

When the number of requests for per minute increase, the performance starts to decrease and there might an increase
in the client receiving 503 or 429 (Server side). This can be reduced by scaling the application in such a way that
number of requests can be routed to each scaled service depending on the availability of resources. This can be 
acheived by either a load balancer and scaling the app vertically meaning increasing the number of servers with a proxy
server in middle or scaling the app horizontally with increase in CPU's as and when needed.

The approach which I implemented is using the docker-compose which is used to run multi-containers Docker applications.
Here in this application using the --scale is used to run multiple instances of a service. This results in multiple containers.

Knowing the port numbers to the client is a tedious process hence we can a load balancer which acts as a proxy, there by
routes the request to each available container. Configuration for nginx is created in `ngix.conf`

`docker-compose up --scale web=10` spins up 10 instances of the application