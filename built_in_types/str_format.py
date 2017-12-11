fruit = ['apple', 'orange', 'watermelon']
colors = ['red', 'black', 'blue']

# by position
format_str_by_pos = '{0}, {1}, {2}'
print( format_str_by_pos.format(fruit[0], fruit[1], fruit[2]) )
print( format_str_by_pos.format(colors[1], colors[2], colors[0]) )

# by name
format_str_by_name = 'T-shirt is {t_shirt_color}; pants is {pants_color}'
print( format_str_by_name.format(t_shirt_color=colors[0], pants_color=colors[2]) )

my_color = {'t_shirt_color': 'white', 'pants_color': 'black'}
print( format_str_by_name.format(**my_color) )

# accessing arguments’ items
format_str_1 = 'T-shirt is {0[0]}; pants is {0[2]}'
print( format_str_1.format(colors) )

# aligning the text and specifying a width
left_aligned_50 = '{:<50}'
right_aligned_50 = '{:>50}'
centered = '{:^50}'
centered_fill_dollor_sign = '{:$^50}'
print( left_aligned_50.format("python 3") )
print( right_aligned_50.format("python 3") )
print( centered.format("python 3") )
print( centered_fill_dollor_sign.format("python 3") )

# different bases
show_diffrent_bases = 'int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}'
show_diffrent_bases_with_prefix = 'int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}'
print( show_diffrent_bases.format(42) )
print( show_diffrent_bases_with_prefix.format(42) )

# thousands separator
thousands_separator = '{:,}'
print( thousands_separator.format(5698563258) )

# percentage
percentage = '{:.3%}'
total_score = 155
score = 6
print( percentage.format( score / total_score ) )