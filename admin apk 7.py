import customtkinter as CTk
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
import json
from tkinter import ttk 
import textwrap

def load_user_data():
    try:
        with open('additional_info.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(user_data):
    with open('additional_info.json', 'w') as file:
        json.dump(user_data, file, indent=4)

def display_user_profile(username):
    user_data = load_user_data()
    
    if username in user_data:
        user_info = user_data[username]

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "civara" and password == "123":
        home()
        admin_app.withdraw()
    elif not username:
        messagebox.showerror("Error", "Please enter a valid username")
    elif not password:
        messagebox.showerror("Error", "Please enter a valid password")
    elif password != "123":
        messagebox.showerror("Error", "Invalid password")
    else:
        messagebox.showerror("Error", "Sorry, you are not admin")

def user_info():
    user_window = CTk.CTkToplevel(admin_app)
    user_window.geometry("1200x680+60+10")
    user_window.title("Admin_Data_Pengguna")
    user_window.grab_set()

    frame_admin = CTk.CTkFrame(master=user_window, width=700, height=500, corner_radius=0)
    frame_admin.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    user_window.grid_rowconfigure(0, weight=1)
    user_window.grid_columnconfigure(0, weight=1)

    user_data = load_user_data()

    def show_user_list():
        for row in treeview.get_children():
            treeview.delete(row)

        for username, data in user_data.items():
            treeview.insert("", "end", values=(
                username, 
                data.get("nama_lengkap"),
                data.get("tanggal_lahir"),
                data.get("jenis_kelamin"),
                data.get("nomor_hp"),
                data.get("nik"),
                data.get("riwayat_penyakit")
            ))

    def delete_user():
        selected_item = treeview.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih pengguna yang ingin dihapus")
            return
        user_delete = treeview.item(selected_item, "values")[0]
        del user_data[user_delete]
        save_user_data(user_data)
        messagebox.showinfo(f"Pengguna {user_delete} berhasil dihapus")
        show_user_list()

    def edit_user():
        selected_item = treeview.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih pengguna yang ingin diedit")
            return
        user_edit = treeview.item(selected_item, "values")[0]
        user_info = user_data[user_edit]

        def save_changes():
            user_info['nama_lengkap'] = entry_nama_lengkap.get()
            user_info['tanggal_lahir'] = entry_tanggal_lahir.get()
            user_info['jenis_kelamin'] = entry_jenis_kelamin.get()
            user_info['nomor_hp'] = entry_nomor_hp.get()
            user_info['nik'] = entry_nik.get()
            user_info['riwayat_penyakit'] = entry_riwayat_penyakit.get()

            user_data[user_edit] = user_info
            save_user_data(user_data)
            messagebox.showinfo("Berhasil", "Data pengguna berhasil diperbarui!")
            edit_window.destroy()
            show_user_list()

        edit_window = CTk.CTk()
        edit_window.geometry("400x400")
        edit_window.title("Edit User Data")

        label_nama_lengkap = CTk.CTkLabel(master=edit_window, text="Nama Lengkap:", font=("Century Gothic", 12))
        label_nama_lengkap.grid(row=0, column=0, pady=5)
        entry_nama_lengkap = CTk.CTkEntry(master=edit_window, font=("Century Gothic", 12))
        entry_nama_lengkap.grid(row=0, column=1, pady=5)
        entry_nama_lengkap.insert(0, user_info['nama_lengkap'])

        label_tanggal_lahir = CTk.CTkLabel(master=edit_window, text="Tanggal Lahir:", font=("Century Gothic", 12))
        label_tanggal_lahir.grid(row=1, column=0, pady=5)
        entry_tanggal_lahir = CTk.CTkEntry(master=edit_window, font=("Century Gothic", 12))
        entry_tanggal_lahir.grid(row=1, column=1, pady=5)
        entry_tanggal_lahir.insert(0, user_info['tanggal_lahir'])

        label_jenis_kelamin = CTk.CTkLabel(master=edit_window, text="Jenis Kelamin:", font=("Century Gothic", 12))
        label_jenis_kelamin.grid(row=2, column=0, pady=5)
        entry_jenis_kelamin = CTk.CTkEntry(master=edit_window, font=("Century Gothic", 12))
        entry_jenis_kelamin.grid(row=2, column=1, pady=5)
        entry_jenis_kelamin.insert(0, user_info['jenis_kelamin'])

        label_nomor_hp = CTk.CTkLabel(master=edit_window, text="Nomor HP:", font=("Century Gothic", 12))
        label_nomor_hp.grid(row=3, column=0, pady=5)
        entry_nomor_hp = CTk.CTkEntry(master=edit_window, font=("Century Gothic", 12))
        entry_nomor_hp.grid(row=3, column=1, pady=5)
        entry_nomor_hp.insert(0, user_info['nomor_hp'])

        label_nik = CTk.CTkLabel(master=edit_window, text="NIK:", font=("Century Gothic", 12))
        label_nik.grid(row=4, column=0, pady=5)
        entry_nik = CTk.CTkEntry(master=edit_window, font=("Century Gothic", 12))
        entry_nik.grid(row=4, column=1, pady=5)
        entry_nik.insert(0, user_info['nik'])

        label_riwayat_penyakit = CTk.CTkLabel(master=edit_window, text="Riwayat Penyakit:", font=("Century Gothic", 12))
        label_riwayat_penyakit.grid(row=5, column=0, pady=5)
        entry_riwayat_penyakit = CTk.CTkEntry(master=edit_window, font=("Century Gothic", 12))
        entry_riwayat_penyakit.grid(row=5, column=1, pady=5)
        entry_riwayat_penyakit.insert(0, user_info['riwayat_penyakit'])

        button_save_changes = CTk.CTkButton(master=edit_window, text="Simpan Perubahan", font=("Century Gothic", 12), command=save_changes)
        button_save_changes.grid(row=6, column=0, columnspan=2, pady=10)

        edit_window.mainloop()

    columns = ("Username", "Nama Lengkap", "Tanggal Lahir", "Jenis Kelamin", "Nomor HP", "NIK", "Riwayat Penyakit")
    global treeview
    treeview = ttk.Treeview(frame_admin, columns=columns, show="headings")
    treeview.grid(row=1, column=0, sticky="nsew", padx=10, pady=20)

    for column in columns:
        treeview.heading(column, text=column)

    treeview.column("Username", width=100)
    treeview.column("Nama Lengkap", width=150)
    treeview.column("Tanggal Lahir", width=120)
    treeview.column("Jenis Kelamin", width=100)
    treeview.column("Nomor HP", width=120)
    treeview.column("NIK", width=100)
    treeview.column("Riwayat Penyakit", width=150)

    frame_admin.grid_rowconfigure(1, weight=1)
    frame_admin.grid_columnconfigure(0, weight=1)

    show_user_list()

    button_delete_user = CTk.CTkButton(master=frame_admin, text="Hapus Pengguna", font=("Century Gothic", 12), command=delete_user)
    button_delete_user.grid(row=2, column=0, pady=10)

    button_edit_user = CTk.CTkButton(master=frame_admin, text="Edit Pengguna", font=("Century Gothic", 12), command=edit_user)
    button_edit_user.grid(row=3, column=0, pady=10)

    admin_frame2 = CTk.CTkFrame(master=user_window, width=1160, height=30, fg_color="#86A3D6", corner_radius=0)
    admin_frame2.place(x=20,y=0)

    button_back = CTk.CTkButton(master=admin_frame2, text="⭠ Back", fg_color="transparent", width=30, text_color="Black", font=("Bahnschrift SemiBold",13),command=user_window.destroy)
    button_back.place(x=0,y=0) 

def admin_poli_gigi():
    admin_PG_window = CTk.CTkToplevel(admin_app)
    admin_PG_window.geometry("1200x680+60+10")
    admin_PG_window.title("Admin Poli Gigi")
    admin_PG_window.grab_set()

    def load_transfer_data():
        try:
            with open("poli_gigi2.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []  

    def save_transfer_data(data):
        with open("poli_gigi2.json", "w") as file:
            json.dump(data, file, indent=4)

    def delete_transfer_data(index):
        transfer_data = load_transfer_data()  
        if 0 <= index < len(transfer_data):
            del transfer_data[index]  
            save_transfer_data(transfer_data) 
            show_transfer_data() 

    def show_transfer_data():
        for widget in admin_frame.winfo_children():
            widget.destroy()

        transfer_data = load_transfer_data()  

        if not transfer_data: 
            CTk.CTkLabel(admin_frame, text="Belum ada bukti transfer yang diterima", font=("Century Gothic", 14)).pack(pady=20)
            return

        CTk.CTkLabel(admin_frame, text="Nama Pemesan", font=("Century Gothic", 12, "bold")).grid(row=0,column=0, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nama Dokter", font=("Century Gothic", 12, "bold")).grid(row=0, column=1, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Jadwal", font=("Century Gothic", 12, "bold")).grid(row=0, column=2, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nomor Antrean", font=("Century Gothic", 12, "bold")).grid(row=0, column=3, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Bukti Transfer", font=("Century Gothic", 12, "bold")).grid(row=0, column=4, padx=35, pady=20)
        
        row_num = 1  

        for index, entry in enumerate(transfer_data):
            CTk.CTkLabel(admin_frame, text=entry['nama pemesan'], font=("Century Gothic", 12, "bold")).grid(row=row_num,column=0, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nama dokter'], font=("Century Gothic", 12)).grid(row=row_num, column=1, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['jadwal yang terpilih'], font=("Century Gothic", 12)).grid(row=row_num, column=2, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nomor antrean'], font=("Century Gothic", 12)).grid(row=row_num, column=3, padx=35, pady=10)

            file_path = entry.get('bukti transfer')
            if file_path:
                try:
                    img = Image.open(file_path)
                    img.thumbnail((200, 200))  
                    img_tk = ImageTk.PhotoImage(img)

                    image_label = CTk.CTkLabel(admin_frame, image=img_tk, text="", fg_color="transparent")
                    image_label.image = img_tk  
                    image_label.grid(row=row_num, column=4, padx=35, pady=10)
                except Exception as e:
                    CTk.CTkLabel(admin_frame, text="Gambar gagal ditampilkan", font=("Century Gothic", 12)).grid(row=row_num, column=4, padx=10, pady=10)

            delete_button = CTk.CTkButton(admin_frame, text="Hapus", command=lambda idx=index: delete_transfer_data(idx))
            delete_button.grid(row=row_num, column=5, padx=35, pady=10)

            row_num += 1 

    admin_frame = CTk.CTkScrollableFrame(master=admin_PG_window, corner_radius=0)
    admin_frame.pack(fill="both", expand=True, padx=10, pady=10)  

    admin_frame2 = CTk.CTkFrame(master=admin_PG_window, width=1180, height=30, fg_color="#86A3D6", corner_radius=0)
    admin_frame2.place(x=10,y=0)

    button_back = CTk.CTkButton(master=admin_frame2, text="⭠ Back", fg_color="transparent", width=30, text_color="Black", font=("Bahnschrift SemiBold",13),command=admin_PG_window.destroy)
    button_back.place(x=0,y=0) 

    show_transfer_data()

def admin_poli_anak():
    admin_PA_window = CTk.CTkToplevel(admin_app)
    admin_PA_window.geometry("1200x680+60+10")
    admin_PA_window.title("Admin Poli Anak")
    admin_PA_window.grab_set()

    def load_transfer_data():
        try:
            with open("poli_anak2.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return [] 

    def save_transfer_data(data):
        with open("poli_anak2.json", "w") as file:
            json.dump(data, file, indent=4)

    def delete_transfer_data(index):
        transfer_data = load_transfer_data()  
        if 0 <= index < len(transfer_data):
            del transfer_data[index]  
            save_transfer_data(transfer_data) 
            show_transfer_data()        

    def show_transfer_data():
        for widget in admin_frame.winfo_children():
            widget.destroy()

        transfer_data = load_transfer_data()  

        if not transfer_data: 
            CTk.CTkLabel(admin_frame, text="Belum ada bukti transfer yang diterima", font=("Century Gothic", 14)).pack(pady=20)
            return

        CTk.CTkLabel(admin_frame, text="Nama Pemesan", font=("Century Gothic", 12, "bold")).grid(row=0,column=0, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nama Dokter", font=("Century Gothic", 12, "bold")).grid(row=0, column=1, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Jadwal", font=("Century Gothic", 12, "bold")).grid(row=0, column=2, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nomor Antrean", font=("Century Gothic", 12, "bold")).grid(row=0, column=3, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Bukti Transfer", font=("Century Gothic", 12, "bold")).grid(row=0, column=4, padx=35, pady=20)
        
        row_num = 1  

        for index, entry in enumerate(transfer_data):
            CTk.CTkLabel(admin_frame, text=entry['nama pemesan'], font=("Century Gothic", 12, "bold")).grid(row=row_num,column=0, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nama dokter'], font=("Century Gothic", 12)).grid(row=row_num, column=1, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['jadwal yang terpilih'], font=("Century Gothic", 12)).grid(row=row_num, column=2, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nomor antrean'], font=("Century Gothic", 12)).grid(row=row_num, column=3, padx=35, pady=10)

            file_path = entry.get('bukti transfer')
            if file_path:
                try:
                    img = Image.open(file_path)
                    img.thumbnail((200, 200))  
                    img_tk = ImageTk.PhotoImage(img)

                    image_label = CTk.CTkLabel(admin_frame, image=img_tk, text="", fg_color="transparent")
                    image_label.image = img_tk  
                    image_label.grid(row=row_num, column=4, padx=35, pady=10)
                except Exception as e:
                    CTk.CTkLabel(admin_frame, text="Gambar gagal ditampilkan", font=("Century Gothic", 12)).grid(row=row_num, column=4, padx=10, pady=10)

            delete_button = CTk.CTkButton(admin_frame, text="Hapus", command=lambda idx=index: delete_transfer_data(idx))
            delete_button.grid(row=row_num, column=5, padx=35, pady=10)

            row_num += 1 

    admin_frame = CTk.CTkScrollableFrame(master=admin_PA_window, corner_radius=0)
    admin_frame.pack(fill="both", expand=True, padx=10, pady=10) 

    admin_frame2 = CTk.CTkFrame(master=admin_PA_window, width=1180, height=30, fg_color="#86A3D6", corner_radius=0)
    admin_frame2.place(x=10,y=0)

    button_back = CTk.CTkButton(master=admin_frame2, text="⭠ Back", fg_color="transparent", width=30, text_color="Black", font=("Bahnschrift SemiBold",13),command=admin_PA_window.destroy)
    button_back.place(x=0,y=0) 

    show_transfer_data()

def admin_poli_jantung():
    admin_PJ_window = CTk.CTkToplevel(admin_app)
    admin_PJ_window.geometry("1200x680+60+10")
    admin_PJ_window.title("Admin Poli Jantung")
    admin_PJ_window.grab_set()

    def load_transfer_data():
        try:
            with open("poli_jantung2.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []  
        
    def save_transfer_data(data):
        with open("poli_jantung2.json", "w") as file:
            json.dump(data, file, indent=4)

    def delete_transfer_data(index):
        transfer_data = load_transfer_data()  
        if 0 <= index < len(transfer_data):
            del transfer_data[index]  
            save_transfer_data(transfer_data) 
            show_transfer_data() 

    def show_transfer_data():
        for widget in admin_frame.winfo_children():
            widget.destroy()

        transfer_data = load_transfer_data()  

        if not transfer_data: 
            CTk.CTkLabel(admin_frame, text="Belum ada bukti transfer yang diterima", font=("Century Gothic", 14)).pack(pady=20)
            return

        CTk.CTkLabel(admin_frame, text="Nama Pemesan", font=("Century Gothic", 12, "bold")).grid(row=0,column=0, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nama Dokter", font=("Century Gothic", 12, "bold")).grid(row=0, column=1, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Jadwal", font=("Century Gothic", 12, "bold")).grid(row=0, column=2, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nomor Antrean", font=("Century Gothic", 12, "bold")).grid(row=0, column=3, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Bukti Transfer", font=("Century Gothic", 12, "bold")).grid(row=0, column=4, padx=35, pady=20)

        row_num = 1  

        for index, entry in enumerate(transfer_data):
            CTk.CTkLabel(admin_frame, text=entry['nama pemesan'], font=("Century Gothic", 12, "bold")).grid(row=row_num,column=0, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nama dokter'], font=("Century Gothic", 12)).grid(row=row_num, column=1, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['jadwal yang terpilih'], font=("Century Gothic", 12)).grid(row=row_num, column=2, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nomor antrean'], font=("Century Gothic", 12)).grid(row=row_num, column=3, padx=35, pady=10)

            file_path = entry.get('bukti transfer')
            if file_path:
                try:
                    img = Image.open(file_path)
                    img.thumbnail((200, 200))  
                    img_tk = ImageTk.PhotoImage(img)

                    image_label = CTk.CTkLabel(admin_frame, image=img_tk, text="", fg_color="transparent")
                    image_label.image = img_tk  
                    image_label.grid(row=row_num, column=4, padx=35, pady=10)
                except Exception as e:
                    CTk.CTkLabel(admin_frame, text="Gambar gagal ditampilkan", font=("Century Gothic", 12)).grid(row=row_num, column=4, padx=10, pady=10)

            delete_button = CTk.CTkButton(admin_frame, text="Hapus", command=lambda idx=index: delete_transfer_data(idx))
            delete_button.grid(row=row_num, column=5, padx=35, pady=10)

            row_num += 1 

    admin_frame = CTk.CTkScrollableFrame(master=admin_PJ_window, corner_radius=0)
    admin_frame.pack(fill="both", expand=True, padx=10, pady=10)  

    admin_frame2 = CTk.CTkFrame(master=admin_PJ_window, width=1180, height=30, fg_color="#86A3D6", corner_radius=0)
    admin_frame2.place(x=10,y=0)

    button_back = CTk.CTkButton(master=admin_frame2, text="⭠ Back", fg_color="transparent", width=30, text_color="Black", font=("Bahnschrift SemiBold",13),command=admin_PJ_window.destroy)
    button_back.place(x=0,y=0) 

    show_transfer_data()

def admin_poli_mata():
    admin_PM_window = CTk.CTkToplevel(admin_app)
    admin_PM_window.geometry("1200x680+60+10")
    admin_PM_window.title("Admin Poli Mata")
    admin_PM_window.grab_set()

    def load_transfer_data():
            try:
                with open("poli_mata2.json", "r") as file:
                    return json.load(file)
            except FileNotFoundError:
                return []  
            
    def save_transfer_data(data):
        with open("poli_mata2.json", "w") as file:
            json.dump(data, file, indent=4)

    def delete_transfer_data(index):
        transfer_data = load_transfer_data()  
        if 0 <= index < len(transfer_data):
            del transfer_data[index]  
            save_transfer_data(transfer_data) 
            show_transfer_data() 

    def show_transfer_data():
        for widget in admin_frame.winfo_children():
            widget.destroy()

        transfer_data = load_transfer_data()  

        if not transfer_data: 
            CTk.CTkLabel(admin_frame, text="Belum ada bukti transfer yang diterima", font=("Century Gothic", 14)).pack(pady=20)
            return
        
        CTk.CTkLabel(admin_frame, text="Nama Pemesan", font=("Century Gothic", 12, "bold")).grid(row=0,column=0, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nama Dokter", font=("Century Gothic", 12, "bold")).grid(row=0, column=1, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Jadwal", font=("Century Gothic", 12, "bold")).grid(row=0, column=2, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nomor Antrean", font=("Century Gothic", 12, "bold")).grid(row=0, column=3, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Bukti Transfer", font=("Century Gothic", 12, "bold")).grid(row=0, column=4, padx=35, pady=20)

        row_num = 1  

        for index, entry in enumerate(transfer_data):
            CTk.CTkLabel(admin_frame, text=entry['nama pemesan'], font=("Century Gothic", 12, "bold")).grid(row=row_num,column=0, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nama dokter'], font=("Century Gothic", 12)).grid(row=row_num, column=1, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['jadwal yang terpilih'], font=("Century Gothic", 12)).grid(row=row_num, column=2, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nomor antrean'], font=("Century Gothic", 12)).grid(row=row_num, column=3, padx=35, pady=10)

            file_path = entry.get('bukti transfer')
            if file_path:
                try:
                    img = Image.open(file_path)
                    img.thumbnail((200, 200))  
                    img_tk = ImageTk.PhotoImage(img)

                    image_label = CTk.CTkLabel(admin_frame, image=img_tk, text="", fg_color="transparent")
                    image_label.image = img_tk  
                    image_label.grid(row=row_num, column=4, padx=35, pady=10)
                except Exception as e:
                    CTk.CTkLabel(admin_frame, text="Gambar gagal ditampilkan", font=("Century Gothic", 12)).grid(row=row_num, column=4, padx=10, pady=10)

            delete_button = CTk.CTkButton(admin_frame, text="Hapus", command=lambda idx=index: delete_transfer_data(idx))
            delete_button.grid(row=row_num, column=5, padx=35, pady=10)

            row_num += 1

    admin_frame = CTk.CTkScrollableFrame(master=admin_PM_window, corner_radius=0)
    admin_frame.pack(fill="both", expand=True, padx=10, pady=10)  

    admin_frame2 = CTk.CTkFrame(master=admin_PM_window, width=1180, height=30, fg_color="#86A3D6", corner_radius=0)
    admin_frame2.place(x=10,y=0)

    button_back = CTk.CTkButton(master=admin_frame2, text="⭠ Back", fg_color="transparent", width=30, text_color="Black", font=("Bahnschrift SemiBold",13),command=admin_PM_window.destroy)
    button_back.place(x=0,y=0) 

    show_transfer_data()

