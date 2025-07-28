import pyautogui
import pyperclip
import time

respostas = {
    "oi": "Olá! Como posso te ajudar? 😊",
    "agenda": "Nossa agenda está aberta de segunda a sexta, das 9h às 18h.",
    "preço": "Os preços variam conforme o serviço. Me diga o que você precisa!",
    "obrigado": "De nada! Qualquer coisa, estou por aqui. 🤗"
}

mensagem_boas_vindas = "Olá! Eu sou um assistente automático. Como posso te ajudar? 🤖"

def responder(mensagem):
    mensagem = mensagem.lower()
    for chave in respostas:
        if chave in mensagem:
            return respostas[chave]
    return "Desculpe, não entendi. Pode reformular a pergunta?"

def ler_mensagem():
    try:
        pyautogui.moveTo(400, 700, duration=0.5)  # Ajuste conforme sua tela
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        mensagem = pyperclip.paste()
        return mensagem.strip()
    except Exception as e:
        print(f"[ERRO AO LER MENSAGEM] {e}")
        return ""

def enviar_resposta(texto):
    try:
        pyautogui.typewrite(texto)
        pyautogui.press("enter")
    except Exception as e:
        print(f"[ERRO AO ENVIAR RESPOSTA] {e}")

print("BOT INICIADO. Posicione no WhatsApp Web na conversa desejada.")
time.sleep(10)  # Tempo para você abrir a conversa

# Envia mensagem de boas-vindas ao iniciar
print("Enviando mensagem inicial...")
enviar_resposta(mensagem_boas_vindas)

ultima_mensagem = ""

try:
    while True:
        mensagem = ler_mensagem()
        if mensagem != "" and mensagem != ultima_mensagem:
            print("Mensagem recebida:", mensagem)
            resposta = responder(mensagem)
            enviar_resposta(resposta)
            ultima_mensagem = mensagem
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[BOT ENCERRADO PELO USUÁRIO]")
### oi kebda