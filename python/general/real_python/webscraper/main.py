import requests

URL = 'https://rip.ie/deathnotices.php?do=get_deathnotices_pages&sEcho=1&iColumns=5&sColumns=&iDisplayStart=0&iDisplayLength=40&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&mDataProp_4=4&iSortingCols=2&iSortCol_0=0&sSortDir_0=desc&iSortCol_1=0&sSortDir_1=asc&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=true&bSortable_4=true&iDisplayLength=40&DateFrom=2020-03-28+00%3A00%3A00&DateTo=2020-04-04+23%3A59%3A59&NoWhere=y'
URL = 'https://rip.ie/deathnotices.php?do=get_deathnotices_pages&sEcho=2&iColumns=5&sColumns=&iDisplayStart=40&iDisplayLength=40&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&mDataProp_4=4&iSortingCols=2&iSortCol_0=0&sSortDir_0=desc&iSortCol_1=0&sSortDir_1=asc&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=true&bSortable_4=true&iDisplayLength=40&DateFrom=2020-03-28+00%3A00%3A00&DateTo=2020-04-04+23%3A59%3A59&NoWhere=y'
data = {"DateFrom": "28/03/2020", "DateTo": "04/04/2020", "search": "SEARCH", "county": "All", "town": "All"}
# page = requests.post(URL, data)
page = requests.get(URL)
print(page.json())



print(results.prettify())
