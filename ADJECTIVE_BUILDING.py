
import requests
from bs4 import BeautifulSoup


#search_word = ''
search_word = 'rusty'
synonyms_list = []

def parse_synonym_initial():
    #multiple = range()
    #search_word = 'rusty'
    url = 'https://www.thesaurus.com/browse/' + search_word
    print(url)
    tier_1 = requests.get( url )
    soup = BeautifulSoup( tier_1.content, 'html.parser' )
    tier_1_results_div = soup.find( 'div' , class_='css-ixatld e15rdun50' )
    tier_1_results = tier_1_results_div.find_all( 'a' , class_='css-1n6g4vv eh475bn0' )

    for list_search_word in tier_1_results:
        list_search_word = list_search_word.text
        synonyms_list.append(list_search_word)
        print(list_search_word)

# tier_2_results_div = 
# tier_2_results = 

# tier_3_results_div = 
# tier_3_results = 


#<a font-weight="inherit" href="/browse/decayed" 
# data-linkid="nn1ov4" class="css-1n6g4vv eh475bn0">decayed<!-- --> 
# </a>

#<div data-testid="word-grid-container" class="css-ixatld e15rdun50">

parse_synonym_initial()
print(synonyms_list)

def parse_each_synonym():
    for each in synonyms_list:
        global search_word
        search_word = each
        if len(synonyms_list) > 50 :
            break
        parse_synonym_initial()
        #print(synonyms_list)

parse_each_synonym()

print(synonyms_list)

#this deletes duplicates
synonyms_list = list(dict.fromkeys(synonyms_list))


print(synonyms_list)