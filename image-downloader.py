import tkinter as tk
import requests

#instanciamento do tkinter:
ws = tk.Tk()
ws.title("Image Downloader")

#definindo as configurações do workspace:
canvas = tk.Canvas(ws, width=600, height=300, bg="#AFEEEE")
canvas.grid(columnspan=6, rowspan=7)

#instruções para o usuário:
instructions = tk.Label(ws, text="Digite a URL da qual você deseja baixar a sua imagem.  Importante que seja uma URL que termine em JPG ou PNG:")
instructions.grid(columnspan=6, column=0, row=0)
instructions2 = tk.Label(ws, text="diga o nome o qual você deseja salvar o arquivo:")
instructions2.grid(columnspan=6, column=0, row=3)

#variáveis:
urlvar = tk.StringVar()
filevar = tk.StringVar()

#Input do usuário:
urlentry=tk.Entry(ws, textvariable=urlvar)
urlentry.grid(columnspan=6, column=0, row=1)
fileEntry=tk.Entry(ws, textvariable=filevar)
fileEntry.grid(columnspan=6, column=0, row=4)

#função de download:
def image_downloader():
    url_link=urlvar.get()
    file = filevar.get()
    file = file + '.jpg'
    url_link = requests.get(url_link)
    with open(file,'wb') as f:
        f.write(url_link.content)

#Butão utilizado pelo usuário:
submitBtn=tk.Button(ws, text="Entrar", command=image_downloader)
submitBtn.grid(columnspan=6, column=0, row=5)

#pop-up de ação bem sucedida:

ws.mainloop()