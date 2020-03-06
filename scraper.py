from requests import get
from bs4 import BeautifulSoup

def scrape():
    '''
    Returns all players on atp site 
    '''
    url = 'https://www.atptour.com/en/rankings/singles?rankDate=2020-03-02&rankRange=1-5000'
    response = get(url)
    print(response.text[:500])

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    table_body = html_soup.find('tbody')
    rows = table_body.find_all('tr')
    #print(len(rows))
    all_cols = []

    for row in rows:
        #cols = row.find_all('td', class_ = 'player-cell')
        cols = row.find_all('td')
        cols=[x.text.strip() for x in cols]
        #print(cols)
        all_cols.append(cols)

    #print(type(all_cols)
    #print(all_cols[0])
    return all_cols


    

