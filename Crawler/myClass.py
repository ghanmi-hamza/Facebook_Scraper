from functions import *
class Personne():
    def __init__(self, name='', intro='',image='',friends=0,posts=''):
        """Constructeur de notre classe"""
        self.name = name
        self.intro = intro
        self.image = image
        self.friends = friends 
        self.posts = []
        
    def profile_data(self,driver,url,usr,pwd):
        """ function that takes the url of a user and your (email+pssword) and
            return some info about the user  """
        driver.get(url)
        try:
            intr=driver.find_element_by_xpath('//*[@id="intro_container_id"]').text
        except:
            intr=''
        popup = WebDriverWait(driver, 10). until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html')))
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
        time.sleep(2)
        try:
            self.friends=driver.find_element_by_xpath('.//*[@class="fsm fwn fcb"]').text
        except Exception:
            self.friends=0
        try:
            self.name=driver.find_element_by_xpath('//*[@id="fb-timeline-cover-name"]').text
            img=driver.find_element_by_xpath('//*[@class="_11kf img"]')
            self.image=img.get_attribute('src')
        except Exception:
            self.image='No profile image'
        self.intro=intr
        basic_info=get_basic_info(driver,url)
        self.gender=basic_info[1]
        self.birthday=basic_info[0]
        n=30
        self.images_urls=get_images(driver,url,n)
        dic={
        'name':self.name,
        'Intro':self.intro,
        'friends':self.friends,
        'image':self.image,
        'Birthday':self.birthday,
        'Gender':self.gender,
        'images_urls':self.images_urls
        }
        print(dic)
    def posts_details(self,n,driver,url,usr,pwd):
        """ function that return info about the first n posts """
        driver.get(url)
        post={}
        time.sleep(2)
        try:
            driver.find_element_by_xpath('//*[@id="intro_container_id"]').text
        except:
            pass
        
        time.sleep(1)

        self.posts={}
        self.people_urls=[]
        for i in range(n):
            try:
                c=driver.find_elements_by_xpath(".//*[@class='_5pcb _4b0l _2q8l']")
                a=post_details(c[i],driver)
                b=comments(c[i],driver)
                a['commentaire']=b[0]
                self.people_urls+=b[1]
                dic={
                'post'+str(i+1):a
                }
                self.posts.update(dic)
                print(i+1)
            except:
                break
        #driver.close()
        
       
