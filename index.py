from tkinter import *
from tkinter import messagebox
import pandas as pd

# Função para validar o login
def login():
    usuario = username_entry.get()
    senha = password_entry.get()

    if usuario == "usuario" and senha == "12345":
        main_screen.deiconify()
        login_screen.destroy()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos")

# Configurações de estilo para os widgets
style = {"bg": "#222831", "fg": "#eeeeee", "font": ("Arial", 10)}
style_button = {"bg": "#00adb5", "fg": "#eeeeee", "font": ("Arial", 10)}


# Função para salvar as informações da ferramenta
def save_info():
    cod_Ferramenta = cod_Ferramenta.get()
    desc_solicitacao = desc_solicitacao.get()
    dt_retirada = dt_retirada.get()
    hr_retirada = hr_retirada.get()
    dt_devolucao = dt_devolucao.get()
    hr_devolucao = hr_devolucao.get()
    tecnico_resp = tecnico_resp.get()

    messagebox.showinfo("Informações salvas", f"Ferramenta: {cod_Ferramenta}\nDescrição: {desc_solicitacao}\nData de retirada: {dt_retirada} às {hr_retirada}\nData de devolução prevista: {dt_devolucao} às {hr_devolucao}\nTecnico: {tecnico_resp}")

# Tela de login
login_screen = Tk()
login_screen.title("Login")
login_screen.geometry("500x250")
login_screen.resizable(False, False)

# Adiciona uma imagem de fundo
photo = PhotoImage(file="estacio.png")
background_label = Label(login_screen, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# entrar tela principal
Button(login_screen, text="✔Entrar", command=login, **style_button).place(x=400, y=4)

# sair da aplicação
Button(login_screen, text="✘ Sair  ", command=login_screen.quit, **style_button).place(x=400, y=35)

# Cria dois frames para organizar os widgets
frame1 = Frame(login_screen)
frame1.pack(pady=10)

frame2 = Frame(login_screen)
frame2.pack(pady=10)

Label(frame1, text="♙ - Usuário").grid(row=0, column=0, padx=5)
username_entry = Entry(frame1)
username_entry.grid(row=0, column=1, padx=5)

Label(frame1, text="⌨ - Senha").grid(row=1, column=0, padx=5)
password_entry = Entry(frame1, show="*")
password_entry.grid(row=1, column=1, padx=5)
password_entry.bind("<Return>", login)


#Define o rodapé da janela
status = Label(text="© 2023 - DevTeam 03 - ✉ faleconosco@devteam03.com.br - ☏ 1234 56789", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# Tela principal
main_screen = Tk()
main_screen.title("Reserva de Ferramentas")
main_screen.geometry("740x260")
main_screen.withdraw()

Label(main_screen, text="➤ Cód. da Ferramenta").grid(row=0, column=0, sticky=W)
Label(main_screen, text="➤ Descrição da Solicitação").grid(row=1, column=0, sticky=W)
Label(main_screen, text="➤ Data de Retirada (D/M/A)").grid(row=2, column=0, sticky=W)
Label(main_screen, text="➤ Hora de Retirada (H:M)").grid(row=3, column=0, sticky=W)
Label(main_screen, text="➤ Data de Devolução Prevista (D/M/A)").grid(row=4, column=0, sticky=W)
Label(main_screen, text="➤ Hora de Devolução Prevista (H:M)").grid(row=5, column=0, sticky=W)
Label(main_screen, text="➤ Técnico responsével(Retirada)").grid(row=6, column=0, sticky=W)

cod_Ferramenta = Entry(main_screen)
desc_solicitacao = Entry(main_screen)
dt_retirada = Entry(main_screen)
hr_retirada = Entry(main_screen)
dt_devolucao = Entry(main_screen)
hr_devolucao = Entry(main_screen)
tecnico_resp = Entry(main_screen)

cod_Ferramenta.grid(row=0, column=1)
desc_solicitacao .grid(row=1, column=1)
dt_retirada.grid(row=2, column=1)
hr_retirada.grid(row=3, column=1)
dt_devolucao.grid(row=4, column=1)
hr_devolucao.grid(row=5, column=1)
tecnico_resp.grid(row=6, column=1)

Button(main_screen, text="✔ Salvar", command=save_info, **style_button).place(x=275, y=170)
Button(main_screen, text="✘ Sair ", command=login_screen.quit, **style_button).place(x=347, y=170)

#botão para cadastro/pesquisar de ferramentas
Button(main_screen, text="✔ Cadastrar", command=save_info, **style_button).place(x=430, y=0)
Button(main_screen, text="⌛ Pesquisar", command=save_info, **style_button).place(x=530, y=0)
Button(main_screen, text="⌚ Reservar", command=save_info, **style_button).place(x=630, y=0)

#botão para cadastro de tecnicos
Button(main_screen, text="✔ Cadastrar", command=save_info, **style_button).place(x=430, y=133)



mainloop()
