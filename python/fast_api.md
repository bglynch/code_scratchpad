# Fast API

https://fastapi.tiangolo.com/

[TOC]



## Setup

```bash
pip install "fastapi[all]"                # install fastapi and additional packages
pip install fastapi "uvicorn[standard]" # install fastapi and basic packages
```

### Basic app

```python
from fastapi import FastAPI

app = FastAPI()   # create and name the app

@app.get("/")     # define the path
async def root() -> dict[str, str]:   # path operation function
    return {"message": "Hello World"}

```

### Run

```bash
uvicorn main:app --reload
```



#### OpenAPI docs out of the box

> http://127.0.0.1:8000/docs
>
> http://127.0.0.1:8000/redoc

### Open API

> ##### Schema
>
> - A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.



---

## [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)

> #### Type enforcement
>
> ```python
> # path with path parameter and type
> @app.get("/items/{item_id}")
> async def read_item(item_id: int):
>     return {"item_id": item_id}
> ```
>
> `item_id` is declared to be an `int`,  this gives out of the box type checking
>
> data validation is performed under the hood by **Pydantic**
>
> #### Value enforcement using `Enum`
>
> - Can return Enums and they will be converted to corresponding values
>
> ```python
> # path with strict param values using Enum
> class ModelName(str, Enum): # By inheriting from str the API docs will be able to know that the values must be of type string
>     alexnet = "alexnet"
>     resnet = "resnet"
>     lenet = "lenet"
> 
> @app.get("/models/{model_name}")
> async def get_model(model_name: ModelName):
>     if model_name is ModelName.alexnet:  # comparison using Enum
>         return {"model_name": model_name, "message": "Deep Learning FTW!"}
> 
>     if model_name.value == "lenet":   # comparison using string
>         return {"model_name": model_name, "message": "LeCNN all the images"}
> 
>     return {"model_name": model_name, "message": "Have some residuals"}
> ```

## [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)

> - When you declare other function parameters that are not part of the path parameters, 
>   they are automatically interpreted as "query" parameters.
> - E.g: **http://127.0.0.1:8000/items/?skip=0&limit=10**
>
> ```python
> fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
> 
> @app.get("/items/")
> async def read_item(skip: int = 0, limit: int = 10):
>     return fake_items_db[skip : skip + limit]
> ```
>
> ### Optional Parameters
>
> - can declare optional query parameters, by setting their default to `None`
> - if param is `bool`, will be auto conversion of strings like `True, true, yes, on, 1`
> - if a default is not given to a query param, it will be **required**
>
> ```python
> # http://127.0.0.1:8000/items-2/1?q=hello
> @app.get("/items/{item_id}")
> async def read_item(item_id: str, q: str | None = None):
>     if q:
>         return {"item_id": item_id, "q": q}
>     return {"item_id": item_id}
> ```
>
> #### Validation
>
> - having `Query(max_length=50)` inside of `Annotated`, we are telling FastAPI that we want it to extract this value from the query parameters
>
> ```python
> # string validation
> @app.get("/items/")
> async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
>     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
>     if q:
>         results.update({"q": q})
>     return results
> 
> # other validaitions
> async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
> async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None):
>   
> # int validation
> item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
> # float validataion
> size: Annotated[float, Query(gt=0, lt=10.5)],
> ```
>



## [Request Body](https://fastapi.tiangolo.com/tutorial/body/)

> #### Basic
>
> ```python
> class Item(BaseModel):
>     name: str
>     description: str | None = None
>     price: float
>     tax: float | None = None
> 
> @app.post("/items/")
> async def create_item(item: Item):
>     return item
> ```
>
> - Create class from `pydantic BaseModel`
> - If `attribute` has default value it will not be required in the request body
> - If not, it will fail with `422` if the attribute is missing
>
> #### Request body + path + query parameters¶
>
> ```python
> @app.put("/items/{item_id}")
> async def update_item(item_id: int, item: Item, q: str | None = None):
>     result = {"item_id": item_id, **item.dict()}
>     if q:
>         result.update({"q": q})
>     return result
> ```
>
> #### Multiple Prameters
>
> ```python
> class User(BaseModel):
>     username: str
>     full_name: str | None = None
> 
> 
> @app.put("/items/{item_id}")
> async def update_item(item_id: int, item: Item, user: User):
>     results = {"item_id": item_id, "item": item, "user": user}
>     return results
> ```
>
> - Sample request and response
>
> - ```json
>   {
>       "item": {
>           "name": "Foo",
>           "description": "The pretender",
>           "price": 42.0,
>           "tax": 3.2
>       },
>       "user": {
>           "username": "dave",
>           "full_name": "Dave Grohl"
>       }
>   }
>           
>   {
>     "item_id": 1,
>     "item": {
>       "name": "Foo",
>       "description": "The pretender",
>       "price": 42.0,
>       "tax": 3.2
>     },
>     "user": {
>       "username": "dave",
>       "full_name": "Dave Grohl"
>     }
>           
>   ```

