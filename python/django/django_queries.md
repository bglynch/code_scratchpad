# Django Queries

## Managers and QuerySets

Making Queries

- `QuerySets`
- Laziness
- `filter()` and `exclude()`
- Limiting and ordering results
- Relations
- Aggregations
- `F()` and `Q()`

#### Model Manager

> Every model has a manager instance, you can see when you do the following in the shell
>
> ```python
> Products.objects
> >> <django.db.models.manager.Manager object at 0x7fcd83ca1b00>
> ```
>
> The manager is an Interface for making queries on the Products table

#### Laziness

> Query sets are lazy. What that means is the SQL call will not be made until it is needed
>
> Example: Getting a list of Products
>
> ```python
> # view.py
> products = products.filter(category__name=category)
> return render(request, "store/filter.html", {'products': products, 'category_name':name})
> 
> # template
> {% for p in products %}     # <== SQL call not made until here
> <div class="row">
>   <div class="col-md-3" style="padding-bottom:1em;">
>       <h3 class="text-secondary">{{ p.name }}</h3>
>       <div class="text-primary">${{ p.price }}</div>
>       <div class="text-primary">In stock: {{ p.stock_count }}</div>
>   </div>
> </div>
> {% empty %}
> Nothing to show.
> {% endfor %}
> ```
>
> Example 2:
>
> ```python
> # QuerySets are lazy. The following does not run any SQL
> in_stock = Products.objects.filter(stock_count__gt=0)
> 
> # This allows chaining of the filters
> socks_in_stocks = in_stock.filter(category__name="Socks")
> cheapest_socks = socks_in_stocks.order_by("price")[5]
> ```
>
> What cause the SQL to get executed?
>
> ```python
> in_stock = Products.objects.filter(stock_count__gt=0)
> 
> # converting to a string, either in python or jinja template
> str(in_stock) or template: {{sock}}
> 
> # looping, can either be in template or view
> for product in in_stock:
> ...
> 
> # convert to list
> list(in_stock)
> ```
>
> 


#### Get, Filter and Exclude

> ```python
> # GET : get() => only allowed return one object, Raises an Exception if not exactly 1 match
> Product.objects.get(pk=1) -> Product  # get() only returns one object
> Product.objects.get(name__contains="met") # can use other options than pk
> 
> # Exception
> Product.objects.get(name__contains="a") # ERROR: this will return an error if multiple object are returned
> 
> # Exception handling
> get_object_or_404(Product, pk=5)
> ```
>
> ```python
> # FILTER : filter() => allows return of 0 or more objects
> Product.objects.filter(name="Kayak") -> QuerySet
> Product.objects.filter(name__endswith="k") -> QuerySet
> Product.objects.filter(name__contains="a", price__lt=100)   # price_lt => Price less than
> 
> # The results of the above commands are printed in the Django shell, the printing forces the SQL to execute.
> # If we assign the commands to a variable,we can futher add filtering before the SQL is executed
> p = Product.objects.filter(name__contains="a", price__lt=100) 
> p.exclude(stock_count__gt=5)
> print(p)
> 
> # Filter depending on relation
> Product.objects.filter(category__name="Climbing gear")  # this does a SQL JOIN
> Product.objects.filter(category__name__contains="gear")
> ```

#### Limiting and Ordering

> ```python
> # LIMITING
> Product.objects.all()[:5] -> Queryset          # get first 5 objects
> Product.objects.all().reverse[:5] -> Queryset  # get last 5 objects (cannot use negative list slicing i.e [-5])
> Product.objects.all().first() -> Product       # get first object
> Product.objects.all().last() -> Product        # get last object
> ```
>
> ```python
> # ORDERING
> Product.objects.order_by("name")[:5] -> QuerySet   # get first 5 objects ordered by name
> Product.objects.order_by("price").values() -> dict # values() is slightly faster as converting sql data to Product is more expensive
> Product.objects.order_by("price").values('name', 'price') -> dict
> Product.objects.order_by("price").values_list('name', 'price') -> QuerySet(tuple)
> ```
>
> ```python
> # REMOVE DUPLICATION
> Product.objects.filter(category__name__contains="gear")  # this can return multiple of the same Product
> Product.objects.filter(category__name__contains="gear").distinct() # only return a Product once
> ```