def admin_poli_penyakit_dalam():
    admin_PP_window = CTk.CTkToplevel(admin_app)
    admin_PP_window.geometry("1200x680+60+10")
    admin_PP_window.title("Admin Poli Penyakit Dalam")
    admin_PP_window.grab_set()

    def load_transfer_data():
            try:
                with open("poli_penyakit_dalam2.json", "r") as file:
                    return json.load(file)
            except FileNotFoundError:
                return []  
            
    def save_transfer_data(data):
        with open("poli_penyakit_dalam2.json", "w") as file:
            json.dump(data, file, indent=4)

    def delete_transfer_data(index):
        transfer_data = load_transfer_data()  
        if 0 <= index < len(transfer_data):
            del transfer_data[index]  
            save_transfer_data(transfer_data) 
            show_transfer_data() 

    def show_transfer_data():
        for widget in admin_frame.winfo_children():
            widget.destroy()

        transfer_data = load_transfer_data()  

        if not transfer_data: 
            CTk.CTkLabel(admin_frame, text="Belum ada bukti transfer yang diterima", font=("Century Gothic", 14)).pack(pady=20)
            return
        
        CTk.CTkLabel(admin_frame, text="Nama Pemesan", font=("Century Gothic", 12, "bold")).grid(row=0,column=0, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nama Dokter", font=("Century Gothic", 12, "bold")).grid(row=0, column=1, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Jadwal", font=("Century Gothic", 12, "bold")).grid(row=0, column=2, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nomor Antrean", font=("Century Gothic", 12, "bold")).grid(row=0, column=3, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Bukti Transfer", font=("Century Gothic", 12, "bold")).grid(row=0, column=4, padx=35, pady=20)

        row_num = 1  

        for index, entry in enumerate(transfer_data):
            CTk.CTkLabel(admin_frame, text=entry['nama pemesan'], font=("Century Gothic", 12, "bold")).grid(row=row_num,column=0, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nama dokter'], font=("Century Gothic", 12)).grid(row=row_num, column=1, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['jadwal yang terpilih'], font=("Century Gothic", 12)).grid(row=row_num, column=2, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nomor antrean'], font=("Century Gothic", 12)).grid(row=row_num, column=3, padx=35, pady=10)

            file_path = entry.get('bukti transfer')
            if file_path:
                try:
                    img = Image.open(file_path)
                    img.thumbnail((200, 200))  
                    img_tk = ImageTk.PhotoImage(img)

                    image_label = CTk.CTkLabel(admin_frame, image=img_tk, text="", fg_color="transparent")
                    image_label.image = img_tk  
                    image_label.grid(row=row_num, column=4, padx=35, pady=10)
                except Exception as e:
                    CTk.CTkLabel(admin_frame, text="Gambar gagal ditampilkan", font=("Century Gothic", 12)).grid(row=row_num, column=4, padx=10, pady=10)

            delete_button = CTk.CTkButton(admin_frame, text="Hapus", command=lambda idx=index: delete_transfer_data(idx))
            delete_button.grid(row=row_num, column=5, padx=35, pady=10)

            row_num += 1

    admin_frame = CTk.CTkScrollableFrame(master=admin_PP_window, corner_radius=0)
    admin_frame.pack(fill="both", expand=True, padx=10, pady=10) 

    admin_frame2 = CTk.CTkFrame(master=admin_PP_window, width=1180, height=30, fg_color="#86A3D6", corner_radius=0)
    admin_frame2.place(x=10,y=0)

    button_back = CTk.CTkButton(master=admin_frame2, text="⭠ Back", fg_color="transparent", width=30, text_color="Black", font=("Bahnschrift SemiBold",13),command=admin_PP_window.destroy)
    button_back.place(x=0,y=0)  

    show_transfer_data()

