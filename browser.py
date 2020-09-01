from selenium import webdriver
import time

def marketSearch():

    alliases = {'neu': 'neuroptics',
                'sys': 'system',
                'cha': 'chassis',
                'bp' : 'blueprint'
                }

    search = input('Recherche : ')
    lst = search.split()

    for i in range(len(lst)):
        if lst[i] in alliases:
            lst[i] = alliases[lst[i]]
    search = ' '.join(lst)

    browser = webdriver.Firefox()
    time.sleep(.01)
    browser.get('https://warframe.market/')

    searchBar = browser.find_element_by_xpath("/html/body/section/section/div/section[1]/div[1]/section/div/section/div/section/span/input")
    searchbutton = browser.find_element_by_xpath("/html/body/section/section/div[2]/section[1]/div[1]/section/div/section/button")
    searchBar.send_keys(search)
    searchbutton.click()

if __name__ == '__main__':
    marketSearch()
