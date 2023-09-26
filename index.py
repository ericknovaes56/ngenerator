import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def gerar_codigo_aleatorio():
    caracteres = string.ascii_letters + string.digits
    codigo_aleatorio = ''.join(random.choice(caracteres) for _ in range(16))
    return codigo_aleatorio

url = 'https://discord.gift/'
mensagem_alvo = 'Código de presente inválido'  # A mensagem alvo sem as tags HTML

quantidade = int(input('Quantidade: '))
print('Executando o navegador !')
# Configurar as opções do navegador Firefox
firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True  # Execute o navegador em segundo plano (opcional)

# Configurar o navegador Firefox
driver = webdriver.Firefox(options=firefox_options)

# Lista para armazenar códigos válidos
codigos_validos = []

for i in range(quantidade):
    codigo = gerar_codigo_aleatorio()
    url_completa = url + codigo
    
    driver.get(url_completa)
    
    try:
        # Esperar até que a mensagem alvo seja carregada dinamicamente (aqui, esperamos até 10 segundos)
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), mensagem_alvo))
        print(f'A mensagem "{mensagem_alvo}" foi encontrada em {url_completa}')
    except:
        print(f'A mensagem "{mensagem_alvo}" não foi encontrada em {url_completa}')
        codigos_validos.append(codigo)  # Adicionar códigos válidos à lista

# Fechar o navegador após o uso
driver.quit()

# Salvar códigos válidos no arquivo code.txt
with open('code.txt', 'w') as arquivo_saida:
    arquivo_saida.write('\n'.join(codigos_validos))

print(f'Códigos válidos foram salvos em code.txt.')
