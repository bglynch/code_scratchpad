# Pydantic

https://docs.pydantic.dev/latest/



## Models

- One of the primary ways of defining schema in Pydantic is via models. 
  Models are simply classes which inherit from [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel) and define fields as annotated attributes.

> ### Basic Usage
>
> ```python
> from pydantic import BaseModel
> 
> class User(BaseModel):
>  id: int
>  name: str = 'Jane Doe'
> 
> user = User(id='123')
> 
> assert user.id == 123   # Note that '123' was coerced to an int and its value is 123
> assert user.name == 'Jane Doe'
> assert user.model_fields_set == {'id'} # The fields which were supplied when user was initialized.
> assert user.model_dump() == {'id': 123, 'name': 'Jane Doe'}
> ```
>



## Fields

```python
from pydantic import BaseModel, Field
```

> ### Default/Auto Generated Values
>
> ```python
> class User(BaseModel):
> name: str = Field(default='John Doe')
> 
> class User(BaseModel):
> id: str = Field(default_factory=lambda: uuid4().hex)
> ```
>
> - `default_factory` to define a callable that will be called to generate a default value
>
> 
>
> ### Field aliases
>
> ##### Alias Types
>
> - `alias` parameter is used for both validation *and* serialization.
>
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
> 
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

## [Configuration](https://docs.pydantic.dev/latest/concepts/config/)

> Behaviour of Pydantic can be controlled via the [`BaseModel.model_config`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_config), and as an argument to [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter).
>
> ```python
> from pydantic import BaseModel, ConfigDict, ValidationError
> 
> 
> class Model(BaseModel):
>     model_config = ConfigDict(str_max_length=10)
>     v: str
> ```
>
> #### Usage
>
> ```python
> try:
>     m = Model(v='x' * 20)
> except ValidationError as e:
>     print(e)
> #> 1 validation error for Model
> #  v
> #    String should have at most 10 characters [type=string_too_long, input_value='xxxxxxxxxxxxxxxxxxxx', input_type=str]
> 
> ```
>
> 



## [Validators](https://docs.pydantic.dev/latest/concepts/validators/)

