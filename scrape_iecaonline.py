import selenium
import json
import requests
import pandas as pd

pd.options.display.max_rows = None
#pd.options.display.max_columns = None
#pd.options.display.max_colwidth = None

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

# defined functions
def isCollege(text):
	if text is None:
		return ''

	if 'College' in text:
		return 'Yes'
	else:
		return ''

def isSchool(text):
	if text is None:
		return ''

	if 'School' in text:
		return 'Yes'
	else:
		return ''

def isTheurapetic(text):
	if text is None:
		return ''

	if 'Therapeutic ' in text:
		return 'Yes'
	else:
		return ''

def isGraduate(text):
	if text is None:
		return ''

	if 'Graduate ' in text:
		return 'Yes'
	else:
		return ''

def isOther(text):
	if text is None:
		return ''

	if 'Other ' in text:
		return 'Yes'
	else:
		return ''

def getCity(addr):
	splitText = addr.split(',')

	return splitText[0]

def getState(addr):
	firstSplit = addr.split(',')

	if 'United States' in addr:		
		secondSplit = firstSplit[1].split(' ')

		return secondSplit[1]
		#return firstSplit[1]
	else:
		return firstSplit[-1]

def getCountry(addr):
	splitText = addr.split(',')

	#return splitText[-1]
	
	if 'United States' in splitText[-1]:
		return 'US'
	else:
		return splitText[-1]	

firefoxOptions = Options()
firefoxOptions.add_argument('-headless')

res = {}
firstNameList = []
lastNameList = []
emailList = []
orgList = []
phoneList = []
siteList = []
collegeList = []
schoolList = []
therapeuticList = []
graduateList = []
otherList = []
cityList = []
stateList = []
countryList = []

webDriverPath = '/opt/firefox/geckodriver/geckodriver'

baseUrl = 'https://www.iecaonline.com/'
memberSearchUrl = 'wp-content/plugins/netforum-importer-with-sync/memberSearchAjax.php'

driver = webdriver.Firefox(executable_path=webDriverPath, options=firefoxOptions)
driver.implicitly_wait(15)
wait = WebDriverWait(driver,15)

headers = {'User-Agent': driver.execute_script('return navigator.userAgent;')}
getResponse = requests.get(baseUrl + memberSearchUrl, headers = headers)
getResult = json.loads(getResponse.text)
#print(result['recordsTotal'])

data = {
	'draw': '1',
	'columns[0][data]': '0',
	'columns[0][name]': '',
	'columns[0][searchable]': 'true',
	'columns[0][orderable]': 'false',
	'columns[0][search][value]': '',
	'columns[0][search][regex]': 'false',
	'columns[1][data]': '1',
	'columns[1][name]': '',
	'columns[1][searchable]': 'true',
	'columns[1][orderable]': 'true',
	'columns[1][search][value]': '',
	'columns[1][search][regex]': 'false',
	'columns[2][data]': '2',
	'columns[2][name]': '',
	'columns[2][searchable]': 'true',
	'columns[2][orderable]': 'true',
	'columns[2][search][value]': '',
	'columns[2][search][regex]': 'false',
	'columns[3][data]': '3',
	'columns[3][name]': '',
	'columns[3][searchable]': 'true',
	'columns[3][orderable]': 'true',
	'columns[3][search][value]': '',
	'columns[3][search][regex]': 'false',
	'columns[4][data]': '4',
	'columns[4][name]': '',
	'columns[4][searchable]': 'true',
	'columns[4][orderable]': 'true',
	'columns[4][search][value]': '',
	'columns[4][search][regex]': 'false',
	'columns[5][data]': '5',
	'columns[5][name]': '',
	'columns[5][searchable]': 'true',
	'columns[5][orderable]': 'true',
	'columns[5][search][value]': '',
	'columns[5][search][regex]': 'false',
	'columns[6][data]': '6',
	'columns[6][name]': '',
	'columns[6][searchable]': 'true',
	'columns[6][orderable]': 'true',
	'columns[6][search][value]': '',
	'columns[6][search][regex]': 'false',
	'columns[7][data]': '7',
	'columns[7][name]': '',
	'columns[7][searchable]': 'true',
	'columns[7][orderable]': 'true',
	'columns[7][search][value]': '',
	'columns[7][search][regex]': 'false',
	'columns[8][data]': '8',
	'columns[8][name]': '',
	'columns[8][searchable]': 'true',
	'columns[8][orderable]': 'true',
	'columns[8][search][value]': '',
	'columns[8][search][regex]': 'false',
	'columns[9][data]': '9',
	'columns[9][name]': '',
	'columns[9][searchable]': 'true',
	'columns[9][orderable]': 'true',
	'columns[9][search][value]': '',
	'columns[9][search][regex]': 'false',
	'columns[10][data]': '10',
	'columns[10][name]': '',
	'columns[10][searchable]': 'true',
	'columns[10][orderable]': 'true',
	'columns[10][search][value]': '',
	'columns[10][search][regex]': 'false',
	'order[0][column]': '0',
	'order[0][dir]': 'asc',
	'start': '0',
	'length': getResult['recordsTotal'],
	'search[value]': '',
	'search[regex]': 'false'
}

