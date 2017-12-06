# list to string transformation
url_src = ['ithelp', 'ithome','com','tw']
joined_url = '.'.join(url_src)
print( "url_src:{}".format(url_src) )
print( "joined_url:{}".format(joined_url) )

# string to list transformation
url = 'https://ithelp.ithome.com.tw'
url_part1 = url.split('://')
url_part2 = url_part1[1].split('/')
print( "url:{}".format(url) )
print( "url_part1:{}".format(url_part1) )
print( "url_part2:{}".format(url_part2) )

# list to tuple transformation
tags = ['apple', 'htc', 'sony', 'samsung', 'mi']
print( "tags:{}".format(tags) )
print( "type of tags:{}".format(type(tags)) )
tags_transform = tuple(tags)
print( "tags_transform:{}".format(tags_transform) )
print( "type of tags_transform:{}".format(type(tags_transform)) )

# tuple to list transformation
tags_transform_back = list(tags_transform)
print( "tags_transform_back:{}".format(tags_transform_back) )
print( "type of tags_transform_back:{}".format(type(tags_transform_back)) )

# list to set transformation (remove dupicate)
color = ['red', 'blue', 'black', 'white', 'yellow', 'red', 'black']
print( "color:{}".format(color) )
print( "type of color:{}".format(type(color)) )
color_transform = set(color)
print( "color_transform:{}".format(color_transform) )
print( "type of color_transform:{}".format(type(color_transform)) )

# set to list transformation
color_transform_back = list(color_transform)
print( "color_transform_back:{}".format(color_transform_back) )
print( "type of color_transform_back:{}".format(type(color_transform_back)) )


# list to dict transformation
# 1st method
home = ['1f', 'park', '2f', 'livingroom', '3f', 'bathroom']
print( "home:{}".format(home) )
print( "type of home:{}".format(type(home)) )
zip_home = zip(home)
print( "home after zip:{}".format(list(zip_home)) )
home_transform = dict(zip(home[0::2], home[1::2]))
print( "home_transform:{}".format(home_transform) )
print( "type of home_transform:{}".format(type(home_transform)) )

# 2nd method
home_transform_2 = {home[x]: home[x+1] for x in range(0, len(home), 2)}
print( "home_transform_2:{}".format(home_transform_2) )
print( "type of home_transform_2:{}".format(type(home_transform_2)) )

# 3rd method
i = iter(home)
print( "home after iter:{}".format(i) )
print(dict(zip(i, i)))

# dict to list transformation
home_transform_back = list(home_transform.values())
print( "home_transform_back:{}".format(home_transform_back) )
print( "type of home_transform_back:{}".format(type(home_transform_back)) )

# counting all items in a list
color = ['red', 'blue', 'black', 'white', 'yellow', 'red', 'black']
print( "color:{}".format(color) )
print( "type of color:{}".format(type(color)) )
counting_colors = [[x, color.count(x)] for x in set(color)]
print( "counting_colors:{}".format(counting_colors) )