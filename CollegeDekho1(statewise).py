import requests
from bs4 import BeautifulSoup # type: ignore
import pandas as pd # type: ignore

all_names = []
def scrape_college_names(url,num):
    
    # print("Last Page: ",num)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    
    box = soup.find("div", class_ ="row collegeBlock")
    names = box.find_all("h2")
    names_list = [i.text.strip() for i in names]

    state_names = soup.find_all("div", class_ = "s-filters-box")
    state_list = [i.text.strip() for i in state_names][0]
    if len(state_list) == 1:
        [i.text.strip() for i in state_names][0]
    else:
        [i.text.strip() for i in state_names][:2]    
    if num==True:
        for items in names_list:
            all_names.append([items,state_list])
        df = pd.DataFrame(all_names, columns = ["Colleges","State"])
        Path = 'D:/'
        df.to_csv(Path + "CollegeDekhoNames4.csv", index=False)
    else:
        for items in names_list:
            all_names.append([items,state_list])

# def getMaxPageNumbers(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text,'html.parser')
#     pages = soup.find_all("div", class_ = "pagination")
#     return len((pages))

def getMaxPageNumbers(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    pages = soup.find("div", class_="pagination")  # Find the pagination section
    if pages:  # Check if pagination section exists
        page_list = pages.find("ul")  # Find the ul tag within pagination
        if page_list:  # Check if ul tag exists
            page_items = page_list.find_all("li")  # Find all li tags within ul
            if len(page_items) >= 2:  # Ensure there are at least two li tags
                second_last_page = page_items[-2].text.strip()  # Get text of second last li tag
                return int(second_last_page)  # Return the page number as integer
    return 0  # Return 0 if pagination section or page numbers are not found

def main():
    state_list = ['bihar']
    
    for items in state_list:
        print(len(state_list))
        state_url = f"https://www.collegedekho.com/colleges-in-{items}/?"
        totalPages = getMaxPageNumbers(state_url)
        if totalPages == 0 :
            totalPages = 1  
        print(f"Total Pages in {items} state:",totalPages)
        for page_num in range(1, totalPages + 1):
            url = f"{state_url}page={page_num}"
            print("Scraping URL: ", url)
            scrape_college_names(url, num=(page_num == totalPages))
            
        if items != state_list[-1]:
            print("Next State: ")
            
if __name__ == "__main__":
    main()