postResponse = requests.post(url = baseUrl + memberSearchUrl, data = data, headers = headers)
postResult = json.loads(postResponse.text)
#print(postResult)

for i in range(getResult['recordsTotal']):
	#print(postResult['data'][i][1].)
	#driver.get(baseUrl + )

	# get first name	
	soup = BeautifulSoup(postResult['data'][i][1], 'html.parser')
	aTags = soup.findAll('a')
	for a in aTags:		
		print('First Name:', a.text.strip())
		firstNameList.append(a.text.strip())

	# get last name
	soup = BeautifulSoup(postResult['data'][i][2], 'html.parser')
	aTags = soup.findAll('a')
	for a in aTags:
		print('Last Name:', a.text.strip())
		lastNameList.append(a.text.strip())

		#print(a['href'])
		driver.get(baseUrl + a['href'])
		
		orgName = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/main/div/div[2]/div[1]/div[2]/div/label[1]')))
		#orgName = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/main/div/div[2]/div[1]/div[2]/div/label[1]')
		orgList.append(orgName.text.strip('Company: '))
		print(orgName.text.strip('Company: '))
		
		primaryPhone = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/main/div/div[2]/div[1]/div[2]/div/label[3]')))
		#primaryPhone = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/main/div/div[2]/div[1]/div[2]/div/label[3]')
		phoneList.append(primaryPhone.text.strip('Primary Phone: '))
		print(primaryPhone.text.strip('Primary Phone: '))

		primaryEmail = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/main/div/div[2]/div[1]/div[2]/div/label[5]/a')))
		#primaryEmail = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/main/div/div[2]/div[1]/div[2]/div/label[5]/a')
		emailList.append(primaryEmail.text)
		print(primaryEmail.text)

		primarySite = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/main/div/div[2]/div[1]/div[2]/div/label[6]/a')))
		#primarySite = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/main/div/div[2]/div[1]/div[2]/div/label[6]/a')
		siteList.append(primarySite.text)
		print(primarySite.text)

		#driver.close()

	# get specialty code		
	collegeList.append(isCollege(postResult['data'][i][3]))
	schoolList.append(isSchool(postResult['data'][i][3]))
	therapeuticList.append(isTheurapetic(postResult['data'][i][3]))
	graduateList.append(isGraduate(postResult['data'][i][3]))
	otherList.append(isOther(postResult['data'][i][3]))

	# get primary address
	cityList.append(getCity(postResult['data'][i][9]))
	stateList.append(getState(postResult['data'][i][9]))
	countryList.append(getCountry(postResult['data'][i][9]))	

	print('--------------')

'''
print('firstNameList: ', len(firstNameList))
print('lastNameList: ', len(lastNameList))
print('cityList: ', len(cityList))
print('stateList: ', len(stateList))
print('countryList: ', len(countryList))
print('collegeList: ', len(collegeList))
print('schoolList: ', len(schoolList))
print('therapeuticList: ', len(therapeuticList))
print('graduateList: ', len(graduateList))
print('otherList: ', len(otherList))
'''

res['firstName'] = firstNameList
res['lastName'] = lastNameList
res['email'] = emailList
res['organizationName'] = orgList
res['website'] = siteList
res['phone'] = phoneList
res['city'] = cityList
res['state'] = stateList
res['country'] = countryList
res['college'] = collegeList
res['school'] = schoolList
res['therapeutic'] = therapeuticList
res['graduate'] = graduateList
res['other'] = otherList

df = pd.DataFrame(res)
print(df)
df.to_csv('ieca_member_list.csv')
