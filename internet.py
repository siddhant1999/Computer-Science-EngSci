import webbrowser
search_terms = []

# ... construct your list of search terms ...

search_terms.append("silicon valley")

for term in search_terms:
    url ="http://www.primewire.ag/index.php?search_keywords=" + str(term)
    webbrowser.open_new_tab(url)