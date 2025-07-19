import pyautogui
import pyperclip
import time

respostas = {
    "oi": "Olá! Como posso te ajudar? 😊",
    "agenda": "Nossa agenda está aberta de segunda a sexta, das 9h às 18h.",
    "preço": "Os preços variam conforme o serviço. Me diga o que você precisa!",
    "obrigado": "De nada! Qualquer coisa, estou por aqui. 🤗"
}

def responder(mensagem):
    mensagem = mensagem.lower()
    for chave in respostas:
        if chave in mensagem:
            return respostas[chave]
    return "Desculpe, não entendi. Pode reformular a pergunta?"

def ler_mensagem():
    pyautogui.moveTo(400, 700)  # Ajuste dependendo da resolução da tela
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    mensagem = pyperclip.paste()
    return mensagem

def enviar_resposta(texto):
    pyautogui.typewrite(texto)
    pyautogui.press("enter")

print("BOT INICIADO. Posicione no WhatsApp Web!")

time.sleep(5)  # Tempo para você abrir o WhatsApp Web

ultima_mensagem = ""

while True:
    try:
        mensagem = ler_mensagem()
        if mensagem != ultima_mensagem:
            print("Mensagem recebida:", mensagem)
            resposta = responder(mensagem)
            enviar_resposta(resposta)
            ultima_mensagem = mensagem
        time.sleep(2)
    except Exception as e:
        print("Erro:", e)
        time.sleep(2)
