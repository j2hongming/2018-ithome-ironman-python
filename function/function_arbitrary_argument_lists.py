def concat(prefix, *chunk, sep="/"):
    return prefix + sep.join(chunk)


result = concat('https://', 'ithelp.ithome.com.tw', 'articles', '10192583')
print( "concat result:{}".format(result) )

url_domain_chunk = ('docs', 'python', 'org')
url_path_chunk = ('3', 'tutorial', 'controlflow.html')

domain = concat('https://', *url_domain_chunk, sep='.')
url = concat(domain, *url_path_chunk)
url_with_tag = concat(url+"#", 'more-on-defining-functions', sep='')
print( "concat domain:{}".format(domain) )
print( "concat url:{}".format(url) )
print( "concat url_with_tag:{}".format(url_with_tag) )