## Model Data Types

> #### Basic
>
> ```python
> from pydantic import Field
> 
> class Item(BaseModel):
>     name: str
>     description: str | None = Field(default=None, title="The description of the item", max_length=300)
>     price: float = Field(gt=0, description="The price must be greater than zero")
>     tax: float | None = None
> ```
>
> #### List Fields
>
> ```python
> class Item(BaseModel):
>   ...
>   tags: list[str] = []
>   # using set will remove duplicates
>   tags: set[str] = set()
> ```
>
> #### Nested
>
> ```python
> class Image(BaseModel):
>     url: str
>     name: str
> 
> class Item(BaseModel):
>     ...
>     image: Image | None = None
> 
> ```
>
> - Expected Body
>
>   ```js
>   {
>       "name": "Foo",
>       "description": "The pretender",
>       "price": 42.0,
>       "tax": 3.2,
>       "tags": ["rock", "metal", "bar"],
>       "image": {
>           "url": "http://example.com/baz.jpg",
>           "name": "The Foo live"
>       }
>   }
>   ```
>
> #### Special Types
>
> Special types can be imported from Pydantic: [Pydantic's exotic types](https://docs.pydantic.dev/latest/concepts/types/).
>
> ```python
> from pydantic import BaseModel, HttpUrl
> 
> class Image(BaseModel):
>   url: HttpUrl
>   ...
> ```
>
> #### Deeply Nested Models
>
> ```python
> class Image(BaseModel):
>     url: HttpUrl
>     ...
> 
> class Item(BaseModel):
>     ...
>     images: list[Image] | None = None
> 
> class Offer(BaseModel):
>     ...
>     items: list[Item]
> 
> @app.post("/offers/")
> async def create_offer(offer: Offer):
>     return offer
> ```

## Header Parameters

> - `Header` auto converts underscore to hyphen, this can be turned off
>
> ```python
> from fastapi import Header
> 
> @app.get("/items/")
> async def read_items(user_agent: Annotated[str | None, Header()] = None):
>     return {"User-Agent": user_agent}
> 
> # turn of underscore conversion
> async def read_items(strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,):
> ```

## Response Model

> #### Basic
>
> ```python
> class Item(BaseModel):
>     name: str
>     description: str | None = None
>     price: float
>     tax: float | None = None
>     tags: list[str] = []
> 
> @app.post("/items/")
> async def create_item(item: Item) -> Item:
>     return item
> 
> @app.get("/items/")
> async def read_items() -> list[Item]:
>     return [
>         Item(name="Portal Gun", price=42.0),
>         Item(name="Plumbus", price=32.0),
>     ]
> ```
>
> #### `response_model` parameter
>
> - you could want to **return a dictionary** or a database object, but **declare it as a Pydantic model**
>
> ```python
> @app.post("/items/", response_model=Item)
> async def create_item(item: Item) -> Any:
>     return item
> 
> @app.get("/items/", response_model=list[Item])
> async def read_items() -> Any:
>     return [
>         {"name": "Portal Gun", "price": 42.0},
>         {"name": "Plumbus", "price": 32.0},
>     ]
> ```
>
> #### Output model
>
> - add model for output to hide user password
>
> ```python
> class UserIn(BaseModel):
>     username: str
>     password: str
>     email: EmailStr
>     full_name: str | None = None
> 
> 
> class UserOut(BaseModel):
>     username: str
>     email: EmailStr
>     full_name: str | None = None
> 
> 
> @app.post("/user/", response_model=UserOut) # <= set response_model as UserOut
> async def create_user(user: UserIn) -> Any:
>     return user
> ```
>
> - Cleaner option to reduce duplication
>
> ```python
> class BaseUser(BaseModel): # create BaseUser
>     username: str
>     email: EmailStr
>     full_name: str | None = None
> 
> class UserIn(BaseUser): # Inherit from BaseUser
>     password: str
> 
> @app.post("/user/")
> async def create_user(user: UserIn) -> BaseUser:
>     return user
> ```
>
> #### Exclude Unset attributes
>
> ```python
> class Item(BaseModel):
>     name: str
>     description: str | None = None
>     price: float
>     tax: float = 10.5
>     tags: list[str] = []
> 
> items = {
>     "foo": {"name": "Foo", "price": 50.2},
>     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
>     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
> }
> 
> @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
> async def read_item(item_id: str):
>     return items[item_id]
> ```
>
> - response for foo
>
>   ```json
>   {
>       "name": "Foo",
>       "price": 50.2
>   }
>   ```
>
> #### Include and Exclude
>
> ```python
> @app.get(
>     "/items/{item_id}/name",
>     response_model=Item,
>     response_model_include={"name", "description"}, # choose fields to include
> )
> async def read_item_name(item_id: str):
>     return items[item_id]
> 
> 
> @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"}) # choose fields to exclude
> async def read_item_public_data(item_id: str):
>     return items[item_id]
> ```

## Error Handling

> #### Basic
>
> ```python
> from fastapi import HTTPException
> 
> items = {"foo": "The Foo Wrestlers"}
> 
> @app.get("/items/{item_id}")
> async def read_item(item_id: str):
>     if item_id not in items:
>         raise HTTPException(status_code=404, detail="Item not found")  # raise error
>     return {"item": items[item_id]}
> ```
>
> - Response 
>
>   ```json
>   {"detail": "Item not found"}
>   ```
>
> #### Basic + Custom Header
>
> ```python
> @app.get("/items-header/{item_id}")
> async def read_item_header(item_id: str):
>     if item_id not in items:
>         raise HTTPException(
>             status_code=404,
>             detail="Item not found",
>             headers={"X-Error": "There goes my error"}, # add custom header
>         )
>     return {"item": items[item_id]}
> ```
>
> #### Custom Exceptions
>
> - You can add custom exception handlers with [the same exception utilities from Starlette](https://www.starlette.io/exceptions/).
>
> ```python
> class UnicornException(Exception):
>   def __init__(self, name: str):
>       self.name = name
> 
> # add custom exception handler
> @app.exception_handler(UnicornException)
> async def unicorn_exception_handler(request: Request, exc: UnicornException):
>     return JSONResponse(
>         status_code=418,
>         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
>     )
>     
> @app.get("/unicorns/{name}")
> async def read_unicorn(name: str):
>     if name == "yolo":
>         raise UnicornException(name=name) # raise custom exception
>     return {"unicorn_name": name}    
> ```

## PUT Request

> ```python
> class Item(BaseModel):
>     name: str | None = None
>     description: str | None = None
>     price: float | None = None
>     tax: float = 10.5
>     tags: list[str] = []
> 
> items = {
>     "foo": {"name": "Foo", "price": 50.2},
>     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
>     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
> }
> 
> @app.get("/items/{item_id}", response_model=Item)
> async def read_item(item_id: str):
>     return items[item_id]
> 
> @app.put("/items/{item_id}", response_model=Item)
> async def update_item(item_id: str, item: Item):
>     update_item_encoded = jsonable_encoder(item)
>     items[item_id] = update_item_encoded
>     return update_item_encoded
> ```
>
> - something to be aware of is that, for a PUT is the value is not set and the Model has a default value, the default value will be used to overwrite the DB value

## PATCH Request

> - used for partial update, 
>
> ```python
> @app.get("/items/{item_id}", response_model=Item)
> async def read_item(item_id: str):
>     return items[item_id]
> 
> 
> @app.patch("/items/{item_id}", response_model=Item)
> async def update_item(item_id: str, item: Item):
>     stored_item_data = items[item_id]
>     stored_item_model = Item(**stored_item_data)
>     update_data = item.dict(exclude_unset=True) # can use exclude_unset so default values are not used to overwrite
>     updated_item = stored_item_model.copy(update=update_data)
>     items[item_id] = jsonable_encoder(updated_item)
>     return updated_item
> ```

## Dependency

> **"Dependency Injection"** means, in programming, that there is a way for your code (in this case, your *path operation functions*) to declare things that it requires to work and use: "dependencies".

> #### Basic Example
>
> ```python
> from fastapi import Depends
> 
> async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
>     return {"q": q, "skip": skip, "limit": limit}
> 
> @app.get("/items/")
> async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
>     return commons
> 
> @app.get("/users/")
> async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
>     return commons
> ```
>
> #### Reduced Duplication
>
> ```python
> CommonsDep = Annotated[dict, Depends(common_parameters)]
> 
> @app.get("/items/")
> async def read_items(commons: CommonsDep):
>     return commons
> 
> @app.get("/users/")
> async def read_users(commons: CommonsDep):
>     return commons
> ```

## Settings and Environment Vars

> Fortunately, Pydantic provides a great utility to handle these settings coming from environment variables with [Pydantic: Settings management](https://docs.pydantic.dev/latest/usage/pydantic_settings/).
>
> - pydantic reads environment vars in a **case-insensitive** way
> - data will be converted and validate
>
> ```python
> from fastapi import FastAPI
> from pydantic_settings import BaseSettings
> 
> 
> class Settings(BaseSettings):
>     app_name: str = "Awesome API"
>     admin_email: str
>     items_per_user: int = 50
> 
> 
> settings = Settings()
> app = FastAPI()
> 
> 
> @app.get("/info")
> async def info():
>     return {
>         "app_name": settings.app_name,
>         "admin_email": settings.admin_email,
>         "items_per_user": settings.items_per_user,
>     }
> ```
>
> #### Settings from `.env` file
>
> ```python
> from pydantic_settings import BaseSettings, SettingsConfigDict
> 
> 
> class Settings(BaseSettings):
>     app_name: str = "Awesome API"
>     admin_email: str
>     items_per_user: int = 50
> 
>     model_config = SettingsConfigDict(env_file=".env")
> ```
>



---

## Appendix: Pydantic

### Models

- One of the primary ways of defining schema in Pydantic is via models. 
  Models are simply classes which inherit from [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel) and define fields as annotated attributes.

> #### Basic Usage
>
> ```python
> from pydantic import BaseModel
> 
> class User(BaseModel):
>     id: int
>     name: str = 'Jane Doe'
> 
> user = User(id='123')
> 
> assert user.id == 123   # Note that '123' was coerced to an int and its value is 123
> assert user.name == 'Jane Doe'
> assert user.model_fields_set == {'id'} # The fields which were supplied when user was initialized.
> assert user.model_dump() == {'id': 123, 'name': 'Jane Doe'}
> ```
>
> 

### Fields

```python
from pydantic import BaseModel, Field
```

> #### Default/Auto Generated Values
>
> ```python
> class User(BaseModel):
>     name: str = Field(default='John Doe')
> 
> class User(BaseModel):
>     id: str = Field(default_factory=lambda: uuid4().hex)
> ```
>
> - `default_factory` to define a callable that will be called to generate a default value
>
> 
>
> #### Field aliases
>
> ##### Alias Types
>
> - `alias` parameter is used for both validation *and* serialization.
> - Can use them seperatly by `validation_alias` and `serialization_alias`
>
> - ```python
>   Field(..., alias='foo')
>   Field(..., validation_alias='foo')
>   Field(..., serialization_alias='foo')
>   ```
>
> ```python
> class User(BaseModel):
>     name: str = Field(..., alias='username')
> 
> user = User(username='johndoe')  
> print(user)
> #> name='johndoe'
> print(user.model_dump(by_alias=True))  
> #> {'username': 'johndoe'}
> ```
>
> ```python
> class User(BaseModel):
>     name: str = Field(..., validation_alias='username')
> 
> user = User(username='johndoe')  
> print(user)
> #> name='johndoe'
> print(user.model_dump(by_alias=True))  
> #> {'name': 'johndoe'}
> ```
>
> ```python
> class User(BaseModel):
>     name: str = Field(..., serialization_alias='username')
> 
> user = User(name='johndoe')  
> print(user)
> #> name='johndoe'
> print(user.model_dump(by_alias=True))  
> #> {'username': 'johndoe'}
> ```
>
> 
>
> ### String Constraints
>
> ```python
> class Foo(BaseModel):
>     short: str = Field(min_length=3)
>     long: str = Field(max_length=10)
>     regex: str = Field(pattern=r'^\d*$')  
> 
> foo = Foo(short='foo', long='foobarbaz', regex='123')
> print(foo)
> #> short='foo' long='foobarbaz' regex='123'
> ```
>
> 
>
> ### The computed_field decorator
>
> ```python
> class Box(BaseModel):
>     width: float
>     height: float
>     depth: float
> 
>     @computed_field
>     def volume(self) -> float:
>         return self.width * self.height * self.depth
> 
> 
> b = Box(width=1, height=2, depth=3)
> print(b.model_dump())
> #> {'width': 1.0, 'height': 2.0, 'depth': 3.0, 'volume': 6.0}
> ```

