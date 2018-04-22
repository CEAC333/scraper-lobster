#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
import csv
import sys

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

driver = webdriver.Chrome("/usr/bin/chromedriver")

def find_between( s, first, last ):
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""


class Item():
	"""docstring for Item"""
	def __init__(self):
		self.item_url 	= ""
		self.name 		= ""
		self.img_url 	= ""
		self.prices     = []
		self.sizes		= []


def get_soup_in_country(option, tries=0):
	def click_country_main_menu():
		dropdown_menu = driver.find_element_by_xpath('//*[@id="country_list"]')
		dropdown_menu.click()
		opt = driver.find_element_by_xpath('//*[@id="country_list"]/option['+str(option)+']')
		opt.click()
	def click_country():
		dropdown_menu = driver.find_element_by_xpath('//*[@id="country_language_form"]/ul/li[1]/div/button')
		dropdown_menu.click()
		opt = driver.find_element_by_xpath('//*[@id="country_language_form"]/ul/li[1]/div/div/ul/li['+str(option)+']')
		opt.click()
	try:
		click_country_main_menu()
	except:
		try:
			click_country()
		except:
			if tries < sys.getrecursionlimit(): 
				return get_soup_in_country(option, tries+1)
			else:
				logger.error("RECURSION LIMIT HIT!!!!!!")
	time.sleep(1)
	soup = BeautifulSoup(driver.page_source, 'lxml')

	return soup



def get_item_urls_in_soup(soup):
	url_list = []
	items = soup.select('.product-grid')
	for item in items:
		logger.info(item.a['href'])
		url_list.append(item.a['href'])
	return url_list


def get_details_of_items(url_list):
	base_url = "https://www.lobstersnowboards.com"
	item_list = []
	for url in url_list: 
		logger.info(base_url+url)
		driver.get(base_url+url)
		new_item = Item()
		for country_option in range(2, 30+1):
			soup = get_soup_in_country(country_option)

			try:
				
				name 		= soup.select(".product-title")[0].text[5:]
				img_url 	= soup.select(".img-responsive")[0]['src']
				country 	= soup.select(".filter-option.pull-left")[0].text
				price 		= soup.select(".product_price")[0].select("h2")[-1].text
				size_soups 	= soup.select(".text")[34:]
				sizes = []
				for size_soup in size_soups:
					sizes.append(size_soup.text)

				logger.info(url)
				logger.info(name)
				logger.info(img_url)
				logger.info(country)
				logger.info(price)
				logger.info(sizes)
				logger.info("-------------------------------------------------------------")

				if new_item.name == "":
					new_item.item_url 	= url
					new_item.name 		= name
					new_item.img_url 	= img_url
				new_item.prices.append({country:price})
				new_item.sizes .append({country:sizes})	
			except:
				logger.error(url+' not available in '+country)

			

		write_in_csv(new_item)

def init_csv():
	with open('lobster.csv', 'w', newline='', encoding='utf-8') as csvfile:
		fields = ['ITEM_URL', 'NAME', 'IMG_URL', 'PRICES', 'SIZES']
		writer = csv.DictWriter(csvfile, fieldnames=fields)
		writer.writeheader()

def write_in_csv(item):
	with open('lobster.csv', 'a', newline='', encoding='utf-8') as csvfile:
		fields = ['ITEM_URL', 'NAME', 'IMG_URL', 'PRICES', 'SIZES']
		writer = csv.DictWriter(csvfile, fieldnames=fields)

		writer.writerow({
							'ITEM_URL'	:	item.item_url,
							'NAME'		:	item.name.encode('utf-8', 'ignore').decode('utf-8', 'ignore'),
							'IMG_URL'	:	item.img_url,
							'PRICES'	:	item.prices,
							'SIZES'		:	item.sizes
						})

def main():
	url = 'https://www.lobstersnowboards.com/shop/'

	driver.get(url)
	driver.maximize_window()

	init_csv()

	soup = get_soup_in_country(2)
	url_list = get_item_urls_in_soup(soup)
	get_details_of_items(url_list)

	driver.quit()