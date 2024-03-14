from bs4 import BeautifulSoup
from lxml import etree, html
import requests
import re

URL_2 = "https://us.louisvuitton.com/eng-us/watches/connected-watches/all-connected-watches/_/N-txd0tau"

HEADERS = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

resp_2 = requests.get(URL_2, headers=HEADERS)
soup_2 = BeautifulSoup(resp_2.content, "html.parser")
dom_2 = etree.HTML(str(soup_2))

all_links_2 = soup_2.findAll('li', class_='lv-product-list__item')
links_lts_2 = []
for item in all_links_2:
  a_tag = item.find('a', class_ = 'lv-smart-link lv-product-card__url')
  if a_tag is not None:
    href = a_tag.get('href')
    links_lts_2 = links_lts_2 + [href]
    # print(href)

def get_reference_number(sample_soup):
  reference_number = None
  reference_number_dom = dom.xpath('//*[@id="main"]/div[2]/div[1]/section/div[2]/div/div/div[1]/span/strong')[0].text
  if reference_number_dom:
      reference_number_dom = reference_number_dom.split('\n')[1]
  return reference_number_dom

def get_style_2(sample_soup):
    style1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[2].find_all('li')
    style = ''
    for div in style1:
        style = style + div.text +', '
    return style

def get_case_material_2(sample_soup):
  case_material = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[0]#.text
  case_material = case_material.find_all('li')
  case_material1 = None
  x = 0
  for div in case_material:
    text_content = div.get_text()
    if text_content.find('Case:') != -1:
      case_material1 = text_content.split('Case:')[1]
      x = x +1
  if x == 0:
    case_matirial_=''
    for div in case_material:
      text_content = div.get_text()
      case_matirial_=case_matirial_+text_content +', '
    case_material1 = case_matirial_
  return case_material1


def get_case_finish_2(sample_soup):
  case_finish = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[0]
  case_finish = case_finish.find_all('li')
  case_finish1 = ''
  x = 0
  for div in case_finish:
    text_content = div.get_text()
    if text_content.find('polished') != -1:
      case_finish1= case_finish1 +  text_content +', '
      x = x +1
  if x == 0:
    case_finish_=' '
    for div in case_finish:
      text_content = div.get_text()
      case_finish_= case_finish_ +  text_content +', '
    case_finish1 = case_finish_
  return case_finish1

def get_caseback_2(sample_soup):
  caseback = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[0]#.text
  caseback = caseback.find_all('li')
  caseback1 = None
  for div in caseback:
    text_content = div.get_text()
    if text_content.find('Case back') != -1:
      caseback1 = text_content.split('back:')[1]
  return caseback1

def get_diameter_2(sample_soup):
  diameter1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[0]#.text
  diameter1 = diameter1.find_all('li')
  diameter = None
  for div in diameter1:
    text_content = div.get_text().split("\n")
    pattern = r'(?i)(?<=diameter:)\s*(\d+(\.\d+)?\s?(mm|inches))'
    matches = re.search(pattern, div.get_text())
    if matches:
      diameter = matches.group(0)
  return diameter

def get_case_thickness_2(sample_soup):
  case_thickness1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[0]#.text
  case_thickness1 = case_thickness1.find_all('li')
  case_thickness = None
  for div in case_thickness1:
    text_content = div.get_text().split("\n")
    pattern = r'(?i)(?<=Thickness:)\s*(\d+(\.\d+)?\s?(mm|inches))'
    matches = re.search(pattern, div.get_text())
    if matches:
      case_thickness = matches.group(0)
  return case_thickness

def get_crystal_2(sample_soup):
  crystal1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[0]#.text
  crystal1 = crystal1.find_all('li')
  crystal = None
  for div in crystal1:
    text_content = div.get_text()
    if text_content.find('crystal') != -1:
      crystal = text_content
  return crystal

def get_water_resistance_2(sample_soup):
    water_resistance1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[1]#.text
    water_resistance1 = water_resistance1.find_all('li')
    water_resistance = None
    for div in water_resistance1:
        text_content = div.get_text()
        if text_content.find('Water') != -1:
            water_resistance = text_content.split('resistance:')[1]
    water_resistance1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[2]#.text
    water_resistance1 = water_resistance1.find_all('li')
    for div in water_resistance1:
        text_content = div.get_text()
        if text_content.find('Water') != -1:
            water_resistance = text_content.split('resistance:')[1]
    return water_resistance

def get_dial_color_2(sample_soup):
  dial_color1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[0]#.text
  dial_color1 = dial_color1.find_all('li')
  dial_color = None
  dial = ''
  for div in dial_color1:
    text_content = div.get_text()
    dial = dial +text_content +', '
  dial_color =dial
  return dial_color

def get_bracelet_material_2(sample_soup):
  bracelet_material1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[0]#.text
  bracelet_material1 = bracelet_material1.find_all('li')
  bracelet_material = None
  x = 0
  for div in bracelet_material1:
    text_content = div.get_text()
    if text_content.find('material') != -1:
      bracelet_material = text_content.split('material')[1]
      x = x +1
  if x == 0:
    material = ''
    for div in bracelet_material1:
      text_content = div.get_text()
      material = material + text_content +', '
    bracelet_material = material
  return bracelet_material

def get_clasp_type_2(sample_soup):
  clasp_type1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[0]#.text
  clasp_type1 = clasp_type1.find_all('li')
  clasp_type = ''
  x = 0
  for div in clasp_type1:
    text_content = div.get_text()
    if text_content.find('Buckle:') != -1:
      clasp_type = text_content.split('Buckle:')[1]
      x = x +1
  if x == 0:
    material = ''
    for div in clasp_type1:
      text_content = div.get_text()
      clasp_type = clasp_type + text_content +', '
  return clasp_type

