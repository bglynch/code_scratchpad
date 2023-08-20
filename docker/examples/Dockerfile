# This Dockerfile has the ability to store multiple images
# -t : choose which image to use
# -f : specify Dockerfile 

############################ HELLO WORLD ############################# 
# BUILD: docker build -t hello_world --target helloworld -f Dockerfile.hello_world .
FROM alpine as helloworld
CMD ["echo", "Helloworld!"]


############################ View File System with tree ############### 
# BUILD: docker build -t hello_tree --target tree -f Dockerfile.hello_world .
FROM alpine as tree
RUN apk add --no-cache tree
RUN mkdir -p /BRIAN/FOLDER    
ENV foo="/bar"
CMD ["tree", "-L", "1"]

############################ Add env variable ############### 
# BUILD: docker build -t hello_envar --target envar .
FROM alpine as envar  
ENV foo="/bar"
CMD ["env"]


# ============ HOW TO RUN
# RUN: docker run --rm hello_world