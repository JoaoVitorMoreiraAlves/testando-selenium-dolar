# Importando o módulo 'webdriver' do Selenium para automação de navegador
from selenium import webdriver

# Importando o 'ChromeDriverManager' do módulo 'webdriver_manager' para gerenciar o driver do Chrome
from webdriver_manager.chrome import ChromeDriverManager

# Importando a classe 'Service' do módulo 'selenium.webdriver.chrome.service' para configurar o serviço do Chrome
from selenium.webdriver.chrome.service import Service

#Importa a classe "Keys" do "selenium.webdriver.common.keys" para poder manipular teclas do teclado como ENTER,SHIFT, CRTL,etc.
from selenium.webdriver.common.keys import Keys



# Configurando o serviço do Chrome utilizando o 'ChromeDriverManager' para instalar o driver automaticamente
servico = Service(ChromeDriverManager().install())

# Criando uma instância do navegador Chrome e passando o serviço configurado
navegador = webdriver.Chrome(service=servico)

# Abrindo a página do Google no navegador
navegador.get('https://google.com/')

#Define o XPath a ser procurado
barra_pesquisa_xpath = '//*[@id="APjFqb"]'

#Acessando a barra de pesquisa através do XPATH
navegador.find_element("xpath", barra_pesquisa_xpath).click()

#Define o XPath a ser digitado na barra de pesquisa
texto_pesquisa = "Dolar"
navegador.find_element("xpath", barra_pesquisa_xpath).send_keys(texto_pesquisa + Keys.RETURN)#Ele vai digitar o valor do texto_pesquisa e ja dar enter com o Keys.Return


#Define o XPath do Dolar a ser pego
dolar_google = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'

#Pega o Dolar em formato TEXT(caso não use o .text a variável dolar irá armazenar um códugo selenium e não o resultado esperado)
dolar = navegador.find_element("xpath", dolar_google).text

print(f'O valor do Dolar no dia de hoje é de: US ${dolar}')
