

## Basic Decorator

> Create a decorator that benchmarks the performance of a function
>
> ```python
> import logging
> from math import sqrt
> from time import perf_counter
> from typing import Any, Callable
> 
> def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
>     def wrapper(*args: Any, **kwargs: Any) -> Any:
>         start_time = perf_counter()
>         value = func(*args, **kwargs)
>         end_time = perf_counter()
>         run_time = end_time - start_time
>         logging.info(f"Execution of {func.__name__} took {run_time:.2f} seconds.")
>         return value
> 
>     return wrapper  # returns a function i.e. a Callable
> 
> 
> def is_prime(number: int) -> bool:
>     if number < 2:
>         return False
>     for element in range(2, sqrt(number) + 1):
>         if number % element == 0:
>             return False
>     return True
>   
> @benchmark    # <= decorator added
> def count_prime_numbers(upper_bound: int) -> int:
>     count = 0
>     for number in range(upper_bound):
>         if is_prime(number):
>             count += 1
>     return count  
> 
> def main() -> None:
>     logging.basicConfig(level=logging.INFO)
>     count_prime_numbers(50000)
> 
> 
> if __name__ == "__main__":
>     main()
> ```
>
> On a lower level the `@benchmark` is the same as the following
>
> ```python
> def main() -> None:
>     logging.basicConfig(level=logging.INFO)
>     wrapper_fn = benchmark(count_prime_numbers)  # decorator ruturns a function
>     value = wrapper(1000)                        # that function is called with the arguements
>     logging.info(f"Number of primes: {value}")
> ```
>
> ### Update to add second decorator to do logging
>
> ```python
> def with_logging(func: Callable[..., Any]) -> Callable[..., Any]: # create new decorator
>     def wrapper(*args: Any, **kwargs: Any) -> Any:
>         logging.info(f"Calling {func.__name__}")
>         value = func(*args, **kwargs)
>         logging.info(f"Finished {func.__name__}")
>         return value
> 
>     return wrapper
> 
> ...
> 
> @with_logging  # add to function
> @benchmark
> def count_prime_numbers(upper_bound: int) -> int:
>     count = 0
>     for number in range(upper_bound):
>         if is_prime(number):
>             count += 1
>     return count
> ```



