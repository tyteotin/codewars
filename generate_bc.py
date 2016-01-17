"""
As breadcrumb menùs are quite popular today, I won't digress much on explaining them, leaving the wiki link doing the dirty work in 
my place.

What might not be so trivial is to get a decent breadcrumb from your current url: for this kata your purpose is to create a function 
that takes a url, strips the first part (labeling it always HOME) and then builds it making each element but the last a <a> element 
linking to the relevant path; last has to be a <span> element getting the active class.

All elements need to be turned into uppercase and separated by a separator, given as the second parameter of the function; the last 
element can terminate in some common extension like .html, .htm, .php or .asp; if the name of the last element is index.something, 
you treat it as if it wasn't there, sending users automatically to the upper folder.

A few examples can be more helpful than thousands of explanations, so here you have them:

generate_bc("mysite.com/pictures/holidays.html", " : ") == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
generate_bc("www.codewars.com/users/GiacomoSorbi", " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
generate_bc("www.microsoft.com/docs/index.htm", " * ") == '<a href="/">HOME</a> * <span class="active">DOCS</span>'

Seems easy enough? Well, probably not, but we have now a last extra rule: if one element (other than the root/home) is longer than 
30 characters, you have to shorten it, acronymizing it (i.e.: taking just the initials of every word); url will be always given in 
the format this-is-an-element-of-the-url and you should ignore words in this array while acronymizing:
["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]; url composed of more words separated by -, but equal or 
less than 30 characters long, needs to be just uppercased with hyphens replaced by spaces.

Ignore anchors (www.url.com#lameAnchorExample) and parameters (www.url.com?codewars=rocks&pippi=rocksToo) when present.

Examples:

generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm", " > ") == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ") == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'

You will always be provided valid url to webpages in common formats, so you probably shouldn't bother validating them.

"""


import re
def check_crumb(crumb):
    skip_word = ["the","of","in","from","by","with",
                "and", "or", "for", "to", "at", "a"]
    if(len(crumb) <= 30):
        res = re.sub(r'-', ' ', crumb)
        return res
    else:
        res = ""
        crumb = crumb.split("-")
        for i in crumb:
            if(i not in skip_word):
                res+= i[0]
        return res
        
    
def generate_bc(url, separator):
    res = "<a href=\"/\">HOME</a>" + separator
    match = re.sub(r'http.*://', '', url)
    match = re.sub(r'^www\.', '', match)
    match = re.sub(r'[?#].*$', '', match)
    url_parts = match.split('/')
    url_parts = [i for i in url_parts if i != '']
    if(len(url_parts) <= 1 or (len(url_parts) == 2 and "index" in url_parts[-1])):
        res = "<span class=\"active\">HOME</span>"
        return res

    site_name = re.match(r'(.*?)(?=\.)', url_parts[0])
    active_class = re.match(r'(.*?)(?=\.)', url_parts[-1])
    
    # If active class has ".htm" or any file extension, strip file extension
    if(active_class == None):
        # No file extension, keep as is
        active_class = url_parts[-1]
    else:
        # Get name only, no file extension
        active_class = active_class.group(0)

    path = ""
    if(active_class != "index"):
        for i in url_parts[1:-1]:
            element = check_crumb(i)            
            if(len(url_parts[1:-1]) <= 1):
                res+="<a href=\"/" + i + "/\">" + element.upper() + "</a>" + separator
            else:
                res+="<a href=\"/" + path + i + "/\">" + element.upper() + "</a>" + separator
                path+= i + "/"  
        if(active_class != ""):
            res+= "<span class=\"active\">" + check_crumb(active_class).upper() + "</span>"
        else:
            res = res[:-len(separator)]
    else:
        for i in url_parts[1:-2]:
            element = check_crumb(i)
            res+="<a href=\"/" + path + i + "/\">" + element.upper() + "</a>" + separator
            path+= i + "/"            
        if(active_class != ""):
            res+= "<span class=\"active\">" + check_crumb(url_parts[-2]).upper() + "</span>"
        else:
            res = res[:-len(separator)]

    return res
