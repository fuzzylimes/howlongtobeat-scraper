from bs4 import BeautifulSoup
import requests, sys, json

HLTB_URL = 'https://howlongtobeat.com/search_results.php?page=1'
HLTB_PRE = 'https://howlongtobeat.com/'

### Main Function ###
def HLTB(title):
    try:
        times, title, url = FindGame(title)
        return {title: {'url': url, 'Main Story': times[0][1], 'Main + Extra': times[1][1],'Completionist': times[2][1]}}
    except:
        raise

#######################################
# Helpers
#######################################
def FindGame(title):
    soup = BeautifulSoup(GetPage(title), 'lxml')
    try:
        page = soup.findAll("div", class_="search_list_details")[0]
    except IndexError as e:
        raise Exception('{} Not Found'.format(title))
    tmp = page.find("a", title=True, href=True)
    title,url = tmp['title'], HLTB_PRE + tmp['href']
    scrape = page.findAll("div", class_="search_list_tidbit")
    result = [
        (scrape[0].text.encode('utf-8').split(' ')[1],"{}Hrs".format(scrape[1].text.encode('utf-8').split(' ')[0])),
        (''.join(scrape[2].text.encode('utf-8').split(' ')[1:]),"{}Hrs".format(scrape[3].text.encode('utf-8').split(' ')[0])),
        (scrape[4].text.encode('utf-8'),"{}Hrs".format(scrape[5].text.encode('utf-8').split(' ')[0]))
    ]
    return result, title, url
    
def GetPage(title):
    data={'queryString':title}
    return requests.post(HLTB_URL,data=data).text

#######################################

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    response = HLTB(' '.join(sys.argv[1:]))
    print(json.dumps(response, indent=4, default=str).decode('unicode-escape'))
