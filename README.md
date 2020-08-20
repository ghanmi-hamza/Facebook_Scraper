A crawler which extract data from a Facebook Profile:
data extracted:

*profile description:
{-Intro part
-image url
-number of friends
-name
-images
-date of birth
-gender}
*posts:
{-who makes the post
-date
-contenu
-comments
}

PS:to run this script go inside Crawler folder and then run this command : python __main__.py --url="A" --n=B --usr="C" --pwd="D"
where:
	A=url of the user
	B=number of posts to scrape
	C=facebook id
	D=facebook password

a folder "data" will be created and inside it you will find multiple folder named X(the name of the user) and inside each one you will
find images and json file contains data about the user X