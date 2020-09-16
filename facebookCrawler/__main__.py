from myClass import *

@click.command()
@click.option('--url', default='', help='url of the user')
@click.option('--n', default=1, help='number of posts')
@click.option('--s', default=False, help='Download data')
@click.option('--usr', default="", help="your Facebook login")
@click.option('--pwd', default="", help='password')

def main(url,n,s,usr,pwd):
    driver=get_browser(url,usr,pwd)
    p = FacebookDriver()
    p.get_user_info(driver,url,usr,pwd)
    p.get_posts(n,driver,url,usr,pwd)
    li=list(set(p.people_urls))
    print(li)
    dic=dictionnaire(p)
    print(dic)
    if s=="True":
        save_data(dic,p.name,r"C:\Users\Hamza\Desktop\Facebook_Crawler\Facebook_Crawler\data\.")
    else:
        pass
if __name__=='__main__':
    main()
