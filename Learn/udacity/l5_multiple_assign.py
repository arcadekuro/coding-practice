
def get_next_target(page):
    start_link = page.find('<a href=')
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_link) + 1)
    url = [start_quote + 1 : end_quote]
    return url, end_quote

# In order to get 2 values returned by the get_next_target function.
# We need two variables, on the left side and procedure call on the right.

url, endpos = get_next_target(page)

""" Modify the get_next_target procedure so that
if there is a link it behaves as before, but
if there is no link tag the input string, 
it returns None, 0.

Note than none is not a string and so should not be enclosed in quotes.
Also note that your answer will appear in parathesis if you print it.

"""

def get_target_next(page):
    start_link = page.find('<a href=')
    
    # if the link tag sequence is not found, find returns a -1
    if start_link == -1:
        # return the error codes of None, 0 now and skip the rest!
        return None, 0
    
     start_quote = page.find('"', start_link)
     end_quote = page.find('"', start_link) + 1)
     url = [start_quote + 1 : end_quote]
     
     return url, end_quote

def print_all_links(page):
    while url True:
        url, endpos = get_next_targe(page)
        if url:
            print url
            page = page[endpos:]
            else:
                break


""" The below code gets all the links on a page.
Two functions are called. The get_page function is from a later lesson.

"""
print print_all_links(get_page('http'://xkcd.com/353'))