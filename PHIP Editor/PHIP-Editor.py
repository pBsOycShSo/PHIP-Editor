import bz2
import io
import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

import PIL.Image
import keyboard as kb
from customtkinter import CTk, CTkCanvas, filedialog, CTkTextbox, CTkOptionMenu, CTkButton, CTkLabel, CTkEntry

try:
    def editor():
        a = os.getcwd()
        kb.add_abbreviation('@help',
                            "--------------------------\nAbout the application\n--------------------------\n! It's pretending it's just like a text editor.\n! But when you are pressing [Ctrl+Shift+P] or [Ctrl+Shift+H]\n! You can see the secret of this application.\n! Guide lines in my github --> https://github.com/KevinMark-MM\n\nThanks for using this app !")

        def phip_edit(phip):
            phip = CTk()
            phip.title("PHIP Injector")
            phip.geometry("500x215")
            phip.iconbitmap('assets\\camera.ico')
            canvas = CTkCanvas(
                phip,
                bg="#2E2E2E",
                height=215,
                width=500,
                bd=0,
                highlightthickness=0,
                relief="ridge",
            )
            canvas.place(x=0, y=0)
            canvas.create_rectangle(
                -1,
                60,
                600,
                60,
                fill="#FFFFFF",
                outline="")
            canvas.create_text(
                10,
                2.5,
                anchor="nw",
                text="INjector",
                fill="#FFFFFF",
                font=("Bauhaus 93", 45 * -1)
            )
            version = CTkLabel(phip, text="v2.1.3", text_color="gray", bg_color="#2E2E2E",
                               font=("Candara Bold Italic", 14))
            version.place(x=175, y=25)

            def img_selection():
                global i, input_photo_path
                input_photo_path = filedialog.askopenfilename(
                    filetypes=(("PNG", "*.png"), ("JPEG", "*.jpeg"), ("JPG", "*.jpg"), ("All files", "*")))
                c = input_photo_path.split("/")
                b = list(c)
                a = len(b)
                img = b[a - 1]
                c = str(img)
                i = c.replace(" ", "")
                entry_img = CTkLabel(phip, text=i, font=("Bold", 13), width=275, corner_radius=20)
                entry_img.place(y=85, x=60)

            def file_selection():
                global ex, input_file_path
                input_file_path = filedialog.askopenfilename(
                    filetypes=(("EXE", "*.exe"), ("MP4", "*.mp4"), ("MP3", "*.mp3"), ("All file", "*")))
                c = input_file_path.split("/")
                b = list(c)
                a = len(b)
                file = b[a - 1]
                c = str(file)
                ex = c.replace(" ", "")
                entry_fil = CTkLabel(phip, text=ex, font=("Bold", 13), width=275, corner_radius=20)
                entry_fil.place(x=60, y=120)

            def hide_exe_in_photo():
                os.chdir(a + "\\Files")
                shutil.copyfile(input_photo_path, i)
                shutil.copyfile(input_file_path, ex)
                with open(ex, 'rb') as f_in, bz2.open("FILE.phip", 'wb') as f_out:
                    f_out.write(f_in.read())
                with open(i, 'ab') as f, open("FILE.phip", 'rb') as e:
                    f.write(e.read())
                os.system(f"DEL {ex}")
                os.system('DEL FILE.phip')
                messagebox.showinfo("Phip-v2", "  Done!     ")
                exit()

            def unhide_exe():
                os.chdir(a + "\\Files")
                for x in os.listdir(a + "\\Files"):
                    if i == x:
                        pass
                    else:
                        shutil.copyfile(input_photo_path, i)
                with open(i, 'rb') as f:
                    content = f.read()
                    offset = content.index(bytes.fromhex('FFD9'))
                    f.seek(offset + 2)
                    with open('FILE.phip', 'wb') as e:
                        e.write(f.read())
                    with bz2.open('FILE.phip', 'rb') as f_in, open(fils, 'wb') as f_out:
                        f_out.write(f_in.read())
                os.system('DEL FILE.phip')
                os.system(f'DEL {i}')
                messagebox.showinfo("Phip-v2", "  Done!     ")
                exit()

            def hide_photo_in_photo():
                os.chdir(a + "\\Files")
                shutil.copyfile(input_photo_path, i)
                shutil.copyfile(input_file_path, ex)
                img = PIL.Image.open(ex)
                byte_arr = io.BytesIO()
                img.save(byte_arr, format='PNG')
                with open(i, 'ab') as f:
                    f.write(byte_arr.getvalue())
                os.system(f"DEL {ex}")
                messagebox.showinfo("Phip-v2", "  Done!     ")
                exit()

            def unhide_photo():
                os.chdir(a + '\\Files')
                for x in os.listdir(a + "\\Files"):
                    if i == x:
                        pass
                    else:
                        shutil.copyfile(input_photo_path, i)
                with open(i, 'rb') as f:
                    content = f.read()
                    offset = content.index(bytes.fromhex('FFD9'))
                    f.seek(offset + 2)
                    new_img = PIL.Image.open(io.BytesIO(f.read()))
                    new_img.save(fils)
                messagebox.showinfo("Phip-v2", "  Done!     ")
                exit()

            def c_photo():
                os.chdir(a + "\\Files")
                with open(i, 'rb') as f:
                    content = f.read()
                    offset = content.index(bytes.fromhex('FFD9'))
                    f.seek(offset + 2)
                    new_img = PIL.Image.open(io.BytesIO(f.read()))
                    new_img.save(i)
                messagebox.showinfo("Phip-v2", "  Done!     ")
                exit()

            def file():
                global fils
                fils = file_name.get()
                if val == "Out photo":
                    unhide_photo()
                else:
                    unhide_exe()

            def file_names():
                global file_name
                nw = CTk()
                nw.title("PHIP Injector")
                nw.geometry("300x100")
                nw.iconbitmap('assets\\camera.ico')
                CTkCanvas(nw, bg="#2E2E2E", height=100, width=300, bd=0, highlightthickness=0, relief="ridge")
                bt = CTkButton(nw, text="OK", width=80, bg_color="#2E2E2E", font=("Candara Bold Italic", 17),
                               command=file)
                bt.place(y=55, x=50)
                btn = CTkButton(nw, text="Cancel", width=80, bg_color="#2E2E2E", font=("Candara Bold Italic", 17),
                                command=nw.destroy)
                btn.place(y=55, x=170)
                file_name = CTkEntry(nw, placeholder_text="Enter the name with extension", width=200,
                                     font=("Candara Bold Italic", 14))
                file_name.place(x=50, y=15)
                nw.resizable(False, False)
                nw.mainloop()

            def GET_value(COMbox):
                global val
                val = COMbox.get()
                if val == "Put photo":
                    hide_photo_in_photo()
                elif val == "Put file":
                    hide_exe_in_photo()
                elif val == "Out photo":
                    file_names()
                elif val == "Out file":
                    file_names()
                elif val == "Change photo":
                    c_photo()
                elif val == "Setup":
                    os.mkdir("Files")
                    messagebox.showinfo("Phip-v2", "  Done!     ")
                    GET_value(COMbox)
                else:
                    exit()

            COMbox = CTkOptionMenu(phip, width=100, bg_color="#2E2E2E", font=("Candara Bold Italic", 14),
                                   values=["Setup", "Put photo", "Put file", "Out photo", "Out file", "Change photo"])
            COMbox.place(y=158, x=350)
            entry_img = CTkLabel(phip, font=("Bold", 13), width=275, text="choose the main image", text_color="gray")
            entry_img.place(y=85, x=60)
            CH_img = CTkButton(phip, text='Choose Image', bg_color="#2E2E2E", width=13,
                               font=("Candara Bold Italic", 15), command=img_selection)
            CH_img.place(x=350, y=85)
            CH_file = CTkButton(phip, text='Choose  File', bg_color="#2E2E2E", width=100,
                                font=("Candara Bold Italic", 15), command=file_selection)
            CH_file.place(x=350, y=120)
            entry_fil = CTkLabel(phip, font=("Bold", 13), width=275, text="choose the file to inject",
                                 text_color="gray")
            entry_fil.place(x=60, y=120)
            St = CTkButton(phip, text='Inject', bg_color="#2E2E2E", fg_color="#2E2E2E", border_color="#145CA6",
                           border_width=2, width=275, font=("Candara Bold Italic", 20),
                           command=lambda: GET_value(COMbox))
            St.place(x=60, y=158)
            phip.resizable(False, False)
            phip.mainloop()

        def open_file(filepath):
            filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if not filepath:
                return
            txt_edit.delete(1.0, tk.END)
            with open(filepath, "r") as input_file:
                txt = input_file.read()
                txt_edit.insert(tk.END, txt)
            root.title(f"phip Text editor - {filepath}")

        def save_file(filepath):
            filepath = asksaveasfilename(defaultextension="txt",
                                         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if not filepath:
                return
            with open(filepath, "w") as output_file:
                text = txt_edit.get(1.0, tk.END)
                output_file.write(text)
                root.title(f"phip Text editor - {filepath}")

        def Hide_Lock(HL):
            HL = CTk()
            HL.title("PHIP HLocker")
            HL.geometry("500x215")
            HL.iconbitmap('assets\\camera.ico')
            canvas = CTkCanvas(
                HL,
                bg="#2E2E2E",
                height=215,
                width=500,
                bd=0,
                highlightthickness=0,
                relief="ridge",
            )
            canvas.place(x=0, y=0)
            canvas.create_rectangle(
                -1,
                60,
                600,
                60,
                fill="#FFFFFF",
                outline="")
            canvas.create_text(
                10,
                2.5,
                anchor="nw",
                text="HLocker",
                fill="#FFFFFF",
                font=("Bauhaus 93", 45 * -1)
            )
            version = CTkLabel(HL, text="v2.3", text_color="gray", bg_color="#2E2E2E", font=("Candara Bold Italic", 14))
            version.place(x=170, y=25)

            def file_sele():
                global inputfile
                inputfile = filedialog.askdirectory()
                h = inputfile.split("/")
                b = list(h)
                l = len(b)
                s = (b[l - 1])
                entry_fil = CTkLabel(HL, text=s, font=("Bold", 13), width=275, corner_radius=20)
                entry_fil.place(x=60, y=85)

            def GET_val(COMbo):
                global vale
                vale = COMbo.get()
                if vale == "Hide":
                    zip()
                elif vale == "Unhidden":
                    unzip()
                else:
                    exit()

            def zip():
                global s
                fi = file_n.get()
                h = inputfile.split("/")
                b = list(h)
                l = len(b)
                s = (b[l - 1])
                w = inputfile.replace(s, "")
                os.chdir(w)
                shutil.make_archive(fi, format='zip', root_dir=s)
                if os.path.isdir(inputfile):
                    shutil.rmtree(inputfile)
                cu = os.path.abspath(fi + ".zip")
                os.system(f'attrib +h +s "{cu}"')
                messagebox.showinfo("Phip-v2", "  Done!     ")
                exit()

            def unzip():
                fi = file_n.get()
                os.chdir(inputfile)
                cu = os.path.abspath(fi + ".zip")
                os.system(f'attrib -h -s "{cu}"')
                shutil.unpack_archive(f"{fi}.zip", "Files")
                os.system(f'DEL "{cu}"')
                messagebox.showinfo("Phip-v2", "  Done!     ")
                exit()

            COMbo = CTkOptionMenu(HL, width=105, bg_color="#2E2E2E", font=("Candara Bold Italic", 14),
                                  values=["Hide", "Unhidden"])
            COMbo.place(y=120, x=350)

            entry_img = CTkLabel(HL, font=("Bold", 13), width=275, text="choose the folder", text_color="gray")
            entry_img.place(y=85, x=60)

            file_n = CTkEntry(HL, placeholder_text="Enter the password", width=275,
                              font=("Candara Bold Italic", 14))
            file_n.place(x=60, y=120)
            btnn = CTkButton(HL, text='HLock', bg_color="#2E2E2E", fg_color="#2E2E2E", border_color="#145CA6",
                             border_width=2, width=275, font=("Candara Bold Italic", 20),
                             command=lambda: GET_val(COMbo))
            btnn.place(x=60, y=158)
            CH_i = CTkButton(HL, text='Choose  Folder', bg_color="#2E2E2E", width=13,
                             font=("Candara Bold Italic", 15), command=file_sele)
            CH_i.place(x=350, y=85)

            HL.resizable(False, False)
            HL.mainloop()

        root = CTk()
        root.title("PHIP Text - New file")
        root.geometry("700x450")
        root.iconbitmap('assets\\camera.ico')
        root.rowconfigure(0, minsize=1, weight=1)
        root.columnconfigure(1, minsize=1, weight=1)
        txt_edit = CTkTextbox(root, width=10000, height=10000, font=('Lithos Pro', 17))
        txt_edit.grid(sticky="ns")

        root.bind("<Control-o>", open_file)
        root.bind("<Control-s>", save_file)
        root.bind("<Control-P>", phip_edit)
        root.bind("<Control-H>", Hide_Lock)

        root.resizable(True, True)
        root.mainloop()


    editor()
except SystemError as e:
    print(e)
