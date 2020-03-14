# An app to share some of my favorite books
# Created by Gloria Apolot

# This file is located in this directory
# C:\Users\Apolot\Your team Dropbox\Gloria Apolot\Gloria\Apps

# First import a package (an add-on) called streamlit
from streamlit import title
from streamlit import subheader
from streamlit import write
from streamlit import image
from streamlit import markdown
from streamlit import info
from streamlit import warning
from streamlit import success

# Then use streamlit to create a title of the App
title("My favourite books")

# Then use streamlit to create a subheader of the App
subheader("Favourite romance books")

# Then use streamlit to write our task for this App
markdown(
	"""
	Number one on my list is the After series by Anna Todd about a bad boy, Hardin and a good girl, Tessa.

	THis is my first dress that I like.
	![Floral Dress](https://cdn.shopify.com/s/files/1/0086/7480/3789/products/Summer-Dress-2019-Short-Sleeve-Hepburn-50s-60s-Vintage-Dress-Elegant-Swing-Party-Dress-Beach-Sexy.jpg_640x640_d61d5b37-6452-446b-9f19-d65d00ccbf08_700x933.jpg?v=1554008982)![Gloria](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/hbz-dresses-index2-1559843396.jpg?crop=0.500xw:1.00xh;0.363xw,0&resize=640:*)
	*This is my caption*

	[Click here](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIbvfYukB2yv-0z4Wan_2TZoVFSNP0aVrlzbE3i42LmGkWfM5PKQ&s)

	* Bullet 1
	* Bullet 2

	1. NUmber 1
	2. Number 3

	**Two stars makes it bold**

	*One star makes it italic*

	> this is an indent






	"""
	)
info("I could spend hours talking about this book but I highly recommend it to anyone trying to find a winter read.")
warning("Number two on my list is Chasing Red by Isabelle Ronin. This too is a bad boy, good girl romance.")
success("Number three on my list is the Cell phone swap.")
image("https://previews.123rf.com/images/firdausexia/firdausexia1303/firdausexia130300002/18236451-only-one-tress.jpg", width=500)
image("https://previews.123rf.com/images/firdausexia/firdausexia1303/firdausexia130300002/18236451-only-one-tress.jpg", width=500)
markdown("text.md")