> ## Annotated Validators
>
> ### Basic Usage
>
> Pydantic provides a way to apply validators via use of `Annotated`. 
> You should use this whenever you want to bind validation to a type instead of model or field.
>
> ```python
> from typing import Any, List
> from typing_extensions import Annotated
> from pydantic import BaseModel, ValidationError
> from pydantic.functional_validators import AfterValidator
> 
> def check_squares(v: int) -> int:
>     assert v**0.5 % 1 == 0, f'{v} is not a square number'
>     return v
> 
> def double(v: Any) -> Any:
>     return v * 2
> 
> MyNumber = Annotated[int, AfterValidator(double), AfterValidator(check_squares)] # add validator
> 
> class DemoModel(BaseModel):
>     number: List[MyNumber]
> ```
>
> #### Usage
>
> ```python
> print(DemoModel(number=[2, 8]))
> #> number=[4, 16]
> 
> try:
>     DemoModel(number=[2, 4])
> except ValidationError as e:
>     print(e)
> 
> #> 1 validation error for DemoModel
> #  number.1
> #    Assertion failed, 8 is not a square number
> #  assert ((8 ** 0.5) % 1) == 0 [type=assertion_error, input_value=4, input_type=int]
> ```
>
> 
>
> ### Before, After, Wrap and Plain validators
>
> - `After` validators run after Pydantic's internal parsing. 
>   They are generally more type safe and thus easier to implement.
> - `Before` validators run before Pydantic's internal parsing and validation (e.g. coercion of a `str` to an `int`). 
>   These are more flexible than `After` validators since they can modify the raw input, but they also have to deal with the raw input, which in theory could be any arbitrary object.
> - `Plain` validators are like a `mode='before'` validator but they terminate validation immediately, 
>   no further validators are called and Pydantic does not do any of its internal validation.
> - `Wrap` validators are the most flexible of all. 
>   You can run code before or after Pydantic and other validators do their thing or you can terminate validation immediately, both with a successful value or an error.
>
> #### Example: `mode='wrap'` validator
>
> ```python
> import json
> from typing import Any, List
> from typing_extensions import Annotated
> from pydantic import BaseModel, ValidationError, ValidationInfo, ValidatorFunctionWrapHandler
> from pydantic.functional_validators import WrapValidator
> 
> def maybe_strip_whitespace(v: Any, handler: ValidatorFunctionWrapHandler, info: ValidationInfo) -> int:
>     if info.mode == 'json':
>         assert isinstance(v, str), 'In JSON mode the input must be a string!'
>         # you can call the handler multiple times
>         try:
>             return handler(v)
>         except ValidationError:
>             return handler(v.strip())
>     assert info.mode == 'python'
>     assert isinstance(v, int), 'In Python mode the input must be an int!'
>     # do no further validation
>     return v
> 
> MyNumber = Annotated[int, WrapValidator(maybe_strip_whitespace)]
> 
> class DemoModel(BaseModel):
>     number: List[MyNumber]
> ```
>
> #### Usage
>
> ```python
> print(DemoModel(number=[2, 8]))
> #> number=[2, 8]
> 
> print(DemoModel.model_validate_json(json.dumps({'number': [' 2 ', '8']})))
> #> number=[2, 8]
> 
> try:
>     DemoModel(number=['2'])
> except ValidationError as e:
>     print(e)
> 
> #> 1 validation error for DemoModel
> #  number.0
> #    Assertion failed, In Python mode the input must be an int!
> #  assert False
> #   +  where False = isinstance('2', int) [type=assertion_error, input_value='2', input_type=str]
> ```
>
> 
>
> ## Validation of default values
>
> Validators won't run when the default value is used. 
> This applies both to `@field_validator` validators and `Annotated` validators. 
> You can force them to run with `Field(validate_default=True)`. Setting `validate_default` to `True` has the closest behavior to using `always=True` in `validator` in Pydantic v1. 
> However, you are generally better off using a `@model_validator(mode='before')` where the function is called before the inner validator is called.
>
> ```python
> from typing_extensions import Annotated
> from pydantic import BaseModel, Field, field_validator
> 
> class Model(BaseModel):
>     x: str = 'abc'
>     y: Annotated[str, Field(validate_default=True)] = 'xyz'
> 
>     @field_validator('x', 'y')
>     @classmethod
>     def double(cls, v: str) -> str:
>         return v * 2
> ```
>
> #### Usage
>
> ```python
> print(Model())
> #> x='abc' y='xyzxyz'
> 
> print(Model(x='foo'))
> #> x='foofoo' y='xyzxyz'
> 
> print(Model(x='abc'))
> #> x='abcabc' y='xyzxyz'
> 
> print(Model(x='foo', y='bar'))
> #> x='foofoo' y='barbar'
> ```
>
> 
>
> ## Field validators
>
> If you want to attach a validator to a specific field of a model you can use the `@field_validator` decorator.
>
> - `@field_validator`s are "class methods", so the first argument value they receive is the `UserModel` class, not an instance of `UserModel`. We recommend you use the `@classmethod` decorator on them below the `@field_validator` decorator to get proper type checking.
> - the second argument is the field value to validate; it can be named as you please
> - the third argument, if present, is an instance of `pydantic.ValidationInfo`
> - validators should either return the parsed value or raise a `ValueError` or `AssertionError` (`assert` statements may be used).
> - A single validator can be applied to multiple fields by passing it multiple field names.
> - A single validator can also be called on *all* fields by passing the special value `'*'`.
>
> ```py
> from pydantic import BaseModel, ValidationError, ValidationInfo, field_validator
> 
> class UserModel(BaseModel):
>     name: str
>     id: int
> 
>     @field_validator('name')
>     @classmethod
>     def name_must_contain_space(cls, v: str) -> str:
>         if ' ' not in v:
>             raise ValueError('must contain a space')
>         return v.title()
> 
>     # you can select multiple fields, or use '*' to select all fields
>     @field_validator('id', 'name')
>     @classmethod
>     def check_alphanumeric(cls, v: str, info: ValidationInfo) -> str:
>         if isinstance(v, str):
>             # info.field_name is the name of the field being validated
>             is_alphanumeric = v.replace(' ', '').isalnum()
>             assert is_alphanumeric, f'{info.field_name} must be alphanumeric'
>         return v
> ```
>
> #### Usage
>
> ```python
> print(UserModel(name='John Doe', id=1))
> #> name='John Doe' id=1
> 
> try:
>     UserModel(name='samuel', id=1)
> except ValidationError as e:
>     print(e)
> #> 1 validation error for UserModel
>     name
>       Value error, must contain a space [type=value_error, input_value='samuel', input_type=str]
> 
> try:
>     UserModel(name='John Doe', id='abc')
> except ValidationError as e:
>     print(e)
> #> 1 validation error for UserModel
> #  id
> #    Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='abc', input_type=str]
> 
> try:
>     UserModel(name='John Doe!', id=1)
> except ValidationError as e:
>     print(e)
> #> 1 validation error for UserModel
> #  name
> #    Assertion failed, name must be alphanumeric
> #  assert False [type=assertion_error, input_value='John Doe!', input_type=str]
> ```
>
> 
>
> ## Model validators
>
> Validation can also be performed on the entire model's data using `@model_validator`.
>
> - Methods decorated with `@model_validator` should return the self instance at the end of the method. 
>   For type checking purposes, you can use `Self` from either `typing` or the `typing_extensions` backport as the return type of the decorated method. In the context of the above example, you could also use `def check_passwords_match(self: 'UserModel)' -> 'UserModel'` to indicate that the method returns an instance of the model.
>
> ```python
> from typing import Any
> from typing_extensions import Self
> from pydantic import BaseModel, ValidationError, model_validator
> 
> class UserModel(BaseModel):
>     username: str
>     password1: str
>     password2: str
> 
>     @model_validator(mode='before')
>     @classmethod
>     def check_card_number_omitted(cls, data: Any) -> Any:
>         if isinstance(data, dict):
>             assert ('card_number' not in data), 'card_number should not be included'
>         return data
> 
>     @model_validator(mode='after')
>     def check_passwords_match(self) -> Self:
>         pw1 = self.password1
>         pw2 = self.password2
>         if pw1 is not None and pw2 is not None and pw1 != pw2:
>             raise ValueError('passwords do not match')
>         return self
> ```
>
> #### Usage
>
> ```python
> print(UserModel(username='scolvin', password1='zxcvbn', password2='zxcvbn'))
> #> username='scolvin' password1='zxcvbn' password2='zxcvbn'
> 
> try:
>     UserModel(username='scolvin', password1='zxcvbn', password2='zxcvbn2')
> except ValidationError as e:
>     print(e)
> #> 1 validation error for UserModel
> #  Value error, passwords do not match [type=value_error, input_value={'username': 'scolvin', '... 'password2': 'zxcvbn2'}, input_type=dict]
> 
> try:
>     UserModel(
>         username='scolvin',
>         password1='zxcvbn',
>         password2='zxcvbn',
>         card_number='1234',
>     )
> except ValidationError as e:
>     print(e)
> #> 1 validation error for UserModel
> #  Assertion failed, card_number should not be included
> #  assert 'card_number' not in {'card_number': '1234', 'password1': 'zxcvbn', 'password2': 'zxcvbn', 'username': 'scolvin'} [type=assertion_error, input_value={'username': 'scolvin', '..., 'card_number': '1234'}, input_type=dict]
> ```
>
> 
>
> ## Handling errors in validators
>
> you can raise either a `ValueError` or `AssertionError` (including ones generated by `assert ...` statements) within a validator to indicate validation failed. You can also raise a `PydanticCustomError` which is a bit more verbose but gives you extra flexibility. Any other errors (including `TypeError`) are bubbled up and not wrapped in a `ValidationError`.
>
> ```python
> from pydantic_core import PydanticCustomError
> from pydantic import BaseModel, ValidationError, field_validator
> 
> class Model(BaseModel):
>     x: int
> 
>     @field_validator('x')
>     @classmethod
>     def validate_x(cls, v: int) -> int:
>         if v % 42 == 0:
>             raise PydanticCustomError(
>                 'the_answer_error',
>                 '{number} is the answer!',
>                 {'number': v},
>             )
>         return v
> ```
>
> #### Usage
>
> ```python
> try:
>     Model(x=42 * 2)
> except ValidationError as e:
>     print(e)
> #> 1 validation error for Model
> #  x
> #  84 is the answer! [type=the_answer_error, input_value=84, input_type=int]
> ```
>
> 

