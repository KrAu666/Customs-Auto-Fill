def new_unicode(query_string):# Convert the query string into ASCII codes with '|' as a delimiter
    ascii_encoded_string = '|'.join([str(ord(char)) for char in query_string.replace("&", "&")])
    return ascii_encoded_string