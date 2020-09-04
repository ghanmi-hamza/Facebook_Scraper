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


def get_browser(url,usr,pwd):
    options = webdriver.firefox.options.Options()
    #options.headless = True
    driver = webdriver.Firefox(executable_path=r"C:\Users\Hamza\Downloads\geckodriver.exe",options=options)
    driver.get(url)
    email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
    email.send_keys(usr)
    password = driver.find_element_by_xpath("//input[@id='pass']")
    password.send_keys(pwd)
    button = driver.find_element_by_xpath("""//*[@id="u_0_2"]""")
    button.click()
    return(driver)
def post_details(data,driver):
    """get details from a post"""
    try:
        driver.execute_script("arguments[0].scrollIntoView();",data)
    except:
        pass
    time.sleep(1)
    try:
        bouton = driver.find_element_by_xpath(".//*[@class='see_more_link']")
        driver.execute_script("arguments[0].click();", bouton)
    except Exception:
        popup = WebDriverWait(driver, 10). until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html')))
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
    try:
        nb_reaction=data.find_element_by_xpath(".//span[@class='gpro0wi8 cwj9ozl2 bzsjyuwj ja2t1vim']").text
    except Exception:
        nb_reaction=0
    try:
        nb_comment=data.find_element_by_xpath(".//span[@class='oi732d6d ik7dh3pa d2edcug0 hpfvmrgz qv66sw1b c1et5uql a8c37x1j muag1w35 enqfppq2 jq4qci2q a3bd9o3v knj5qynh m9osqain']").text
    except Exception:
        nb_comment=0
    q=data
    user=q.find_element_by_xpath(".//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p']").text
    date=q.find_element_by_xpath(".//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw']").get_attribute("aria-label")
    contenu=q.find_element_by_xpath(".//div[@class='ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a']").text
    try:
        img=q.find_element_by_xpath(".//a[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 a8c37x1j mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l tm8avpzi']")
        image=img.get_attribute('href')
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
def comments(id,driver):
    """get comments details from a post"""
    comments=[]
    lxlx=[]
    time.sleep(1)
    try:
        data = driver.find_element_by_xpath(".//*[@class='commentable_item']")
        reply_links = driver.find_elements_by_xpath(
            ".//a[contains(@class,'_4sxc _42ft')]")
        for link in reply_links:
            try:
                driver.execute_script("arguments[0].click();", link)
            except Exception:
                pass
        see_more_links = driver.find_elements_by_xpath(
            ".//a[contains(@class,'_5v47 fss')]")
        for link in see_more_links:
            try:
                driver.execute_script("arguments[0].click();", link)
            except Exception:
                pass
    except Exception:
        pass
    part = id.find_element_by_xpath(".//*[@class='commentable_item']")
    data = part.find_elements_by_xpath(".//div[@aria-label='Comment']")
    for d in data:
        try:
            lxlx.append(d.find_element_by_xpath(".//a[@class='_6qw4']").get_attribute('href').split('?')[0])
            author = d.find_element_by_xpath(".//a[@class='_6qw4']").text
            text = d.find_element_by_xpath(".//span[contains(@class,'_3l3x')]").text
            date=d.find_element_by_xpath(".//abbr[contains(@class,'livetimestamp')]").get_attribute('data-tooltip-content')
            comments.append([author, text, date])
        except Exception:
            pass
    reply=part.find_elements_by_xpath(".//div[@class='_2h2j']")
    for d in reply:
        try:
            author = d.find_element_by_xpath(".//a[@class='_6qw4']").text
            text = d.find_element_by_xpath(".//span[contains(@class,'_3l3x')]").text
            date=d.find_element_by_xpath(".//abbr[contains(@class,'livetimestamp')]").get_attribute('data-tooltip-content')
            comments.append([author, text, date])
        except Exception:
            pass
    
    return(comments,lxlx)
def posts_details(n,url,usr,pwd):
    """get info from the n first posts of a user """
    driver=get_browser(url,usr,pwd)
    post={}
    time.sleep(2)
    info = profile_data(driver)
    posts={}
    for i in range(n):
        c=driver.find_elements_by_xpath(".//*[@class='_5pcb _4b0l _2q8l']")
        a=post_details(c[i],driver)
        b=comments(c[i],driver)
        dic={
            'post'+str(i+1):a,
            'commentaire_post'+str(i+1):b
            }
        posts.update(dic)   
    return(posts)
def get_basic_info(driver,url):
    """get the birthday and gender info from a user url"""
    driver.get(url+"/about_contact_and_basic_info")
    try:
        BirthDay=driver.find_element_by_xpath(".//li[contains(@class, '_3pw9 _2pi4 _2ge8 _4vs2')]").text
    except:
        BirthDay=''
    try:
        Gender=driver.find_element_by_xpath(".//li[contains(@class, '_3pw9 _2pi4 _2ge8 _3ms8')]").text
    except:    
        Gender=''
    return(BirthDay,Gender)
def get_images(driver,url,n):
    """return the n first images urls"""
    url_list=[]
    driver.get(url+"/photos_all")
    time.sleep(2)
    for i in range(n):
        sc = WebDriverWait(driver, 10). until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html')))
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', sc)
        try:
            c=driver.find_elements_by_xpath(".//li[contains(@class, 'fbPhotoStarGridElement')]/a/div/i")
            d=c[i].get_attribute('style')
            url=d.split("url")[1][2:-3]
            url_list.append(url)
        except:
            break
    return(url_list)
def dictionnaire(p):
    """create a dict from a class p """
    dic={
        "name":p.name,
        "friends":p.friends,
        "image":p.image,
        "intro":p.intro,
        "Gender":p.gender,
        "Birthday":p.birthday,
        "images_urls":p.images_urls,
        "posts":p.posts
        }
    return(dic)
def save_data(data,name,folder_path):
    """save data in a specific folder path with the name as argument"""
    try:
        pathlib.Path(folder_path+name).mkdir(parents=True, exist_ok=False)
        images=data["images_urls"]
        images.append(data['image'])
        for e in data['posts']:
            images.append(data['posts'][e]['image'])
        i=0
        print(len(images))
        for e in images:
            try:
                urllib.request.urlretrieve(e,folder_path+name+"/"+str(i) + '.png')
                i=i+1
                print("succ")
            except:
                i=i+1
                print("errr")
        with open(folder_path+name+"\data.json", "a+", encoding="utf8") as json_file:
            json_file.write("\n")
            json.dump(data, json_file, ensure_ascii=False)
    except:
        print("folder already exists")
        pass


