"""
File: webcrawler.py
Name: JP WU
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': 't-stripe'})
        total_male = 0
        total_female = 0
        for tag in tags:
            tbodys = tag.find_all('tbody')
            for tbody in tbodys:
                trs = tbody.find_all('tr')
                for tr in trs:
                    token = tr.text.split()
                    if len(token) == 5:
                        total_male += turn_num(token[2])
                        total_female += turn_num(token[4])
        print('Male Number: ', total_male)
        print('Female Number: ', total_female)


def turn_num(token):
    """
    Args:
        token (str): Number with comma. Python see it as a string.
    Returns:
        number (int): Number without comma. Python ses it as a integer.
    """
    num = ''
    for i in range(len(token)):
        if token[i] != ',':
            num += token[i]
    return int(num)


if __name__ == '__main__':
    main()
