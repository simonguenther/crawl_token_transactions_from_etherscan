import json, re
from Helper import get_html_cloud, save_dictionary_to_json, save_list_to_file, add_to_file
from bs4 import BeautifulSoup
from time import gmtime, strftime

# Enter Base URL here
BASE_URL = "https://etherscan.io/token/generic-tokentxns2?contractAddress=0x0000000000000000000000000000000000000000&mode=&p="

# change output file!
LOGFILE = "all_blockv_transactions_crawled_from_etherscan.io.txt"

# DO NOT CHANGE BELOW THIS LINE!
all_regex = r"A\sTotal\sof\s[0-9]*\sevents\sfound"

all_hashes = []

def get_total_number_of_transactions(url):
    html = get_html_cloud(BASE_URL+"1")
    #print html
    results = re.findall(all_regex, html, 0)
    results = results[0].split(' ')
    return results[3]

def get_tx_hashes_from_page(html):
    soup = BeautifulSoup(html, "lxml")
    hashes = []
    for results in soup.findAll("span", { "class": "address-tag"}):
        if len(results.text) == 66:
            hashes.append(results.text)
            add_to_file(LOGFILE,results.text)
    return hashes

total_txs =get_total_number_of_transactions(BASE_URL)
pages = int(total_txs)/50
print str(strftime("%H:%M:%S", gmtime()))+ ": Total number of transactions: %s (%s pages)" % (total_txs, pages+1)

for i in range (1, pages+2):
    print str(strftime("%H:%M:%S", gmtime())) + ": Processing page %s / %s" % (i, pages+1)
    url = BASE_URL + str(i)
    html = get_html_cloud(url)
    page_hashes = get_tx_hashes_from_page(html)
    all_hashes.extend(page_hashes)

print "Transaction hashes collected: %s " % str(len(all_hashes))
