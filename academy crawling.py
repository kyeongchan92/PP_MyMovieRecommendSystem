# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:11:49 2021

@author: KYEONGCHAN LEE

CSS selector

- tag1, tag2
- tag1 tag2 => 자손 (find_all(recursive=True))
- tag1 > tag2 => 자식 (find_all(recursive=False))
- tag1 + tag2 => 형제(다음노드) => tag2
- a:nth-of-type()
"""
#%%
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re
import pandas as pd

#%%
# driver.close()


url = 'http://awardsdatabase.oscars.org/'
data_PATH = 'J:/내 드라이브/015GithubRepos/MyMovieRecommendSystem/data/'
driver = webdriver.Chrome('J:/내 드라이브/015GithubRepos/MyMovieRecommendSystem/chromedriver.exe')
wait = WebDriverWait(driver,40)


driver.get(url)

# driver.close()

wantfromy = 2020
wanttoy = 2020

# 화면 최대화
# driver.maximize_window()

# from year dropdown 클릭
drop_down_click = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.row-search-delimiters button:nth-of-type(1)")))
drop_down_click.click()


# from year dropdown 연도 클릭
for _ in driver.find_elements_by_css_selector(
    'div#basicsearch div.row-search-delimiters div.control-multiselect-showyear:nth-of-type(1) ul li'):
    if str(wantfromy) in _.text:
        _.click()


# to year dropdown 클릭
# 화면이 좁아져서 from year의 dropdown이 to year를 가리면 안된다.
drop_down_click = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.row-search-delimiters div.control-multiselect-showyear:nth-of-type(2) button")))
drop_down_click.click()
for _ in driver.find_elements_by_css_selector(
    'div#basicsearch div.row-search-delimiters div.control-multiselect-showyear:nth-of-type(2) ul li'):
    if str(wanttoy) in _.text:
        _.click()


# search 버튼 클릭
driver.find_elements_by_css_selector('button#btnbasicsearch')[0].click()









#%%




prizename = []
nominationstatement = []
films = []
win = []
charactor = []
songtitle = []

dom = BeautifulSoup(driver.page_source, 'html.parser')
for prize in dom.select('div.result-subgroup.subgroup-awardcategory-chron'):
    
    # prize_name
    pnm = prize.select_one('.result-subgroup-title').text.strip()
    print(f'prize name : {pnm}')

    
    nominationst = ''
    film_title = ''
    chrt = ''
    songt = ''
    
    
    # 후보 구분자 class : actingorsimilar : 후보이름(사람)-상영작 {작품이름}의 경우, 각 candidate구분자
    if prize.select('.result-details.awards-result-actingorsimilar'):
        print('actingorsimilar 유형\n')
        
        # 후보들 for문
        for candidate in prize.select('.result-details.awards-result-actingorsimilar'):

            # nomination statement ex) 최우식
            nominationst = candidate.select_one('.awards-result-nominationstatement').text.strip()
            print(f'nominationstatement : {nominationst}')

            # film info1 ex) Parasite
            film_title = candidate.select_one('.awards-result-film').text.strip()
            print(f'film_title : {film_title}')

            # character ex) 기우역
            if candidate.select_one('.awards-result-character'):
                chrt = candidate.select_one('.awards-result-character').text.strip()
                print(f'character : {chrt}')
            
            # winner 여부
            if candidate.select_one('span'):
                winornot = 1
                print('winner+++++++++')
            else:
                winornot = 0
                
            prizename.append(pnm)
            nominationstatement.append(nominationst)
            films.append(film_title)
            charactor.append(chrt)
            songtitle.append(songt)
            win.append(winornot)


            print()

        
    # 후보 구분자 class : other : 작품이름-사람이름의 경우, 각 candidate구분자
    elif prize.select('.result-details.awards-result-other'):
        print('other 유형\n')
        
        # 후보들 for문
        for candidate in prize.select('.result-details.awards-result-other'):
            
            # nomination statement
            nominationst = candidate.select_one('.awards-result-nominationstatement').text.strip()
            print(f'nominationstatement : {nominationst}')
            
            # film_title
            film_title = candidate.select_one('.awards-result-film a').text.strip()
            print(f'film_title : {film_title}')

            # winner 여부
            if candidate.select_one('span'):
                winornot = 1
                print('winner+++++++++')
            else:
                winornot = 0
                
            print()
            
            prizename.append(pnm)
            nominationstatement.append(nominationst)
            films.append(film_title)
            charactor.append(chrt)
            songtitle.append(songt)
            win.append(winornot)
    
    # 후보 구분자 class : song (주제가상)
    elif prize.select('.result-details.awards-result-song'):
        print('song 유형\n')
        
        # 후보들 for문
        for candidate in prize.select('.result-details.awards-result-song'):
            
            # nomination statement
            nominationst = candidate.select_one('.awards-result-nominationstatement').text.strip()
            print(f'nominationstatement : {nominationst}')
            
            # film_title
            film_title = candidate.select_one('.awards-result-film a').text.strip()
            print(f'film_title : {film_title}')
            
            # song title
            songt = candidate.select_one('.awards-result-songtitle').text.strip()
            print(f'song_title : {songt}')
            
            # winner 여부
            if candidate.select_one('span'):
                winornot = 1
                print('winner+++++++++')
            else:
                winornot = 0
                
            prizename.append(pnm)
            nominationstatement.append(nominationst)
            films.append(film_title)
            charactor.append(chrt)
            songtitle.append(songt)
            win.append(winornot)
                
            print()
        
        
        
        
        
        
        
    print('***********************************')


#%%
df = pd.DataFrame({
    'prizename': prizename,
    'nominationstatement': nominationstatement,
    'films': films,
    'charactor': charactor,
    'songtitle': songtitle,
    'win': win
})


#%%

# box = prize
<div class="result-subgroup subgroup-awardcategory-chron">
    

    #상 제목
    <div class="result-subgroup-header">
        <div class="result-subgroup-title">
        # 상 제목
        </div>
    </div>
    
    
    
    # candidate
    <div class="awards-result-subgroup-items">
        
        # 수상작일때
        <span class="glyphicon glyphicon-star" title="Winner"></span>
    
    
        # 후보1
        <div class="result-details awards-result-actingorsimilar">------------------------------
        
            # 후보1의 정보들***************************************************************
            <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                
                # 후보 이름+++++++++++++++++++++++++++++++++++++
                <div class="awards-result-nominationstatement">
                후보 이름
                </div>
                # 후보 이름+++++++++++++++++++++++++++++++++++++
                
                <div class="awards-result-film">
                후보 정보
                </div>
                
                <div class="awards-result-character">
                후보정보2
                </div>
                
            </div>
            # 후보1의 정보들***************************************************************
            
        </div>--------------------------------------------------------------------------------
        # 후보1
        
        
    
        # 후보2
        <div class="result-details awards-result-actingorsimilar">
        </div>
        
        # 후보3
        <div class="result-details awards-result-actingorsimilar">
        </div>
        
        # 후보4
        <div class="result-details awards-result-actingorsimilar">
        </div>
        
        # 후보5
        <div class="result-details awards-result-actingorsimilar">
        </div>
        
    </div>
<div>

#%%
Animated Feature film

# box = prize
<div class="result-subgroup subgroup-awardcategory-chron">

    # prize name
    <div class="result-subgroup-header">
        <div class="result-subgroup-title">
            <a class="nominations-link">ANIMATED FEATURE FILM</a> # 상 제목
        </div>
    </div>
    
    # 후보들
    <div class="awards-result-subgroup-items"> 
    
        # 후보1
        <div class="result-details awards-result-other">--------------------------------------------
        
        
            # 수상작일때
            <span class="glyphicon glyphicon-star" title="Winner"></span>
        
        
            # 후보1의 정보들*************************************************************************
            <div class="awards-result-nomination awards-result-nomination-other">
            
                
                <div class="awards-result-film">
                    
                    # 후보 이름+++++++++++++++++++++++++++++++
                    <div class="awards-result-film-title">
                        <a class="nominations-link">Onward</a> # 후보 이름
                    </div>
                    # 후보 이름+++++++++++++++++++++++++++++++
                    
                </div>
                
                
                #후보 정보
                <div class="awards-result-nominationstatement">
                    <a class="nominations-link">Dan Scanlon and Kori Rae</a> 
                </div>
                #후보 정보
                
                
            </div>
            # 후보1의 정보들*************************************************************************
            
        </div> # 후보1---------------------------------------------------------------------------------
        
        # 후보2
        <div class="result-details awards-result-other">
            <!--Other-->
            <div class="awards-result-nomination awards-result-nomination-other">
                        <div class="awards-result-film">
                            <div class="awards-result-film-title"><a class="nominations-link" href="/Search/Nominations?filmId=5090&amp;view=2-Film%20Title-Alpha">Over the Moon</a></div>
                            <div class="awards-result-separator">--</div>
                        </div>
                        <div class="awards-result-nominationstatement"><a class="nominations-link" href="/Search/Nominations?nominationId=11407&amp;view=1-Nominee-Alpha">Glen Keane, Gennie Rim and Peilin Chou</a></div>
                                                                                                                                                                                            </div>
        </div>
        
        # 후보3
        <div class="result-details awards-result-other">
            <!--Other-->
            <div class="awards-result-nomination awards-result-nomination-other">
                        <div class="awards-result-film">
                            <div class="awards-result-film-title"><a class="nominations-link" href="/Search/Nominations?filmId=5096&amp;view=2-Film%20Title-Alpha">A Shaun the Sheep Movie: Farmageddon</a></div>
                            <div class="awards-result-separator">--</div>
                        </div>
                        <div class="awards-result-nominationstatement"><a class="nominations-link" href="/Search/Nominations?nominationId=11447&amp;view=1-Nominee-Alpha">Richard Phelan, Will Becher and Paul Kewley</a></div>
                                                                                                                                                                                            </div>
        </div>
        
        # 후보4
        <div class="result-details awards-result-other">
            <!--Other-->
                <span class="glyphicon glyphicon-star" title="Winner"></span>
            <div class="awards-result-nomination awards-result-nomination-other">
                        <div class="awards-result-film">
                            <div class="awards-result-film-title"><a class="nominations-link" href="/Search/Nominations?filmId=5097&amp;view=2-Film%20Title-Alpha">Soul</a></div>
                            <div class="awards-result-separator">--</div>
                        </div>
                        <div class="awards-result-nominationstatement"><a class="nominations-link" href="/Search/Nominations?nominationId=11437&amp;view=1-Nominee-Alpha">Pete Docter and Dana Murray</a></div>
                                                                                                                                                                                            </div>
        </div>
        
        # 후보5
        <div class="result-details awards-result-other">
            <!--Other-->
            <div class="awards-result-nomination awards-result-nomination-other">
                        <div class="awards-result-film">
                            <div class="awards-result-film-title"><a class="nominations-link" href="/Search/Nominations?filmId=5106&amp;view=2-Film%20Title-Alpha">Wolfwalkers</a></div>
                            <div class="awards-result-separator">--</div>
                        </div>
                        <div class="awards-result-nominationstatement"><a class="nominations-link" href="/Search/Nominations?nominationId=11466&amp;view=1-Nominee-Alpha">Tomm Moore, Ross Stewart, Paul Young and Stéphan Roelants</a></div>
                                                                                                                                                                                            </div>
        </div>
    </div>
</div>
