"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *


from webdriver_manager.chrome import ChromeDriverManager

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


# Function to search words 

def pesquisar_clima(bot, cidade):
    
    while len(bot.find_elements('//*[@id="APjFqb"]', By.XPATH)) <1:
        bot.wait(1000)
        print("Searching")
    bot.find_element('//*[@id="APjFqb"]',By.XPATH).send_keys(cidade)
    bot.wait(1000)
    bot.enter()


def extrair_dados(bot):
    cont = 0
    while cont <8:
        cont += 1
        dia_da_semana = bot.find_element(f'//*[@id="wob_dp"]/div[{cont}]/div[1]', By.XPATH).text
        temperatura_max = bot.find_element(f'//*[@id="wob_dp"]/div[1]/div[3]/div[{1}]/span[1]', By.XPATH).text
        temperatura_min = bot.find_element(f'//*[@id="wob_dp"]/div[1]/div[3]/div[{2}]/span[1]', By.XPATH).text
        print('Dia:', dia_da_semana)
        print('Temperatura:')
        print('Max=', temperatura_max + '|' + 'Min=',temperatura_min)
        print("----------------------------------------------------------------")
        
        

        




def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

    bot.browse("https://www.google.com")
    bot.maximize_window()


    try:
        pesquisar_clima(bot,'manaus clima')
        bot.wait(1000)
        extrair_dados(bot)
    except Exception as e:
        print(f"Error: {e}")
        bot.save_screenshot("erro.png")
        # Handle the exception and mark the task as failed on BotMaestro
        # maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.FAILED,
        #     message=f"Error searching for the city: {e}"
        # )
        raise e
    finally:
        bot.wait(3000)


    # Wait 3 seconds before closing
    #bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    #bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
