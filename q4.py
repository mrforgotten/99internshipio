from urllib import request as ur
import bs4 as bs
import json
def logo_json():
    url = "https://theinternship.io/"
    url_contents = ur.urlopen(url).read()
    soup = bs.BeautifulSoup(url_contents,"html.parser")
    partner_list= soup.find_all("div",{"class":"partner"})

    companies_logo_dict = {"companies":[]}
    partner_tuple=list()
    for i in range(len(partner_list)):
        logo = partner_list[i].find("img")['src']
        span = partner_list[i].find("span",{"class":"list-company"}).text.strip()
        partner_tuple.append((logo,span))
        

    partner_tuple=sorted(partner_tuple, key = lambda partner : len(str(partner[1])) ,reverse=True)

    for i in partner_tuple:
        companies_logo_dict["companies"].append({"logo":"https://theinternship.io/{0}".format(i[0])})

    return json.dumps(companies_logo_dict, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print(logo_json())