# Importações necessárias
from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select
from webdriver_manager.chrome import ChromeDriverManager

# Função para configurar o navegador: maximizar e entrar em tela cheia
def configurar_navegador(bot):
    bot.driver.maximize_window()  # Maximiza a janela do navegador
    bot.wait(1000)  # Espera 1 segundo para garantir que a janela esteja maximizada

    # Enviar comando para o navegador entrar em tela cheia
    bot.driver.execute_script("document.documentElement.requestFullscreen()")
    
    bot.wait(1000)  

def fechar_popup(bot):
    try:
        # Esperar até que o popup esteja visível e acessível
        bot.wait(2000)  # Esperar mais tempo para garantir que o popup tenha aparecido

        # Localizar o botão de fechar do popup usando o XPath fornecido
        bot.find_element('//*[@id="form:mdAvisos"]/div[3]/a', By.XPATH).click()
        print("Popup fechado com sucesso.")
    except Exception as e:
        print("Erro ao fechar o popup.", e)


def entrar_no_iframe(bot):
    try:
        # Acesse o iframe pelo XPath ou outro seletor. Exemplo usando XPath:
        iframe = bot.find_element(selector='/html/frameset/frame', by=By.ID)
        bot.enter_iframe(iframe)
        # Mude o contexto para o iframe
        print("Entrou no iframe com sucesso.")

        bot.find_element(selector='#form1',by=By.ID)
        print("Localizou o formulário no iframe.")
    except Exception as e:
        print("Erro ao entrar no iframe.", e)


def voltar_para_o_contexto_principal(bot):
    # Volta para o contexto principal (fora do iframe)
    bot.driver.switch_to.default_content()
    print("Voltou para o contexto principal.")



def achou_campo(bot):
    print("Tentando localizar o campo CPF.")
    bot.wait(6000) 
    try:
        campo_cpf = bot.find_element(selector='#form1\:j_id6_body > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2) > input',by=By.CSS_SELECTOR)
        if campo_cpf:
            print("Campo CPF encontrado.")
            campo_cpf.click()
            print("clicou")  # Substitua pelo valor correto
        else:
            print("Campo CPF não encontrado.")
    except Exception as e:
        print(f"Erro ao localizar o campo: {e}")





def main():
    bot = WebBot()

    # Configurar para não rodar em headless mode (abrir interface gráfica)
    bot.headless = False

    # Configurar para usar o navegador Chrome
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    # Acessar o portal SEFAZ MA
    bot.browse("https://sistemas1.sefaz.ma.gov.br/portalsefaz/jsp/principal/principal.jsf")

    # Configurar o navegador (maximizar e entrar em tela cheia)
    configurar_navegador(bot)

    # Esperar a página carregar
    bot.wait(5000)

    # Tentar fechar o popup se aparecer
    fechar_popup(bot)

    # Navegar até a seção de download de XML
    bot.find_element('//*[@id="mosaic"]/a[2]/div/h3', By.XPATH).click()

    # Navegar até a seção projetos Nacionais
    bot.find_element('//*[@id="servicos"]/ul/li[10]/a/div/h3', By.XPATH).click()
    
    # Navegar Download da NF-e XML - https://sistemas1.sefaz.ma.gov.br/download-nfe/.
    bot.find_element('//*[@id="form:j_id74"]/div/div/div[2]/p[2]/a',By.XPATH).click()

    # Esperar a nova página carregar
    bot.wait(3000)

    entrar_no_iframe(bot)
    achou_campo(bot)


    #achou_campo(bot)

    #------------------------------------------------------------------------------

   


                                

     
    # Preencher o campo de IE Empresa
    
    # # Preencher o campo de CPF Sócio
    # bot.find_element('//*[@id="form1:j_id6_body"]/table[1]/tbody/tr[2]/td[2]/input"]', By.XPATH).send_keys("12345678900")  # Coloque o XPath correto
    
    # # Preencher o campo de Último Protocolo DIEF
    # bot.find_element('//*[@id="id_protocolo_dief"]', By.XPATH).send_keys("123456789")  # Coloque o XPath correto

    # # Preencher o campo de Data Inicial
    # bot.find_element('//*[@id="id_data_inicial"]', By.XPATH).send_keys("01/01/2023")  # Coloque o XPath correto
    
    # # Preencher o campo de Data Final
    # bot.find_element('//*[@id="id_data_final"]', By.XPATH).send_keys("31/01/2023")  # Coloque o XPath correto

    # # Clicar no botão de "Baixar XML"
    # bot.find_element('//*[@id="btn_download"]', By.XPATH).click()  # Coloque o XPath correto

    # Esperar o download ser concluído
    bot.wait(10000)

    # Limpar o formulário para a próxima operação
    # bot.find_element('//*[@id="btn_limpar"]', By.XPATH).click()  # Coloque o XPath correto

    # # Esperar um pouco após limpar o formulário
    # bot.wait(3000)

    # # Finalizar o navegador
    bot.stop_browser()

if __name__ == '__main__':
    main()