#### Aggregate and Annotate

> ```python
> from django.db.models import Avg, COunt
> 
> # AGGREGATE
> Product.objects.aggregate(Avg('price')) -> dict  # get the average price of all products
> Product.objects.annotate(cat_count=Count('categories')).filter(cat_count__gt=1)
> 
> # ANNOTATE
> Category.objects.annotate(Avg('products__price')) -> QuerySet # get avg price of products for each category
> Category.objects.annotate(Avg('products__price')).values() -> dict # ditto, but as dict with name of category and avg price
> Category.objects.annotate(avg_price=Avg('products__price')).values() -> dict # ditto, but have custom key for avg price in dict
> Category.objects.annotate(avg_price=Avg('products__price')).order_by('avg_price')
> ```
>
> 

#### Relations: ManyToManyField

> ```python
> # MODELS
> class Product(models.Model):
>   name = models.CharField(max_length=100)
>   stock_count = models.IntegerField(help_text="How many items are currently in stock.")
>   price = models.DecimalField(max_digits=6, decimal_places=2)
>   description = models.TextField(default="", blank=True)
>   sku = models.CharField(verbose_name="Stock Keeping Unit", max_length=20, unique=True)
> 
> class Category(models.Model):
>   name = models.CharField(max_length=100)
>   products = models.ManyToManyField('Product')
> ```
>
> ```python
> # CATEGORY SIDE OF RELATION
> c = Category.objects.get(pk=1)  # Django is lazy, so catrgory Product are not loaded here
> 
> c.products  # returns a ManyRelatedManager
> >> '<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager'
> 
> c.products.all() -> QuerySet(Products)
> c.products.filter(price_lt=10) -> QuerySet(Products)
> ```
>
> #### Following relationships “backward”
>
> - Docs: https://docs.djangoproject.com/en/3.2/topics/db/queries/#following-relationships-backward
>
> ```python
> # PRODUCT SIDE OF RELATION: PART 1
> p = Product.objects.get(name="Helmet")
> 
> # Although Prodouct does not have a categories field, we can still see categories using 'category_set'
> p.category_set
> >>  <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.
> 
> p.category_set.all() -> QuerySet(Categories)  # user category_set
> 
> ```
>
> ```python
> # PRODUCT SIDE OF RELATION: PART 2 - custom related name
> 
> # To use custom related name instead of 'category_set', change the following line in the 'Category' model
> products = models.ManyToManyField('Product', related_name="categories")
> 
> p = Product.objects.get(name="Helmet")
> p.categories.all() -> QuerySet(Categories)
> 
> # if you do this, will need to update qery args..e.g
> products = Product.objects.filter(category__name=name)   # old
> products = Product.objects.filter(categories__name=name) # updated
> ```
>
> 

#### `F()` and `Q()`

> ```python
> # F : Reference to the value of a model field
> from django.db.models import F
> 
> ```
>
> ```python
> # Q
> from django.db.models import Q
> 
> in_stock = Q(stock_count__gt=0)
> no_img = Q(images=None)
> 
> # basic usage
> Products.objects.filter(in_stock)  # get products in stock
> Products.objects.filter(~in_stock)  # get products NOT in stock
> # combinine Q expressions in filter argument
> Products.objects.filter(no_img | in_stock)  # get products that are in stock OR have no image
> Products.objects.filter(no_img & in_stock)  # get products that are in stock AND have no image
> # combining Q expressions
> no_img_or_no_stock = no_img|~in_stock
> 
> ```



## Optimizing the ORM

https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

#### QuerySet Caching

