from .functions import *
from abc import ABC
class Driver(ABC):

    def get_user_info(self,user_id):
        pass
    def get_publications(self,user_id,comments,n):
        pass
    
    def get_images(self,user_id,n):
        pass
    def get_basic_info(self,user_id):
        pass
    def get_comment_by_key(self,key,n):
        pass
    def get_comment_by_keys(self,keys,n):
        pass
    def get_comments(self,post_id):
        pass
class FacebookDriver(Driver):
    def __init__(self,name=''):
        self.name=name
        """Constructeur de notre classe"""
        pass
    def get_browser(self,usr,pwd):
        options = webdriver.firefox.options.Options()
        options.headless = True
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Hamza\Downloads\geckodriver.exe",options=options)
        self.driver.set_window_position(0, 0) #NOTE: 0,0 might fail on some systems
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        email = self.driver.find_element_by_xpath("//input[@id='email' or @name='email']")
        email.send_keys(usr)
        password = self.driver.find_element_by_xpath("//input[@id='pass']")
        password.send_keys(pwd)
        button = self.driver.find_element_by_xpath("""//*[@id="u_0_b"]""")
        button.click()
        
    def get_user_info(self,user_id):
        self.driver.get("https://www.facebook.com/"+str(user_id))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, ".//div[@class= 'rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr p8fzw8mz pcp91wgn iuny7tx3 ipjc6fyt']")))
        try:
            intro=self.driver.find_element_by_xpath(".//div[@class= 'rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr p8fzw8mz pcp91wgn iuny7tx3 ipjc6fyt']").text
        except:
            intro=""
        try:
            self.friends=self.driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/a[3]/div[1]/span/span[2]").text
        except Exception:
            self.friends=0
        self.name=self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/div/span/h1').text
        dic={
        'name':self.name,
        'Intro':intro,
        'friends':self.friends
        }
        return(dic)
    
    def get_publications(self,user_id,comments,n):
        """ function that return info about the first n posts """
        self.driver.get("https://www.facebook.com/"+str(user_id))
        post={}
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, ".//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")))
        dic={}
        j=0
        for i in range(n):
            #id of a facebook publication
            c=self.driver.find_elements_by_xpath(".//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")
            for e in c[j:]:
                data=self.post_details(e)
                if comments == "T":
                    comm= self.get_comments(e)
                    data["comments"]=comm
                dic["post"+str(j+1)]=data
                j+=1
            if j>=n:
                break
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();",c[len(c)-1])
                time.sleep(2)
            except:
                pass
        return(dic)
    

    def get_images(self,user_id,n):
        """return the n first images urls"""
        url_list=[]
        self.driver.get("https://www.facebook.com/"+str(user_id)+"/photos_all")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, ".//div[@class='rq0escxv rj1gh0hx buofh1pr ni8dbmo4 stjgntxs l9j0dhe7']/div/div/a/img")))
        for i in range(n):
            try:
                #id of an image
                c=self.driver.find_elements_by_xpath('.//div[@class="rq0escxv rj1gh0hx buofh1pr ni8dbmo4 stjgntxs l9j0dhe7"]/div/div/a/img')
                url=c[i].get_attribute('src')
                url_list.append(url)
                try:
                    self.driver.execute_script("arguments[0].scrollIntoView();",c[i])
                except:
                    pass
            except:
                break
        return(url_list)
    def get_basic_info(self,user_id):
        """get the birthday and gender info from a user url"""
        self.driver.get("https://www.facebook.com/"+str(user_id)+"/about_contact_and_basic_info")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div[3]/div/div[2]')))
        try:
            BirthDay=self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div[3]/div/div[2]').text
        except:
            BirthDay=''
        try:
            Gender=self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/div[1]').text
        except:    
            Gender=''
        return(BirthDay,Gender)
    def post_details(self,publication_id):
        """return info about a publication """
        try:
            nb_reaction=publication_id.find_element_by_xpath(".//span[@class='gpro0wi8 cwj9ozl2 bzsjyuwj ja2t1vim']").text
        except Exception:
            nb_reaction=0
        try:
            nb_comment=publication_id.find_element_by_xpath(".//div[@class='bp9cbjyn j83agx80 pfnyh3mw p1ueia1e']").text
        except:
            nb_comment=0
        user=publication_id.find_element_by_xpath(".//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p']").text
        date=publication_id.find_element_by_xpath(".//*[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw']").get_attribute("aria-label")
        try:
            contenu=publication_id.find_element_by_xpath(".//div[@class='ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a']").text
        except:
            contenu=''
        try:
            img=publication_id.find_element_by_xpath(".//img[@class='i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm bixrwtb6']")
            image=img.get_attribute('src')
        except Exception:
            image='No image'
        dic={
                'user':user,
                'date':date,
                'contenu':contenu,
                'image':image,
                'nb_reaction':nb_reaction,
                'nb_comment':nb_comment
            }
        
        return(dic)
    def get_comments(self,post_id):
        """get comments from a post"""
        comments=[]
        try:
            see_more_comments = post_id.find_elements_by_xpath(".//div[@class='oajrlxb2 bp9cbjyn g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 g5gj957u p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys p8fzw8mz qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh gpro0wi8 m9osqain buofh1pr']")
            for link in see_more_comments:
                try:
                    self.driver.execute_script("arguments[0].click();", link)
                except:
                    pass
        except Exception:
            pass
        time.sleep(2)
        #list of comments 
        data = post_id.find_elements_by_xpath(".//div[@class='l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 dati1w0a lzcic4wl btwxx1t3 j83agx80']")
        for d in data:
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((d)))
            except:
                pass
            
            author = d.find_element_by_xpath(".//span[@class='pq6dq46d']").text
            try:
                text = d.find_element_by_xpath(".//div[@class='ecm0bbzt e5nlhep0 a8c37x1j']").text
            except:
                text=""
            date=d.find_element_by_xpath(".//*[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl m9osqain gpro0wi8 knj5qynh']").text
            comments.append([author, text, date])
        return(comments)
    def get_comment_by_key(self,key,n):
        self.driver.get("https://www.facebook.com/search/posts/?q="+str(key))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="hpfvmrgz g5gj957u buofh1pr rj1gh0hx o8rfisnq"]/a/span')))
        try:
            popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html')))
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
            self.driver.find_elements_by_xpath('//div[@class="hpfvmrgz g5gj957u buofh1pr rj1gh0hx o8rfisnq"]/a/span')[-1].click()
            time.sleep(2)
        except:
            pass
        #make scroll untill the end of the page
        body = self.driver.find_element_by_tag_name('body')
        for _ in range(100):
           body.send_keys(Keys.PAGE_DOWN)
           time.sleep(0.2)
        li=[]
        #list of data
        c=self.driver.find_elements_by_xpath(".//div[@class='sjgh65i0']")
        for i in range(n):
            try:
                name=c[i].find_element_by_xpath(".//div[@class='qzhwtbm6 knvmm38d']").text
                content = c[i].find_element_by_xpath(".//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l']").text
                date=c[i].find_element_by_xpath(".//span[@class='oi732d6d ik7dh3pa d2edcug0 hpfvmrgz qv66sw1b c1et5uql jq4qci2q a3bd9o3v knj5qynh m9osqain']").text
                dic={"name":name,"date":date,"content":content}          
                
                li.append(dic)
            except:
                break
        return(li)
    def get_comment_by_keys(self,keys,n):
        result=[]
        for word in keys:
            li=self.get_comment_by_key(word,n)
            result.append(li)
        
        return(result)
    def get_friends(self,user_id,nb_friends):
        self.driver.get("https://www.facebook.com/"+str(user_id)+"/friends")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,".//h2[@class='gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl d2edcug0 hpfvmrgz']")))
        users=[]
        i=0
        while(i<=nb_friends):
            
            #list of friends
            c=self.driver.find_elements_by_xpath(".//span[@class='oi732d6d ik7dh3pa d2edcug0 hpfvmrgz qv66sw1b c1et5uql a8c37x1j s89635nw ew0dbk1b a5q79mjw g1cxx5fr lrazzd5p oo9gr5id']")
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();",c[len(c)-1])
            except:
                break
            time.sleep(2)
            i+=8
        for e in c:
            users.append(e.text)
        return(users)
    def get_event_data(self,url):
        """get info from an event url"""
        self.driver.get(str(url))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,".//div[@class='ni8dbmo4 stjgntxs l9j0dhe7 k4urcfbm du4w35lb']")))
        #event name
        name=self.driver.find_element_by_xpath(".//span[@class ='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 oi732d6d ik7dh3pa d2edcug0 hpfvmrgz qv66sw1b c1et5uql irj2b8pg q9se6cdp m6dqt4wy h7mekvxk hnhda86s erlsw9ld hzawbc8m']").text
        try:
            nb_people=self.driver.find_elements_by_xpath("//div[@class='discj3wi ihqw7lf3']/div")[1].text
            date=self.driver.find_elements_by_xpath("//div[@class='discj3wi ihqw7lf3']/div")[2].text
            lieu=self.driver.find_elements_by_xpath("//div[@class='discj3wi ihqw7lf3']/div")[3].text
            info=self.driver.find_elements_by_xpath("//div[@class='discj3wi ihqw7lf3']/div")[4].text
            details=self.driver.find_elements_by_xpath("//div[@class='discj3wi ihqw7lf3']/div")[6].text
            dic={"nb_people":nb_people,"date":date,"lieu":lieu,"info":info,"details":details}
            i=i+1
        except:
            pass
        return(dic,name)
    def get_events(self,user_id,scroll,n):
        self.driver.get("https://www.facebook.com/"+str(user_id)+"/events")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,".//h2[@class='gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl d2edcug0 hpfvmrgz']")))
        li=[]
        urls=[]
        for i in range(scroll):
            time.sleep(2)
            #list of events
            c=self.driver.find_elements_by_xpath(".//div[@class ='bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr']")
            links = self.driver.find_elements_by_xpath("//a[@href]")
            for link in links:
                if 'events' in link.get_attribute("href") and user_id not in link.get_attribute("href"):
                    li.append(link.get_attribute("href"))
            urls+=li
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();",c[len(c)-1])
            except:
                pass
        urls=list(set(urls))[:n]
        result={}
        i=1
        for e in urls:
            data=self.get_event_data(e)
            result[str(data[1])]=data[0]
            i=i+1
        return(result)
    def get_likes(self,user_id,scroll,n):
        """return list of pages(name+url)"""
        self.driver.get("https://www.facebook.com/"+str(user_id)+"/likes")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,".//h2[@class='gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl d2edcug0 hpfvmrgz']")))
        li=[]
        for i in range(scroll):
            #ist of pages
            c=self.driver.find_elements_by_xpath(".//div[@class ='j83agx80 btwxx1t3 lhclo0ds']/div")
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();",c[len(c)-1])
            except:
                pass
            time.sleep(2)
        c=self.driver.find_elements_by_xpath(".//div[@class ='j83agx80 btwxx1t3 lhclo0ds']/div")
        for e in c[:n]:
            link=e.find_element_by_xpath(".//a[@role ='link']").get_attribute("href")
            name=e.find_element_by_xpath(".//div[@class ='qzhwtbm6 knvmm38d']/span").text
            dic={"name":name,"link":link}
            li.append(dic)
        return(li)
            
    def get_page(self,page_id,n,comments):
        """get details about the first n publications"""
        self.driver.get("https://www.facebook.com/"+str(page_id))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,".//div[@class='ni8dbmo4 stjgntxs l9j0dhe7 k4urcfbm du4w35lb']")))
        c=self.driver.find_elements_by_xpath("//div[@class='cbu4d94t j83agx80 cwj9ozl2']/div")
        l=[]
        for e in c:
            l.append(e.text)
        j=0
        dic={"page_info":l}
        for i in range(n):
            #list of publications
            c=self.driver.find_elements_by_xpath(".//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")
            for e in c[j:]:
                data=self.post_details(e)
                if comments == "T":
                    comm= self.get_comments(e)
                    data["comments"]=comm
                dic["post"+str(j+1)]=data
                j+=1
            if j>=n:
                break
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();",c[len(c)-1])
                time.sleep(2)
            except:
                pass
        return(dic)
            
                
        
        
        

