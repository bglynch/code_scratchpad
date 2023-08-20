# Docker Networking

[TOC]



## [CLI](https://docs.docker.com/engine/reference/commandline/network/)

> ```bash
> docker network ls                     # view networks
> docker network inspect bridge | jq    # inspect netwrok with the name 'bridge'
> docker network prune	                # Remove all unused networks
> ```



## Example: Use the DEFAULT bridge network

> start two different `alpine` containers on the same Docker host and 
> do some tests to understand how they communicate with each other

#### View networks

> ```bash
> docker network ls
> 
> NETWORK ID          NAME                DRIVER              SCOPE
> 17e324f45964        bridge              bridge              local
> 6ed54d316334        host                host                local
> 7092879f2cc8        none                null                local
> ```

#### Create 2 apline containers

> ###### Start Containers
>
> ```bash
> docker run -dit --name alpine1 alpine ash
> docker run -dit --name alpine2 alpine ash
> # -dit: d: detached (in the background)
> #       i: interactive (with the ability to type into it)
> #       t: TTY (so you can see the input and output)
> ```
>
> Because you have not specified any `--network` flags, the containers connect to the default `bridge` network.
>
> ###### Check they are running
>
> ```bash
> docker container ls
> 
> CONTAINER ID    IMAGE     COMMAND    CREATED          STATUS          PORTS     NAMES
> 602dbf1edc81    alpine    "ash"      4 seconds ago    Up 3 seconds              alpine2
> da33b7aa74b0    alpine    "ash"      17 seconds ago   Up 16 seconds             alpine1
> ```

#### Inspect the `bridge` network to see what containers are connected to it.

> ```bash
> docker network inspect bridge | jq
> 
> [
>   {
>   	# Information about the Network
>     "Name": "bridge",
>     "Id": "1c414fd8b8734b06532ee4c96666f3fd9e59e357281bed765956068c6211c900",
>     "Created": "2021-09-29T11:03:19.600543085Z",
>     "Scope": "local",
>     "Driver": "bridge",
>     "EnableIPv6": false,
>     "IPAM": {
>       "Driver": "default",
>       "Options": null,
>       "Config": [
>         {
>           "Subnet": "172.17.0.0/16",
>           "Gateway": "172.17.0.1"
>         }
>       ]
>     },
>     "Internal": false,
>     "Attachable": false,
>     "Ingress": false,
>     "ConfigFrom": {
>       "Network": ""
>     },
>     "ConfigOnly": false,
>     "Containers": {
>     	# Can see here, each container connected to the network
>       "11c33dbc148bd501b04d20e87d441f2511ec11cefbba73322253b2d32e6305c4": {
>         "Name": "alpine1",     # alpine1 connected to 'bridge'
>         "EndpointID": "5650ed3dc2f96b3685109a6ad3d9f546caf63b7498aaf8f894769c645ad71b04",
>         "MacAddress": "02:42:ac:11:00:03",
>         "IPv4Address": "172.17.0.3/16",  # can see IP address for the container
>         "IPv6Address": ""
>       },
>       "3c6de0ae07c0070289f3d6d54fc3c72328561878851c69ba496a59a5ac920ca6": {
>         "Name": "alpine2",    # alpine2 connected to 'bridge'
>         "EndpointID": "fbb077ec77b68b788d0c2225e2f7728598e038cae6adccc3642f9109ceb7f1af",
>         "MacAddress": "02:42:ac:11:00:04",
>         "IPv4Address": "172.17.0.4/16",
>         "IPv6Address": ""
>       }
>     },
>     "Options": {
>       "com.docker.network.bridge.default_bridge": "true",
>       "com.docker.network.bridge.enable_icc": "true",
>       "com.docker.network.bridge.enable_ip_masquerade": "true",
>       "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
>       "com.docker.network.bridge.name": "docker0",
>       "com.docker.network.driver.mtu": "1500"
>     },
>     "Labels": {}
>   }
> ]
> ```

