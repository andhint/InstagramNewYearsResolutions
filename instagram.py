import requests, bs4, math


def getCount(instaStr):
	# returns the count for tag
	#
	# instaStr : string of script from webpage containing count information
	#
	# Searches through string for ' "count": ' and ','. From there the total count for
	# the tag can be scraped via the difference in index. Searching the string is done 
	# using str.find(). The initial search starts after an index of 600 to keep it efficient 
	# and allow ample room between differences in string length. Slicing isn't possible because 
	# the length of each string changes between each webpage slightly.

	# define search strings for str.find()
	startFlag = 'count":'
	endFlag = ','

	# find index where startFlag occurs in main string, starting search from index = 600
	begIndex = instaStr.find(startFlag, 600)
	# find index where endFlag occurs in main string, starting search from index = begIndex found in previous step
	endIndex = instaStr.find(endFlag, begIndex)

	try:
		# Convert string to int
		count = int(instaStr[begIndex + len(startFlag):endIndex])
	except ValueError:
		# Handles rare case where value is a float. For example 12257.0
		# The decimal is always .0 in these cases so int(float(string)) is all that is needed
		count = int(float(instaStr[begIndex + len(startFlag):endIndex]))

	return count

def main():
	# open file to write data to
	textFile = open("instagramData.txt", "w")
	# create loop to go through every day in the year
	for j in range(1,366):
		#create site url
	    site = "https://www.instagram.com/explore/tags/day" + str(j)
	    # get site using requests library
	    res = requests.get(site)
	    # create Beautiful Soup object and select the sixth string in the html markup as a string
	    markup = bs4.BeautifulSoup(res.text,"html.parser")
	    instaStr = str(markup.select('script')[6])
	    # get count value for that day (j)
	    count = getCount(instaStr)
	    # write the day number and count to file
	    textFile.write(str(j) +"," + str(count) + "\n")
	    #printing out progress
	    percent = (float(j) / 365) * 100
	    print("%.2f" % percent + "%")
	#close file
	textFile.close()


main()