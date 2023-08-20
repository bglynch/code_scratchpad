# generators



> ###### Example of memory used when computing the sum of a list
>
> ```py
> import sys
> 
> # sum usinf a list
> my_list = [i for i in range(1000)]
> print(sum(my_list))
> print(sys.getsizeof(my_list), "bytes")
> 
> # sum using a generator
> my_gen = (i for i in range(1000))   # round brackets create a generatot, square([]) brackets creates a list
> print(sum(my_gen))
> print(sys.getsizeof(my_gen), "bytes")
> 
> Out[1]: 49995000
> Out[2]: 87632 bytes
> Out[3]: 49995000
> Out[4]: 128 bytes  # <= can see the generator uses alot less memory
> ```

