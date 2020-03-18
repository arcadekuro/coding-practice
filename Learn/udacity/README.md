# Lesson 5 

## 2 New concepts 
* Procedures - a way to package code so we can reuse it more easily (also known as functions).
* Control - we need a wat to make decisions and do repition, to find all the links on a page. 

The aim of this introduction to Computer science by Udacity is to create a webcrawler. 
To build a good web crawler. We don't just care about the first link that is in the output but all of them. 

Extracting the first URL from as page:

``` 
page = ... contents of a webpage
start_link = page.find('<ahref=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = [start_quote + 1 : end_quote]
print(url)
````

Tho find the second code on the page we could write this code all over again. 