def get_movement_2(sample_soup):
  movement1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[2]#.text
  movement1 = movement1.find_all('li')
  movement = None
  for div in movement1:
    text_content = div.get_text()
    if str(text_content).find('Compatibility') != -1:
      movement = text_content
  movement1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[1]#.text
  movement1 = movement1.find_all('li')
  for div in movement1:
    text_content = div.get_text()
    if str(text_content).find('Compatibility') != -1:
      movement = text_content
  return movement

# def get_calibre_2(sample_soup):
#   calibre1 = soup.find(True, {'class':'lv-product-detailed-features__description'}).findAll('li')
#   calibre = None
#   for div in calibre1:
#       text_content = div.get_text().split("\n")
#       if str(text_content).find('calibre') != -1:
#           calibre =  text_content
#   return calibre

def get_power_reserve_2(sample_soup):
  power = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[1]#.text
  power = power.find_all('li')
  power_reserve = None
  for div in power:
    text_content = div.get_text()
    if str(text_content).find('battery') != -1:
      power_reserve = text_content.split('life:')[1]
  power = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[2]#.text
  power = power.find_all('li')
  for div in power:
    text_content = div.get_text()
    if str(text_content).find('battery') != -1:
      power_reserve = text_content.split('life:')[1]
  return power_reserve

def get_frequency_2(sample_soup):
  frequency1 = soup.findAll(True, 
{'class':'lv-product-detailed-features__description'})[0]#.text
  frequency1 = frequency1.find_all('li')
  frequency = None
  for div in frequency1:
    text_content = div.get_text()
    if str(text_content).find('Frequency') != -1:
      frequency = text_content
  return frequency

def get_price(sample_soup):
  prices = dom.xpath('//*[@id="main"]/div[2]/div[1]/section/div[2]/div/div/div[2]/span')[0].text
  prices = prices.split('$')[1]
  return prices

def get_parent_model(sample_soup):
  parent_model_dom = None
  parent_model_dom = dom.xpath('//*[@id="main"]/div[2]/div[1]/section/div[2]/div/div/div[1]/h1')
  if parent_model_dom:
      parent_model_dom = parent_model_dom[0].text.split('\n')[1]
  return parent_model_dom

def get_img(sample_soup):
  image_URL = [e.get('src') for e in dom.xpath('/html/body/div/div/div/main/div[2]/div[1]/section/div[1]/div/div/ul/li[1]/button/div/noscript/img')]
  return image_URL


sample_list_2 = []
x = 0
for url in links_lts_2:
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        dom = etree.HTML(str(soup))
        
        reference_number = get_reference_number(soup)
        # print(reference_number)
        types= None
        brand= 'Louis Vuitton'
        watch_URL= url
        # print(watch_URL)
        year_introduced= None
        parent_model= get_parent_model(soup)
        specific_model= get_parent_model(soup)
        nickname= None
        marketing_name= None
        style= get_style_2(soup)
        currency= 'USD'
        price= get_price(soup)
        image_URL= get_img(soup)
        made_in= None
        case_shape= None
        case_material= get_case_material_2(soup)
        case_finish= get_case_finish_2(soup)
        caseback= get_caseback_2(soup)
        diameter= get_diameter_2(soup)
        between_lugs= None
        lug_to_lug= None
        case_thickness= get_case_thickness_2(soup)
        bezel_material= None
        bezel_color= None
        crystal= get_crystal_2(soup)
        water_resistance= get_water_resistance_2(soup)
        weight= None
        dial_color= get_dial_color_2(soup)
        numerals= None
        bracelet_material= get_bracelet_material_2(soup)
        bracelet_color= None
        clasp_type= get_clasp_type_2(soup)
        movement= get_movement_2(soup)
        caliber= None
        power_reserve= get_power_reserve_2(soup)
        frequency= get_frequency_2(soup)
        # print(frequency)
        jewels= None
        features= None
        description= None
        short_description = None
        x = x+1
        sample_list_2.append([ reference_number, watch_URL, types, brand, 
year_introduced, parent_model, specific_model, nickname, marketing_name, 
style, currency, price, image_URL, made_in, case_shape, case_material, 
case_finish, caseback, diameter, between_lugs, lug_to_lug, case_thickness, 
bezel_material, bezel_color, crystal, water_resistance, weight, 
dial_color, numerals, bracelet_material, bracelet_color, clasp_type, 
movement, caliber, power_reserve, frequency, jewels, features, 
description, short_description ])
    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")

import csv
with open('list_7.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sample_list_2)

from pandas import read_csv  
import pandas as pd    
df_2 = read_csv('list_7.csv',header=None)
df_2

df_2.columns = ['reference_number',
        'watch_URL',
        'type',
        'brand', 
        'year_introduced',
        'parent_model',
        'specific_model',
        'nickname',
        'marketing_name',
        'style',
        'currency',
        'price',
        'image_URL',
        'made_in',
        'case_shape',
        'case_material',
        'case_finish',
        'caseback',
        'diameter',
        'between_lugs',
        'lug_to_lug',
        'case_thickness',
        'bezel_material',
        'bezel_color',
        'crystal',
        'water_resistance',
        'weight',
        'dial_color',
        'numerals',
        'bracelet_material',
        'bracelet_color',
        'clasp_type',
        'movement',
        'caliber',
        'power_reserve',
        'frequency',
        'jewels',
        'features',
        'description',
        'short_description']

df_2.to_csv('list_7.csv',index=False)
