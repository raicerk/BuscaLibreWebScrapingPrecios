import Scraping as scraping

if __name__ == "__main__":
    scr = scraping.scraping()
    scr.url = 'https://www.buscalibre.cl/libro-y-si-el-tiempo-no-existiera/9788425440571/p/51475704'
    result = scr.scrap()
    print (result)