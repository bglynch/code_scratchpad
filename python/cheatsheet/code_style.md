# Self Documenting Code

https://javascript.plainenglish.io/the-ultimate-guide-to-writing-self-documenting-code-998ea9a38bd3

## Naming Conventions



### Function Names

#### Example using fucntion to get a User's Id

##### Bad

```python
get_user_id()
```

##### Good => using more descriptive function name

###### 	Get UserId, no parameters

```javascript
getUserIdFromCookie()
getUserIdFromStorage()
```

###### 	Get UserId, using properties you send to that function.   Uses `from`

```javascript
getUserIdFromBlogpost(blogpostdata);
getUserIdFromChat(chatObject);
getUserIdFromFriend(friendObject);
```

###### 	Get UserId, using specific other property tied to that user.  Uses `with`

```javascript
getUserIdWithEmail(email);
getUserIdWithIP(ip);
```



#### `from`  vs  `with`

- `from` in a function-name defines you should provide an object from which the function can return the first part of the function

##### examples

```javascript
var userId = getUserIdFromBlog(blog)
var url = getUrlFromBlog(blog)
var numberOfWords = getNumberOfWordsFromBlog(blog)
```

function name defines what you **get from it**, and it defines **what it needs** in order for you to get what you want



- `with` in a function-name defines the function will be able to fetch data from another source based on the information you’re giving.

```javascript
var userId = getUserIdWithEmail(email)
var blog = getBlogWithDateStamp(date)
var user = getUserWithUserId(userId);
```

`with` returns information, but we get information back that we couldn’t have known without an external source



Types of functions

- create

- get

  - get
  - find
  - extract

- set something

  

  **mutating functions**

- modify

  - convert something from x to y
  - transform
  - modify

- clean

  - parse
  - normalise



- filter
- map
- reduce







### Filenames

