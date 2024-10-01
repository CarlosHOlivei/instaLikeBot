import pyautogui
import webbrowser
from time import sleep



login_instagram = pyautogui.prompt(text='Digite seu login', title='informações obrigatórias')
senha_instagram = pyautogui.password(text='Digite seu senha', title='informações obrigatórias', mask='*')

def logout():
    pyautogui.click(1057,114, duration=1.2)
    sleep(1)
    pyautogui.click(40,605, duration=1.3)
    sleep(3)
    pyautogui.click(849,143, duration=1.4)
    sleep(1)
    pyautogui.click(542,683, duration=1.4)


while True:
    webbrowser.open_new('https://www.instagram.com/')
    sleep(4)
    campo_login = pyautogui.locateCenterOnScreen('campoLogin.png')
    campo_senha = pyautogui.locateCenterOnScreen('campoSenha.png')
    botao_entrar = pyautogui.locateCenterOnScreen('botaoEntrar.png')
    sleep(1)
    pyautogui.click(campo_login[0],campo_login[1],duration=1)
    #digitar login
    pyautogui.typewrite(login_instagram)
    sleep(1.3)
    #achar campo senha
    pyautogui.click(campo_senha[0], campo_senha[1],duration=1.2)
    #digitar senha
    pyautogui.typewrite(senha_instagram)
    sleep(0.5)
    #clicar em entrar
    pyautogui.click(botao_entrar[0],botao_entrar[1], duration=1.5)
    sleep(10)
    #clicar agora não 1x
    agora_nao = pyautogui.locateCenterOnScreen('botaoAgoraNao.png')
    pyautogui.click(agora_nao[0],agora_nao[1]+45,duration=1)
    sleep(5)
    #clicar agora não 2x
    #clicar na lupa
    lupa = pyautogui.locateCenterOnScreen('lupa.png')
    pyautogui.click(lupa[0], lupa[1], duration=0.9)
    sleep(3)
    #clicar na barra de pesquisa
    barra_pesquisar=pyautogui.locateCenterOnScreen('barraPesquisar.png')
    pyautogui.click(barra_pesquisar[0],barra_pesquisar[1],duration=1)
    sleep(2)
    #digitar nike
    pyautogui.typewrite('nike')
    sleep(2)
    #clicar no primeiro perfil
    perfil_alvo = pyautogui.locateCenterOnScreen('nike.png')
    pyautogui.click(perfil_alvo[0],perfil_alvo[1],duration=1.4)
    sleep(4)
    #clicar na primeira postagem
    post=pyautogui.locateCenterOnScreen('publicacoes.png')
    pyautogui.click(post[0]-60,post[1]+50,duration=1.3)
    sleep(5)
    #verificar se já curtimos
    
    try:
        coracao = pyautogui.locateCenterOnScreen('coracao.png')
        sleep(2)
        if coracao is not None:
    #se sim, pausar bot por 24h
            logout()
            sleep(43000)
    except:
        #se não, clicar em curtir
        curtir=pyautogui.locateCenterOnScreen('coracaovazio.png')
        comentario=pyautogui.locateCenterOnScreen('comentario.png')
        pyautogui.click(curtir[0],curtir[1],duration=1)
        sleep(3)
        pyautogui.click(comentario[0],comentario[1], duration=2)
        sleep(1.2)
        pyautogui.typewrite('Muito Legal! Gostei demais')
        publicar=pyautogui.locateCenterOnScreen('publicar.png')
        pyautogui.click(publicar[0],publicar[1], duration=1.3)
        sleep(3)
        logout()
        sleep(86000)

    #clicar em adicione um comentario

    #clicar em publicar
    #pausar bot 24h, rodar tudo de novo