#### The containers are running in the background. Use the `docker attach` command to connect to `alpine1`.

> ###### Enter container shell
>
> ```bash
> docker attach alpine1
> ```
>
> ###### Ping Google to make sure you can connect to the internet
>
> ```bash
> # alpine1 shell
> ping -c 2 google.com      # -c 2 : limits the command to two `ping` attempts
> 
> PING google.com (172.217.164.110): 56 data bytes
> 64 bytes from 172.217.164.110: seq=0 ttl=37 time=154.353 ms
> 64 bytes from 172.217.164.110: seq=1 ttl=37 time=153.466 ms
> 
> --- google.com ping statistics ---
> 2 packets transmitted, 2 packets received, 0% packet loss
> round-trip min/avg/max = 153.466/153.909/154.353 ms
> ```

#### Ping alpine2 from alpine1

> ###### First, ping it by its IP address, `172.17.0.4`
>
> ```bash
> # alpine1 shell
> ping -c 2 127.17.0.4
> 
> PING 127.17.0.4 (127.17.0.4): 56 data bytes
> 64 bytes from 127.17.0.4: seq=0 ttl=64 time=0.063 ms
> 64 bytes from 127.17.0.4: seq=1 ttl=64 time=0.100 ms
> 
> --- 127.17.0.4 ping statistics ---
> 2 packets transmitted, 2 packets received, 0% packet loss
> round-trip min/avg/max = 0.063/0.081/0.100 ms
> ```
>
> ###### Ping alpine2 container by 'name', `alpine2`
>
> ```bash
> # alpine1 shell
> ping -c 2 alpine2
> ping: bad address 'alpine2'
> ```

#### Clean Up

> ```bash
> docker container stop alpine1 alpine2
> docker container rm alpine1 alpine2
> ```

#### Conclusion

> - Created 2 docker containers
> - Network wasn't specified, so the default 'bridge' network was used
> - Entered shell on one container and confirmed connected to the 2nd container using `ping`



---



## Example: Custom Network, Use user-defined bridge networks

#### Create a custom network

> ###### Create a NEW network, `alpine-net`
>
> You do not need the `--driver bridge` flag since it’s the default, but this example shows how to specify it.
>
> ```bash
> docker network create --driver bridge alpine-net
> ```
>
> ###### Confirm network created
>
> ```bash
> docker network ls
> 
> NETWORK ID          NAME           DRIVER      SCOPE
> e9261a8c9a19        alpine-net     bridge      local  # newly created network
> 17e324f45964        bridge         bridge      local 
> 6ed54d316334        host           host        local
> 7092879f2cc8        none           null        local
> ```
>
> ###### Inspect the new `alpine-net` network
>
> ```bash
> docker network inspect alpine-net | jq
> [
>   {
>     "Name": "alpine-net",
>     "Id": "21f5a82fbee31cbe46cec2741ee06f8c9eed91232f4eb87e41224fe40fbf66dd",
>     "Created": "2021-09-30T13:49:48.198435Z",
>     "Scope": "local",
>     "Driver": "bridge",
>     "EnableIPv6": false,
>     "IPAM": {
>       "Driver": "default",
>       "Options": {},
>       "Config": [
>         {
>           "Subnet": "172.28.0.0/16",
>           "Gateway": "172.28.0.1"     # can see the IP address of the Gateway
>         }
>       ]
>     },
>     "Internal": false,
>     "Attachable": false,
>     "Ingress": false,
>     "ConfigFrom": {
>       "Network": ""
>     },
>     "ConfigOnly": false,
>     "Containers": {},        # can see NO containers connected to this network
>     "Options": {},
>     "Labels": {}
>   }
> ]
> ```
>
>
> Can see that this network’s gateway is `172.28.0.1`, as opposed to the default bridge network, whose gateway is `172.17.0.1`.

#### Create containers inside this network

