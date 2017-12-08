demo = "https://ithelp.ithome.com.tw"
print( "demo data:{}".format(demo) )

# indexed
print( "first data:{}".format(demo[0]) )
print( "last data:{}".format(demo[-1]) )

try:
    print(demo[28])
except IndexError as e:
    print( "Index Error: {0}, the last idx is: {1}".format(e, len(demo)-1) )

try:
    print(demo["10"])
except TypeError as e:
    print( "Type Error: {0}".format(e) )

# sliced
s1 = demo[:]
print( "sliced 1:{}".format(s1) )

s2 = demo[2:]
print( "sliced 2:{}".format(s2) )

s3 = demo[2:5]
print( "sliced 3:{}".format(s3) )

s4 = demo[:5]
print( "sliced 4:{}".format(s4) )

s5 = demo[-3:]
print( "sliced 5:{}".format(s5) )

s6 = demo[::2]
print( "sliced 6:{}".format(s6) )

s7 = demo[1::2]
print( "sliced 7:{}".format(s7) )

# iteration
concate = ""
idx = 0
while idx < len(demo):  
    print(demo[idx])
    concate += demo[idx]
    idx += 1
print( "concate:{}".format(concate) )

# concate with other type
try:
    result = 2
    demo2 = "1+1="
    concate2 = demo2 + result
    print( "concate2: {}".format(concate2) )
except TypeError as e:
    print( "Type Error: {0}".format(e) )
    concate2 = demo2 + str(result)
    print( "concate2: {}".format(concate2) )

# other function
# count
chars = []
idx = 0
while idx < len(demo):
    if demo[idx] not in chars:
        print( "{} count number is {}".format(demo[idx], demo.count(demo[idx])) )
    chars.append(demo[idx])
    idx += 1

# find
ithome_idx = demo.find("ithome")
s8 = demo[ithome_idx:]
print( "sliced 8: {}".format(s8) )

# splitlines, strip, split, replace
# source from https://hackernoon.com/25-hints-youre-working-on-a-high-performing-team-c4d02f27dd3
section = """\
Here’s the personal checklist I came up with. Of course, it is always a journey.
You’re never done. As I point out in #1, my primary “signal” is a growth 
mindset and some awareness of what better might look like.
"""
section_words = []
lines = section.splitlines()
print( "lines: {}".format(lines) )
for line in lines:
    words = line.strip().split(" ")
    for word in words:
        if word.find(".") > 0:
            section_words.append(word.replace(".", ""))
        elif word.find(",") > 0:
            section_words.append(word.replace(",", ""))
        elif word.find("\"") > 0:
            section_words.append(word.replace("\"", ""))
        elif word.find("“") > 0:
            section_words.append(word.replace("“", ""))
        else:
            section_words.append(word)
print( "section_words: {}".format(section_words) )
for word in set(section_words):
    word_freq = section_words.count(word)
    print( "{}=>{}".format(word, word_freq) )