> Note: if you need the same results multiple times, reuse the QuerySet objects and this will not cause any extra queries
>
> ```python
> from store.models import Product
> 
> q = Product.objects.all()
> products = list(q)           # forces sql to run and values to be returned
> # now the results in q are cached
> for p in q: print(p)         # this doesnt make a sql call due to caching
> 
> # ------------------------------------------------ example with filter()
> q2 = Products.objects.filter(price__gt=100)
> for p in q2: print(p)  # inital loop runs the query
> for p in q2: print(p)  # doing it a second time gives the cached results
> q2[2]	                 # doesnt make a call, gets second element from cache
> 
> # -------------------------------------------------
> # if you create a QuerySet and only do slicing, it will not cache, and make a sql call each time
> q3 = Product.objects.all()
> q3[2]  # sql call made
> q3[2]  # sql call made
> q3[3]  # sql call made
> list(q3)  # once QuerySet evaluated completely, cache is then used
> ```
>
> ##### Example: Temple example for checking for the fitst image and then showing it
>
> ```python
> # BEFORE OPTIMISATION
> {% for p in products %}
> {% if p.images.all.0 %}                      # sql call made here
>  <img src="/media/{{ p.images.all.0 }}">    # sql call made here again
> {% endif %}
> {% endfor %}
> ```
>
> ```python
> # OPTIMISED
> {% with p.images.all.0 as img %}    # single sql call
> {% if img %}            
> 	<img src="/media/{{ img }}">    # img gotten from cache
> {% endif %}
> {% endwith %}
> ```

#### Reducing the Number of Queries

> ##### Example:  `select_related`  ONLY WORKS with `ForeignKey`
>
> ```python
> class ProductImage(models.Model):
>  image = models.ImageField()
>  product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="images")
> ```
>
> ```python
> # BEFORE OPTIMISATION
> img = ProductImage.objects.get(pk=1)  # sql call made here  'SELECT * from product_image WHERE "id" = 1'
> img.product     # 2nd query made here to get the Product  'SELECT * from product WHERE "id" = 2'
> ```
>
> ```python
> # OPTIMISED
> img = ProductImage.objects.select_related('product').get(pk=1) # makes a single query
> # SELECT .. FROM product_image INNER JOIN product ON product_image.product_id = product.id
> ```
>
> ##### Example 2: `prefetch_related`
>
> ```
> 
> ```

#### Raw SQL

> Note: Django doesnt check whether your query is correct
>
> ```python
> products = Product.objects.raw('SELECT * FROM product where price < 100')        # basic
> products = Product.objects.raw('SELECT * FROM product where price < %s', [100])  # with parameters
> ```



## Debugging

### View SQL Queries

> ###### Setup
>
> ```python
> pip install ipython  # adds color and autocomplete to shell
> pip install rich     # use of inspect function, colored outputs
> 
> from django.db import connection
> from django.db import reset_queries
> from rich import inspect
> %load_ext autoreload
> %load_ext rich
> from models import Books
> ```
>
> ###### 
>
> ```python
> # run django query
> Books.objects.all()
> 
> # view sql queries created and time to execute
> print(connection.queries)
> # same with color
> from rich.console import Console
> from rich.syntax import Syntax
> console = Console()
> for x in connection.queries:print(console.print(Syntax(str(x['sql']), 'sql', line_numbers=True),soft_wrap=True), x['time'])  
> 
> # all addition queries are appended to a list
> # to clear the list run
> db.reset_queries()
> ```
>
> ```python
> # run django query, with query appended to the end
> print(Books.objects.all().query)
> 
> # same with syntax highlighting
> from rich.console import Console
> from rich.syntax import Syntax
> console.print(Syntax(str(Books.objects.all().query), 'sql', line_numbers=True),soft_wrap=True)
> ```

### Log sql statements when using Django Shell

> https://www.yellowduck.be/posts/enabling-sql-logging-in-django
>
> ```python
> # settings.py
> LOGGING = {
> 	"version": 1,
> 	"handlers": {"console": {"class": logging.StreamHandler}},
> 	"loggers": {"django.db.backends": {"level": "DEBUG"}},
> 	"root": {"handlers": ["console"]},
> }
> ```





---

### Links

- Docs: [How can I see the raw SQL queries Django is running?](https://docs.djangoproject.com/en/4.1/faq/models/#how-can-i-see-the-raw-sql-queries-django-is-running)