> ###### Create containers and change network after
>
> ```bash
> docker run -dit --name alpine1 --network alpine-net alpine ash
> docker run -dit --name alpine2 --network alpine-net alpine ash
> docker run -dit --name alpine3 alpine ash
> docker run -dit --name alpine4 --network alpine-net alpine ash
> 
> docker network connect bridge alpine4    # add 'apline4' to the 'bridge' network
> ```
>
> ###### Verify Container running
>
> ```bash
> docker container ls
> 
> CONTAINER ID   IMAGE    COMMAND   CREATED              STATUS              PORTS   NAMES
> 156849ccd902   alpine   "ash"     41 seconds ago       Up 41 seconds               alpine4
> fa1340b8d83e   alpine   "ash"     51 seconds ago       Up 51 seconds               alpine3
> a535d969081e   alpine   "ash"     About a minute ago   Up About a minute           alpine2
> 0a02c449a6e9   alpine   "ash"     About a minute ago   Up About a minute           alpine1
> ```
>
> ###### Inspect `bridge` network to see containers connected
>
> ```bash
> docker network inspect bridge | jq
> 
> [
>   {
>     "Name": "bridge",
>     "Id": "1c414fd8b8734b06532ee4c96666f3fd9e59e357281bed765956068c6211c900",
>     "Created": "2021-09-29T11:03:19.600543085Z",
>     "Scope": "local",
>     "Driver": "bridge",
>     "EnableIPv6": false,
>     "IPAM": {
>       "Driver": "default",
>       "Options": null,
>       "Config": [
>         {
>           "Subnet": "172.17.0.0/16",
>           "Gateway": "172.17.0.1"
>         }
>       ]
>     },
>     "Internal": false,
>     "Attachable": false,
>     "Ingress": false,
>     "ConfigFrom": {
>       "Network": ""
>     },
>     "ConfigOnly": false,
>     "Containers": {
>       # can see "alpine3" and "alpine4" are connected to the network
>       "3a6f3b4350be5e1ff0c407f0d8fae04ab9924ee34660cd6abc91af7a692b7e0d": {
>         "Name": "alpine3",
>         "EndpointID": "de3ab87717f63adf7c7f6846d9ace71ec853dda972f89cfab8f86e31baa478fd",
>         "MacAddress": "02:42:ac:11:00:02",
>         "IPv4Address": "172.17.0.2/16",
>         "IPv6Address": ""
>       },
>       "ff7cf1829cfa61faf753d9a29e90d13331d1af38c1d9c4ae3109724f8a045923": {
>         "Name": "alpine4",
>         "EndpointID": "9089cb44f51c2ef1459a5ac5d14bee8f726833f9373d35fe83f9120dc7482d76",
>         "MacAddress": "02:42:ac:11:00:03",
>         "IPv4Address": "172.17.0.3/16",
>         "IPv6Address": ""
>       }
>     },
>     "Options": {
>       ...
>     },
>     "Labels": {}
>   }
> ]
> ```
>
> ###### Inspect the `alpine-net` network
>
> ```bash
> docker network inspect alpine-net | jq
> 
> [
>   {
>     "Name": "alpine-net",
>     "Id": "21f5a82fbee31cbe46cec2741ee06f8c9eed91232f4eb87e41224fe40fbf66dd",
>     "Created": "2021-09-30T13:49:48.198435Z",
>     "Scope": "local",
>     "Driver": "bridge",
>     "EnableIPv6": false,
>     "IPAM": {
>       "Driver": "default",
>       "Options": {},
>       "Config": [
>         {
>           "Subnet": "172.28.0.0/16",
>           "Gateway": "172.28.0.1"
>         }
>       ]
>     },
>     "Internal": false,
>     "Attachable": false,
>     "Ingress": false,
>     "ConfigFrom": {
>       "Network": ""
>     },
>     "ConfigOnly": false,
>     "Containers": {
>     	# can see "alpine1", "alpine2" and "alpine4" are connected to the network
>       "bc0a25ee688211f505764355c88958d17bd7b7530b2ecf22afaa1a64a2ee8d33": {
>         "Name": "alpine2",
>         "EndpointID": "fec5db82988c601b06cfefa0957a5b16565e4138361c22560aa51b7d039cae14",
>         "MacAddress": "02:42:ac:1c:00:03",
>         "IPv4Address": "172.28.0.3/16",
>         "IPv6Address": ""
>       },
>       "f9d5693e16cfccdf08567eb833e5745b5ad7987fbdd6dbd2b9197c5443360fda": {
>         "Name": "alpine1",
>         "EndpointID": "b5c02f3d55f6e4da9308ac5519dbd7b1a8dfc04f9f1b6da978621201ca8198ba",
>         "MacAddress": "02:42:ac:1c:00:02",
>         "IPv4Address": "172.28.0.2/16",
>         "IPv6Address": ""
>       },
>       "ff7cf1829cfa61faf753d9a29e90d13331d1af38c1d9c4ae3109724f8a045923": {
>         "Name": "alpine4",
>         "EndpointID": "8f2ed35c23530484117e07b28964de3c44f3633d32e1c8b13e774231cabcedbb",
>         "MacAddress": "02:42:ac:1c:00:04",
>         "IPv4Address": "172.28.0.4/16",
>         "IPv6Address": ""
>       }
>     },
>     "Options": {},
>     "Labels": {}
>   }
> ]
> ```
>
> 

