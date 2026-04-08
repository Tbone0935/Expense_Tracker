import urllib.request

fhand = urllib.reques.urlopen("http://data.prde.org/cover.jpg")
for line in fhand:
        print(line)