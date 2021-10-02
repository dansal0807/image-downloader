import tkinter as tk
import requests
from tkinter import filedialog

#instanciamento do tkinter:
ws = tk.Tk()
ws.title("Image Downloader")

#definindo as configurações do workspace:
canvas = tk.Canvas(ws, width=800, height=400, bg="#AFEEEE")
canvas.grid(columnspan=6, rowspan=7)

#instruções para o usuário:
instructions = tk.Label(ws, bg="#AFEEEE", text="Digite a URL da qual você deseja baixar a sua imagem.  \nImportante que seja uma URL que termine em JPG ou PNG:", font=('Helvatical bold',11))
instructions.grid(columnspan=6, column=0, row=2)

#variáveis:
urlvar = tk.StringVar()

#Input do usuário:
urlentry=tk.Entry(ws, textvariable=urlvar, width=50, font=("default", 11))
urlentry.grid(columnspan=6, column=0, row=3)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Sucesso")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack(pady=5)
    popup.mainloop()

#função de download:
def image_downloader():
    url_link=urlvar.get()
    file_request = filedialog.asksaveasfilename(defaultextension='.jpg')
    url_link = requests.get(url_link)
    f = open(file_request, 'wb')
    f.write(url_link.content)
    f.close()
    popupmsg("Seu download foi bem sucedido!")
#Não há necessidade de usar a função save, pois se pretende não fazer uma lista de arquivos.


#Butão utilizado pelo usuário:
saveAsButton = tk.Button(text='Baixar imagem', command=image_downloader, bg='green', fg='white', font=('Arial', 12, 'bold'))
canvas.create_window(150, 180, window=saveAsButton)
saveAsButton.grid(columnspan=6, column=0, row=4)

ws.mainloop()