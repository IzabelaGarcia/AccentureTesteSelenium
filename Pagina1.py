from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Sampleapp:
    def __init__(self,url,driver_path):
        self.url = url
        self.driver_path = driver_path

    def openbrowser (self):
       self.browsercontrol = webdriver.Chrome(self.driver_path)
       self.browsercontrol.get(self.url)
    
    def fill (self,writeUuid,filldata):
        write = self.browsercontrol.find_element_by_id(writeUuid)
        write.click()
        write.send_keys(filldata)
        write.send_keys(Keys.RETURN)
    
    def selection (self,options):
        tochoose = self.browsercontrol.find_element_by_xpath(options)
        tochoose.click()

    def proceed (self,nextpage):
        clickbutton = self.browsercontrol.find_element_by_id(nextpage)
        clickbutton.click()
    def wait (self):
        self.browsercontrol.implicitly_wait(25)

#Funcionalidade: Preencher formulario
#Como usuario do sistema
#Eu quero preencher o formulario com os dados do veiculo
#A fim de calcular o seguro dele'''
#Cenario: Preenchimento do formulario para pedido de seguro
#Dado acesso a pagina inicial da Tricentis para o seguro do veiculo
sampleapp = Sampleapp("http://sampleapp.tricentis.com/101/app.php","chromedriver.exe")
sampleapp.openbrowser()
#Quando clico na opção Automobile
#E preencho os dados do formulario dos dados do veiculo
sampleapp.fill("make","Audi")
sampleapp.fill("model","Scooter")
sampleapp.fill("cylindercapacity","1000")
sampleapp.fill("engineperformance","1000")
sampleapp.fill("dateofmanufacture","01/02/2020")
sampleapp.fill("numberofseats","5")
sampleapp.selection("//*[@id='insurance-form']/div/section[1]/div[7]/p/label[1]/span")
sampleapp.fill("numberofseatsmotorcycle","2")
sampleapp.fill("fuel","Electric Power")
sampleapp.fill("payload","1000")
sampleapp.fill("totalweight","1000")
sampleapp.fill("listprice","1000")
sampleapp.fill("licenseplatenumber","1000")
sampleapp.fill("annualmileage","1000")
#E clico para ir para a etapa de dados do segurado
#E preencho os dados do formulario dos dados do segurado
sampleapp.proceed("nextenterinsurantdata")
sampleapp.fill("firstname","Izabela")
sampleapp.fill("lastname","Garcia")
sampleapp.fill("birthdate","01/26/1997")
sampleapp.selection("//*[@id='insurance-form']/div/section[2]/div[4]/p/label[1]/span")
sampleapp.fill("streetaddress","Rua Não existe")
sampleapp.fill("country","Brazil")
sampleapp.fill("zipcode","123456")
sampleapp.fill("city","Inexistente")
sampleapp.fill("occupation","Employee")
sampleapp.selection("//*[@id='insurance-form']/div/section[2]/div[10]/p/label[5]/span")
sampleapp.selection("//*[@id='insurance-form']/div/section[2]/div[10]/p/label[1]/span")
sampleapp.fill("website","www.teste.com")
#E clico para ir para a etapa de dados do produto
#E preencho os dados do formulario dos dados do produto
sampleapp.proceed("nextenterproductdata")
sampleapp.fill("startdate","01/02/2025")
sampleapp.fill("insurancesum","3.000.000,00")
sampleapp.fill("meritrating","Bonus 1")
sampleapp.fill("damageinsurance","No Coverage")
sampleapp.selection("//*[@id='insurance-form']/div/section[3]/div[5]/p/label[1]/span")
sampleapp.fill("courtesycar","No")
#E clico para ir para a etapa de seleção do preço
#E escolho a opção de seguro
sampleapp.proceed("nextselectpriceoption")
sampleapp.wait()
sampleapp.selection("//*[@id='priceTable']/tfoot/tr/th[2]/label[1]/span")
#E clico para ir para a etapa de envio da proposta por e-mail
#E preencho os dados para envio do e-mail com a proposta
#E clico para enviar a proposta
#Então verificar se a mensagem foi a correta
sampleapp.proceed("nextsendquote")
sampleapp.fill("email","teste@teste.com")
sampleapp.fill("phone","123456789")
sampleapp.fill("username","Teste")
sampleapp.fill("password","Teste.123")
sampleapp.fill("confirmpassword","Teste.123")
sampleapp.fill("Comments","Teste")
sampleapp.proceed("sendemail")

