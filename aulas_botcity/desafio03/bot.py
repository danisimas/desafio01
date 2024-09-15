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
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

import json
from PIL import image 


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


# def read json 
def read_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data['load']['products']



# find and click 
def find_and_click(bot, needle, label):
    if not bot.find(needle=needle):
        print(f"Elemento não encontrado: {label}")
        return False
    bot.click()
    return True


def fill_product_form(bot, product):
    if find_and_click(bot, 'path_to_item_number_image.png', "Número do Item"):
        bot.paste(product['item_number'])

    if find_and_click(bot, 'path_to_name_image.png', "Nome"):
        bot.paste(product['name'])

    # Repita o processo para outros campos do formulário
    # Exemplo: Descrição
    if find_and_click(bot, 'path_to_description_image.png', "Descrição"):
        bot.paste(product['description'])

    # Assumindo que exista um botão para salvar
    if find_and_click(bot, 'path_to_save_button.png', "Botão Salvar"):
        print("Produto salvo com sucesso!")




def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    products = read_json_file('caminho_para_seu_arquivo.json')
    bot.start()
    for product in products:
        fill_product_form(bot, product)
    bot.stop()


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