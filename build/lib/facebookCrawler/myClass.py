
import time
import pathlib 
import json
import click
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from abc import ABC
class Driver(ABC):

    def get_user_info(self,user_id):
        pass
    def get_publications(user_id,comments,n):
        pass
    
    def get_images(self,user_id):
        pass
    def get_basic_info(self,user_id):
        pass
    def get_comments(self,id,driver):
        pass
class FacebookDriver(Driver):
    def __init__(self,name=''):
        self.name=name
        """Constructeur de notre classe"""
        pass
    def get_browser(self,usr,pwd):
        options = webdriver.firefox.options.Options()
        #options.headless = True
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Hamza\Downloads\geckodriver.exe",options=options)
        self.driver.get("https://www.facebook.com/")
        email = self.driver.find_element_by_xpath("//input[@id='email' or @name='email']")
        email.send_keys(usr)
        password = self.driver.find_element_by_xpath("//input[@id='pass']")
        password.send_keys(pwd)
        button = self.driver.find_element_by_xpath("""//*[@id="u_0_b"]""")
        button.click()
        
    def get_user_info(self,user_id):
        self.driver.get("https://www.facebook.com/"+str(user_id))
        time.sleep(3)
        try:
            intro=self.driver.find_element_by_xpath(".//div[contains(@class, 'rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr p8fzw8mz')]").text
        except:
            intro=''
        #popup = WebDriverWait(driver, 10). until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html')))
        #driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
        time.sleep(3)

        try:
            self.friends=self.driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/a[3]/div[1]/span/span[2]").text
        except Exception:
            self.friends=0
        self.name=self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/div/span/h1').text
        try:
            img=self.driver.find_element_by_xpath('//*[@class="_11kf img"]')
            self.image=img.get_attribute('src')
        except Exception:
            self.image='No profile image'
        
        #basic_info=self.get_basic_info(driver,url)
        #self.gender=basic_info[1]
        #self.birthday=basic_info[0]
        #n=30
        #self.images_urls=self.get_images(driver,url,n)
        dic={
        'name':self.name,
        'Intro':intro,
        'friends':self.friends,
        'image':self.image,
        }
        print(dic)
    def get_publications(self,user_id,comments,n):
        """ function that return info about the first n posts """
        self.driver.get("https://www.facebook.com/"+str(user_id))
        post={}
        time.sleep(2)
        """try:
            self.driver.find_element_by_xpath('//*[@id="intro_container_id"]').text
        except:
            pass"""
        time.sleep(1)

        self.posts={}
        for i in range(n):
            try:
                c=self.driver.find_elements_by_xpath(".//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")
                a=self.post_details(c[i])
                if comments=="T":
                    b=self.get_comments(c[i])
                else:
                    b=''
                a['commentaire']=b
                dic={
                'post'+str(i+1):a
                }
                self.posts.update(dic)
                print(i+1)
            except:
                break

    def get_images(self,user_id):
        """return the n first images urls"""
        url_list=[]
        self.driver.get("https://www.facebook.com/"+str(user_id)+"/photos_all")
        time.sleep(3)
        for i in range(10):
            try:
                c=self.driver.find_elements_by_xpath('.//div[@class="rq0escxv rj1gh0hx buofh1pr ni8dbmo4 stjgntxs l9j0dhe7"]/div/div/a/img')
                url=c[i].get_attribute('src')
                url_list.append(url)
                try:
                    self.driver.execute_script("arguments[0].scrollIntoView();",c[i])
                except:
                    pass
            except:
                break
        print(url_list)
        return(url_list)
    def get_basic_info(self,user_id):
        """get the birthday and gender info from a user url"""
        self.driver.get("https://www.facebook.com/"+str(user_id)+"/about_contact_and_basic_info")
        time.sleep(3)
        try:
            BirthDay=self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div[3]/div/div[2]').text
        except:
            BirthDay=''
        try:
            Gender=self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/div[1]').text
        except:    
            Gender=''
        return(BirthDay,Gender)
    def post_details(publication_id):
        """get details from a post"""
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();",publication_id)
        except:
            pass
        time.sleep(1)
        try:
            bouton = self.driver.find_element_by_xpath(".//*[@class='see_more_link']")
            self.driver.execute_script("arguments[0].click();", bouton)
        except Exception:
            popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html')))
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
        try:
            nb_reaction=publication_id.find_element_by_xpath(".//span[@class='gpro0wi8 cwj9ozl2 bzsjyuwj ja2t1vim']").text
        except Exception:
            nb_reaction=0
        try:
            nb_comment=publication_id.find_element_by_xpath(".//span[@class='oi732d6d ik7dh3pa d2edcug0 hpfvmrgz qv66sw1b c1et5uql a8c37x1j muag1w35 enqfppq2 jq4qci2q a3bd9o3v knj5qynh m9osqain']").text
        except:
            nb_comment=0
        q=data
        user=publication_id.find_element_by_xpath(".//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p']").text
        date=publication_id.find_element_by_xpath(".//*[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw']").get_attribute("aria-label")
        try:
            contenu=publication_id.find_element_by_xpath(".//div[@class='ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a']").text
        except:
            contenu=publication_id.find_element_by_xpath(".//div[@id='jsc_c_2k']").text
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
        """get comments details from a post"""
        comments=[]
        time.sleep(1)
        try:
            see_more_comments = post_id.find_elements_by_xpath(".//div[@class='oajrlxb2 bp9cbjyn g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 g5gj957u p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys p8fzw8mz qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh gpro0wi8 m9osqain buofh1pr']")
            for link in see_more_comments:
                try:
                    self.driver.execute_script("arguments[0].click();", link)
                except Exception:
                    pass
        except Exception:
            pass
        data = post_id.find_elements_by_xpath(".//div[@class='stjgntxs ni8dbmo4 g3eujd1d']")
        for d in data:
            try:
                author = d.find_element_by_xpath(".//div[@class='nc684nl6']").text
                try:
                    text = d.find_element_by_xpath(".//div[@class='ecm0bbzt e5nlhep0 a8c37x1j']").text
                except:
                    text=""
                date=d.find_element_by_xpath(".//*[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl m9osqain gpro0wi8 knj5qynh']").text
                comments.append([author, text, date])
            except Exception:
                pass
        return(comments)


            
       
