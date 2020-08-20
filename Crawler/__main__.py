from myClass import *

@click.command()
@click.option('--url', default='', help='url of the user')
@click.option('--n', default=1, help='number of posts')
@click.option('--usr', default="", help="your Facebook login")
@click.option('--pwd', default="", help='password')

def main(url,n,usr,pwd):
    driver=get_browser(url,usr,pwd)
    p = Personne()
    p.profile_data(driver,url,usr,pwd)
    p.posts_details(n,driver,url,usr,pwd)
    li=list(set(p.people_urls))
    print(li)
    dic=dictionnaire(p)
    save_data(dic,p.name,r"C:\Users\Hamza\Desktop\Facebook_Crawler\Facebook_Crawler\data\.")
    for e in li:
        try:
            p = Personne()
            p.profile_data(driver,e,usr,pwd)
            p.posts_details(n,driver,e,usr,pwd)
            dic=dictionnaire(p)
            save_data(dic,p.name,r"C:\Users\Hamza\Desktop\Facebook_Crawler\Facebook_Crawler\data\.")
            lj=list(set(p.people_urls))
            for m in lj:
                try:
                    p = Personne()
                    p.profile_data(driver,m,usr,pwd)
                    p.posts_details(n,driver,m,usr,pwd)
                    dic=dictionnaire(p)
                    save_data(dic,p.name,r"C:\Users\Hamza\Desktop\Facebook_Crawler\Facebook_Crawler\data\.")
                except:
                    pass
                
        except:
            pass
if __name__=='__main__':
    main()