def admin_poli_umum():
    admin_PU_window = CTk.CTkToplevel(admin_app)
    admin_PU_window.geometry("1200x680+60+10")
    admin_PU_window.title("Admin Poli Umum")
    admin_PU_window.grab_set()

    CTk.set_appearance_mode("System")
    CTk.set_default_color_theme("blue")

    def load_transfer_data():
        try:
            with open("poli_umum2.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []  
        
    def save_transfer_data(data):
        with open("poli_umum2.json", "w") as file:
            json.dump(data, file, indent=4)

    def delete_transfer_data(index):
        transfer_data = load_transfer_data()  
        if 0 <= index < len(transfer_data):
            del transfer_data[index]  
            save_transfer_data(transfer_data) 
            show_transfer_data() 

    def show_transfer_data():
        for widget in admin_frame.winfo_children():
            widget.destroy()
            
        transfer_data = load_transfer_data()  

        if not transfer_data: 
            CTk.CTkLabel(admin_frame, text="Belum ada bukti transfer yang diterima", font=("Century Gothic", 14)).pack(pady=20)
            return
        
        CTk.CTkLabel(admin_frame, text="Nama Pemesan", font=("Century Gothic", 12, "bold")).grid(row=0,column=0, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nama Dokter", font=("Century Gothic", 12, "bold")).grid(row=0, column=1, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Jadwal", font=("Century Gothic", 12, "bold")).grid(row=0, column=2, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Nomor Antrean", font=("Century Gothic", 12, "bold")).grid(row=0, column=3, padx=35, pady=20)
        CTk.CTkLabel(admin_frame, text="Bukti Transfer", font=("Century Gothic", 12, "bold")).grid(row=0, column=4, padx=35, pady=20)

        row_num = 1       

        for index, entry in enumerate(transfer_data):
            CTk.CTkLabel(admin_frame, text=entry['nama pemesan'], font=("Century Gothic", 12, "bold")).grid(row=row_num,column=0, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nama dokter'], font=("Century Gothic", 12)).grid(row=row_num, column=1, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['jadwal yang terpilih'], font=("Century Gothic", 12)).grid(row=row_num, column=2, padx=35, pady=10)
            CTk.CTkLabel(admin_frame, text=entry['nomor antrean'], font=("Century Gothic", 12)).grid(row=row_num, column=3, padx=35, pady=10)

            file_path = entry.get('bukti transfer')
            if file_path:
                try:
                    img = Image.open(file_path)
                    img.thumbnail((200, 200))  
                    img_tk = ImageTk.PhotoImage(img)

                    image_label = CTk.CTkLabel(admin_frame, image=img_tk, text="", fg_color="transparent")
                    image_label.image = img_tk  
                    image_label.grid(row=row_num, column=4, padx=35, pady=10)
                except Exception as e:
                    CTk.CTkLabel(admin_frame, text="Gambar gagal ditampilkan", font=("Century Gothic", 12)).grid(row=row_num, column=4, padx=10, pady=10)

            delete_button = CTk.CTkButton(admin_frame, text="Hapus", command=lambda idx=index: delete_transfer_data(idx))
            delete_button.grid(row=row_num, column=5, padx=35, pady=10) 

            row_num += 1

    admin_frame = CTk.CTkScrollableFrame(master=admin_PU_window, corner_radius=0)
    admin_frame.pack(fill="both", expand=True, padx=10, pady=10)

    admin_frame2 = CTk.CTkFrame(master=admin_PU_window, width=1180, height=30, fg_color="#86A3D6", corner_radius=0)
    admin_frame2.place(x=10,y=0)

    button_back = CTk.CTkButton(master=admin_frame2, text="⭠ Back", fg_color="transparent", width=30, text_color="Black", font=("Bahnschrift SemiBold",13),command=admin_PU_window.destroy)
    button_back.place(x=0,y=0)   

    show_transfer_data()

def admin_rating():
    admin_rating = CTk.CTkToplevel(admin_app)
    admin_rating.title("Admin Rating")
    admin_rating.geometry("1200x680+60+10")
    admin_rating.grab_set()

    def load_rating():
        try:
            with open ("rating2.json","r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        
    def save_rating(data):
        with open ("rating2.json","w") as file:
            json.dump(data, file, indent=4)

    def delete_rating_data(index):
        rating_data = load_rating()  
        if 0 <= index < len(rating_data):
            del rating_data[index]  
            save_rating(rating_data) 
            show_rating_data() 

    def show_rating_data():
            for widget in rating_frame.winfo_children():
                widget.destroy()
                
            rating_data = load_rating()  
            
            CTk.CTkLabel(rating_frame, text="Rating Pelayanan", font=("Century Gothic", 15, "bold")).grid(row=0,column=0, padx=35, pady=20)
            CTk.CTkLabel(rating_frame, text="Rating Tempat", font=("Century Gothic", 15, "bold")).grid(row=0, column=1, padx=35, pady=20)
            CTk.CTkLabel(rating_frame, text="Komentar Pelayanan", font=("Century Gothic", 15, "bold")).grid(row=0, column=2, padx=35, pady=20)
            CTk.CTkLabel(rating_frame, text="Komentar Tempat", font=("Century Gothic", 15, "bold")).grid(row=0, column=3, padx=35, pady=20)

            row_num = 1  

            for index, entry in enumerate(rating_data):
                CTk.CTkLabel(rating_frame, text=entry['rating_pelayanan'], font=("Century Gothic", 15)).grid(row=row_num,column=0, padx=35, pady=10)
                CTk.CTkLabel(rating_frame, text=entry['rating_tempat'], font=("Century Gothic", 15)).grid(row=row_num, column=1, padx=35, pady=10)
                komentar_pelayanan = "\n".join(textwrap.wrap(entry['komentar_pelayanan'], width=30))
                CTk.CTkLabel(rating_frame, text=komentar_pelayanan, font=("Century Gothic", 15)).grid(row=row_num, column=2, padx=35, pady=10)
                komentar_tempat = "\n".join(textwrap.wrap(entry['komentar_tempat'], width=30))
                CTk.CTkLabel(rating_frame, text=komentar_tempat, font=("Century Gothic", 15)).grid(row=row_num, column=3, padx=35, pady=10)

                delete_button = CTk.CTkButton(rating_frame, text="Hapus", command=lambda idx=index: delete_rating_data(idx))
                delete_button.grid(row=row_num, column=5, padx=35, pady=10)

                row_num += 1

    rating_frame = CTk.CTkScrollableFrame(master=admin_rating, corner_radius=0)
    rating_frame.pack(fill="both", expand=True, padx=10, pady=10)

    admin_frame2 = CTk.CTkFrame(master=admin_rating, width=1180, height=30, fg_color="#86A3D6", corner_radius=0)
    admin_frame2.place(x=10,y=0)

    button_back = CTk.CTkButton(master=admin_frame2, text="⭠ Back", fg_color="transparent", width=30, text_color="Black", font=("Bahnschrift SemiBold",13),command=admin_rating.destroy)
    button_back.place(x=0,y=0) 

    show_rating_data()

def home():
    home = CTk.CTkToplevel(admin_app)
    home.geometry("1200x680+60+10")
    home.title("Home")
    home.grab_set()

    img = Image.open("admin.jpg")
    img1 = ImageTk.PhotoImage(img)

    background = CTk.CTkLabel(master=home, text="", image=img1)
    background.image = img1
    background.place(x=0, y=0, relwidth=1, relheight=1)

    home.grid_rowconfigure(0, weight=1)
    home.grid_columnconfigure(0, weight=1)

    frame_admin = CTk.CTkFrame(master=home, width=500, height=520, corner_radius=0)
    frame_admin.grid(row=0, column=0)

    frame_admin.grid_rowconfigure(0, weight=1)
    frame_admin.grid_columnconfigure(0, weight=1)

    img1 = ImageTk.PhotoImage(Image.open("admin2.jpg"))
    image_label1 = CTk.CTkLabel(master=frame_admin, image=img1, text="")
    image_label1.place(x=50, y=20)

    button_user_data = CTk.CTkButton(master=frame_admin, width=400, text="Data Pengguna", command=user_info)
    button_user_data.place(x=50,y=214)

    button_poli_mata = CTk.CTkButton(master=frame_admin, width=400, text="Poli Mata", command=admin_poli_mata)
    button_poli_mata.place(x=50,y=250)

    button_poli_gigi = CTk.CTkButton(master=frame_admin, width=400, text="Poli Gigi", command=admin_poli_gigi)
    button_poli_gigi.place(x=50,y=286)

    button_poli_jantung = CTk.CTkButton(master=frame_admin, width=400, text="Poli Jantung", command=admin_poli_jantung)
    button_poli_jantung.place(x=50,y=322)

    button_poli_anak = CTk.CTkButton(master=frame_admin, width=400, text="Poli Anak", command=admin_poli_anak)
    button_poli_anak.place(x=50,y=358)

    button_poli_penyakit_dalam = CTk.CTkButton(master=frame_admin, width=400, text="Poli Penyakit Dalam", command=admin_poli_penyakit_dalam)
    button_poli_penyakit_dalam.place(x=50,y=394)

    button_poli_umum = CTk.CTkButton(master=frame_admin, width=400, text="Poli Umum", command=admin_poli_umum)
    button_poli_umum.place(x=50,y=430)

    button_rating = CTk.CTkButton(master=frame_admin, width=400, text="Rating", command=admin_rating)
    button_rating.place(x=50,y=466)

admin_app = CTk.CTk()
admin_app.geometry("1200x680+60+10")
admin_app.title("Admin Panel")

img = Image.open("admin.jpg")
img1 = ImageTk.PhotoImage(img)

background = CTk.CTkLabel(master=admin_app, text="", image=img1)
background.image = img1
background.place(x=0, y=0, relwidth=1, relheight=1)

admin_app.grid_rowconfigure(0, weight=1)
admin_app.grid_columnconfigure(0, weight=1)

frame_admin = CTk.CTkFrame(master=admin_app, width=450, height=450, corner_radius=0)
frame_admin.grid(row=0, column=0)

frame_admin.grid_rowconfigure(0, weight=1)
frame_admin.grid_columnconfigure(0, weight=1)

img1 = ImageTk.PhotoImage(Image.open("admin2.jpg"))
image_label1 = CTk.CTkLabel(master=frame_admin, image=img1, text="")
image_label1.place(x=25, y=30)

username_entry = CTk.CTkEntry(master=frame_admin, width=400, placeholder_text="username")
username_entry.place(x=25,y=234)

password_entry = CTk.CTkEntry(master=frame_admin, width=400, placeholder_text="password")
password_entry.place(x=25,y=274)

button_login = CTk.CTkButton(master=frame_admin, width=400, text="LOG IN", command=login)
button_login.place(x=25,y=316)

admin_app.mainloop()



