import requests
from bs4 import BeautifulSoup # type: ignore
import pandas as pd # type: ignore
from itertools import zip_longest
import itertools

all_names = []
def scrape_college_names(url,num):
    
    # print("Last Page: ",num)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    
    box = soup.find("div", class_ ="row collegeBlock")
    names = box.find_all("h2")
    names_list = [i.text.strip() for i in names]

    state_names = soup.find_all("div", class_ = "s-filters-box")
    state_list = [i.text.strip() for i in state_names][1]    
        
    degree_names = soup.find_all("div", class_ = "s-filters-box")
    degree_list = [i.text.strip() for i in degree_names][0]
    
    if num==True:
        for items in names_list:
            all_names.append([items,state_list,degree_list])
        df = pd.DataFrame(all_names, columns = ["Colleges","State","Degree"])
        Path = 'D:/'
        df.to_csv(Path + "CollegeDekho_FINALE.csv", index=False)
    else:
        for items in names_list:
            all_names.append([items,state_list,degree_list])

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



    state_list = ['uttaranchal',
                  'uttar-pradesh',
                  'west-bengal',
                  'telangana',
                  'dubai',
                  'ladakh',
                  'nagaland',
                  'lakshadweep']
    
    
    degree_list = ['bsc','diploma','ba','bcom','mba_degree','bed','msc','btech','ma','bhms','bams','bpth'
                    ,'ca','baf','mtech','llb','other','bhm','bba','bbm','bms','bft','bbs',
                    'bmm','biba','bim','certificate','bfsc','bped','llm','ms','pgexp',
                    'bba_mba','bbm_mba','btech_mba','mfm','mmm','mbs','mhrdm','bfa','mcm','mpm','mdes',
                    'bp','btech_mtech','bs_ms','bca','ba_llb','bcom_llb','bba_llb','mch','mhm','btm','bjmc','mjmc'
                    ,'mha','mmc','med','bs','bplan','bfad','bdes','mtm','bhmct','bmc','msc_mba',
                    'bcom_mba','bsc_llb','bbi','bvs','gnm','ba_bed','bsc_bed','mta','msw','mfc','mtech_phd','pgdm'
                    ,'mms','bam','mam_2','bca_mca','bsw','mfm_fashion','mfac','mplan','mca','pgd','md_2','ms_surgery',
                    'bachelor_of_dental_surgery_bds','auxiliary_nursing_and_midwifery_anm','bachelor_of_visual_arts_bva',
                    'master_of_visual_arts_mva','bpharm_mpharm','bpharm_mba','mpharm_mba','bachelor_of_library_sciences_blib'
                    ,'master_of_library_sciences_mlib','btech_ms','masters_in_international_business_mib',
                    'bdes_mdes_integrated','bachelor_in_hospitality_management','msc_phd','post_graduate_program_in_management'
                    ,'btech_llb','master_of_physical_education','bachelor_of_fashion_technology','bachelor_of_occupational_therapy'
                    ,'master_of_occupational_therapy_moth','bachelor_of_para_medical_technology_bpmt',
                    'bachelor_of_medical_lab_technology_bmlt','doctor_of_pharmacy_pharmd','basic_teacher_certificate_btc',
                    'mbapgdm','bachelor_of_commercemaster_of_commerce_bcommcom','bachelor_of_vocational_bvoc','bachelor_of_unani_medicine_and_surgery_bums'
                    ,'bachelor_of_multimedia_communication_bmmc','bachelor_of_multimedia_bmm','bachelor_of_elementary_education_beled',
                    'master_of_ayurvedic_medicine_and_surgery_mams','master_of_business_management_mbm','bachelor_of_naturopathy_and_yogic_sciences_bnys',
                    'bachelor_of_financial_markets_bfm','master_of_foreign_trade_mft','bachelor_of_hospital_management','bachelor_preparatory_programme_bpp'
                    ,'bachelor_of_home_science_bhs','master_of_hospitality_management_mhm','bachelor_of_music_bmus','master_of_music_mmus',
                    'master_of_business_economics_mbe','bachelor_of_human_resources_management','bachelor_of_legal_science_bachelor_of_law_b_l_s_ll_b',
                    'master_of_fishery_science_mfsc','bachelor_of_sciencemaster_of_science_bscmsc','bachelor_of_textile_btext','mtext',
                    'diplomate_of_national_board_dnb','master_in_fashion_apparel_design_mfad','post_doctoral_of_medicine_dm',
                    'master_of_journalism_mass_communication_mjmc_pgp_in_media_management_mjmc_pgp','bachelor_of_law_master_of_law_llbllm',
                    'bachelor_of_hotel_management_and_catering_technology_master_of_business_administration_bhmct_mba',
                    'bachelor_of_artsmaster_of_arts','bachelor_of_optometry','master_of_optometry_mot','master_of_veterinary_science_mvsc',
                    'bachelor_of_siddha_medicine_and_surgery_bsms','bachelor_of_visual_communication_bvc',
                    'bachelor_of_computer_application_master_of_business_administration_bca_mba','bsc_mba'
                    ,'master_of_vocational_mvoc','bedmed','executive_mba','executive_pgdm','master_of_philosophy_phd','llmmba','master_of_information_management'
                    ,'post_graduate_diploma_in_business_management_pgdbm','other_2','master_of_public_health','bachelor_in_sports_management',
                    'masters_in_sports_management','master_in_business_law','bachelor_of_performing_arts_bpa','master_of_performing_arts_mpa',
                    'bachelor_in_audiology_speech_language_pathology','mba_pgpm','diploma_btech','master_of_tourism_and_travel_management',
                    'bachelor_of_business_administration_bba_post_graduate_diploma_pgd','bhm_mba_bachelor_of_hospitality_management_master_in_business_management',
                    'post_graduation_degree','practice_degree','bhabachelor_of_hospital_administration','master_of_global_business'
                    ,'bgfm','master_of_media_science','bca_llb','diploma_in_vocation','master_in_medical_laboratory_technology','post_graduate_diploma_in_computer_application',
                    'master_in_human_resources_management','diploma_in_pharmacy','lld_doctor_of_law','dsc_doctor_of_science','dlitt_doctor_of_literature',
                    'pgp_post_graduate_programme','bachelor_in_tourism_and_hotel_management',
                    'post_doctoral_certificate_course','master_in_valuation','master_in_labour_welfare','diploma_bba','llm_phd',
                    'be_me','llb_mba','licence','bachelor_of_oriental_learning','vachaspati','medical_records_management_mrm','master_of_social_work',
                    'bachelor_of_travel_and_tourism_management_bttm_master_of_travel_and_tourism_managementmttm','bachelor_of_social_work_and_master_of_social_work',
                    'integrated_teacher_education_programme','practical_training_and_skill_development_program','integrated_master_of_rural_studies',
                    'bachelor_of_performing_arts_and_master_of_performing_arts','diploma_in_performing_arts','doctor_of_philosophy_phd_in_life_science']

    # Generate all combinations of state and degree using itertools.product
    combinations = list(itertools.product(state_list, degree_list))

    for state, degree in combinations:
        state_url = f"https://www.collegedekho.com/{degree}-colleges-in-{state}/?"
        totalPages = getMaxPageNumbers(state_url)    
        print(f"Total Pages in {state} state for {degree} degree:", totalPages)
        for page_num in range(1, totalPages+1):
            url = f"{state_url}page={page_num}"
            print("Scraping URL: ", url)
            scrape_college_names(url, num=(page_num == totalPages))        
    # if state != state_list[-1]:
    #     print("Next State: ")
            
if __name__ == "__main__":
    main()