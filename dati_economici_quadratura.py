import time
import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

#chrome_options = Options()
#chrome_options.add_argument("--headless")
tempo_iniziale = datetime.datetime.now()
driver = webdriver.Chrome('/usr/bin/chromedriver')
#driver = webdriver.PhantomJS()
#driver.set_window_size(1120, 550)
driver.get('https://nsis.sanita.it');
actionChains = ActionChains(driver)
wait = WebDriverWait(driver, 10)
content = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID,'content')))
credentials = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'credentials')))
utente = wait.until(EC.visibility_of_element_located((By.NAME, 'Ecom_User_ID')))
utente.send_keys('mi141180')
password = wait.until(EC.visibility_of_element_located((By.NAME, 'Ecom_Password')))
password.send_keys('Palmito.34')
tasto_login = wait.until(EC.visibility_of_element_located((By.NAME, 'loginButton2')))
tasto_login.click()
frame_menu = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'menu')))
link_economici = wait.until(EC.visibility_of_element_located((By.XPATH, \
                        '/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/ul/li[6]/a')))
link_economici.click()
time.sleep(5)
tab_economici = driver.window_handles[1]
driver.switch_to.window(tab_economici)
tasto_bo = wait.until(EC.visibility_of_element_located((By.XPATH, \
                        '/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[6]/td/table/tbody/tr/td/img')))
print('numero di finestre prima di cliccare il tasto BO', len(driver.window_handles))
tasto_bo.click()
print('numero di finestre subito dopo aver cliccato il tasto BO', len(driver.window_handles))
time.sleep(10)
print('numero di finestre dopo 10 secondi', len(driver.window_handles))
#time.sleep(10)
#print('numero di finestre dopo 20 secondi', len(driver.window_handles))
tab_bo = driver.window_handles[2]
driver.switch_to.window(tab_bo)
print('switch al tab Business Objects')
nomi_tabelle = ['tabella\xa0CE', 'tabella\xa0LA', 'tabella\xa0CP', 'tabella\xa0SP']
#navigazione nei frame fino a quello centrale di interesse
###headerPlusFrame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'headerPlusFrame')))
###print('switch al frame headerPlusFrame')
servletBridgeIframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'servletBridgeIframe')))
print('switch al frame servletBridgeIframe')
print(servletBridgeIframe)
###dataFrame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'dataFrame')))
###print('switch al frame dataFrame')
iframe4577 = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID,'iframe4577-9827')))
print('switch al frame iframe4577-9827')
ygtvlabelel4 = wait.until(EC.visibility_of_element_located((By.ID,'ygtvlabelel4')))
print('switch al link ygtvlabelel4')
print(ygtvlabelel4)
ygtvlabelel4.click()
time.sleep(3)

ricerca_tabella = "//*[contains(text(), 'tabella\xa0CE')]"
tabella = wait.until(EC.visibility_of_element_located((By.ID, 'ListingURE_detailView_listNode11_0')))
tabella.click()
time.sleep(2)
print(' cliccato')

###workspaceFrame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'workspaceFrame')))
###print('switch al frame workspaceFrame')
cartella_flussi_economici = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Flussi Economici')]")))
print(cartella_flussi_economici)
ListingURE_accordionView = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'ListingURE_accordionView')))
print('switch al frame ListingURE_accordionView')
workspaceBodyFrame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'workspaceBodyFrame')))
print('switch al frame workspaceBodyFrame')
#link_preferiti = driver.find_element_by_xpath('//*[@id="ListingURE_treeNode2_name"]')
link_preferiti = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ListingURE_treeNode2_name"]')))
link_preferiti.click()
#actionChains.double_click(link_preferiti).perform()
#time.sleep(5)
#wait = WebDriverWait(driver, 10)
#preferiti_compresso = driver.find_element_by_xpath('//*[@id="ygtvt2"]/div/a')
try:
    preferiti_compresso = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ygtvt2"]/div/a')))
    preferiti_compresso.click()
    print('cliccato preferiti compresso')
except TimeoutException:
    print('Timeout cercando preferiti compresso')
#link_flussi_economici = driver.find_element_by_xpath("//*[contains(text(), 'Flussi Economici')]")
try:
    link_flussi_economici = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Flussi Economici')]")))
    link_flussi_economici.click()
    print('cliccato link flussi economici')
except TimeoutException:
    print('Timeout cercando link flussi economici')
#actionChains.double_click(link_flussi_economici).perform()
#time.sleep(7)
#wait = WebDriverWait(driver, 20)
#ricerca pagina 2 flussi economici
try:
    box_pagina = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ListingURE_pageNumberInput"]')))
    box_pagina.click()
    box_pagina.clear()
    print('box pagina pulito')
    box_pagina.send_keys('2' + Keys.ENTER)
    print('inserita pagina 2 nel box')
except TimeoutException:
    print('Timeout cercando box pagina')
