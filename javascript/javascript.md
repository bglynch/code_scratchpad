# Javascript

---

```javascript
// testing element
document.addEventListener('click', function (event) {
  let element = event.target;
  let child = event.target.firstElementChild;
  let parent = event.target.parentElement;  
  let grandparent = event.target.parentElement.parentElement;
  
  console.log('document click', event)
  console.log('element', element)
  console.log('child', child)
  console.log('parent', parent)
  console.log('grandparent', grandparent)
  }
})
```

## Querys

https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector

> ###### get element
>
> ```javascript
> document.getElementById('quickEditModal')
> document.querySelector('.rateRecipe.btns-one-small')
> ```
>
> ###### get elements
>
> ```javascript
> // get all buttons inside element with id=job-list-tab
> document.querySelectorAll('#job-list-tab button')
> 
> // get elements by class name
> document.querySelectorAll('.love-button.love-button--loved')
> document.getElementsByClassName('rateRecipe btns-one-small')
> ```

## Filter

> ```javascript
> [...document.querySelectorAll('.tab-content li button')]
>   	.filter(li => li.innerText == "All")
> ```

## Checks

> ###### Element contains class
>
> ```javascript
> if(element.classList.contains('bi-star-fill')){
>   console.log('unbookmark this job')
> }
> ```

## data attributes

> ```html
> <article
>   id="electric-cars"
>   data-columns="3"
>   data-index-number="12314"
>   data-parent="cars">
>   …
> </article>
> 
> <style>
>   const article = document.querySelector("#electric-cars");
>   // The following would also work:
>   // const article = document.getElementById("electric-cars")
> 
>   article.dataset.columns;     // "3"
>   article.dataset.indexNumber; // "12314"
>   article.dataset.parent;      // "cars"
> </style>  
> ```
>
> 



---

## Forms

### GET

> ```java
> fetch(config.url.jobList, {
>   method: "GET",
>   headers: {
>     "X-Requested-With": "XMLHttpRequest",
>   }
> })
> .then(response => response.json())
> ```
>
> 