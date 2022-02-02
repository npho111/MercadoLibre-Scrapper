from datetime import date
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
data_paises = {'Argentina':'https://tendencias.mercadolibre.com.ar',
            'Brasil':'https://tendencias.mercadolivre.com.br',
            'Chile':'https://tendencias.mercadolibre.cl',
          'Colombia':'https://tendencias.mercadolibre.com.co',
          'Dominicana':'https://tendencias.mercadolibre.com.do',
          'Ecuador':'https://tendencias.mercadolibre.com.ec',
          'Peru':'https://tendencias.mercadolibre.com.pe',
          'México':'https://tendencias.mercadolibre.com.mx',
            'Panama':'https://tendencias.mercadolibre.com.pa',
            'Perú':'https://tendencias.mercadolibre.com.pe',
          'Uruguay':'https://tendencias.mercadolibre.com.uy',
          'Venezuela':'https://tendencias.mercadolibre.com.ve',}

class ScrapperMercadoLibre:
    def __init__(self,paises):
        self.today = date.today()
        self.paises = paises
        self.data = pd.read_csv('/home/nikoh/Desktop/toy api/DATA.csv') #pd.DataFrame(columns=['ranking','Producto','Fecha','Pais','Link'])
    def scrap(self):
        for paises,urls in self.paises.items():
            uClient = uReq(urls)
            page_html = uClient.read()
            page_soup = soup(page_html,"html.parser")
            masusadas = page_soup.findAll("li",{"class":"searches__item"})
            today = str(date.today())
            for i in range(len(masusadas)):
                self.data.loc[i] = [i+1,masusadas[i].a.text,today,paises,masusadas[i].a['href']]
            self.data.to_csv('/home/nikoh/Desktop/toy api/DATA.csv',mode='a', header=False,index=False)


ScrapperMercadoLibre(data_paises).scrap()