#### Communicate between containers

> ###### Note: Automatic Service Discovery
>
> - On user-defined networks(e.g. `alpine-net`), 
>   containers can communicate by **IP address** AND **container name**
> - On default `bridge` network
>   containers can communicate only by **IP address**
>
> ###### Current State
>
> ```sql
> bridge(default)   | apline-net(custom)
> ------------------|-------------------
> alpine3           | alpine1
> alpine4           | alpine2
>                   | alpine4
> ```
>
> ###### Enter apline1 shell and ping other containers
>
> ```
> docker container attach alpine1
> ```
>
> ```bash
> # SUCCESSFUL PINGS
> ping -c 2 alpine2
> PING alpine2 (172.28.0.3): 56 data bytes
> 64 bytes from 172.28.0.3: seq=0 ttl=64 time=0.249 ms
> 64 bytes from 172.28.0.3: seq=1 ttl=64 time=0.195 ms
> --- alpine2 ping statistics ---
> 2 packets transmitted, 2 packets received, 0% packet loss
> round-trip min/avg/max = 0.195/0.222/0.249 ms
> 
> ping -c 2 alpine1
> PING alpine1 (172.28.0.2): 56 data bytes
> 64 bytes from 172.28.0.2: seq=0 ttl=64 time=0.062 ms
> 64 bytes from 172.28.0.2: seq=1 ttl=64 time=0.165 ms
> --- alpine1 ping statistics ---
> 2 packets transmitted, 2 packets received, 0% packet loss
> round-trip min/avg/max = 0.062/0.113/0.165 ms
> 
> ping -c 2 alpine4
> PING alpine4 (172.28.0.4): 56 data bytes
> 64 bytes from 172.28.0.4: seq=0 ttl=64 time=0.173 ms
> 64 bytes from 172.28.0.4: seq=1 ttl=64 time=0.478 ms
> --- alpine4 ping statistics ---
> 2 packets transmitted, 2 packets received, 0% packet loss
> round-trip min/avg/max = 0.173/0.325/0.478 ms
> ```
>
> ```bash
> # UNSUCCESSFUL PING: 
> # Cannot ping `alpine3`, by name or IP, as it's located in a different network to `alpine1`
> ping -c 2 alpine3
> ping: bad address 'alpine3'
> 
> ping -c 2 172.17.0.2
> PING 172.17.0.2 (172.17.0.2): 56 data bytes
> 
> --- 172.17.0.2 ping statistics ---
> 2 packets transmitted, 0 packets received, 100% packet loss
> ```
>
> Detach from `alpine1` using detach sequence, `CTRL` + `p` `CTRL` + `q` (hold down `CTRL` and type `p` followed by `q`).
>
> ###### Enter apline4 shell and ping other containers
>
> - `alpine4` is in both network, should be able to reach all of the other containers
>
> ```bash
> docker container attach alpine4
> ```
>
> - Note: must ping `alpine3` by IP address as its on the `bridge` network
>
> ```bash
> # SUCCESSFUL PING
> ping -c 2 alpine1
> PING alpine1 (172.28.0.2): 56 data bytes
> 64 bytes from 172.28.0.2: seq=0 ttl=64 time=0.160 ms
> 64 bytes from 172.28.0.2: seq=1 ttl=64 time=0.104 ms
> --- alpine1 ping statistics ---
> 2 packets transmitted, 2 packets received, 0% packet loss
> round-trip min/avg/max = 0.104/0.132/0.160 ms
> 
> ping -c 2 alpine2
> PING alpine2 (172.28.0.3): 56 data bytes
> 64 bytes from 172.28.0.3: seq=0 ttl=64 time=0.115 ms
> 64 bytes from 172.28.0.3: seq=1 ttl=64 time=0.201 ms
> --- alpine2 ping statistics ---
> 2 packets transmitted, 2 packets received, 0% packet loss
> round-trip min/avg/max = 0.115/0.158/0.201 ms
> 
> ping -c 2 172.17.0.2  # <= alpine3 IP address
> PING 172.17.0.2 (172.17.0.2): 56 data bytes
> 64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.173 ms
> 64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.192 ms
> --- 172.17.0.2 ping statistics ---
> 2 packets transmitted, 2 packets received, 0% packet loss
> round-trip min/avg/max = 0.173/0.182/0.192 ms
> 
> ping -c 2 alpine4
> PING alpine4 (172.28.0.4): 56 data bytes
> 64 bytes from 172.28.0.4: seq=0 ttl=64 time=0.066 ms
> 64 bytes from 172.28.0.4: seq=1 ttl=64 time=0.168 ms
> --- alpine4 ping statistics ---
> 2 packets transmitted, 2 packets received, 0% packet loss
> round-trip min/avg/max = 0.066/0.117/0.168 ms
> ```
>
> ```bash
> # UNSUCCESSFUL PING
> ping -c 2 alpine3    # <= unsuccessful as 'bridge' netwrok doesn't have 'automatic service discovery'
> ping: bad address 'alpine3'
> ```

