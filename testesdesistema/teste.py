from selenium import webdriver

navegador= webdriver.Chrome()
# 1 PASSO: Entrar no endereço
navegador.get("http://127.0.0.1:8000/")
# 2 PASSO: Criar conta
navegador.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[2]').click()
# 3 PASSO: Preencher info de usuario
navegador.find_element_by_name('nome').send_keys('Dávila')
navegador.find_element_by_name('email').send_keys('davila@gmail.com')
navegador.find_element_by_name('senha1').send_keys('1234')
navegador.find_element_by_name('senha2').send_keys('1234')
# 4 PASSO: Cadastrar
navegador.find_element_by_id('cadastrar-usuario').click()
# 5 PASSO: Preencher info de login
navegador.find_element_by_name('email').send_keys('davila@gmail.com')
navegador.find_element_by_name('senha').send_keys('1234')
# 6 PASSO: Logar
navegador.find_element_by_id('logar').click()