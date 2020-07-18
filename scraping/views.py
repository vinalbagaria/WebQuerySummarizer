from django.shortcuts import redirect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# Create your views here.
def scrapePages(request,que):
    name = que
    search_item = que + " wikipedia"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    webdriver_path = r'C:\Users\Mohit-PC\.wdm\drivers\chromedriver\win32\83.0.4103.39\chromedriver.exe'  # Enter the file directory of the Chromedriver
    browser = webdriver.Chrome(webdriver_path, options=options)
    url = 'https://www.google.com/'
    browser.get(url)
    search_bar = browser.find_element_by_name('q')
    search_bar.send_keys(search_item, Keys.RETURN)
    time.sleep(2)
    l = []
    usedLinks = []
    i = 1
    count = 0
    flag = 0
    pages = 0
    while count != 14:
        try:
            t = browser.find_element_by_xpath(
                "/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[" + str(
                    i) + "]/div/div[1]/a")
            print(t.get_attribute('href'))
            usedLinks.append(t.get_attribute('href'))
            browser.get(t.get_attribute('href'))
            try:
                element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.tagName, "p")))
            except:
                pass
            try:
                full_page = browser.find_element_by_id('container')
                textpage = full_page.find_elements_by_tag_name('p')
                pages += 1
                for j in textpage:
                    l.append(j.text)
                count += 1
            except:
                try:
                    full_page = browser.find_elements_by_tag_name('p')
                    pages += 1
                    for j in full_page:
                        l.append(j.text)
                    count += 1
                except:
                    pass

            browser.back()
            time.sleep(1)
        except:
            flag += 1
            if flag == 2:
                i = 0
                search_bar = browser.find_element_by_class_name('G0iuSb').click()
                time.sleep(2)
            if flag == 4:
                break
            print("yes")
            pass
        i += 1
    browser.close()
    text_file = open("static/whole_text.txt", "w")
    for i in l:
        if i:
            try:
                text_file.write(i)
                text_file.write("\n")
            except:
                pass
    text_file.close()

    links_file = open('static/links.txt','w')
    for j in usedLinks:
        if j:
            try:
                links_file.write(j)
                links_file.write("\n")
            except:
                pass
    links_file.close()
    #Scrape,clean and make whole_text.txt
    return redirect(to='/summarize/')