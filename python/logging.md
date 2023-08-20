## Logging

- log service: give you easier eay to visualise and search log, alos how  log are they saved and back-up 
  - e.g Papertrail
- 

##### Basic setup

```python
import logging

def main() -> None:
	logging.basicConfig(level=logging.WARNING)  # can change this to change which level shows
  
  logging.debug("This is a debug message")
  logging.info("This is a info message")
  logging.warning("This is a warning message")
  logging.error("This is a error message")
  logging.critical("This is a critical message")

if __name__ == "__main__":
  main()
```

##### Change formatting

```python
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s %(level)s %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S",
  filename="basic.log"
)
```

---

## Links

- [Logging in Python like a pro](https://guicommits.com/how-to-log-in-python-like-a-pro/)
- [A Comprehensive Guide to Logging in Python](https://betterstack.com/community/guides/logging/how-to-start-logging-with-python/): Blog on logging
- [How to Get Started with Logging in Django](https://betterstack.com/community/guides/logging/how-to-start-logging-with-django/): 
