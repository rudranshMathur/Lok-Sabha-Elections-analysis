import requests
from bs4 import BeautifulSoup
import csv


#Dict of State/UnionTerr as it was in html option
state={
    'U01': 'Andaman & Nicobar Islands',
    'S01': 'Andhra Pradesh',
    'S02': 'Arunachal Pradesh',
    'S03': 'Assam',
    'S04': 'Bihar',
    'U02': 'Chandigarh',
    'S26': 'Chhattisgarh',
    'U03': 'Dadra & Nagar Haveli and Daman & Diu',
    'S05': 'Goa',
    'S06': 'Gujarat',
    'S07': 'Haryana',
    'S08': 'Himachal Pradesh',
    'U08': 'Jammu and Kashmir',
    'S27': 'Jharkhand',
    'S10': 'Karnataka',
    'S11': 'Kerala',
    'U09': 'Ladakh',
    'U06': 'Lakshadweep',
    'S12': 'Madhya Pradesh',
    'S13': 'Maharashtra',
    'S14': 'Manipur',
    'S15': 'Meghalaya',
    'S16': 'Mizoram',
    'S17': 'Nagaland',
    'U05': 'NCT OF Delhi',
    'S18': 'Odisha',
    'U07': 'Puducherry',
    'S19': 'Punjab',
    'S20': 'Rajasthan',
    'S21': 'Sikkim',
    'S22': 'Tamil Nadu',
    'S29': 'Telangana',
    'S23': 'Tripura',
    'S24': 'Uttar Pradesh',
    'S28': 'Uttarakhand',
    'S25': 'West Bengal'
}

for i in ['U01', 'S01', 'S02', 'S03', 'S04', 'U02', 'S26', 'U03', 'S05', 'S06', 'S07', 'S08', 'U08', 'S27', 'S10', 'S11', 'U09', 'U06', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'U05', 'S18', 'U07', 'S19', 'S20', 'S21', 'S22', 'S29', 'S23', 'S24', 'S28', 'S25']:
    url= "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-" + i + ".htm"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')

    if table:
        with open( state[i]+'.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            rows = table.find_all('tr')

            for row in rows:
                csvwriter.writerow([cell.text.strip() for cell in row.find_all(['td', 'th'])])

        print('Table data has been saved to' +state[i]+ '.csv')

    else:
        print('Table not found on the webpage.')
