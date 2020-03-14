# An app for selling clothes
# Created by Gloria Apolot

# This file is located in this directory
# C:\Users\Apolot\Your team Dropbox\Gloria Apolot\Gloria\Apps

# First import a package (an add-on) called streamlit
from streamlit import title
from streamlit import subheader
from streamlit import image
from streamlit import write
from streamlit import info
from streamlit import warning
from streamlit import success


# Then use streamlit to create a title for the App
title("STYLE ON A BUDGET")

# Then use streamlit to create a subheader for the App
subheader("*-Looking good is an attitude not the price of the outfit-*")

# Then use streamlit to write our task for the App
write(
	"""	
	In preparation for the summer, every girl's wadrobe needs an influx of cute summer dresses and stylish tops like these. 

    """
	)

# Then use streamlit to create an image for the App
image("https://res.cloudinary.com/dxhxtu400/image/upload/c_scale,h_943/wxfgd8yj40t0via6ubxz.jpg", width=500)


write(
	"""

     > This is the Spring-Summer collection by Versus Versace.

    """
	)



image("https://i.pinimg.com/736x/5a/3f/85/5a3f85a5ebcf5d69675b1dc08d658e0c.jpg", width=400)


write(
	"""

	> This dress is from the summer collection by Hannibal Laguna.

    """
    )


warning("I don't know if it's just me but I always like to create wishlists on various online shopping sites for items I would like to buy.")



write(
	"""

	[Click here to view my summer collection wishlist on Aliexpress](https://my.aliexpress.com/wishlist/wish_list_product_list.htm?spm=a2g0o.detail.1000001.9.19c712efdhguAm)


    """
	)
