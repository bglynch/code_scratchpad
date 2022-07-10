# Makefile

##### Useful Resources

- https://makefiletutorial.com/#getting-started
- https://devhints.io/makefile
- https://gist.github.com/isaacs/62a2d1825d04437c6f08

Running

```bash
make <target>
make -f <filename/filepath> <target>
```



### Add print statements

```makefile
# general
make_target:
	@echo "===================="               # basic
	@echo ${TMP}															 # varible
	@echo "====\033[33m text \033[0m======"		 # add color

# time 
START=`date +%s`  # set start time globally
make_target:
	@sleep 1
	@echo "\033[33mtime: $$(( $(START) - $(shell date "+%s") ))\033[0m"
```



### Variables

##### Assignment

```makefile
# =   only looks for the variables when the command is used, not when it's defined
# :=  normal imperative programming. only those defined so far get expanded. allows appending to a variable
# ?=  only sets variables if they have not yet been set
# +=  append to a variable

make:
	@$(eval TMP := BRIAN)    # assign/overwrite varible{

# use makefile variable
$(VAR) or ${VAR}

# use bash variable
$$VAR
```



### ifeq

DO NOT indent `ifeq, else, endif`

```makefile
# conditional if/else
foo = ok
all:
ifeq ($(foo), ok)
	@echo "foo equals ok"
else
	@echo "nope"
endif


# Check if a variable is empty
nullstring =
foo = $(nullstring) # end of line; there is a space here
all:
ifeq ($(strip $(foo)),)
	@echo "foo is empty after being stripped"
endif
ifeq ($(nullstring),)
	@echo "nullstring doesn't even have spaces"
endif


# BASH if statement
redeploy_push: __check_tfstate_exists
	@$(eval updated_images := $(shell python -c 'from scripts.redeploy_dev import get_services_to_be_redeployed;get_services_to_be_redeployed()' || exit;))
	@for image_name in $(updated_images); do\
		if [ $$image_name = "service_1" ];then \
			echo "- \033[33mTagging and Pushing SERVICE_1033[0m"; \
			docker tag $(SERVICE_1_LOCAL_IMAGE) $(SERVICE_1_REMOTE_IMAGE); \
			docker push $(SERVICE_1_REMOTE_IMAGE); \
		elif [ $$image_name = "service_2" ];then \
			echo "- \033[33mTagging and Pushing SERVICE_2\033[0m"; \
			docker tag $(SERVICE_2_LOCAL_IMAGE) $(SERVICE_2_REMOTE_IMAGE); \
			docker push $(SERVICE_2_REMOTE_IMAGE); \
		elif [ $$image_name = "service_3" ];then \
			echo "- \033[33mTagging and Pushing SERVICE_3\033[0m"; \
			docker tag $(SERVICE_3_LOCAL_IMAGE) $(SERVICE_3_REMOTE_IMAGE); \
			docker push $(SERVICE_3_REMOTE_IMAGE); \
		fi;\
	done
```



#### for loop

```makefile
LIST = one two three
not:
	@	for i in $(LIST); do echo $$i; done
```



#### error or exit

```makefile
# ================================================= . 
ifeq ($(shell svnversion --version | sed s/[^0-9\.]*://), 1.4) 
    $(error Bad svnversion v1.4, please install v1.6)
endif 

# ================================================= exit with message
single-containerized-test: 
	@docker images | grep search-term && echo "hello" || \
		(echo "Exit message"; exit 1)
	@echo "foo is empty after being stripped"

> Exit message
> make: *** [single-containerized-test] Error 1

# ================================================= ..
```



#### To Examine

```
.ONESHELL
```

