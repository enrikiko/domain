# Set your domain
## Steps:

1. Generate server:
	- python3 -m http.server 8080
	- python3 -m http.server 8081
2. Install haproxy
	- sudo apt-get install haproxy
	- sudo service haproxy status
	- sudo vim /etc/haproxy/haproxy.cfg
	- sudo service haproxy restart
3. Configure local router to local ip
4. Create Recort Set Route53 to your public ip
5. Create AWS policy to change Route53
6. Create lambda function to change Route53
7. Create Api Gategate to forward public ip to lambda
9. Create a docker container that execute lambda

> [Youtube Tutorial](https://www.youtube.com/watch?v=kn9Y-CBiyGY)