#time.sleep(10)
print('Inizio ciclo scaricamento tabelle')
for nome_tabella in nomi_tabelle:
    ricerca_tabella = "//*[contains(text(), '" + nome_tabella + "')]"
    try:
        tabella = wait.until(EC.visibility_of_element_located((By.XPATH, ricerca_tabella)))
        tabella.click()
        time.sleep(2)
        print(nome_tabella + ' cliccato')
    except TimeoutException:
        print('timeout ' + ricerca_tabella + ' \nprobabilmente non ha cambiato la pagina')
    #menu_azioni = driver.find_element_by_xpath('//*[@id="IconImg_iconMenu_arrow_ListingURE_usage0_10"]')
    menu_azioni = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="IconImg_iconMenu_arrow_ListingURE_usage0_10"]')))
    menu_azioni.click()
    print('menu Azioni cliccato')
    time.sleep(2)
    #voce_visualizza = driver.find_element_by_xpath('//*[@id="iconMenu_menu_ListingURE_usage0_10_text_Webi_View"]')
    voce_visualizza = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="iconMenu_menu_ListingURE_usage0_10_text_Webi_View"]')))
    voce_visualizza.click()
    print('visualizza cliccato')
    time.sleep(1)
    wait = WebDriverWait(driver, 20)
    #il webiViewFrame viene trovato dopo che il waitDlg è scomparso
    #quindi non serve aspettare la comparsa e scomparsa del waitDlg
    webiViewFrame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'webiViewFrame')))
    print('switch al frame webiViewFrame')
    time.sleep(1)
    #menu_documento = driver.find_element_by_xpath('//*[@id="IconImg_Txt_iconMenu_icon_docMenu"]')
    #freccia_avanti = wait.until(EC.visibility_of_element_located((By.XPATH, '// *[ @ id = "IconImg_nextIcn"]')))
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="titledialog_waitDlg"]')))
    menu_documento = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="IconImg_Txt_iconMenu_icon_docMenu"]')))
    menu_documento.click()
    print('menu Documento cliccato')
    time.sleep(2)
    #salva_come = driver.find_element_by_xpath('//*[@id="iconMenu_menu_docMenu_span_text_saveDocComputerAs"]')
    salva_come = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="iconMenu_menu_docMenu_span_text_saveDocComputerAs"]')))
    salva_come.click()
    print('voce menu Salva con nome cliccato')
    time.sleep(2)
    #link_salva_XLSX = driver.find_element_by_xpath('//*[@id="saveDocComputerMenu_span_text_saveXLSX"]')
    link_salva_XLSX = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="saveDocComputerMenu_span_text_saveXLSX"]')))
    link_salva_XLSX.send_keys(Keys.ENTER)
    print('salva come XLSX cliccato')
    time.sleep(2)
    #loop di attesa scaricamento file
    print('inizio attesa scaricamento ' + '/home/flavio/Scaricati/' + nome_tabella + '.xlsx')
    while not os.path.exists('/home/flavio/Scaricati/' + nome_tabella.replace('\xa0', ' ') + '.xlsx'):
        time.sleep(2)
    print('fine attesa scaricamento')
    menu_documento.click()
    print('menu Documento cliccato')
    time.sleep(2)
    #chiudi = driver.find_element_by_xpath('//*[@id="iconMenu_menu_docMenu_text_closeDoc"]')
    chiudi = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="iconMenu_menu_docMenu_text_closeDoc"]')))
    chiudi.click()
    print('voce menu Chiudi cliccata')
    time.sleep(2)
    wait.until(EC.alert_is_present())
    print('alert chiusura visualizzato')
    wait.until(EC.alert_is_present()).accept()
    print('azione chiusura accettata')
    time.sleep(2)
    #driver.switch_to.parent_frame()
    driver.switch_to.default_content()
    print('switchato al default_content')
    time.sleep(5)
    # navigazione nei frame fino a quello centrale di interesse
    wait = WebDriverWait(driver, 30)
    headerPlusFrame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'headerPlusFrame')))
    dataFrame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'dataFrame')))
    workspaceFrame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'workspaceFrame')))
    workspaceBodyFrame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'workspaceBodyFrame')))

print('Scaricamento files terminato')
tempo_scaricamento = datetime.datetime.now()
print('Tempo impiegato per scaricare i files: ', tempo_scaricamento - tempo_iniziale)
driver.quit()
print('Fase caricamento tabelle nel database')
# Lancia il job esportato da Talend per l'import azione dei dati economici
os.system("/home/flavio/jobs_talend/importa_dati_economici_xlsx/importa_dati_economici_xlsx_run.sh")
tempo_importazione = datetime.datetime.now()
print('Fase creazione files di quadratura CE-LA')
# Lancia il job esportato da Talend per la quadratura CE-LA
os.system("/home/flavio/jobs_talend/quadratura_CE_LA_2012_xlsx/quadratura_CE_LA_2012_xlsx_run.sh")
tempo_finale = datetime.datetime.now()
print('Tempo impiegato per caricare le tabelle nel database: ', tempo_importazione - tempo_scaricamento)
print('Tempo impiegato per la quadratura CE-LA: ', tempo_finale - tempo_importazione)
print('Tempo complessivo job:', tempo_finale - tempo_iniziale)