#### Clean Up: Delete and Remove Containers and Bridge

> ```bash
> docker container stop alpine1 alpine2 alpine3 alpine4
> docker container rm alpine1 alpine2 alpine3 alpine4
> docker network rm alpine-net
> ```



---

## Networking features in Docker Desktop for Mac

https://docs.docker.com/desktop/mac/networking/



### I want to connect from a container to a service on the host

Run a python server on port 8000

```bash
python -m http.server 8000
```

Run a container and make a request to that server

```bash
$ docker run --rm -it alpine sh

/ # apk add curl
fetch https://dl-cdn.alpinelinux.org/alpine/v3.14/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.14/community/x86_64/APKINDEX.tar.gz
(1/5) Installing ca-certificates (20191127-r5)
(2/5) Installing brotli-libs (1.0.9-r5)
(3/5) Installing nghttp2-libs (1.43.0-r0)
(4/5) Installing libcurl (7.79.1-r0)
(5/5) Installing curl (7.79.1-r0)
Executing busybox-1.33.1-r3.trigger
Executing ca-certificates-20191127-r5.trigger
OK: 8 MiB in 19 packages

/ # curl http://host.docker.internal:8000
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
</ul>
<hr>
</body>
</html>
```



### I want to connect from a container to a container ported to the host

Run an nginx webserver on port 80

```bash
$ docker run -d -p 80:80 --name webserver nginx
```

Run a simple alpine container.
Can see that the curl return the webpage that's running on `http://localhost:80`

```bash
$ docker run --rm -it alpine sh

/ # apk add curl

/ # curl http://host.docker.internal:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```



---

## Links

- https://docs.docker.com/network/network-tutorial-standalone/
