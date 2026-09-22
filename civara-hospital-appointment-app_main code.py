import tkinter
import customtkinter as CTk
from PIL import ImageTk, Image
from tkinter import END
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *
import json

user_saat_ini = ""

def load_accounts():
    try:
        with open("accounts5.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_accounts(accounts):
    try:
        with open("accounts5.json", "w") as file:
            json.dump(accounts, file, indent=4)
    except Exception as e:
        print(f"Error saving accounts: {e}")

def load_user_data():
    try:
        with open('additional_info.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def display_user_profile(username):
    user_data = load_user_data()
    
    if username in user_data:
        user_info = user_data[username]
        nama2.configure(text=user_info['nama_lengkap'])
        tanggal_lahir2.configure(text=user_info['tanggal_lahir'])
        jenis_kelamin2.configure(text=user_info['jenis_kelamin'])
        nomor_hp2.configure(text=user_info['nomor_hp'])
        nik2.configure(text=user_info['nik'])
        penyakit2.configure(text=user_info['riwayat_penyakit'])
    else:
        messagebox.showerror("Error", "User not found!")

    
def login():
    global user_saat_ini
    username = username_entry.get()
    password = password_entry.get()
    accounts = load_accounts()

    if username in accounts and accounts[username]["password"] == password:
        user_saat_ini = username
        dashboard()
        app.withdraw()

    elif not username:
            messagebox.showerror("Error", "Please enter a valid username")
            return
    
    elif not password:
            messagebox.showerror("Error", "Please enter a valid password")
            return
    else:
        messagebox.showerror("Error", "Invalid username or password")

def register_window():
    global reg_username_entry, reg_email_entry, reg_password_entry, register_window
    register_window = CTk.CTkToplevel(app)
    register_window.geometry("400x680+100+15")
    register_window.title("Register")
    register_window.resizable(False, False)
    register_window.grab_set()

    img2 = ImageTk.PhotoImage(Image.open("background.png"))
    background2 = CTk.CTkLabel(master=register_window, image=img2)
    background2.pack()

    frame = CTk.CTkFrame(master=register_window, width=320, height=460, corner_radius=15, fg_color="#70C4E5")
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    img2 = ImageTk.PhotoImage(Image.open("rumahsakit3.jpg"))
    image2_label = CTk.CTkLabel(master=register_window, image=img2, text="", fg_color="transparent")
    image2_label.place(x=120, y=170)

    reg_username_entry = CTk.CTkEntry(master=frame, width=260, placeholder_text="Username")
    reg_username_entry.place(x=30, y=170)

    reg_email_entry = CTk.CTkEntry(master=frame, width=260, placeholder_text="Email")
    reg_email_entry.place(x=30, y=210)

    reg_password_entry = CTk.CTkEntry(master=frame, width=260, placeholder_text="Password")
    reg_password_entry.place(x=30, y=250)

    button3 = CTk.CTkButton(master=frame, width=260, text="Register", corner_radius=6, command=register)
    button3.place(x=30, y=300)


def dashboard():
    global img_menu, img_menu2
    dashboard_window = CTk.CTkToplevel(app)
    dashboard_window.geometry("400x680+100+15")
    dashboard_window.title("Dasboard")
    dashboard_window.resizable(False, False)

    background = CTk.CTkLabel(master=dashboard_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    img = ImageTk.PhotoImage(Image.open("rumahsakit.png"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="transparent")
    image_label.place(x=0, y=-15)

    label2 = CTk.CTkLabel(master=dashboard_window, text="Melayani anda dengan sepenuh hati", font=("Century Gothic", 14,"bold"), fg_color="#A5BDD2", text_color="#000000")
    label2.place(x=9, y=102)

    label1 = CTk.CTkLabel(master=dashboard_window, text="CIVARA HOSPITAL", font=("Century Gothic", 20,"bold"), fg_color="#A5BDD2", text_color="#000000")
    label1.place(x=9, y=82)

    Frame = CTk.CTkFrame(master=dashboard_window, width=270, height=5, fg_color="black")
    Frame.place(x=0,y=130)

    Frame = CTk.CTkFrame(master=dashboard_window, width=300, height=60, fg_color="#A7BEE4")
    Frame.place(x=40,y=152)

    img = ImageTk.PhotoImage(Image.open("dasboard5.jpg"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="transparent")
    image_label.place(x=20, y=140)

    label3 = CTk.CTkLabel(
        master=dashboard_window, 
        text=(
        "VISI\n"
        "Menjadi rumah sakit terdepan yang memberikan pelayanan\n "
        "kesehatan berkualitas, inovatif, dan terjangkau,\n"
        "dengan berfokus pada kesejahteraan pasien, pendidikan medis,\n "
        "serta penerapan teknologi kesehatan yang canggih untuk\n "
        "menciptakan masyarakat yang lebih sehat."
        ), 
        font=("Calibri", 8), 
        justify="center",
        fg_color="#A7BEE4", 
        text_color="#000000"
    )
    label3.place(x=110, y=150)

    Frame = CTk.CTkFrame(master=dashboard_window, width=330, height=45, fg_color="#A7BEE4")
    Frame.place(x=30,y=250)

    img = ImageTk.PhotoImage(Image.open("dashboard6.jpg"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="transparent")
    image_label.place(x=295, y=235)

    label4 = CTk.CTkLabel(
        master=dashboard_window, 
        text=(
            "                                                     MISI\n"
            "1. Meningkatkan kualitas pelayanan dengan menggunakan teknologi\n"
            "2. Meningkatkan loyalitas pelanggan dengan layanan prima yang humanis\n"
            "3. Mengembangkan rumah sakit berbasis digital\n"
            "4. Membangun kepercayaan pasien melalui pelayanan yang profesional dan etis\n"
            "5. Meningkatkan akses kesehatan bagi semua kalangan masyarakat\n"
        ), 
        font=("Calibri", 8), 
        justify="left",
        fg_color="#A7BEE4", 
        text_color="#000000"
    )
    label4.place(x=30, y=235)

    Frame = CTk.CTkFrame(master=dashboard_window, width=320, height=60, fg_color="#A7BEE4")
    Frame.place(x=40,y=335)

    img = ImageTk.PhotoImage(Image.open("dashboard7.jpg"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="transparent")
    image_label.place(x=20, y=325)

    label3 = CTk.CTkLabel(
        master=dashboard_window, 
        text=(
            "Civara Hospital senantiasa bekerja keras untu melayani Anda dengan\n"
            "sepenuh hati. Dengan dedikasi dan keahlian, kami berkomitmen\n" 
            "untuk menjaga kesehatan Anda setiap saat\n. "
        ), 
        font=("Calibri", 9), 
        justify="left",
        fg_color="#A7BEE4", 
        text_color="#000000"
    )
    label3.place(x=110, y=347)

    Frame = CTk.CTkFrame(master=dashboard_window, width=330, height=80, fg_color="#A7BEE4")
    Frame.place(x=30,y=425)

    img = ImageTk.PhotoImage(Image.open("dashboard9.jpg"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="transparent")
    image_label.place(x=298, y=423)

    Frame = CTk.CTkFrame(master=dashboard_window, width=400, height=80, fg_color="#A7BEE4")
    Frame.place(x=0,y=630)

    img = ImageTk.PhotoImage(Image.open("komponen1.png"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="#A7BEE4")
    image_label.place(x=30, y=426)

    label4 = CTk.CTkLabel(master=dashboard_window, text=("Merawat Anda dengan Penuh Kasih Sayang"), font=("Calibri", 10, "bold"),fg_color="#A7BEE4", text_color="#000000")
    label4.place(x=65, y=425)

    img = ImageTk.PhotoImage(Image.open("komponen2.png"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="#A7BEE4")
    image_label.place(x=30, y=444)

    label5 = CTk.CTkLabel(master=dashboard_window, text=("Empati yang Membawa Kesembuhan"), font=("Calibri", 10, "bold"),fg_color="#A7BEE4", text_color="#000000")
    label5.place(x=65, y=444)

    img = ImageTk.PhotoImage(Image.open("komponen3.png"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="#A7BEE4")
    image_label.place(x=30, y=462)

    label6 = CTk.CTkLabel(master=dashboard_window, text=("Kami Datang Tepat Waktu"), font=("Calibri", 10, "bold"),fg_color="#A7BEE4", text_color="#000000")
    label6.place(x=65, y=463)

    img = ImageTk.PhotoImage(Image.open("komponen4.png"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="#A7BEE4")
    image_label.place(x=30, y=480)

    label6 = CTk.CTkLabel(master=dashboard_window, text=("Ramah dalam Pelayanan, Tulus dalam Perawatan"), font=("Calibri", 10, "bold"),fg_color="#A7BEE4", text_color="#000000")
    label6.place(x=65, y=480)
    Frame = CTk.CTkFrame(master=dashboard_window, width=400, height=80, fg_color="#A7BEE4")
    Frame.place(x=0,y=630)

    img = ImageTk.PhotoImage(Image.open("sertif1.jpg"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="transparent")
    image_label.place(x=20, y=560)

    img = ImageTk.PhotoImage(Image.open("sertif2.jpg"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="transparent")
    image_label.place(x=120, y=560)

    img = ImageTk.PhotoImage(Image.open("sertif2.jpg"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="transparent")
    image_label.place(x=220, y=560)

    img = ImageTk.PhotoImage(Image.open("contact.png"))
    image_label = CTk.CTkLabel(master=dashboard_window, image=img, text="", fg_color="transparent")
    image_label.place(x=0, y=626)

    global img_profil
    img_profil = ImageTk.PhotoImage(Image.open("profil.jpg"))
    button_profil =  tkinter.Button(master=dashboard_window, image=img_profil, bg="#A5BDD2", border=0, activebackground="#A5BDD2", command=lambda: show_profile(user_saat_ini))
    button_profil.place(x=320, y=85)

    def menu():
        frame1 = CTk.CTkFrame(dashboard_window, width=100, height=250, fg_color="#7AA9D2")
        frame1.place(x=300, y=80)

        button1 = CTk.CTkButton(master=frame1, width=80, text="POLI", 
                                command=lambda: poli_window())
        button1.place(x=10, y=50)

        button2 = CTk.CTkButton(master=frame1, width=80, text="Fasilitas", command=fasilitas)
        button2.place(x=10, y=90)

        button3 = CTk.CTkButton(master=frame1, width=80, text="FAQ", command=FAQ)
        button3.place(x=10, y=130)

        button4 = CTk.CTkButton(master=frame1, width=80, text="RATING", command=rating_window)
        button4.place(x=10, y=170)

        button5 = CTk.CTkButton(master=frame1, width=80, text="Pesanan", command=Pemesanan)
        button5.place(x=10, y=210)

        def delete():
            frame1.destroy()

        global img_menu
        img_menu = ImageTk.PhotoImage(Image.open("menu2.jpg"))
        button_close = tkinter.Button(frame1, image=img_menu, border=0, command=delete, bg="#7AA9D2", activebackground="#7AA9D2")
        button_close.place(x=60, y=10)


    global img_menu2
    img_menu2 = ImageTk.PhotoImage(Image.open("menu.jpg"))
    menu_button = tkinter.Button(dashboard_window, image=img_menu2, command=menu, bg="#A5BDD2", border=0, activebackground="#A5BDD2")
    menu_button.place(x=360, y=85)

def FAQ():
    FAQ = CTk.CTkToplevel(app)
    FAQ.geometry("400x680+100+15")
    FAQ.title("Dashboard")
    FAQ.resizable(False, False)
    FAQ.grab_set()

    background = CTk.CTkLabel(master=FAQ, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    def answer(question, answer_labels, buttons, icons):
        answer_label = answer_labels[question]
        if answer_label.winfo_ismapped():
            answer_label.pack_forget()
            buttons[question].configure(image=icons["down"])
        else:
            answer_label.pack(fill="x", padx=5, pady=5)
            buttons[question].configure(image=icons["up"])

    def main():
        questions = [
            "Jam berapa operasional rumah sakit?",
            "Bagaimana cara membuat janji dengan dokter?",
            "Apakah rumah sakit ini menerima asuransi kesehatan?",
            "Apa yang perlu dibawa saat melakukan pemeriksaan?",
            "Apakah rumah sakit ini menyediakan layanan darurat?",
        ]

        answers = {
            "Jam berapa operasional rumah sakit?": "Rumah sakit kami buka 24 jam sehari, 7 hari seminggu, termasuk hari libur. Anda dapat datang kapan saja untuk mendapat perawatan medis.",
            "Bagaimana cara membuat janji dengan dokter?": "Anda bisa membuat janji dengan dokter kami dengan menghubungi pusat pendaftaran kami pada menu poli.",
            "Apakah rumah sakit ini menerima asuransi kesehatan?": "Ya, kami menerima sebagian besar jenis asuransi kesehatan, silakan menghubungi kontak kami untuk informasi lebih lanjut.",
            "Apa yang perlu dibawa saat melakukan pemeriksaan?": "Saat datang untuk pemeriksaan, pastikan untuk membawa identitas diri yang valid, kartu asuransi (jika berlaku), catatan medis terakhir, dan daftar obat-obatan yang Anda konsumsi.",
            "Apakah rumah sakit ini menyediakan layanan darurat?": "Ya, kami memiliki layanan darurat yang buka 24 jam. Untuk keadaan darurat, segera datang ke rumah sakit atau hubungi kontak kami untuk mendapat bantuan medis segera.",
        }

        icons = {
            "down": ImageTk.PhotoImage(Image.open("panah.png")), 
            "up": ImageTk.PhotoImage(Image.open("panah2.png")),  
        }

        answer_labels = {}
        buttons = {}

        for question in questions:
            frame = CTk.CTkFrame(FAQ)
            frame.pack(fill="x", padx=8, pady=5)

            top_frame = CTk.CTkFrame(frame, fg_color="transparent")
            top_frame.pack(fill="x", padx=5, pady=5)

            question_label = CTk.CTkLabel(top_frame, text=question, font=("Arial", 12))
            question_label.pack(side="left", padx=5)

            button = CTk.CTkButton(
                master=top_frame,
                text="",
                image=icons["down"],
                width=50,
                height=50,
                fg_color="transparent",
                hover_color="lightgray",
                command=lambda r=question: answer(r, answer_labels, buttons, icons),
            )
            button.pack(side="right", padx=5)

            answer_text = answers[question]
            answer_label = CTk.CTkLabel(
                master=frame, text=answer_text, wraplength=370, justify="left", anchor="w"
            )
            answer_label.pack(fill="x", padx=5, pady=5)
            answer_label.pack_forget()

            answer_labels[question] = answer_label
            buttons[question] = button

            frame_FAQ = CTk.CTkFrame(master=FAQ, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
            frame_FAQ.place(x=0,y=0)

            button_back = CTk.CTkButton(master=FAQ, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=FAQ.destroy)
            button_back.place(x=0,y=0)

    main()

def show_profile(username):
    global user_saat_ini
    profil = CTk.CTkToplevel(app)
    profil.title("Profil")
    profil.geometry("400x680+100+15")
    profil.resizable(False, False)
    profil.grab_set()

    background = CTk.CTkLabel(master=profil, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame1 = CTk.CTkFrame(master=profil, width=372, height=600)
    frame1.place(x=15, y=40)

    frame2 = CTk.CTkFrame(master=profil, width=340, height=520, fg_color="#A5BDD2")
    frame2.place(x=30, y=90)

    logo_profil = ImageTk.PhotoImage(Image.open("logoprofil.jpg"))
    image_label = CTk.CTkLabel(master=frame2, image=logo_profil, text="", fg_color="transparent")
    image_label.place(x=135, y=7)

    nama = CTk.CTkLabel(master=frame2, text="Nama Lengkap:")
    nama.place(x=10, y=90)
    frame3 = CTk.CTkFrame(master=frame2, width=320, height=30)
    frame3.place(x=10, y=120)
    global nama2
    nama2 = CTk.CTkLabel(master=frame3, text="")
    nama2.place(x=5, y=2)

    tanggal_lahir = CTk.CTkLabel(master=frame2, text="Tanggal Lahir:")
    tanggal_lahir.place(x=10, y=155)
    frame4 = CTk.CTkFrame(master=frame2, width=320, height=30)
    frame4.place(x=10, y=185)
    global tanggal_lahir2
    tanggal_lahir2 = CTk.CTkLabel(master=frame4, text="")
    tanggal_lahir2.place(x=5, y=2)

    jenis_kelamin = CTk.CTkLabel(master=frame2, text="Jenis Kelamin:")
    jenis_kelamin.place(x=10, y=220)
    frame5 = CTk.CTkFrame(master=frame2, width=320, height=30)
    frame5.place(x=10, y=250)
    global jenis_kelamin2
    jenis_kelamin2 = CTk.CTkLabel(master=frame5, text="")
    jenis_kelamin2.place(x=5,y=2)

    nomor_hp = CTk.CTkLabel(master=frame2, text="Nomor HP:")
    nomor_hp.place(x=10, y=285)
    frame6 = CTk.CTkFrame(master=frame2, width=320, height=30)
    frame6.place(x=10, y=315)
    global nomor_hp2
    nomor_hp2 = CTk.CTkLabel(master=frame6, text="")
    nomor_hp2.place(x=5,y=2)

    nik = CTk.CTkLabel(master=frame2, text="NIK:")
    nik.place(x=10, y=345)
    frame7 = CTk.CTkFrame(master=frame2, width=320, height=30)
    frame7.place(x=10, y=375)
    global nik2
    nik2 = CTk.CTkLabel(master=frame7, text="")
    nik2.place(x=5,y=2)

    penyakit = CTk.CTkLabel(master=frame2, text="Riwayat Penyakit:")
    penyakit.place(x=10, y=410)
    frame8 = CTk.CTkFrame(master=frame2, width=320, height=30)
    frame8.place(x=10, y=440)
    global penyakit2
    penyakit2 = CTk.CTkLabel(master=frame8, text="")
    penyakit2.place(x=5,y=2)

    display_user_profile(user_saat_ini)

    frame_profil4 = CTk.CTkFrame(master=profil, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_profil4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=profil, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=profil.destroy)
    button_back.place(x=0,y=0)

#<=======================================================Batas Profil==================================================>

def poli_gigi_jhonson():
    johnson_window = CTk.CTkToplevel(app)
    johnson_window.geometry("400x680+100+15")
    johnson_window.title("Poli Gigi Johnson") 
    johnson_window.resizable(False, False)
    johnson_window.grab_set()

    background = CTk.CTkLabel(master=johnson_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_jhonson1 = CTk.CTkFrame(master=johnson_window, width=372, height=600, corner_radius=0)
    frame_jhonson1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_jhonson2 = CTk.CTkFrame(master=johnson_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_jhonson2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_jhonson1 = ImageTk.PhotoImage(Image.open("drg.Johnson, Sp.Ort.png"))
    image_label_jhonson = CTk.CTkLabel(master=johnson_window, image=img_jhonson1, text="", fg_color="transparent")
    image_label_jhonson.place(x=24, y=63)

    label_jhonson1 = CTk.CTkLabel(master=frame_jhonson2, text="drg. Johnson, Sp.Ort", font=("Century Gothic", 13))
    label_jhonson1.place(x=85, y=5)

    label_jhonson2 = CTk.CTkLabel(master=frame_jhonson2, text="Spesialis Ortodonti", font=("Century Gothic", 10))
    label_jhonson2.place(x=85, y=27)

    frame_jhonson3 = CTk.CTkFrame(master=johnson_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_jhonson3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_jhonson = CTk.CTkLabel(master=frame_jhonson3, text="Biodata drg.Johnson", font=("Century Gothic", 13))
    label_biodata_jhonson.place(x=10, y=10)

    label_jhonson3 = CTk.CTkLabel(master=frame_jhonson3, text="Dokter Gigi, Universitas Indonesia, 2008\nSpesialis Ortodonti, Universitas Gadjah Mada, 2013\nMenjadi dokter spesialis ortodonti selama 6 tahun", font=("Century Gothic", 13), justify="left")
    label_jhonson3.place(x=10, y=35)

    def save_jadwal_and_transfer_Jhonson(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_gigi2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_gigi2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan berhasil")
        johnson_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_jhonson(selected_time):
        try:
            with open("poli_gigi2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry.get("jadwal yang terpilih") == selected_time)

        return count

    selected_jadwal_johnson = tkinter.StringVar()

    jadwal_Johnson1 = "Senin, 07:00 - 13:00"
    jadwal_Johnson2 = "Rabu, 15:00 - 21:00"

    label_jadwal_jhonson = CTk.CTkLabel(master=frame_jhonson1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_jhonson.place(x=150, y=300)

    jadwal_jhonson1 = CTk.CTkRadioButton(master=frame_jhonson1, text=jadwal_Johnson1, variable=selected_jadwal_johnson, value=jadwal_Johnson1)
    jadwal_jhonson1.place(x=10, y=350)

    jadwal_jhonson2 = CTk.CTkRadioButton(master=frame_jhonson1, text=jadwal_Johnson2, variable=selected_jadwal_johnson, value=jadwal_Johnson2)
    jadwal_jhonson2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_jhonson1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Jhonson(selected_jadwal_johnson.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Jhonson(jadwal_button, selected_time):
        current_booking_count = get_jadwal_jhonson(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Jhonson(selected_jadwal):

        selected_time = selected_jadwal_johnson.get()

        current_booking_count = get_jadwal_jhonson(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=johnson_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_jhonson4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_jhonson4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_jhonson = CTk.CTkLabel(master=frame_jhonson4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_jhonson.place(x=10, y=10)
        
        label_payment_jhonson = CTk.CTkLabel(master=frame_jhonson4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_jhonson.place(x=10, y=50)

        label_antrian_jhonson = CTk.CTkLabel(master=frame_jhonson4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_jhonson.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_jhonson(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                command=lambda: [save_jadwal_and_transfer_Jhonson("drg. Johnson, Sp.Ort", selected_jadwal, current_booking_number,
                                                            selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)
                                        

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Jhonson(jadwal_jhonson1, jadwal_Johnson1)
    check_and_disable_jadwal_Jhonson(jadwal_jhonson2, jadwal_Johnson2)

    frame_Johnson4 = CTk.CTkFrame(master=johnson_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Johnson4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=johnson_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=johnson_window.destroy)
    button_back.place(x=0,y=0)

def poli_gigi_Alicia():
    Alicia_window = CTk.CTkToplevel(app)
    Alicia_window.geometry("400x680+100+15")
    Alicia_window.title("Poli Gigi Alicia")
    Alicia_window.resizable(False, False)
    Alicia_window.grab_set()

    background = CTk.CTkLabel(master=Alicia_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_alicia1 = CTk.CTkFrame(master=Alicia_window, width=372, height=600, corner_radius=0)
    frame_alicia1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_alicia2 = CTk.CTkFrame(master=Alicia_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_alicia2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_alicia1 = ImageTk.PhotoImage(Image.open("drg.Alicia, Sp.Pros.png"))
    image_label_alicia = CTk.CTkLabel(master=Alicia_window, image=img_alicia1, text="", fg_color="transparent")
    image_label_alicia.place(x=24, y=63)

    label_alicia1 = CTk.CTkLabel(master=frame_alicia2, text="drg.Alicia, Sp.Pros", font=("Century Gothic", 13))
    label_alicia1.place(x=85, y=5)

    label_alicia2 = CTk.CTkLabel(master=frame_alicia2, text="Spesialis Prostodonsia", font=("Century Gothic", 10))
    label_alicia2.place(x=85, y=27)

    frame_alicia3 = CTk.CTkFrame(master=Alicia_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_alicia3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata = CTk.CTkLabel(master=frame_alicia3, text="Biodata drg.Alicia", font=("Century Gothic", 13))
    label_biodata.place(x=10, y=10)

    label_alicia3 = CTk.CTkLabel(master=frame_alicia3, text="Dokter Gigi, Universitas Brawijaya, 2006\nSpesialis Prostodonsia, Universitas Hasanuddin, 2012\nMenjadi Dokter Spesialis Prostodonsia selama 5 tahun", font=("Century Gothic", 13), justify="left")
    label_alicia3.place(x=10, y=35)

    def save_jadwal_and_transfer_Alicia(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_gigi2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)

        with open("poli_gigi2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan berhasil")
        Alicia_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Alicia(selected_time):
        try:
            with open("poli_gigi2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count 

    selected_jadwal_alicia = tkinter.StringVar()

    jadwal_Alicia1 = "Selasa, 07:00 - 13:00"
    jadwal_Alicia2 = "Kamis, 15:00 - 21:00"

    label_jadwal_alicia = CTk.CTkLabel(master=frame_alicia1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_alicia.place(x=150, y=300)

    jadwal_alicia1 = CTk.CTkRadioButton(master=frame_alicia1, text=jadwal_Alicia1, variable=selected_jadwal_alicia, value=jadwal_Alicia1)
    jadwal_alicia1.place(x=10, y=350)

    jadwal_alicia2 = CTk.CTkRadioButton(master=frame_alicia1, text=jadwal_Alicia2, variable=selected_jadwal_alicia, value=jadwal_Alicia2)
    jadwal_alicia2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_alicia1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Alicia(selected_jadwal_alicia.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Alicia(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Alicia(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Alicia(selected_jadwal):
        selected_time = selected_jadwal_alicia.get()

        current_booking_count = get_jadwal_Alicia(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Alicia_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_alicia4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_alicia4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_alicia = CTk.CTkLabel(master=frame_alicia4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_alicia.place(x=10, y=10)
        
        label_payment_alicia = CTk.CTkLabel(master=frame_alicia4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_alicia.place(x=10, y=50)

        label_antrian_alicia = CTk.CTkLabel(master=frame_alicia4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_alicia.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        
        current_booking_number = get_jadwal_Alicia(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Alicia("drg.Alicia, Sp.Pros", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Alicia(jadwal_alicia1, jadwal_Alicia1)
    check_and_disable_jadwal_Alicia(jadwal_alicia2, jadwal_Alicia2)

    frame_Alicia4 = CTk.CTkFrame(master=Alicia_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Alicia4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Alicia_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Alicia_window.destroy)
    button_back.place(x=0,y=0)

def poli_gigi_Maria():
    maria_window = CTk.CTkToplevel(app)
    maria_window.geometry("400x680+100+15")
    maria_window.title("Poli Gigi Maria")
    maria_window.resizable(False, False)
    maria_window.grab_set()

    background = CTk.CTkLabel(master=maria_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_maria1 = CTk.CTkFrame(master=maria_window, width=372, height=600, corner_radius=0)
    frame_maria1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_maria2 = CTk.CTkFrame(master=maria_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_maria2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_maria1 = ImageTk.PhotoImage(Image.open("drg.Maria.jpg"))
    image_label_maria = CTk.CTkLabel(master=maria_window, image=img_maria1, text="", fg_color="transparent")
    image_label_maria.place(x=24, y=63)

    label_maria1 = CTk.CTkLabel(master=frame_maria2, text="drg. Maria Andini, Sp.Ort", font=("Century Gothic", 13))
    label_maria1.place(x=85, y=5)

    label_maria2 = CTk.CTkLabel(master=frame_maria2, text="Spesialis Ortodonti", font=("Century Gothic", 10))
    label_maria2.place(x=85, y=27)

    frame_maria3 = CTk.CTkFrame(master=maria_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_maria3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_maria = CTk.CTkLabel(master=frame_maria3, text="Biodata drg.Maria Andini", font=("Century Gothic", 13))
    label_biodata_maria.place(x=10, y=10)

    label_maria3 = CTk.CTkLabel(master=frame_maria3, text="Dokter Gigi, Universitas Indonesia, 2006\nSpesialis Ortodonti, Universitas Gadjah Mada, 2013\nDokter Spesialis Ortodonti selama 7 tahun", font=("Century Gothic", 13), justify="left")
    label_maria3.place(x=10, y=35)

    def save_jadwal_and_transfer_Maria(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }

        try:
            with open("poli_gigi2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_gigi2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan Berhasil")
        maria_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Maria(selected_time):
        try:
            with open("poli_gigi2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_maria = tkinter.StringVar()

    jadwal_Maria1 = "Selasa, 15:00 - 21:00"
    jadwal_Maria2 = "Jumat, 07:00 - 13:00"
    
    label_jadwal_maria1 = CTk.CTkLabel(master=frame_maria1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_maria1.place(x=150, y=300)

    jadwal_maria1 = CTk.CTkRadioButton(master=frame_maria1, text=jadwal_Maria1, variable=selected_jadwal_maria, value=jadwal_Maria1)
    jadwal_maria1.place(x=10, y=350)

    jadwal_maria2 = CTk.CTkRadioButton(master=frame_maria1, text=jadwal_Maria2, variable=selected_jadwal_maria, value=jadwal_Maria2)
    jadwal_maria2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_maria1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Maria(selected_jadwal_maria.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Maria(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Maria(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Maria(selected_jadwal):
        selected_time = selected_jadwal_maria.get()

        current_booking_count = get_jadwal_Maria(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=maria_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_maria4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_maria4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_maria = CTk.CTkLabel(master=frame_maria4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_maria.place(x=10, y=10)
        
        label_payment_maria = CTk.CTkLabel(master=frame_maria4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_maria.place(x=10, y=50)

        label_antrian_maria = CTk.CTkLabel(master=frame_maria4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_maria.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Maria(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Maria("drg. Maria Andini, Sp.Ort", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Maria(jadwal_maria1, jadwal_Maria1)
    check_and_disable_jadwal_Maria(jadwal_maria2, jadwal_Maria2)

    frame_Maria4 = CTk.CTkFrame(master=maria_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Maria4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=maria_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=maria_window.destroy)
    button_back.place(x=0,y=0)

def poli_gigi_Budi():
    budi_window = CTk.CTkToplevel(app)
    budi_window.geometry("400x680+100+15")
    budi_window.title("Poli Gigi Budi")
    budi_window.resizable(False, False)
    budi_window.grab_set()

    background = CTk.CTkLabel(master=budi_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_budi1 = CTk.CTkFrame(master=budi_window, width=372, height=600, corner_radius=0)
    frame_budi1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_budi2 = CTk.CTkFrame(master=budi_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_budi2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_budi1 = ImageTk.PhotoImage(Image.open("drg.Budi.jpg"))
    image_label = CTk.CTkLabel(master=budi_window, image=img_budi1, text="", fg_color="transparent")
    image_label.place(x=24, y=63)

    label_budi1 = CTk.CTkLabel(master=frame_budi2, text="drg. Budi Santoso, Sp.KGA", font=("Century Gothic", 13))
    label_budi1.place(x=85, y=5)

    label_budi2 = CTk.CTkLabel(master=frame_budi2, text="Spesialis Kedokteran Gigi Anak", font=("Century Gothic", 10))
    label_budi2.place(x=85, y=27)

    frame_budi3 = CTk.CTkFrame(master=budi_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_budi3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_budi = CTk.CTkLabel(master=frame_budi3, text="Biodata drg.Budi Santoso", font=("Century Gothic", 13))
    label_biodata_budi.place(x=10, y=10)

    label_budi3 = CTk.CTkLabel(master=frame_budi3, text="Dokter Gigi, Universitas Brawijaya, 2008\nSpesialis Kedokteran Gigi Anak, Universitas Airlangga, 2015\nDokter Spesialis Kedokteran Gigi Anak selama 9 tahun", font=("Century Gothic", 11), justify="left")
    label_budi3.place(x=10, y=35)

    def save_jadwal_and_transfer_Budi(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_gigi2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)

        with open("poli_gigi2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan Berhasil")
        budi_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Budi(selected_time):
        try:
            with open("poli_gigi2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_budi = tkinter.StringVar()

    jadwal_Budi1 = "Rabu, 07:00 - 13:00"
    jadwal_Budi2 = "Jumat, 15:00 - 21:00"
    
    label_jadwal_budi = CTk.CTkLabel(master=frame_budi1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_budi.place(x=150, y=300)

    jadwal1 = CTk.CTkRadioButton(master=frame_budi1, text=jadwal_Budi1, variable=selected_jadwal_budi, value=jadwal_Budi1)
    jadwal1.place(x=10, y=350)

    jadwal2 = CTk.CTkRadioButton(master=frame_budi1, text=jadwal_Budi2, variable=selected_jadwal_budi, value=jadwal_Budi2)
    jadwal2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_budi1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Budi(selected_jadwal_budi.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Budi(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Budi(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Budi(selected_jadwal):
        selected_time = selected_jadwal_budi.get()

        current_booking_count = get_jadwal_Budi(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=budi_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_budi4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_budi4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_budi = CTk.CTkLabel(master=frame_budi4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_budi.place(x=10, y=10)
        
        label_payment_budi = CTk.CTkLabel(master=frame_budi4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_budi.place(x=10, y=50)

        label_antrian_budi = CTk.CTkLabel(master=frame_budi4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_budi.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Budi(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Budi("drg. Budi Santoso, Sp.KGA", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Budi(jadwal1, jadwal_Budi1)
    check_and_disable_jadwal_Budi(jadwal2, jadwal_Budi2)

    frame_Budi4 = CTk.CTkFrame(master=budi_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Budi4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=budi_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=budi_window.destroy)
    button_back.place(x=0,y=0)

def poli_gigi_Alex():
    alex_window = CTk.CTkToplevel(app)
    alex_window.geometry("400x680+100+15")
    alex_window.title("Poli Gigi Alex")
    alex_window.resizable(False, False)
    alex_window.grab_set()

    background = CTk.CTkLabel(master=alex_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_alex1 = CTk.CTkFrame(master=alex_window, width=372, height=600, corner_radius=0)
    frame_alex1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_alex2 = CTk.CTkFrame(master=alex_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_alex2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_alex1 = ImageTk.PhotoImage(Image.open("drg.Alex, Sp.Perio.png"))
    image_label_alex = CTk.CTkLabel(master=alex_window, image=img_alex1, text="", fg_color="transparent")
    image_label_alex.place(x=24, y=63)

    label_alex1 = CTk.CTkLabel(master=frame_alex2, text="drg. Alex, Sp.Perio", font=("Century Gothic", 13))
    label_alex1.place(x=85, y=5)

    label_alex2 = CTk.CTkLabel(master=frame_alex2, text="Spesialis Periodontik", font=("Century Gothic", 10))
    label_alex2.place(x=85, y=27)

    frame_alex3 = CTk.CTkFrame(master=alex_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_alex3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_alex = CTk.CTkLabel(master=frame_alex3, text="Biodata drg.Alex", font=("Century Gothic", 13))
    label_biodata_alex.place(x=10, y=10)

    label_alex3 = CTk.CTkLabel(master=frame_alex3, text="Dokter Gigi, Universitas Padjadjaran, 2004\nSpesialis Periodontik, Universitas Airlangga, 2011\nMenjadi Dokter Spesialis Periodontik selama 6 tahun", font=("Century Gothic", 13), justify="left")
    label_alex3.place(x=10, y=35)

    def save_jadwal_and_transfer_Alex(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }

        try:
            with open("poli_gigi2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_gigi2.json", "w") as file:
            json.dump(booking_data, file, indent=4)

        messagebox.showinfo("Success","Pemesanan Berhasil")
        alex_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)
    
    def get_jadwal_Alex(selected_time):
        try:
            with open("poli_gigi2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_alex = tkinter.StringVar()

    jadwal_Alex1 = "Senin, 15:00 - 21:00"
    jadwal_Alex2 = "Kamis, 07:00 - 13:00"
    
    label1_jadwal = CTk.CTkLabel(master=frame_alex1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label1_jadwal.place(x=150, y=300)

    jadwal_alex1 = CTk.CTkRadioButton(master=frame_alex1, text=jadwal_Alex1, variable=selected_jadwal_alex, value=jadwal_Alex1)
    jadwal_alex1.place(x=10, y=350)

    jadwal_alex2 = CTk.CTkRadioButton(master=frame_alex1, text=jadwal_Alex2, variable=selected_jadwal_alex, value=jadwal_Alex2)
    jadwal_alex2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_alex1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Alex(selected_jadwal_alex.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Alex(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Alex(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Alex(selected_jadwal):
        selected_time = selected_jadwal_alex.get()

        current_booking_count = get_jadwal_Alex(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=alex_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_alex4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_alex4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Alex = CTk.CTkLabel(master=frame_alex4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Alex.place(x=10, y=10)
        
        label_payment_Alex = CTk.CTkLabel(master=frame_alex4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Alex.place(x=10, y=50)

        label_antrian_Alex = CTk.CTkLabel(master=frame_alex4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Alex.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Alex(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                command=lambda: [save_jadwal_and_transfer_Alex("drg. Alex, Sp. Perio", selected_jadwal, current_booking_number,
                                                            selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Alex(jadwal_alex1, jadwal_Alex1)
    check_and_disable_jadwal_Alex(jadwal_alex2, jadwal_Alex2)

    frame_Alex4 = CTk.CTkFrame(master=alex_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Alex4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=alex_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=alex_window.destroy)
    button_back.place(x=0,y=0)

def poli_gigi():
    poli_gigi_window = CTk.CTkToplevel(app)
    poli_gigi_window.geometry("400x680+100+15")
    poli_gigi_window.title("Poli Gigi")
    poli_gigi_window.resizable("false","false")
    poli_gigi_window.grab_set() 

    background = CTk.CTkLabel(master=poli_gigi_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame1 = CTk.CTkFrame(master=poli_gigi_window, width=352, height=80, corner_radius=0)
    frame1.place(x=24,y=48)

    img1 = ImageTk.PhotoImage(Image.open("drg.Johnson, Sp.Ort.png"))
    image_label = CTk.CTkLabel(master=poli_gigi_window, image=img1, text="", fg_color="transparent")
    image_label.place(x=24, y=48)

    label1 = CTk.CTkLabel(master=frame1, text="drg. Johnson, Sp.Ort", font=("Century Gothic", 13))
    label1.place(x=85, y=5)

    label2 = CTk.CTkLabel(master=frame1, text="Spesialis Ortodonti", font=("Century Gothic", 10))
    label2.place(x=85, y=27)

    button1 = CTk.CTkButton(master=frame1, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_gigi_jhonson)
    button1.place(x=80, y=50)

    frame2 = CTk.CTkFrame(master=poli_gigi_window, width=352, height=80, corner_radius=0)
    frame2.place(x=24,y=165)

    img3 = ImageTk.PhotoImage(Image.open("drg.Alex, Sp.Perio.png"))
    image_label = CTk.CTkLabel(master=poli_gigi_window, image=img3, text="", fg_color="transparent")
    image_label.place(x=295, y=165)

    label3 = CTk.CTkLabel(master=frame2, text="drg. Alex, Sp.Perio", font=("Century Gothic", 13))
    label3.place(x=10, y=5)

    label4 = CTk.CTkLabel(master=frame2, text="Spesialis Periodontik", font=("Century Gothic", 10))
    label4.place(x=10, y=27)

    button2 = CTk.CTkButton(master=frame2, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_gigi_Alex)
    button2.place(x=10, y=50)

    frame3 = CTk.CTkFrame(master=poli_gigi_window, width=352, height=80, corner_radius=0)
    frame3.place(x=24,y=280)

    img5 = ImageTk.PhotoImage(Image.open("drg.Alicia, Sp.Pros.png"))
    image_label = CTk.CTkLabel(master=poli_gigi_window, image=img5, text="", fg_color="transparent")
    image_label.place(x=24, y=280)

    label5 = CTk.CTkLabel(master=frame3, text="drg. Alicia, Sp.Pros", font=("Century Gothic", 13))
    label5.place(x=85, y=5)

    label6 = CTk.CTkLabel(master=frame3, text="Spesialis Prostodonsia", font=("Century Gothic", 10))
    label6.place(x=85, y=27)

    button3 = CTk.CTkButton(master=frame3, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_gigi_Alicia)
    button3.place(x=80, y=50)

    frame4 = CTk.CTkFrame(master=poli_gigi_window, width=352, height=80, corner_radius=0)
    frame4.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER)

    frame5 = CTk.CTkFrame(master=poli_gigi_window, width=352, height=80, corner_radius=0)
    frame5.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    img6 = ImageTk.PhotoImage(Image.open("drg.Maria.jpg"))
    image_label = CTk.CTkLabel(master=poli_gigi_window, image=img6, text="", fg_color="transparent")
    image_label.place(x=296, y=388)

    label7 = CTk.CTkLabel(master=frame4, text="drg.Maria Andini, Sp.Ort", font=("Century Gothic", 13))
    label7.place(x=10, y=5)

    label8 = CTk.CTkLabel(master=frame4, text="Spesialis Ortodonti", font=("Century Gothic", 10))
    label8.place(x=10, y=27)

    button4 = CTk.CTkButton(master=frame4, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_gigi_Maria)
    button4.place(x=10, y=50)

    img7 = ImageTk.PhotoImage(Image.open("drg.Budi.jpg"))
    image_label = CTk.CTkLabel(master=poli_gigi_window, image=img7, text="", fg_color="transparent")
    image_label.place(x=24, y=504)

    label9 = CTk.CTkLabel(master=frame5, text="drg.Budi Santoso, Sp.KGA", font=("Century Gothic", 13))
    label9.place(x=85, y=5)

    label10 = CTk.CTkLabel(master=frame5, text="Spesialis Kedokteran Gigi Anak", font=("Century Gothic", 10))
    label10.place(x=85, y=27)

    button5 = CTk.CTkButton(master=frame5, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_gigi_Budi)
    button5.place(x=80, y=50)

    frame_poli_gigi4 = CTk.CTkFrame(master=poli_gigi_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_poli_gigi4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=poli_gigi_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=poli_gigi_window.destroy)
    button_back.place(x=0,y=0)

#<=======================================================Batas Poli Gigi============================================================>

def poli_mata_Variesa():
    variesa_window = CTk.CTkToplevel(app)
    variesa_window.geometry("400x680+100+15")
    variesa_window.title("Poli Mata Variesa")
    variesa_window.resizable(False, False)
    variesa_window.grab_set()

    background = CTk.CTkLabel(master=variesa_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_variesa1 = CTk.CTkFrame(master=variesa_window, width=372, height=600, corner_radius=0)
    frame_variesa1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_variesa2 = CTk.CTkFrame(master=variesa_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_variesa2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_variesa1 = ImageTk.PhotoImage(Image.open("dr. variesa.png"))
    image_label_variesa = CTk.CTkLabel(master=variesa_window, image=img_variesa1, text="", fg_color="transparent")
    image_label_variesa  .place(x=24, y=63)

    label_variesa1 = CTk.CTkLabel(master=frame_variesa2, text="dr.Variesa Sabita, Sp.M", font=("Century Gothic", 13))
    label_variesa1.place(x=85, y=5)

    label_variesa2 = CTk.CTkLabel(master=frame_variesa2, text="Spesialis Mata", font=("Century Gothic", 10))
    label_variesa2.place(x=85, y=27)

    frame_variesa3 = CTk.CTkFrame(master=variesa_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_variesa3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_variesa = CTk.CTkLabel(master=frame_variesa3, text="Biodata dr. Variesa", font=("Century Gothic", 13))
    label_biodata_variesa.place(x=10, y=10)

    label_variesa3 = CTk.CTkLabel(master=frame_variesa3, text="Dokter Umum, Fakultas Kedokteran Universitas Indonesia, 2007\nSpesialis Mata, Universitas Hasanuddin, 2013\nDokter Spesialis Mata di RS Cicendo Bandung selama 5 tahun", font=("Century Gothic", 11), justify="left")
    label_variesa3.place(x=5, y=35)

    def save_jadwal_and_transfer_Variesa(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_mata2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)

        with open("poli_mata2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan Berhasil")
        variesa_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Variesa(selected_time):
        try:
            with open("poli_mata2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry.get("jadwal yang terpilih") == selected_time)

        return count

    selected_jadwal_variesa = tkinter.StringVar()

    jadwal_Variesa1 = "Senin, 07:00 - 13:00"
    jadwal_Variesa2 = "Rabu, 15:00 - 21:00"
    
    label_jadwal_variesa1 = CTk.CTkLabel(master=frame_variesa1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_variesa1.place(x=150, y=300)

    jadwal_variesa1 = CTk.CTkRadioButton(master=frame_variesa1, text=jadwal_Variesa1, variable=selected_jadwal_variesa, value=jadwal_Variesa1)
    jadwal_variesa1.place(x=10, y=350)

    jadwal_variesa2 = CTk.CTkRadioButton(master=frame_variesa1, text=jadwal_Variesa2, variable=selected_jadwal_variesa, value=jadwal_Variesa2)
    jadwal_variesa2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_variesa1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Variesa(selected_jadwal_variesa.get()))
    button_payment.place(x=100, y=480)


    def check_and_disable_jadwal_Variesa(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Variesa(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Variesa(selected_jadwal):
        selected_time = selected_jadwal_variesa.get()

        current_booking_count = get_jadwal_Variesa(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=variesa_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_variesa4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_variesa4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_variesa = CTk.CTkLabel(master=frame_variesa4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_variesa.place(x=10, y=10)
        
        label_payment_variesa = CTk.CTkLabel(master=frame_variesa4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_variesa.place(x=10, y=50)

        label_antrian_variesa = CTk.CTkLabel(master=frame_variesa4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_variesa.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        current_booking_number = get_jadwal_Variesa(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Variesa("dr. Variesa Sabita, Sp.M", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path


    check_and_disable_jadwal_Variesa(jadwal_variesa1, jadwal_Variesa1)
    check_and_disable_jadwal_Variesa(jadwal_variesa2, jadwal_Variesa2)

    frame_Variesa4 = CTk.CTkFrame(master=variesa_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Variesa4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=variesa_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=variesa_window.destroy)
    button_back.place(x=0,y=0)

def poli_mata_Rizky():
    rizky_window = CTk.CTkToplevel(app)
    rizky_window.geometry("400x680+100+15")
    rizky_window.title("Poli Mata Rizky")
    rizky_window.resizable(False, False)
    rizky_window.grab_set()

    background = CTk.CTkLabel(master=rizky_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_rizky1 = CTk.CTkFrame(master=rizky_window, width=372, height=600, corner_radius=0)
    frame_rizky1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_rizky2 = CTk.CTkFrame(master=rizky_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_rizky2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_rizky1 = ImageTk.PhotoImage(Image.open("dr.Rizky.jpg"))
    image_label_rizky = CTk.CTkLabel(master=rizky_window, image=img_rizky1, text="", fg_color="transparent")
    image_label_rizky.place(x=24, y=63)

    label_rizky1 = CTk.CTkLabel(master=frame_rizky2, text="dr.Rizky Pratama Sp.M", font=("Century Gothic", 13))
    label_rizky1.place(x=85, y=5)

    label_rizky2 = CTk.CTkLabel(master=frame_rizky2, text="Spesialis Mata", font=("Century Gothic", 10))
    label_rizky2.place(x=85, y=27)

    frame_rizky3 = CTk.CTkFrame(master=rizky_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_rizky3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_rizky = CTk.CTkLabel(master=frame_rizky3, text="Biodata dr. Rizky Pratama", font=("Century Gothic", 13))
    label_biodata_rizky.place(x=10, y=10)

    label_rizky3 = CTk.CTkLabel(master=frame_rizky3, text="Dokter Umum, Fakultas Kedokteran Universitas Gadjah Mada, 2009\nSpesialis Mata, Universitas Hasanuddin, 2015\nDokter Spesialis Mata selama 6 tahun", font=("Century Gothic", 10), justify="left")
    label_rizky3.place(x=5, y=35)

    def save_jadwal_and_transfer_Rizky(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_mata2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)

        with open("poli_mata2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan berhasil")
        rizky_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Rizky(selected_time):
        try:
            with open("poli_mata2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry.get("jadwal yang terpilih") == selected_time)

        return count

    selected_jadwal_rizky = tkinter.StringVar()

    jadwal_Rizky1 = "Rabu, 07:00 - 13:00"
    jadwal_Rizky2 = "Jumat, 15:00 - 21:00"
    
    label_jadwal_rizky = CTk.CTkLabel(master=frame_rizky1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_rizky.place(x=150, y=300)

    jadwal_rizky1 = CTk.CTkRadioButton(master=frame_rizky1, text=jadwal_Rizky1, variable=selected_jadwal_rizky, value=jadwal_Rizky1)
    jadwal_rizky1.place(x=10, y=350)

    jadwal_rizky2 = CTk.CTkRadioButton(master=frame_rizky1, text=jadwal_Rizky2, variable=selected_jadwal_rizky, value=jadwal_Rizky2)
    jadwal_rizky2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_rizky1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Rizky(selected_jadwal_rizky.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Rizky(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Rizky(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Rizky(selected_jadwal):
        selected_time = selected_jadwal_rizky.get()

        current_booking_count = get_jadwal_Rizky(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=rizky_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_rizky4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_rizky4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_rizky = CTk.CTkLabel(master=frame_rizky4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_rizky.place(x=10, y=10)
        
        label_payment_rizky = CTk.CTkLabel(master=frame_rizky4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_rizky.place(x=10, y=50)

        label_antrian_rizky = CTk.CTkLabel(master=frame_rizky4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_rizky.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        
        current_booking_number = get_jadwal_Rizky(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Rizky("dr.Rizky Pratama Sp.M", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path


    check_and_disable_jadwal_Rizky(jadwal_rizky1, jadwal_Rizky1)
    check_and_disable_jadwal_Rizky(jadwal_rizky2, jadwal_Rizky2)

    frame_Rizky4 = CTk.CTkFrame(master=rizky_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Rizky4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=rizky_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=rizky_window.destroy)
    button_back.place(x=0,y=0)

def poli_mata_Dewanggi():
    dewanggi_window = CTk.CTkToplevel(app)
    dewanggi_window.geometry("400x680+100+15")
    dewanggi_window.title("Poli Mata Dewanggi")
    dewanggi_window.resizable(False, False)
    dewanggi_window.grab_set()

    background = CTk.CTkLabel(master=dewanggi_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_dewanggi1 = CTk.CTkFrame(master=dewanggi_window, width=372, height=600, corner_radius=0)
    frame_dewanggi1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_dewanggi2 = CTk.CTkFrame(master=dewanggi_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_dewanggi2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_dewanggi1 = ImageTk.PhotoImage(Image.open("dr dewanggie.png"))
    image_label_dewanggi = CTk.CTkLabel(master=dewanggi_window, image=img_dewanggi1, text="", fg_color="transparent")
    image_label_dewanggi.place(x=24, y=63)

    label_dewanggi1 = CTk.CTkLabel(master=frame_dewanggi2, text="dr. Dewanggi, SP.M", font=("Century Gothic", 13))
    label_dewanggi1.place(x=85, y=5)

    label_dewanggi2 = CTk.CTkLabel(master=frame_dewanggi2, text="Spesialis Mata", font=("Century Gothic", 10))
    label_dewanggi2.place(x=85, y=27)

    frame_dewanggi3 = CTk.CTkFrame(master=dewanggi_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_dewanggi3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_dewanggi = CTk.CTkLabel(master=frame_dewanggi3, text="Biodata dr.Dewanggi", font=("Century Gothic", 13))
    label_biodata_dewanggi.place(x=10, y=10)

    label = CTk.CTkLabel(master=frame_dewanggi3, text="Dokter Umum, Universitas Gadjah Mada, 2006\nSpesialis Mata, Universitas Airlangga, 2013\nDokter Spesialis Mata selama 6 tahun", font=("Century Gothic", 13), justify="left")
    label.place(x=10, y=35)

    def save_jadwal_and_transfer_Dewanggi(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_mata2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_mata2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan Berhasil")
        dewanggi_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Dewanggi(selected_time):
        try:
            with open("poli_mata2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry.get("jadwal yang terpilih") == selected_time)

        return count

    selected_jadwal_Dewanggi = tkinter.StringVar()

    jadwal_Dewanggi1 = "Senin, 15:00 - 21:00"
    jadwal_Dewanggi2 = "Kamis, 07:00 - 13:00"
    
    label1_jadwal = CTk.CTkLabel(master=frame_dewanggi1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label1_jadwal.place(x=150, y=300)

    jadwal1 = CTk.CTkRadioButton(master=frame_dewanggi1, text=jadwal_Dewanggi1, variable=selected_jadwal_Dewanggi, value=jadwal_Dewanggi1)
    jadwal1.place(x=10, y=350)

    jadwal2 = CTk.CTkRadioButton(master=frame_dewanggi1, text=jadwal_Dewanggi2, variable=selected_jadwal_Dewanggi, value=jadwal_Dewanggi2)
    jadwal2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_dewanggi1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Dewanggi(selected_jadwal_Dewanggi.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Dewanggi(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Dewanggi(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Dewanggi(selected_jadwal):
        selected_time = selected_jadwal_Dewanggi.get()

        current_booking_count = get_jadwal_Dewanggi(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=dewanggi_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Dewanggi4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Dewanggi4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Dewanggi = CTk.CTkLabel(master=frame_Dewanggi4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Dewanggi.place(x=10, y=10)
        
        label_payment_Dewanggi = CTk.CTkLabel(master=frame_Dewanggi4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Dewanggi.place(x=10, y=50)

        label_antrian_Dewanggi = CTk.CTkLabel(master=frame_Dewanggi4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Dewanggi.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)


        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        current_booking_number = get_jadwal_Dewanggi(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Dewanggi("dr. Dewanggi, SP.M", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Dewanggi(jadwal1, jadwal_Dewanggi1)
    check_and_disable_jadwal_Dewanggi(jadwal2, jadwal_Dewanggi2)

    frame_Dewanggi4 = CTk.CTkFrame(master=dewanggi_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Dewanggi4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=dewanggi_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=dewanggi_window.destroy)
    button_back.place(x=0,y=0)

def poli_mata_Celine():
    celine_window = CTk.CTkToplevel(app)
    celine_window.geometry("400x680+100+15")
    celine_window.title("Poli Mata Celine")
    celine_window.resizable(False, False)
    celine_window.grab_set()

    background = CTk.CTkLabel(master=celine_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_celine1 = CTk.CTkFrame(master=celine_window, width=372, height=600, corner_radius=0)
    frame_celine1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_celine2 = CTk.CTkFrame(master=celine_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_celine2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_celine1 = ImageTk.PhotoImage(Image.open("dr. celine.png"))
    image_label_celine = CTk.CTkLabel(master=celine_window, image=img_celine1, text="", fg_color="transparent")
    image_label_celine.place(x=24, y=63)

    label_celine1 = CTk.CTkLabel(master=frame_celine2, text="dr.Celine Evangelina, Sp.M", font=("Century Gothic", 13))
    label_celine1.place(x=85, y=5)

    label_celine2 = CTk.CTkLabel(master=frame_celine2, text="Spesialis Mata", font=("Century Gothic", 10))
    label_celine2.place(x=85, y=27)

    frame_celine3 = CTk.CTkFrame(master=celine_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_celine3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata = CTk.CTkLabel(master=frame_celine3, text="Biodata dr. Celine", font=("Century Gothic", 13))
    label_biodata.place(x=10, y=10)

    label_celine = CTk.CTkLabel(master=frame_celine3, text="Dokter Umum, Fakultas Kedokteran Universitas Airlangga, 2008\nSpesialis Mata, Universitas Indonesia, 2014\nDokter Spesialis Mata selama 7 tahun", font=("Century Gothic", 11), justify="left")
    label_celine.place(x=5, y=35)

    def save_jadwal_and_transfer_Celine(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_mata2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_mata2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan Berhasil")
        celine_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Celine(selected_time):
        try:
            with open("poli_mata2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry.get("jadwal yang terpilih") == selected_time)

        return count

    selected_jadwal_celine = tkinter.StringVar()

    jadwal_Celine1 = "Selasa, 07:00 - 13:00"
    jadwal_Celine2 = "Kamis, 15:00 - 21:00"
    
    label1_jadwal_celine = CTk.CTkLabel(master=frame_celine1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label1_jadwal_celine.place(x=150, y=300)

    jadwal_celine1 = CTk.CTkRadioButton(master=frame_celine1, text=jadwal_Celine1, variable=selected_jadwal_celine, value=jadwal_Celine1)
    jadwal_celine1.place(x=10, y=350)

    jadwal_celine2 = CTk.CTkRadioButton(master=frame_celine1, text=jadwal_Celine2, variable=selected_jadwal_celine, value=jadwal_Celine2)
    jadwal_celine2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_celine1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Celine(selected_jadwal_celine.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Celine(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Celine(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Celine(selected_jadwal):
        selected_time = selected_jadwal_celine.get()

        current_booking_count = get_jadwal_Celine(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=celine_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Celine4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Celine4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Celine = CTk.CTkLabel(master=frame_Celine4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Celine.place(x=10, y=10)
        
        label_payment_Celine = CTk.CTkLabel(master=frame_Celine4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Celine.place(x=10, y=50)

        label_antrian_Celine = CTk.CTkLabel(master=frame_Celine4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Celine.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Celine(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Celine("dr.Celine Evangelina, Sp.M", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path


    check_and_disable_jadwal_Celine(jadwal_celine1, jadwal_Celine1)
    check_and_disable_jadwal_Celine(jadwal_celine2, jadwal_Celine2)

    frame_Celine4 = CTk.CTkFrame(master=celine_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Celine4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=celine_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=celine_window.destroy)
    button_back.place(x=0,y=0)

def poli_mata_Ayu():
    ayu_window = CTk.CTkToplevel(app)
    ayu_window.geometry("400x680+100+15")
    ayu_window.title("Poli Mata Ayu")
    ayu_window.resizable(False, False)
    ayu_window.grab_set()

    background = CTk.CTkLabel(master=ayu_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_ayu1 = CTk.CTkFrame(master=ayu_window, width=372, height=600, corner_radius=0)
    frame_ayu1 .place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_ayu2 = CTk.CTkFrame(master=ayu_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_ayu2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_ayu1 = ImageTk.PhotoImage(Image.open("dr.Ayu.jpg"))
    image_label_ayu = CTk.CTkLabel(master=ayu_window, image=img_ayu1, text="", fg_color="transparent")
    image_label_ayu.place(x=24, y=63)

    label_ayu1 = CTk.CTkLabel(master=frame_ayu2, text="dr.Ayu Lestari Sp.M", font=("Century Gothic", 13))
    label_ayu1.place(x=85, y=5)

    label_ayu2 = CTk.CTkLabel(master=frame_ayu2, text="Spesialis Mata", font=("Century Gothic", 10))
    label_ayu2.place(x=85, y=27)

    frame_ayu3 = CTk.CTkFrame(master=ayu_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_ayu3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_ayu = CTk.CTkLabel(master=frame_ayu3, text="Biodata dr. Ayu Lestari", font=("Century Gothic", 13))
    label_biodata_ayu.place(x=10, y=10)

    label_ayu = CTk.CTkLabel(master=frame_ayu3, text="Dokter Umum, Fakultas Kedokteran Universitas Padjadjaran, 2010\nSpesialis Mata, Universitas Airlangga, 2016\nDokter Spesialis Mata selama 5 tahun", font=("Century Gothic", 11), justify="left")
    label_ayu.place(x=5, y=35)

    def save_jadwal_and_transfer_Ayu(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_mata2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_mata2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success", "Pemesanan berhasil")
        ayu_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)
        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Ayu(selected_time):
        try:
            with open("poli_mata2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry.get("jadwal yang terpilih") == selected_time)

        return count

    selected_jadwal_ayu = tkinter.StringVar()

    jadwal_Ayu1 = "Selasa, 15:00 - 21:00"
    jadwal_Ayu2 = "Jumat, 07:00 - 13:00"
    
    label1_jadwal_ayu = CTk.CTkLabel(master=frame_ayu1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label1_jadwal_ayu.place(x=150, y=300)

    jadwal_ayu1 = CTk.CTkRadioButton(master=frame_ayu1, text=jadwal_Ayu1, variable=selected_jadwal_ayu, value=jadwal_Ayu1)
    jadwal_ayu1.place(x=10, y=350)

    jadwal_ayu2 = CTk.CTkRadioButton(master=frame_ayu1, text=jadwal_Ayu2, variable=selected_jadwal_ayu, value=jadwal_Ayu2)
    jadwal_ayu2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_ayu1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Ayu(selected_jadwal_ayu.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Ayu(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Ayu(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Ayu(selected_jadwal):
        selected_time = selected_jadwal_ayu.get()

        current_booking_count = get_jadwal_Ayu(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=ayu_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Ayu4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Ayu4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Ayu = CTk.CTkLabel(master=frame_Ayu4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Ayu.place(x=10, y=10)
        
        label_payment_Ayu = CTk.CTkLabel(master=frame_Ayu4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Ayu.place(x=10, y=50)

        label_antrian_Ayu = CTk.CTkLabel(master=frame_Ayu4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Ayu.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)
        
        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        
        current_booking_number = get_jadwal_Ayu(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Ayu("dr. Ayu lestari Sp.M", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Ayu(jadwal_ayu1, jadwal_Ayu1)
    check_and_disable_jadwal_Ayu(jadwal_ayu2, jadwal_Ayu2)

    frame_Ayu4 = CTk.CTkFrame(master=ayu_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Ayu4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=ayu_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=ayu_window.destroy)
    button_back.place(x=0,y=0)

def poli_mata():
    poli_mata_window = CTk.CTkToplevel(app)
    poli_mata_window.geometry("400x680+100+15")
    poli_mata_window.title("Poli Mata")
    poli_mata_window.resizable("false","false")
    poli_mata_window.grab_set()

    background = CTk.CTkLabel(master=poli_mata_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_PM1 = CTk.CTkFrame(master=poli_mata_window, width=352, height=80, corner_radius=0)
    frame_PM1.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER)
    
    dokter_1_PM = ImageTk.PhotoImage(Image.open("dr. variesa.png"))
    image_label_PM1 = CTk.CTkLabel(master=poli_mata_window, image=dokter_1_PM, text="", fg_color="transparent")
    image_label_PM1.place(x=24, y=48)

    label_PM1 = CTk.CTkLabel(master=frame_PM1, text="dr.Variesa Sabita, Sp.M", font=("Century Gothic", 13))
    label_PM1.place(x=85, y=7)

    label_spm1 = CTk.CTkLabel(master=frame_PM1, text="Spesialis Mata", font=("Century Gothic", 10))
    label_spm1.place(x=85, y=27)

    button_pm1 = CTk.CTkButton(master=frame_PM1, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_mata_Variesa)
    button_pm1.place(x=80, y=50)

    frame_PM2 = CTk.CTkFrame(master=poli_mata_window, width=352, height=80, corner_radius=0)
    frame_PM2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    dokter_2_PM = ImageTk.PhotoImage(Image.open("dr dewanggie.png"))
    image_label_PM2 = CTk.CTkLabel(master=poli_mata_window, image=dokter_2_PM, text="", fg_color="transparent")
    image_label_PM2.place(x=295, y=165)

    label_PM2 = CTk.CTkLabel(master=frame_PM2, text="dr. Dewanggi Erchinta, Sp.M", font=("Century Gothic", 13))
    label_PM2.place(x=10, y=7)

    label_spm2 = CTk.CTkLabel(master=frame_PM2, text="Spesialis Mata", font=("Century Gothic", 10))
    label_spm2.place(x=10, y=27)

    button_pm2 = CTk.CTkButton(master=frame_PM2, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_mata_Dewanggi)
    button_pm2.place(x=10, y=50)

    frame_PM3 = CTk.CTkFrame(master=poli_mata_window, width=352, height=80, corner_radius=0)
    frame_PM3.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)

    dokter_3_PM = ImageTk.PhotoImage(Image.open("dr. celine.png"))
    image_label_PM3 = CTk.CTkLabel(master=poli_mata_window, image=dokter_3_PM, text="", fg_color="white")
    image_label_PM3.place(x=24, y=280)

    label_PM3 = CTk.CTkLabel(master=frame_PM3, text="dr.Celine Evangelina, Sp.M", font=("Century Gothic", 13))
    label_PM3.place(x=85, y=7)

    label_spm3 = CTk.CTkLabel(master=frame_PM3, text="Spesialis Mata", font=("Century Gothic", 10))
    label_spm3.place(x=85, y=27)

    button_pm3 = CTk.CTkButton(master=frame_PM3, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_mata_Celine)
    button_pm3.place(x=85, y=50)

    frame_PM4 = CTk.CTkFrame(master=poli_mata_window, width=352, height=80, corner_radius=0)
    frame_PM4.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER)

    frame_PM5 = CTk.CTkFrame(master=poli_mata_window, width=352, height=80, corner_radius=0)
    frame_PM5.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    dokter_4_PM = ImageTk.PhotoImage(Image.open("dr.Ayu.jpg"))
    image_label_PM4 = CTk.CTkLabel(master=poli_mata_window, image=dokter_4_PM, text="", fg_color="transparent")
    image_label_PM4.place(x=295, y=388)

    label_PM4 = CTk.CTkLabel(master=frame_PM4, text="dr.Ayu Lestari, Sp.M", font=("Century Gothic", 13))
    label_PM4.place(x=10, y=5)

    label_spm4 = CTk.CTkLabel(master=frame_PM4, text="Spesialis Mata", font=("Century Gothic", 10))
    label_spm4.place(x=10, y=27)

    button_pm4 = CTk.CTkButton(master=frame_PM4, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_mata_Ayu)
    button_pm4.place(x=10, y=50)

    dokter_5_PM = ImageTk.PhotoImage(Image.open("dr.Rizky.jpg"))
    image_label_PM5 = CTk.CTkLabel(master=poli_mata_window, image=dokter_5_PM, text="", fg_color="transparent")
    image_label_PM5.place(x=24, y=504)

    label_PM5 = CTk.CTkLabel(master=frame_PM5, text="dr.Rizky Pratama, SP.M", font=("Century Gothic", 13))
    label_PM5.place(x=85, y=5)

    label_spm5 = CTk.CTkLabel(master=frame_PM5, text="Spesialis Mata", font=("Century Gothic", 10))
    label_spm5.place(x=85, y=27)

    button_pm5 = CTk.CTkButton(master=frame_PM5, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_mata_Rizky)
    button_pm5.place(x=80, y=50)

    frame_poli_mata4 = CTk.CTkFrame(master=poli_mata_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_poli_mata4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=poli_mata_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=poli_mata_window.destroy)
    button_back.place(x=0,y=0)

#<==================================================Batas Poli Mata=======================================================>

def poli_jantung_lina():
    lina_window = CTk.CTkToplevel(app)
    lina_window.geometry("400x680+100+15")
    lina_window.title("Poli Jantung Lina")
    lina_window.resizable(False, False)
    lina_window.grab_set()

    background = CTk.CTkLabel(master=lina_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_lina1 = CTk.CTkFrame(master=lina_window, width=372, height=600, corner_radius=0)
    frame_lina1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_lina2 = CTk.CTkFrame(master=lina_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_lina2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_lina1 = ImageTk.PhotoImage(Image.open("dr.lena.jpeg"))
    image_label_lina = CTk.CTkLabel(master=lina_window, image=img_lina1, text="", fg_color="transparent")
    image_label_lina.place(x=24, y=63)

    label_lina1 = CTk.CTkLabel(master=frame_lina2, text="dr. Lina, Sp.JP", font=("Century Gothic", 13))
    label_lina1.place(x=85, y=5)

    label_lina2 = CTk.CTkLabel(master=frame_lina2, text="Spesialis Jantung dan Pembuluh Darah", font=("Century Gothic", 10))
    label_lina2.place(x=85, y=27)

    frame_lina3 = CTk.CTkFrame(master=lina_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_lina3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_lina = CTk.CTkLabel(master=frame_lina3, text="Biodata dr.Lina", font=("Century Gothic", 13))
    label_biodata_lina.place(x=10, y=10)

    label_lina3 = CTk.CTkLabel(master=frame_lina3, text="Dokter Umum, Fakultas Kedokteran Universitas Indonesia, 2008\nSpesialis Jantung dan Pembuluh Darah, Universitas Padjadjaran, 2014\nDokter Spesialis Jantung di RS Jantung Jakarta selama 7 tahun", font=("Century Gothic", 10), justify="left")
    label_lina3.place(x=10, y=35)

    def save_jadwal_and_transfer_Lina(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_jantung2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_jantung2.json", "w") as file:
            json.dump(booking_data, file, indent=4)  
        messagebox.showinfo('Success',"Pemesanan Berhasil")
        lina_window.destroy()

    def get_jadwal_Lina(selected_time):
        try:
            with open("poli_jantung2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_lina = tkinter.StringVar()

    jadwal_Lina1 = "Selasa, 15:00 - 21:00"
    jadwal_Lina2 = "Jumat, 07:00 - 13:00"
    
    label_jadwal_lina = CTk.CTkLabel(master=frame_lina1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_lina.place(x=150, y=300)

    jadwal_lina1 = CTk.CTkRadioButton(master=frame_lina1, text=jadwal_Lina1, variable=selected_jadwal_lina, value=jadwal_Lina1)
    jadwal_lina1.place(x=10, y=350)

    jadwal_lina2 = CTk.CTkRadioButton(master=frame_lina1, text=jadwal_Lina2, variable=selected_jadwal_lina, value=jadwal_Lina2)
    jadwal_lina2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_lina1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Lina(selected_jadwal_lina.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Lina(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Lina(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Lina(selected_jadwal):
        selected_time = selected_jadwal_lina.get()

        current_booking_count = get_jadwal_Lina(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=lina_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_lina4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_lina4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_lina = CTk.CTkLabel(master=frame_lina4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_lina.place(x=10, y=10)
        
        label_payment_lina = CTk.CTkLabel(master=frame_lina4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_lina.place(x=10, y=50)

        label_antrian_lina = CTk.CTkLabel(master=frame_lina4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_lina.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Lina(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Lina("dr. Lina, Sp.JP", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Lina(jadwal_lina1, jadwal_Lina1)
    check_and_disable_jadwal_Lina(jadwal_lina2, jadwal_Lina2)

    frame_Lina4 = CTk.CTkFrame(master=lina_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Lina4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=lina_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=lina_window.destroy)
    button_back.place(x=0,y=0)


def poli_jantung_rachel():
    rachel_window = CTk.CTkToplevel(app)
    rachel_window.geometry("400x680+100+15")
    rachel_window.title("Poli Jantung Rachel")
    rachel_window.resizable(False, False)
    rachel_window.grab_set()

    background = CTk.CTkLabel(master=rachel_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_rachel1 = CTk.CTkFrame(master=rachel_window, width=372, height=600, corner_radius=0)
    frame_rachel1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_rachel2 = CTk.CTkFrame(master=rachel_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_rachel2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_rachel1 = ImageTk.PhotoImage(Image.open("dr. rachel.png"))
    image_label_rachel = CTk.CTkLabel(master=rachel_window, image=img_rachel1, text="", fg_color="transparent")
    image_label_rachel.place(x=24, y=63)

    label_rachel1 = CTk.CTkLabel(master=frame_rachel2, text="dr. Rachel, Sp.JP", font=("Century Gothic", 13))
    label_rachel1.place(x=85, y=5)

    label_rachel2 = CTk.CTkLabel(master=frame_rachel2, text="Spesialis Jantung dan Pembuluh Darah", font=("Century Gothic", 10))
    label_rachel2.place(x=85, y=27)

    frame_rachel3 = CTk.CTkFrame(master=rachel_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_rachel3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata = CTk.CTkLabel(master=frame_rachel3, text="Biodata dr.Rachel", font=("Century Gothic", 13))
    label_biodata.place(x=10, y=10)

    label_rachel3 = CTk.CTkLabel(master=frame_rachel3, text="Dokter Umum, Universitas Indonesia, 2007\nSpesialis Jantung dan Pembuluh Darah, UI, 2015\nDokter Spesialis Bedah Jantung di RSUP selama 5 tahun", font=("Century Gothic", 12), justify="left")
    label_rachel3.place(x=10, y=35)

    def save_jadwal_and_transfer_Rachel(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_jantung2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_jantung2.json", "w") as file:
            json.dump(booking_data, file, indent=4)    
        messagebox.showinfo("Success", "Pemesanan Berhasil")
        rachel_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Rachel(selected_time):
        try:
            with open("poli_jantung2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_rachel = tkinter.StringVar()

    jadwal_Rachel1 = "Senin, 15:00 - 21:00"
    jadwal_Rachel2 = "Kamis, 07:00 - 13:00"
    
    label_jadwal_rachel1 = CTk.CTkLabel(master=frame_rachel1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_rachel1.place(x=150, y=300)

    jadwal_rachel1 = CTk.CTkRadioButton(master=frame_rachel1, text=jadwal_Rachel1, variable=selected_jadwal_rachel, value=jadwal_Rachel1)
    jadwal_rachel1.place(x=10, y=350)

    jadwal_rachel2 = CTk.CTkRadioButton(master=frame_rachel1, text=jadwal_Rachel2, variable=selected_jadwal_rachel, value=jadwal_Rachel2)
    jadwal_rachel2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_rachel1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Rachel(selected_jadwal_rachel.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Rachel(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Rachel(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Rachel(selected_jadwal):
        selected_time = selected_jadwal_rachel.get()

        current_booking_count = get_jadwal_Rachel(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=rachel_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_rachel4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_rachel4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_rachel = CTk.CTkLabel(master=frame_rachel4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_rachel.place(x=10, y=10)
        
        label_payment_rachel = CTk.CTkLabel(master=frame_rachel4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_rachel.place(x=10, y=50)

        label_antrian_rachel = CTk.CTkLabel(master=frame_rachel4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_rachel.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Rachel(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Rachel("dr. Rachel, Sp.JP", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Rachel(jadwal_rachel1, jadwal_Rachel1)
    check_and_disable_jadwal_Rachel(jadwal_rachel2, jadwal_Rachel2)

    frame_Rachel4 = CTk.CTkFrame(master=rachel_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Rachel4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=rachel_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=rachel_window.destroy)
    button_back.place(x=0,y=0)

def poli_jantung_Rey():
    rey_window = CTk.CTkToplevel(app)
    rey_window.geometry("400x680+100+15")
    rey_window.title("Poli Jantung Rey")
    rey_window.resizable(False, False)
    rey_window.grab_set()

    background = CTk.CTkLabel(master=rey_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_rey1 = CTk.CTkFrame(master=rey_window, width=372, height=600, corner_radius=0)
    frame_rey1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_rey2 = CTk.CTkFrame(master=rey_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_rey2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_rey1 = ImageTk.PhotoImage(Image.open("dr. akira.png"))
    image_label_rey = CTk.CTkLabel(master=rey_window, image=img_rey1, text="", fg_color="transparent")
    image_label_rey.place(x=24, y=63)

    label_rey1 = CTk.CTkLabel(master=frame_rey2, text="dr. Rey Akira, Sp.JP", font=("Century Gothic", 13))
    label_rey1.place(x=85, y=5)

    label_rey2 = CTk.CTkLabel(master=frame_rey2, text="Spesialis Jantung dan Pembuluh Darah", font=("Century Gothic", 10))
    label_rey2.place(x=85, y=27)
    
    frame_rey3 = CTk.CTkFrame(master=rey_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_rey3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_rey = CTk.CTkLabel(master=frame_rey3, text="Biodata dr.Rey Akira", font=("Century Gothic", 13))
    label_biodata_rey.place(x=10, y=10)

    label_rey3 = CTk.CTkLabel(master=frame_rey3, text="Dokter Umum, Universitas Gadjah Mada, 2007\nSpesialis Jantung dan Pembuluh Darah, Unair, 2013\nDokter Spesialis Jantung di RS Harapan Kita selama 6 tahun", font=("Century Gothic", 10), justify="left")
    label_rey3.place(x=10, y=35)

    def save_jadwal_and_transfer_Rey(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_jantung2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_jantung2.json", "w") as file:
            json.dump(booking_data, file, indent=4)    
        messagebox.showinfo("Success", "Pemesanan Berhasil") 
        rey_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Rey(selected_time):
        try:
            with open("poli_jantung2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_rey = tkinter.StringVar()

    jadwal_Rey1 = "Selasa, 07:00 - 13:00"
    jadwal_Rey2 = "Kamis, 15:00 - 21:00"
    
    label_jadwal_rey1 = CTk.CTkLabel(master=frame_rey1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_rey1.place(x=150, y=300)

    jadwal_rey1 = CTk.CTkRadioButton(master=frame_rey1, text=jadwal_Rey1, variable=selected_jadwal_rey, value=jadwal_Rey1)
    jadwal_rey1.place(x=10, y=350)

    jadwal_rey2 = CTk.CTkRadioButton(master=frame_rey1, text=jadwal_Rey2, variable=selected_jadwal_rey, value=jadwal_Rey2)
    jadwal_rey2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_rey1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Rey(selected_jadwal_rey.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Rey(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Rey(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Rey(selected_jadwal):
        selected_time = selected_jadwal_rey.get()

        current_booking_count = get_jadwal_Rey(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=rey_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_rey4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_rey4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_rey = CTk.CTkLabel(master=frame_rey4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_rey.place(x=10, y=10)
        
        label_payment_rey = CTk.CTkLabel(master=frame_rey4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_rey.place(x=10, y=50)

        label_antrian_rey = CTk.CTkLabel(master=frame_rey4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_rey.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Rey(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Rey("dr. Rey Akira, Sp.JP", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Rey(jadwal_rey1, jadwal_Rey1)
    check_and_disable_jadwal_Rey(jadwal_rey2, jadwal_Rey2)

    frame_Rey4 = CTk.CTkFrame(master=rey_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Rey4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=rey_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=rey_window.destroy)
    button_back.place(x=0,y=0)

def poli_jantung_david():
    david_window = CTk.CTkToplevel(app)
    david_window.geometry("400x680+100+15")
    david_window.title("Poli Jantung David")
    david_window.resizable(False, False)
    david_window.grab_set()

    background = CTk.CTkLabel(master=david_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_david1 = CTk.CTkFrame(master=david_window, width=372, height=600, corner_radius=0)
    frame_david1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_david2 = CTk.CTkFrame(master=david_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_david2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_david1 = ImageTk.PhotoImage(Image.open("dr. david.png"))
    image_label_david = CTk.CTkLabel(master=david_window, image=img_david1, text="", fg_color="transparent")
    image_label_david.place(x=24, y=63)

    label_david1 = CTk.CTkLabel(master=frame_david2, text="dr. David, Sp.JP", font=("Century Gothic", 13))
    label_david1.place(x=85, y=5)

    label_david2 = CTk.CTkLabel(master=frame_david2, text="Spesialis Jantung dan Pembuluh Darah", font=("Century Gothic", 10))
    label_david2.place(x=85, y=27)

    frame_david3 = CTk.CTkFrame(master=david_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_david3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_david = CTk.CTkLabel(master=frame_david3, text="Biodata dr.David", font=("Century Gothic", 13))
    label_biodata_david.place(x=10, y=10)

    label_david3 = CTk.CTkLabel(master=frame_david3, text="Dokter Umum, Universitas Indonesia, 2004\nSpesialis Jantung dan Pembuluh Darah, UI, 2012\nDokter Spesialis Jantung di RS Bros Jakarta selama 6 tahun", font=("Century Gothic", 12), justify="left")
    label_david3.place(x=5, y=35)

    def save_jadwal_and_transfer_David(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_jantung2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_jantung2.json", "w") as file:
            json.dump(booking_data, file, indent=4)  
        messagebox.showinfo("Success", "Pemesanan Berhasil")
        david_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_David(selected_time):
        try:
            with open("poli_jantung2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_david = tkinter.StringVar()

    jadwal_David1 = "Senin, 07:00 - 13:00"
    jadwal_David2 = "Rabu, 15:00 - 21:00"
    
    label_jadwal_david1 = CTk.CTkLabel(master=frame_david1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_david1.place(x=150, y=300)

    jadwal_david1 = CTk.CTkRadioButton(master=frame_david1, text=jadwal_David1, variable=selected_jadwal_david, value=jadwal_David1)
    jadwal_david1.place(x=10, y=350)

    jadwal_david2 = CTk.CTkRadioButton(master=frame_david1, text=jadwal_David2, variable=selected_jadwal_david, value=jadwal_David2)
    jadwal_david2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_david1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_David(selected_jadwal_david.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_David(jadwal_button, selected_time):
        current_booking_count = get_jadwal_David(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_David(selected_jadwal):
        selected_time = selected_jadwal_david.get()

        current_booking_count = get_jadwal_David(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=david_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_david4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_david4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_david = CTk.CTkLabel(master=frame_david4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_david.place(x=10, y=10)
        
        label_payment_david = CTk.CTkLabel(master=frame_david4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_david.place(x=10, y=50)

        label_antrian_david = CTk.CTkLabel(master=frame_david4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_david.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_David(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_David("dr. David, Sp.JP", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_David(jadwal_david1, jadwal_David1)
    check_and_disable_jadwal_David(jadwal_david2, jadwal_David2)

    frame_David4 = CTk.CTkFrame(master=david_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_David4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=david_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=david_window.destroy)
    button_back.place(x=0,y=0)

def poli_jantung_ayusita():
    ayusita_window = CTk.CTkToplevel(app)
    ayusita_window.geometry("400x680+100+15")
    ayusita_window.title("Poli Jantung Ayusita")
    ayusita_window.resizable(False, False)
    ayusita_window.grab_set()

    background = CTk.CTkLabel(master=ayusita_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_ayusita1 = CTk.CTkFrame(master=ayusita_window, width=372, height=600, corner_radius=0)
    frame_ayusita1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_ayusita2 = CTk.CTkFrame(master=ayusita_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_ayusita2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Ayusita = ImageTk.PhotoImage(Image.open("dr.Ayusita.jpg"))
    image_label_ayusita = CTk.CTkLabel(master=ayusita_window, image=img_Ayusita, text="", fg_color="transparent")
    image_label_ayusita.place(x=24, y=63)

    label_ayusita1 = CTk.CTkLabel(master=frame_ayusita2, text="dr. Ayusita, Sp.JP", font=("Century Gothic", 13))
    label_ayusita1.place(x=85, y=5)

    label_ayusita2 = CTk.CTkLabel(master=frame_ayusita2, text="Spesialis Jantung dan Pembuluh Darah", font=("Century Gothic", 10))
    label_ayusita2.place(x=85, y=27)

    frame_ayusita3 = CTk.CTkFrame(master=ayusita_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_ayusita3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_ayusita = CTk.CTkLabel(master=frame_ayusita3, text="Biodata dr.Ayusita", font=("Century Gothic", 13))
    label_biodata_ayusita.place(x=10, y=10)

    label_ayusita3 = CTk.CTkLabel(master=frame_ayusita3, text="Dokter Umum, Universitas Diponegoro, 2009\nSpesialis Jantung dan Pembuluh Darah, Unhas, 2015\nDokter Spesialis Jantung di RS Bintaro selama 5 tahun", font=("Century Gothic", 12), justify="left")
    label_ayusita3.place(x=7, y=35)

    def save_jadwal_and_transfer_Ayusita(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_jantung2.json", "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []
        
        existing_data.append(data)
        
        with open("poli_jantung2.json", "w") as file:
            json.dump(existing_data, file, indent=4)  
        messagebox.showinfo("Success", "Pemesanan Berhasil")
        ayusita_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Ayusita(selected_time):
        try:
            with open("poli_jantung2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_ayusita = tkinter.StringVar()

    jadwal_Ayusita1 = "Rabu, 07:00 - 13:00"
    jadwal_Ayusita2 = "Jumat, 15:00 - 21:00"
    
    label_jadwal_ayusita1 = CTk.CTkLabel(master=frame_ayusita1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_ayusita1.place(x=150, y=300)

    jadwal_ayusita1 = CTk.CTkRadioButton(master=frame_ayusita1, text=jadwal_Ayusita1, variable=selected_jadwal_ayusita, value=jadwal_Ayusita1)
    jadwal_ayusita1.place(x=10, y=350)

    jadwal_ayusita2 = CTk.CTkRadioButton(master=frame_ayusita1, text=jadwal_Ayusita2, variable=selected_jadwal_ayusita, value=jadwal_Ayusita2)
    jadwal_ayusita2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_ayusita1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Ayusita(selected_jadwal_ayusita.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Ayusita(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Ayusita(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Ayusita(selected_jadwal):
        selected_time = selected_jadwal_ayusita.get()

        current_booking_count = get_jadwal_Ayusita(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=ayusita_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_ayusita4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_ayusita4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_ayusita = CTk.CTkLabel(master=frame_ayusita4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_ayusita.place(x=10, y=10)
        
        label_payment_ayusita = CTk.CTkLabel(master=frame_ayusita4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_ayusita.place(x=10, y=50)

        label_antrian_ayusita = CTk.CTkLabel(master=frame_ayusita4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_ayusita.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Ayusita(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Ayusita("dr. Ayusita, Sp.JP", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Ayusita(jadwal_ayusita1, jadwal_Ayusita1)
    check_and_disable_jadwal_Ayusita(jadwal_ayusita2, jadwal_Ayusita2)

    frame_Ayusita4 = CTk.CTkFrame(master=ayusita_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Ayusita4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=ayusita_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=ayusita_window.destroy)
    button_back.place(x=0,y=0)

def poli_jantung():
    poli_jantung_window = CTk.CTkToplevel(app)
    poli_jantung_window.geometry("400x680+100+15")
    poli_jantung_window.title("Poli Jantung")
    poli_jantung_window.resizable("false","false")
    poli_jantung_window.grab_set()

    background = CTk.CTkLabel(master=poli_jantung_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_PJ1 = CTk.CTkFrame(master=poli_jantung_window, width=352, height=80, corner_radius=0)
    frame_PJ1.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER)
    
    dokter_1_PJ = ImageTk.PhotoImage(Image.open("dr. david.png"))
    image_label_PJ1 = CTk.CTkLabel(master=poli_jantung_window, image=dokter_1_PJ, text="", fg_color="transparent")
    image_label_PJ1.place(x=24, y=48)

    label_PJ1 = CTk.CTkLabel(master=frame_PJ1, text="dr.David, Sp.JP", font=("Century Gothic", 13))
    label_PJ1.place(x=85, y=7)

    label_spj1 = CTk.CTkLabel(master=frame_PJ1, text="Spesialis Jantung dan Pembuluh darah", font=("Century Gothic", 9))
    label_spj1.place(x=85, y=27)

    button_pj1 = CTk.CTkButton(master=frame_PJ1, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_jantung_david)
    button_pj1.place(x=80, y=50)

    frame_PJ2 = CTk.CTkFrame(master=poli_jantung_window, width=352, height=80, corner_radius=0)
    frame_PJ2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    dokter_2_PJ = ImageTk.PhotoImage(Image.open("dr. rachel.png"))
    image_label_PJ2 = CTk.CTkLabel(master=poli_jantung_window, image=dokter_2_PJ, text="", fg_color="transparent")
    image_label_PJ2.place(x=295, y=165)

    label_PJ2 = CTk.CTkLabel(master=frame_PJ2, text="dr. Rachel, Sp.JP", font=("Century Gothic", 13))
    label_PJ2.place(x=10, y=7)

    label_spj2 = CTk.CTkLabel(master=frame_PJ2, text="Spesialis Bedah Jantung dan Pembuluh Darah", font=("Century Gothic", 9))
    label_spj2.place(x=10, y=27)

    button_pj2 = CTk.CTkButton(master=frame_PJ2, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_jantung_rachel)
    button_pj2.place(x=10, y=50)

    frame_PJ3 = CTk.CTkFrame(master=poli_jantung_window, width=352, height=80, corner_radius=0)
    frame_PJ3.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)

    dokter_3_PJ = ImageTk.PhotoImage(Image.open("dr. akira.png"))
    image_label_PJ3 = CTk.CTkLabel(master=poli_jantung_window, image=dokter_3_PJ, text="", fg_color="white")
    image_label_PJ3.place(x=24, y=280)

    label_PJ3 = CTk.CTkLabel(master=frame_PJ3, text="dr. Rey Akira, Sp.JP", font=("Century Gothic", 13))
    label_PJ3.place(x=85, y=7)

    label_spj3 = CTk.CTkLabel(master=frame_PJ3, text="Spesialis Jantung dan Pembuluh darah", font=("Century Gothic", 9))
    label_spj3.place(x=85, y=27)

    button_pj3 = CTk.CTkButton(master=frame_PJ3, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_jantung_Rey)
    button_pj3.place(x=85, y=50)

    frame_PJ4 = CTk.CTkFrame(master=poli_jantung_window, width=352, height=80, corner_radius=0)
    frame_PJ4.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER)

    frame_PJ5 = CTk.CTkFrame(master=poli_jantung_window, width=352, height=80, corner_radius=0)
    frame_PJ5.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    dokter_4_PJ = ImageTk.PhotoImage(Image.open("dr.lena.jpeg"))
    image_label_PJ4 = CTk.CTkLabel(master=poli_jantung_window, image=dokter_4_PJ, text="", fg_color="transparent")
    image_label_PJ4.place(x=295, y=388)

    label_PJ4 = CTk.CTkLabel(master=frame_PJ4, text="dr.Lina, Sp.JP", font=("Century Gothic", 13))
    label_PJ4.place(x=10, y=5)

    label_spj4 = CTk.CTkLabel(master=frame_PJ4, text="Spesialis Jantung dan Pembuluh darah", font=("Century Gothic", 10))
    label_spj4.place(x=10, y=27)

    button_pj4 = CTk.CTkButton(master=frame_PJ4, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_jantung_lina)
    button_pj4.place(x=10, y=50)

    dokter_5_PJ = ImageTk.PhotoImage(Image.open("dr.Ayusita.jpg"))
    image_label_PJ5 = CTk.CTkLabel(master=poli_jantung_window, image=dokter_5_PJ, text="", fg_color="transparent")
    image_label_PJ5.place(x=24, y=504)

    label_PJ5 = CTk.CTkLabel(master=frame_PJ5, text="dr.Ayusita, SP.JP", font=("Century Gothic", 13))
    label_PJ5.place(x=85, y=5)

    label_spj5 = CTk.CTkLabel(master=frame_PJ5, text="Spesialis Jantung dan Pembuluh darah", font=("Century Gothic", 10))
    label_spj5.place(x=85, y=27)

    button_pj5 = CTk.CTkButton(master=frame_PJ5, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_jantung_ayusita)
    button_pj5.place(x=80, y=50)

    frame_poli_jantung4 = CTk.CTkFrame(master=poli_jantung_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_poli_jantung4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=poli_jantung_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=poli_jantung_window.destroy)
    button_back.place(x=0,y=0)

#<===========================================batas poli jantung==================================================================>

def poli_penyakit_dalam_Lena():
    lena_window = CTk.CTkToplevel(app)
    lena_window.geometry("400x680+100+15")
    lena_window.title("Poli Penyakit Dalam Lena")
    lena_window.resizable(False, False)
    lena_window.grab_set()

    background = CTk.CTkLabel(master=lena_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_lena1 = CTk.CTkFrame(master=lena_window, width=372, height=600, corner_radius=0)
    frame_lena1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_lena2 = CTk.CTkFrame(master=lena_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_lena2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_lena = ImageTk.PhotoImage(Image.open("dr.lena.jpeg"))
    image_label_lena = CTk.CTkLabel(master=lena_window, image=img_lena, text="", fg_color="transparent")
    image_label_lena.place(x=24, y=63)

    label_lena1 = CTk.CTkLabel(master=frame_lena2, text="dr. Lena, Sp.PD", font=("Century Gothic", 13))
    label_lena1.place(x=85, y=5)

    label_lena2 = CTk.CTkLabel(master=frame_lena2, text="Spesialis Penyakit Dalam", font=("Century Gothic", 10))
    label_lena2.place(x=85, y=27)

    frame_lena3 = CTk.CTkFrame(master=lena_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_lena3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_lena = CTk.CTkLabel(master=frame_lena3, text="Biodata dr. Lena", font=("Century Gothic", 13))
    label_biodata_lena.place(x=10, y=10)

    label_lena3 = CTk.CTkLabel(master=frame_lena3, text="Dokter Umum, Universitas Hasanuddin, 2008\nSpesialis Penyakit Dalam, Universitas Indonesia, 2013\nMenjadi Dokter Spesialis Penyakit Dalam selama 7 tahun", font=("Century Gothic", 11), justify="left")
    label_lena3.place(x=10, y=35)

    def save_jadwal_and_transfer_lena(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }

        try:
            with open("poli_penyakit_dalam2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []

        booking_data.append(data)  

        with open("poli_penyakit_dalam2.json", "w") as file:
            json.dump(booking_data, file, indent=4)  
        messagebox.showinfo("Success","Pemesanan berhasil")
        lena_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_lena(selected_time):
        try:
            with open("poli_penyakit_dalam2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_lena = tkinter.StringVar()

    jadwal_lena1 = "Selasa, 15:00 - 21:00"
    jadwal_lena2 = "Jumat, 07:00 - 13:00"
    
    label1_jadwal_lena = CTk.CTkLabel(master=frame_lena1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label1_jadwal_lena.place(x=150, y=300)

    jadwal_lena1 = CTk.CTkRadioButton(master=frame_lena1, text=jadwal_lena1, variable=selected_jadwal_lena, value=jadwal_lena1)
    jadwal_lena1.place(x=10, y=350)

    jadwal_lena2 = CTk.CTkRadioButton(master=frame_lena1, text=jadwal_lena2, variable=selected_jadwal_lena, value=jadwal_lena2)
    jadwal_lena2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_lena1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_lena(selected_jadwal_lena.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_lena(jadwal_button, selected_time):
        current_booking_count = get_jadwal_lena(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_lena(selected_jadwal):
        selected_time = selected_jadwal_lena.get()

        current_booking_count = get_jadwal_lena(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=lena_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_lena4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_lena4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_lena = CTk.CTkLabel(master=frame_lena4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_lena.place(x=10, y=10)
        
        label_payment_lena = CTk.CTkLabel(master=frame_lena4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_lena.place(x=10, y=50)

        label_antrian_lena = CTk.CTkLabel(master=frame_lena4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_lena.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        current_booking_number = get_jadwal_lena(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_lena("dr. Lena, Sp.PD", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path


    check_and_disable_jadwal_lena(jadwal_lena1, jadwal_lena1)
    check_and_disable_jadwal_lena(jadwal_lena2, jadwal_lena2)

    frame_Lena4 = CTk.CTkFrame(master=lena_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Lena4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=lena_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=lena_window.destroy)
    button_back.place(x=0,y=0)


def poli_penyakit_dalam_Andi():
    Andi_window = CTk.CTkToplevel(app)
    Andi_window.geometry("400x680+100+15")
    Andi_window.title("Poli Penyakit Dalam Andi")
    Andi_window.resizable(False, False)
    Andi_window.grab_set()

    background = CTk.CTkLabel(master=Andi_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Andi1 = CTk.CTkFrame(master=Andi_window, width=372, height=600, corner_radius=0)
    frame_Andi1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Andi2 = CTk.CTkFrame(master=Andi_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Andi2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Andi = ImageTk.PhotoImage(Image.open("dr.andi.jpg"))
    image_label_Andi = CTk.CTkLabel(master=Andi_window, image=img_Andi, text="", fg_color="transparent")
    image_label_Andi.place(x=24, y=63)

    label_Andi1 = CTk.CTkLabel(master=frame_Andi2, text="dr. Andi, Sp.PD", font=("Century Gothic", 13))
    label_Andi1.place(x=85, y=5)

    label_Andi2 = CTk.CTkLabel(master=frame_Andi2, text="Spesialis Penyakit Dalam", font=("Century Gothic", 10))
    label_Andi2.place(x=85, y=27)

    frame_Andi3 = CTk.CTkFrame(master=Andi_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Andi3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Andi = CTk.CTkLabel(master=frame_Andi3, text="Biodata dr. Andi", font=("Century Gothic", 13))
    label_biodata_Andi.place(x=10, y=10)

    label_Andi3 = CTk.CTkLabel(master=frame_Andi3, text="Dokter Umum, Universitas Hasanuddin, 2008\nSpesialis Penyakit Dalam, Universitas Indonesia, 2013\nMenjadi Dokter Spesialis Penyakit Dalam selama 7 tahun", font=("Century Gothic", 11), justify="left")
    label_Andi3.place(x=10, y=35)

    def save_jadwal_and_transfer_Andi(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }

        try:
            with open("poli_penyakit_dalam2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []

        booking_data.append(data)  

        with open("poli_penyakit_dalam2.json", "w") as file:
            json.dump(booking_data, file, indent=4)  
        messagebox.showinfo("Success","Pemesanan berhasil")
        Andi_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Andi(selected_time):
        try:
            with open("poli_penyakit_dalam2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_Andi = tkinter.StringVar()

    jadwal_andi1 = "Rabu, 07:00 - 13:00"
    jadwal_andi2 = "Jumat, 15:00 - 21:00"
    
    label1_jadwal_Andi = CTk.CTkLabel(master=frame_Andi1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label1_jadwal_Andi.place(x=150, y=300)

    jadwal_Joe1 = CTk.CTkRadioButton(master=frame_Andi1, text=jadwal_andi1, variable=selected_jadwal_Andi, value=jadwal_andi1)
    jadwal_Joe1.place(x=10, y=350)

    jadwal_Joe2 = CTk.CTkRadioButton(master=frame_Andi1, text=jadwal_andi2, variable=selected_jadwal_Andi, value=jadwal_andi2)
    jadwal_Joe2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Andi1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Andi(selected_jadwal_Andi.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Andi(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Andi(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Andi(selected_jadwal):
        selected_time = selected_jadwal_Andi.get()

        current_booking_count = get_jadwal_Andi(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Andi_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Andi4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Andi4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Andi = CTk.CTkLabel(master=frame_Andi4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Andi.place(x=10, y=10)
        
        label_payment_Andi = CTk.CTkLabel(master=frame_Andi4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Andi.place(x=10, y=50)

        label_antrian_Andi = CTk.CTkLabel(master=frame_Andi4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Andi.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        current_booking_number = get_jadwal_Andi(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Andi("dr. Andi, Sp.PD", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Andi(jadwal_Joe1, jadwal_andi1)
    check_and_disable_jadwal_Andi(jadwal_Joe2, jadwal_andi2)

    frame_Andi4 = CTk.CTkFrame(master=Andi_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Andi4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Andi_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Andi_window.destroy)
    button_back.place(x=0,y=0)

def poli_penyakit_dalam_Joe():
    Joe_window = CTk.CTkToplevel(app)
    Joe_window.geometry("400x680+100+15")
    Joe_window.title("Poli Penyakit Dalam Joe")
    Joe_window.resizable(False, False)
    Joe_window.grab_set()

    background = CTk.CTkLabel(master=Joe_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Joe1 = CTk.CTkFrame(master=Joe_window, width=372, height=600, corner_radius=0)
    frame_Joe1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Joe2 = CTk.CTkFrame(master=Joe_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Joe2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Joe = ImageTk.PhotoImage(Image.open("dr. joe.png"))
    image_label_Joe = CTk.CTkLabel(master=Joe_window, image=img_Joe, text="", fg_color="transparent")
    image_label_Joe.place(x=24, y=63)

    label_Joe1 = CTk.CTkLabel(master=frame_Joe2, text="dr. Joe, Sp.PD", font=("Century Gothic", 13))
    label_Joe1.place(x=85, y=5)

    label_Joe2 = CTk.CTkLabel(master=frame_Joe2, text="Spesialis Penyakit Dalam", font=("Century Gothic", 10))
    label_Joe2.place(x=85, y=27)

    frame_Joe3 = CTk.CTkFrame(master=Joe_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Joe3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Jax = CTk.CTkLabel(master=frame_Joe3, text="Biodata dr. Joe", font=("Century Gothic", 13))
    label_biodata_Jax.place(x=10, y=10)

    label_Joe3 = CTk.CTkLabel(master=frame_Joe3, text="Dokter Umum, Universitas Hasanuddin, 2008\nSpesialis Penyakit Dalam, Universitas Indonesia, 2013\nMenjadi Dokter Spesialis Penyakit Dalam selama 7 tahun", font=("Century Gothic", 11), justify="left")
    label_Joe3.place(x=10, y=35)

    def save_jadwal_and_transfer_Joe(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }

        try:
            with open("poli_penyakit_dalam2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []

        booking_data.append(data)  

        with open("poli_penyakit_dalam2.json", "w") as file:
            json.dump(booking_data, file, indent=4)  
        messagebox.showinfo("Success","Pemesanan berhasil")
        Joe_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Joe(selected_time):
        try:
            with open("poli_penyakit_dalam2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_Joe = tkinter.StringVar()

    jadwal_joe1 = "Senin, 07:00 - 13:00"
    jadwal_joe2 = "Rabu, 15:00 - 21:00"
    
    label1_jadwal_Joe = CTk.CTkLabel(master=frame_Joe1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label1_jadwal_Joe.place(x=150, y=300)

    jadwal_Joe1 = CTk.CTkRadioButton(master=frame_Joe1, text=jadwal_joe1, variable=selected_jadwal_Joe, value=jadwal_joe1)
    jadwal_Joe1.place(x=10, y=350)

    jadwal_Joe2 = CTk.CTkRadioButton(master=frame_Joe1, text=jadwal_joe2, variable=selected_jadwal_Joe, value=jadwal_joe2)
    jadwal_Joe2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Joe1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Joe(selected_jadwal_Joe.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Joe(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Joe(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Joe(selected_jadwal):
        selected_time = selected_jadwal_Joe.get()

        current_booking_count = get_jadwal_Joe(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Joe_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Joe4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Joe4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Joe = CTk.CTkLabel(master=frame_Joe4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Joe.place(x=10, y=10)
        
        label_payment_Joe = CTk.CTkLabel(master=frame_Joe4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Joe.place(x=10, y=50)

        label_antrian_Joe = CTk.CTkLabel(master=frame_Joe4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Joe.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        current_booking_number = get_jadwal_Joe(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Joe("dr. Joe, Sp.PD", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Joe(jadwal_Joe1, jadwal_joe1)
    check_and_disable_jadwal_Joe(jadwal_Joe2, jadwal_joe2)

    frame_Joe4 = CTk.CTkFrame(master=Joe_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Joe4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Joe_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Joe_window.destroy)
    button_back.place(x=0,y=0)

def poli_penyakit_dalam_Jax():
    Jax_window = CTk.CTkToplevel(app)
    Jax_window.geometry("400x680+100+15")
    Jax_window.title("Poli Penyakit Dalam Jax")
    Jax_window.resizable(False, False)
    Jax_window.grab_set()

    background = CTk.CTkLabel(master=Jax_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Jax1 = CTk.CTkFrame(master=Jax_window, width=372, height=600, corner_radius=0)
    frame_Jax1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Jax2 = CTk.CTkFrame(master=Jax_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Jax2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Jax = ImageTk.PhotoImage(Image.open("dr. jax.png"))
    image_label_Jax = CTk.CTkLabel(master=Jax_window, image=img_Jax, text="", fg_color="transparent")
    image_label_Jax.place(x=24, y=63)

    label_Jax1 = CTk.CTkLabel(master=frame_Jax2, text="dr. Jax, Sp.GK", font=("Century Gothic", 13))
    label_Jax1.place(x=85, y=5)

    label_Jax2 = CTk.CTkLabel(master=frame_Jax2, text="Spesialis Penyakit Dalam", font=("Century Gothic", 10))
    label_Jax2.place(x=85, y=27)

    frame_Jax3 = CTk.CTkFrame(master=Jax_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Jax3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Jax = CTk.CTkLabel(master=frame_Jax3, text="Biodata dr. Jax", font=("Century Gothic", 13))
    label_biodata_Jax.place(x=10, y=10)

    label_Jax3 = CTk.CTkLabel(master=frame_Jax3, text="Dokter Umum, Universitas Indonesia, 2010\nSpesialis Penyakit Dalam, Universitas Airlangga, 2015\nMenjadi Dokter Spesialis Penyakit Dalam selama 7 tahun", font=("Century Gothic", 11), justify="left")
    label_Jax3.place(x=10, y=35)

    def save_jadwal_and_transfer_Jax(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }

        try:
            with open("poli_penyakit_dalam2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []

        booking_data.append(data)  

        with open("poli_penyakit_dalam2.json", "w") as file:
            json.dump(booking_data, file, indent=4)  
        messagebox.showinfo("Success","Pemesanan berhasil")
        Jax_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Jax(selected_time):
        try:
            with open("poli_penyakit_dalam2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_Jax = tkinter.StringVar()

    jadwal_jax1 = "Selasa, 07:00 - 13:00"
    jadwal_jax2 = "Kamis, 15:00 - 21:00"
    
    label1_jadwal_Jax = CTk.CTkLabel(master=frame_Jax1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label1_jadwal_Jax.place(x=150, y=300)

    jadwal_Jax1 = CTk.CTkRadioButton(master=frame_Jax1, text=jadwal_jax1, variable=selected_jadwal_Jax, value=jadwal_jax1)
    jadwal_Jax1.place(x=10, y=350)

    jadwal_Jax2 = CTk.CTkRadioButton(master=frame_Jax1, text=jadwal_jax2, variable=selected_jadwal_Jax, value=jadwal_jax2)
    jadwal_Jax2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Jax1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Jax(selected_jadwal_Jax.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Jax(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Jax(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Jax(selected_jadwal):
        selected_time = selected_jadwal_Jax.get()

        current_booking_count = get_jadwal_Jax(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Jax_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Jax4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Jax4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Jax = CTk.CTkLabel(master=frame_Jax4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Jax.place(x=10, y=10)
        
        label_payment_Jax = CTk.CTkLabel(master=frame_Jax4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Jax.place(x=10, y=50)

        label_antrian_Jax = CTk.CTkLabel(master=frame_Jax4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Jax.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        current_booking_number = get_jadwal_Jax(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Jax("dr. Jax, Sp.GK", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Jax(jadwal_Jax1, jadwal_jax1)
    check_and_disable_jadwal_Jax(jadwal_Jax2, jadwal_jax2)

    frame_Jax4 = CTk.CTkFrame(master=Jax_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Jax4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Jax_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Jax_window.destroy)
    button_back.place(x=0,y=0)

def poli_penyakit_dalam_Elle():
    Elle_window = CTk.CTkToplevel(app)
    Elle_window.geometry("400x680+100+15")
    Elle_window.title("Poli Penyakit Dalam Elle")
    Elle_window.resizable(False, False)
    Elle_window.grab_set()

    background = CTk.CTkLabel(master=Elle_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Elle1 = CTk.CTkFrame(master=Elle_window, width=372, height=600, corner_radius=0)
    frame_Elle1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Elle2 = CTk.CTkFrame(master=Elle_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Elle2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Elle = ImageTk.PhotoImage(Image.open("dr. elle.png"))
    image_label_Elle = CTk.CTkLabel(master=Elle_window, image=img_Elle, text="", fg_color="transparent")
    image_label_Elle.place(x=24, y=63)

    label_Elle1 = CTk.CTkLabel(master=frame_Elle2, text="dr. Elle, Sp.PD", font=("Century Gothic", 13))
    label_Elle1.place(x=85, y=5)

    label_Elle2 = CTk.CTkLabel(master=frame_Elle2, text="Spesialis Penyakit Dalam", font=("Century Gothic", 10))
    label_Elle2.place(x=85, y=27)

    frame_Elle3 = CTk.CTkFrame(master=Elle_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Elle3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Daniel = CTk.CTkLabel(master=frame_Elle3, text="Biodata dr. Elle", font=("Century Gothic", 13))
    label_biodata_Daniel.place(x=10, y=10)

    label_Elle3 = CTk.CTkLabel(master=frame_Elle3, text="Dokter Umum, Universitas Airlangga, 2009\nSpesialis Penyakit Dalam, Universitas Gadjah Mada, 2014\nMenjadi Dokter Spesialis Penyakit Dalam selama 5 tahun", font=("Century Gothic", 11), justify="left")
    label_Elle3.place(x=10, y=35)

    def save_jadwal_and_transfer_Elle(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }

        try:
            with open("poli_penyakit_dalam2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []

        booking_data.append(data)  

        with open("poli_penyakit_dalam2.json", "w") as file:
            json.dump(booking_data, file, indent=4)  
        messagebox.showinfo("Success","Pemesanan berhasil")
        Elle_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Elle(selected_time):
        try:
            with open("poli_penyakit_dalam2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_Elle = tkinter.StringVar()

    jadwal_Elle1 = "Senin, 15:00 - 21:00"
    jadwal_Elle2 = "Kamis, 07:00 - 13:00"
    
    label1_jadwal_Elle = CTk.CTkLabel(master=frame_Elle1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label1_jadwal_Elle.place(x=150, y=300)

    jadwal_elle1 = CTk.CTkRadioButton(master=frame_Elle1, text=jadwal_Elle1, variable=selected_jadwal_Elle, value=jadwal_Elle1)
    jadwal_elle1.place(x=10, y=350)

    jadwal_elle2 = CTk.CTkRadioButton(master=frame_Elle1, text=jadwal_Elle2, variable=selected_jadwal_Elle, value=jadwal_Elle2)
    jadwal_elle2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Elle1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Elle(selected_jadwal_Elle.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Elle(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Elle(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Elle(selected_jadwal):
        selected_time = selected_jadwal_Elle.get()

        current_booking_count = get_jadwal_Elle(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Elle_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Elle4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Elle4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Elle = CTk.CTkLabel(master=frame_Elle4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Elle.place(x=10, y=10)
        
        label_payment_Elle = CTk.CTkLabel(master=frame_Elle4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Elle.place(x=10, y=50)

        label_antrian_Elle = CTk.CTkLabel(master=frame_Elle4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Elle.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        current_booking_number = get_jadwal_Elle(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Elle("dr. Elle, Sp.PD", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path


    check_and_disable_jadwal_Elle(jadwal_elle1, jadwal_Elle1)
    check_and_disable_jadwal_Elle(jadwal_elle2, jadwal_Elle2)

    frame_Elle4 = CTk.CTkFrame(master=Elle_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Elle4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Elle_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Elle_window.destroy)
    button_back.place(x=0,y=0)

def poli_penyakit_dalam():
    poli_penyakit_dalam_window = CTk.CTkToplevel(app)
    poli_penyakit_dalam_window.geometry("400x680+100+15")
    poli_penyakit_dalam_window.title("Poli Penyakit Dalam")
    poli_penyakit_dalam_window.resizable(False,False)
    poli_penyakit_dalam_window.grab_set()

    background = CTk.CTkLabel(master=poli_penyakit_dalam_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_PPD1 = CTk.CTkFrame(master=poli_penyakit_dalam_window, width=352, height=80, corner_radius=0)
    frame_PPD1.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER)
    
    dokter_1_PPD = ImageTk.PhotoImage(Image.open("dr. elle.png"))
    image_label_PPD1 = CTk.CTkLabel(master=poli_penyakit_dalam_window, image=dokter_1_PPD, text="", fg_color="transparent")
    image_label_PPD1.place(x=24, y=48)

    label_PPD1 = CTk.CTkLabel(master=frame_PPD1, text="dr. Elle, Sp.PD", font=("Century Gothic", 13))
    label_PPD1.place(x=85, y=7)

    label_PPD2 = CTk.CTkLabel(master=frame_PPD1, text="Spesialis Penyakit Dalam", font=("Century Gothic", 10))
    label_PPD2.place(x=85, y=27)

    button_PPD1 = CTk.CTkButton(master=frame_PPD1, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_penyakit_dalam_Elle)
    button_PPD1.place(x=80, y=50)

    frame_PPD2 = CTk.CTkFrame(master=poli_penyakit_dalam_window, width=352, height=80, corner_radius=0)
    frame_PPD2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    dokter_2_PPD = ImageTk.PhotoImage(Image.open("dr. joe.png"))
    image_label_PPD2 = CTk.CTkLabel(master=poli_penyakit_dalam_window, image=dokter_2_PPD, text="", fg_color="transparent")
    image_label_PPD2.place(x=295, y=165)

    label_PPD3 = CTk.CTkLabel(master=frame_PPD2, text="dr. Joe, Sp.PD", font=("Century Gothic", 13))
    label_PPD3.place(x=10, y=7)

    label_PPD4 = CTk.CTkLabel(master=frame_PPD2, text="Spesialis Penyakit Dalam", font=("Century Gothic", 10))
    label_PPD4.place(x=10, y=27)

    button_PPD2 = CTk.CTkButton(master=frame_PPD2, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_penyakit_dalam_Joe)
    button_PPD2.place(x=10, y=50)

    frame_PPD3 = CTk.CTkFrame(master=poli_penyakit_dalam_window, width=352, height=80, corner_radius=0)
    frame_PPD3.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)

    dokter_3_PPD = ImageTk.PhotoImage(Image.open("dr. jax.png"))
    image_label_PPD3 = CTk.CTkLabel(master=poli_penyakit_dalam_window, image=dokter_3_PPD, text="", fg_color="white")
    image_label_PPD3.place(x=24, y=280)

    label_PPD5 = CTk.CTkLabel(master=frame_PPD3, text="dr. Jax, Sp.Pd", font=("Century Gothic", 13))
    label_PPD5.place(x=85, y=7)

    label_PPD6 = CTk.CTkLabel(master=frame_PPD3, text="Spesialis Penyakit Dalam", font=("Century Gothic", 10))
    label_PPD6.place(x=85, y=27)

    button_PPD3 = CTk.CTkButton(master=frame_PPD3, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_penyakit_dalam_Jax)
    button_PPD3.place(x=85, y=50)

    frame_PPD4 = CTk.CTkFrame(master=poli_penyakit_dalam_window, width=352, height=80, corner_radius=0)
    frame_PPD4.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER)

    frame_PPD5 = CTk.CTkFrame(master=poli_penyakit_dalam_window, width=352, height=80, corner_radius=0)
    frame_PPD5.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    dokter_4_PPD = ImageTk.PhotoImage(Image.open("dr.lena.jpeg"))
    image_label_PPD4 = CTk.CTkLabel(master=poli_penyakit_dalam_window, image=dokter_4_PPD, text="", fg_color="transparent")
    image_label_PPD4.place(x=295, y=388)

    label_PPD7 = CTk.CTkLabel(master=frame_PPD4, text="dr. Lena, Sp.PD", font=("Century Gothic", 13))
    label_PPD7.place(x=10, y=5)

    label_PPD8 = CTk.CTkLabel(master=frame_PPD4, text="Spesialis Penyakit Dalam", font=("Century Gothic", 10))
    label_PPD8.place(x=10, y=27)

    button_PPD4 = CTk.CTkButton(master=frame_PPD4, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_penyakit_dalam_Lena)
    button_PPD4.place(x=10, y=50)

    dokter_5_PPD = ImageTk.PhotoImage(Image.open("dr.andi.jpg"))
    image_label_PPD5 = CTk.CTkLabel(master=poli_penyakit_dalam_window, image=dokter_5_PPD, text="", fg_color="transparent")
    image_label_PPD5.place(x=24, y=504)

    label_PPD9 = CTk.CTkLabel(master=frame_PPD5, text="dr. Andi, Sp.PD", font=("Century Gothic", 13))
    label_PPD9.place(x=85, y=5)

    label_PPD10 = CTk.CTkLabel(master=frame_PPD5, text="Spesialis Penyakit Dalam", font=("Century Gothic", 10))
    label_PPD10.place(x=85, y=27)

    button_PPD5 = CTk.CTkButton(master=frame_PPD5, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_penyakit_dalam_Andi)
    button_PPD5.place(x=80, y=50)

    frame_poli_penyakit_dalam4 = CTk.CTkFrame(master=poli_penyakit_dalam_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_poli_penyakit_dalam4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=poli_penyakit_dalam_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=poli_penyakit_dalam_window.destroy)
    button_back.place(x=0,y=0)

# <===========================================batas poli penyakit dalam==================================================================>

def poli_anak_Zoe():
    Zoe_window = CTk.CTkToplevel(app)
    Zoe_window.geometry("400x680+100+15")
    Zoe_window.title("Poli Anak Zoe")
    Zoe_window.resizable(False, False)
    Zoe_window.grab_set()

    background = CTk.CTkLabel(master=Zoe_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Zoe1 = CTk.CTkFrame(master=Zoe_window, width=372, height=600, corner_radius=0)
    frame_Zoe1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Zoe2 = CTk.CTkFrame(master=Zoe_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Zoe2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Zoe = ImageTk.PhotoImage(Image.open("dr.Zoe.jpg"))
    image_label_Zoe = CTk.CTkLabel(master=Zoe_window, image=img_Zoe, text="", fg_color="transparent")
    image_label_Zoe.place(x=24, y=63)

    label_Zoe1 = CTk.CTkLabel(master=frame_Zoe2, text="dr. Zoe, Sp.A", font=("Century Gothic", 13))
    label_Zoe1.place(x=85, y=5)

    label_Zoe2 = CTk.CTkLabel(master=frame_Zoe2, text="Spesialis Anak", font=("Century Gothic", 10))
    label_Zoe2.place(x=85, y=27)

    frame_Zoe3 = CTk.CTkFrame(master=Zoe_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Zoe3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Zoe = CTk.CTkLabel(master=frame_Zoe3, text="Biodata dr. Zoe, Sp.A", font=("Century Gothic", 13))
    label_biodata_Zoe.place(x=10, y=10)

    label_Zoe3 = CTk.CTkLabel(master=frame_Zoe3, text="Dokter Umum, Universitas Gadjah Mada, 2007\nSpesialis Anak, Universitas Padjadjaran, 2015\nMenjadi dokter spesialis anak selama 9 tahun", font=("Century Gothic", 13), justify="left")
    label_Zoe3.place(x=10, y=35)

    def save_jadwal_and_transfer_Zoe(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_anak2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_anak2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan Berhasil")
        Zoe_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Zoe(selected_time):
        try:
            with open("poli_anak2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count 

    selected_jadwal_zoe = tkinter.StringVar()

    jadwal_zoe1 = "Rabu, 07:00 - 13:00"
    jadwal_zoe2 = "Jumat, 15:00 - 21:00"

    label_jadwal_Zoe = CTk.CTkLabel(master=frame_Zoe1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_Zoe.place(x=150, y=300)

    jadwal_Zoe1 = CTk.CTkRadioButton(master=frame_Zoe1, text=jadwal_zoe1, variable=selected_jadwal_zoe, value=jadwal_zoe1)
    jadwal_Zoe1.place(x=10, y=350)

    jadwal_Zoe2 = CTk.CTkRadioButton(master=frame_Zoe1, text=jadwal_zoe2, variable=selected_jadwal_zoe, value=jadwal_zoe2)
    jadwal_Zoe2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Zoe1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Zoe(selected_jadwal_zoe.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Zoe(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Zoe(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Zoe(selected_jadwal):
        selected_time = selected_jadwal_zoe.get()

        current_booking_count = get_jadwal_Zoe(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Zoe_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Zoe4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Zoe4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info = CTk.CTkLabel(master=frame_Zoe4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info.place(x=10, y=10)
        
        label_payment = CTk.CTkLabel(master=frame_Zoe4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment.place(x=10, y=50)

        label_antrian = CTk.CTkLabel(master=frame_Zoe4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Zoe(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Zoe("dr. Zoe, Sp.A", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Zoe(jadwal_Zoe1, jadwal_zoe1)
    check_and_disable_jadwal_Zoe(jadwal_Zoe2, jadwal_zoe2)

    frame_Zoe4 = CTk.CTkFrame(master=Zoe_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Zoe4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Zoe_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Zoe_window.destroy)
    button_back.place(x=0,y=0)


def poli_anak_Samuel():
    Samuel_window = CTk.CTkToplevel(app)
    Samuel_window.geometry("400x680+100+15")
    Samuel_window.title("Poli Anak Samuel")
    Samuel_window.resizable(False, False)
    Samuel_window.grab_set()

    background = CTk.CTkLabel(master=Samuel_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Samuel1 = CTk.CTkFrame(master=Samuel_window, width=372, height=600, corner_radius=0)
    frame_Samuel1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Samuel2 = CTk.CTkFrame(master=Samuel_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Samuel2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Samuel = ImageTk.PhotoImage(Image.open("dr.Samuel, Sp.A.png"))
    image_label_Samuel = CTk.CTkLabel(master=Samuel_window, image=img_Samuel, text="", fg_color="transparent")
    image_label_Samuel.place(x=24, y=63)

    label_Samuel1 = CTk.CTkLabel(master=frame_Samuel2, text="dr.Samuel, Sp.A", font=("Century Gothic", 13))
    label_Samuel1.place(x=85, y=5)

    label_Samuel2 = CTk.CTkLabel(master=frame_Samuel2, text="Spesialis Anak", font=("Century Gothic", 10))
    label_Samuel2.place(x=85, y=27)

    frame_Samuel3 = CTk.CTkFrame(master=Samuel_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Samuel3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Samuel = CTk.CTkLabel(master=frame_Samuel3, text="Biodata dr.Samuel, Sp.A", font=("Century Gothic", 13))
    label_biodata_Samuel.place(x=10, y=10)

    label_Samuel3 = CTk.CTkLabel(master=frame_Samuel3, text="Dokter Umum, Universitas Gadjah Mada, 2003\nSpesialis Anak, Universitas Diponegoro, 2009\nMenjadi dokter spesialis anak selama 5 tahun", font=("Century Gothic", 13), justify="left")
    label_Samuel3.place(x=10, y=35)

    def save_jadwal_and_transfer_Samuel(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_anak2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_anak2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan Berhasil")
        Samuel_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Samuel(selected_time):
        try:
            with open("poli_anak2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count 

    selected_jadwal_samuel = tkinter.StringVar()

    jadwal_samuel1 = "Senin, 15:00 - 21:00"
    jadwal_samuel2 = "Kamis, 07:00 - 13:00"

    label_jadwal_Samuel = CTk.CTkLabel(master=frame_Samuel1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_Samuel.place(x=150, y=300)

    jadwal_Samuel1 = CTk.CTkRadioButton(master=frame_Samuel1, text=jadwal_samuel1, variable=selected_jadwal_samuel, value=jadwal_samuel1)
    jadwal_Samuel1.place(x=10, y=350)

    jadwal_Samuel2 = CTk.CTkRadioButton(master=frame_Samuel1, text=jadwal_samuel2, variable=selected_jadwal_samuel, value=jadwal_samuel2)
    jadwal_Samuel2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Samuel1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Samuel(selected_jadwal_samuel.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Samuel(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Samuel(selected_time)

        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Samuel(selected_jadwal):
        selected_time = selected_jadwal_samuel.get()

        current_booking_count = get_jadwal_Samuel(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Samuel_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Samuel4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Samuel4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Samuel = CTk.CTkLabel(master=frame_Samuel4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Samuel.place(x=10, y=10)
        
        label_payment_Samuel = CTk.CTkLabel(master=frame_Samuel4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Samuel.place(x=10, y=50)

        label_antrian_Samuel = CTk.CTkLabel(master=frame_Samuel4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Samuel.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Samuel(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Samuel("dr.Samuel, Sp.A", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Samuel(jadwal_Samuel1, jadwal_samuel1)
    check_and_disable_jadwal_Samuel(jadwal_Samuel2, jadwal_samuel2)

    frame_Samuel4 = CTk.CTkFrame(master=Samuel_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Samuel4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Samuel_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Samuel_window.destroy)
    button_back.place(x=0,y=0)

def poli_anak_Jay():
    Jay_window = CTk.CTkToplevel(app)
    Jay_window.geometry("400x680+100+15")
    Jay_window.title("Poli Anak Jay")
    Jay_window.resizable(False, False)
    Jay_window.grab_set()

    background = CTk.CTkLabel(master=Jay_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Jay1 = CTk.CTkFrame(master=Jay_window, width=372, height=600, corner_radius=0)
    frame_Jay1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Jay2 = CTk.CTkFrame(master=Jay_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Jay2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Jay = ImageTk.PhotoImage(Image.open("dr. Jay, Sp.A.png"))
    image_label_Jay = CTk.CTkLabel(master=Jay_window, image=img_Jay, text="", fg_color="transparent")
    image_label_Jay.place(x=24, y=63)

    label_Jay1 = CTk.CTkLabel(master=frame_Jay2, text="dr. Jay, Sp.A", font=("Century Gothic", 13))
    label_Jay1.place(x=85, y=5)

    label_Jay2 = CTk.CTkLabel(master=frame_Jay2, text="Spesialis Anak", font=("Century Gothic", 10))
    label_Jay2.place(x=85, y=27)

    frame_Jay3 = CTk.CTkFrame(master=Jay_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Jay3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Jay = CTk.CTkLabel(master=frame_Jay3, text="Biodata dr. Jay, Sp.A", font=("Century Gothic", 13))
    label_biodata_Jay.place(x=10, y=10)

    label = CTk.CTkLabel(master=frame_Jay3, text="Dokter Umum, Universitas Brawijaya, 2004\nSpesialis Anak, Universitas Airlangga, 2010\nMenjadi dokter spesialis anak selama 7 tahun", font=("Century Gothic", 13), justify="left")
    label.place(x=10, y=35)

    def save_jadwal_and_transfer_Jay(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_anak2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_anak2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Succes", "Pemesanan Berhasil")
        Jay_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Jay(selected_time):
        try:
            with open("poli_anak2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count 

    selected_jadwal_jay = tkinter.StringVar()

    jadwal_jay1 = "Selasa, 07:00 - 13:00"
    jadwal_jay2 = "Kamis, 15:00 - 21:00"

    label_jadwal_Jay = CTk.CTkLabel(master=frame_Jay1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_Jay.place(x=150, y=300)

    jadwal_Jay1 = CTk.CTkRadioButton(master=frame_Jay1, text=jadwal_jay1, variable=selected_jadwal_jay, value=jadwal_jay1)
    jadwal_Jay1.place(x=10, y=350)

    jadwal_Jay2 = CTk.CTkRadioButton(master=frame_Jay1, text=jadwal_jay2, variable=selected_jadwal_jay, value=jadwal_jay2)
    jadwal_Jay2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Jay1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Jay(selected_jadwal_jay.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Jay(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Jay(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Jay(selected_jadwal):
        selected_time = selected_jadwal_jay.get()

        current_booking_count = get_jadwal_Jay(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Jay_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Jay4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Jay4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Jay = CTk.CTkLabel(master=frame_Jay4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Jay.place(x=10, y=10)
        
        label_payment_Jay = CTk.CTkLabel(master=frame_Jay4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Jay.place(x=10, y=50)

        label_antrian_Jay = CTk.CTkLabel(master=frame_Jay4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Jay.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Jay(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Jay("dr. Jay, Sp.A", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Jay(jadwal_Jay1, jadwal_jay1)
    check_and_disable_jadwal_Jay(jadwal_Jay2, jadwal_jay2)

    frame_Jay4 = CTk.CTkFrame(master=Jay_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Jay4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Jay_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Jay_window.destroy)
    button_back.place(x=0,y=0)

def poli_anak_Ray():
    Ray_window = CTk.CTkToplevel(app)
    Ray_window.geometry("400x680+100+15")
    Ray_window.title("Poli Anak Ray")
    Ray_window.resizable(False, False)
    Ray_window.grab_set()

    background = CTk.CTkLabel(master=Ray_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Ray1 = CTk.CTkFrame(master=Ray_window, width=372, height=600, corner_radius=0)
    frame_Ray1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Ray2 = CTk.CTkFrame(master=Ray_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Ray2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Ray = ImageTk.PhotoImage(Image.open("dr.Ray.jpg"))
    image_label_Ray = CTk.CTkLabel(master=Ray_window, image=img_Ray, text="", fg_color="transparent")
    image_label_Ray.place(x=24, y=63)

    label_Ray1 = CTk.CTkLabel(master=frame_Ray2, text="dr. Ray, Sp.A", font=("Century Gothic", 13))
    label_Ray1.place(x=85, y=5)

    label_Ray2 = CTk.CTkLabel(master=frame_Ray2, text="Spesialis Anak", font=("Century Gothic", 10))
    label_Ray2.place(x=85, y=27)

    frame_Ray3 = CTk.CTkFrame(master=Ray_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Ray3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Ray = CTk.CTkLabel(master=frame_Ray3, text="Biodata dr. Ray, Sp.A", font=("Century Gothic", 13))
    label_biodata_Ray.place(x=10, y=10)

    label = CTk.CTkLabel(master=frame_Ray3, text="Dokter Umum, Universitas Indonesia, 2005\nSpesialis Anak, Universitas Airlangga, 2013\nMenjadi dokter spesialis anak selama 10 tahun", font=("Century Gothic", 13), justify="left")
    label.place(x=10, y=35)

    def save_jadwal_and_transfer_Ray(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_anak2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_anak2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success", "Pemesanan Berhasil")
        Ray_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Ray(selected_time):
        try:
            with open("poli_anak2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count 

    selected_jadwal_Ray = tkinter.StringVar()

    jadwal_ray1 = "Selasa, 15:00 - 21:00"
    jadwal_ray2 = "Jumat, 07:00 - 13:00"

    label_jadwal_Ray = CTk.CTkLabel(master=frame_Ray1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_Ray.place(x=150, y=300)

    jadwal_Ray1 = CTk.CTkRadioButton(master=frame_Ray1, text=jadwal_ray1, variable=selected_jadwal_Ray, value=jadwal_ray1)
    jadwal_Ray1.place(x=10, y=350)

    jadwal_Ray2 = CTk.CTkRadioButton(master=frame_Ray1, text=jadwal_ray2, variable=selected_jadwal_Ray, value=jadwal_ray2)
    jadwal_Ray2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Ray1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Ray(selected_jadwal_Ray.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Ray(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Ray(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Ray(selected_jadwal):
        selected_time = selected_jadwal_Ray.get()

        current_booking_count = get_jadwal_Ray(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Ray_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Ray4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Ray4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Ray = CTk.CTkLabel(master=frame_Ray4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Ray.place(x=10, y=10)
        
        label_payment_Ray = CTk.CTkLabel(master=frame_Ray4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Ray.place(x=10, y=50)

        label_antrian_Ray = CTk.CTkLabel(master=frame_Ray4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Ray.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Ray(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Ray("dr. Ray Sp.A", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Ray(jadwal_Ray1, jadwal_ray1)
    check_and_disable_jadwal_Ray(jadwal_Ray2, jadwal_ray2)

    frame_Ray4 = CTk.CTkFrame(master=Ray_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Ray4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Ray_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Ray_window.destroy)
    button_back.place(x=0,y=0)

def poli_anak_Angelica():
    angelica_window = CTk.CTkToplevel(app)
    angelica_window.geometry("400x680+100+15")
    angelica_window.title("Poli Anak Angelica")
    angelica_window.resizable(False, False)
    angelica_window.grab_set()

    background = CTk.CTkLabel(master=angelica_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Angelica1 = CTk.CTkFrame(master=angelica_window, width=372, height=600, corner_radius=0)
    frame_Angelica1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Angelica2 = CTk.CTkFrame(master=angelica_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Angelica2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Angelica = ImageTk.PhotoImage(Image.open("dr.Angelica, Sp.A.png"))
    image_label_Angelica = CTk.CTkLabel(master=angelica_window, image=img_Angelica, text="", fg_color="transparent")
    image_label_Angelica.place(x=24, y=63)

    label_Angelica1 = CTk.CTkLabel(master=frame_Angelica2, text="dr.Angelica, Sp.A", font=("Century Gothic", 13))
    label_Angelica1.place(x=85, y=5)

    label_Angelica2 = CTk.CTkLabel(master=frame_Angelica2, text="Spesialis Anak", font=("Century Gothic", 10))
    label_Angelica2.place(x=85, y=27)

    frame_Angelica3 = CTk.CTkFrame(master=angelica_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Angelica3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Angelica = CTk.CTkLabel(master=frame_Angelica3, text="Biodata dr.Angelica, Sp.A", font=("Century Gothic", 13))
    label_biodata_Angelica.place(x=10, y=10)

    label_Angelica3 = CTk.CTkLabel(master=frame_Angelica3, text="Dokter Anak, Universitas Padjadjaran, 2007\nSpesialis Anak, Universitas Hasanuddin, 2013\nMenjadi dokter spesialis anak selama 5 tahun", font=("Century Gothic", 13), justify="left")
    label_Angelica3.place(x=10, y=35)

    def save_jadwal_and_transfer_Angelica(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_anak2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_anak2.json", "w") as file:
            json.dump(booking_data, file, indent=4)

        messagebox.showinfo("Success", "Pemesanan Berhasil")
        angelica_window.destroy()
        
        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Angelica(selected_time):
        try:
            with open("poli_anak2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count 

    selected_jadwal_angelica = tkinter.StringVar()

    jadwal_angelica1 = "Senin, 07:00 - 13:00"
    jadwal_angelica2 = "Rabu, 15:00 - 21:00"

    label_jadwal_Angelica = CTk.CTkLabel(master=frame_Angelica1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_Angelica.place(x=150, y=300)

    jadwal_Angelica1 = CTk.CTkRadioButton(master=frame_Angelica1, text=jadwal_angelica1, variable=selected_jadwal_angelica, value=jadwal_angelica1)
    jadwal_Angelica1.place(x=10, y=350)

    jadwal_Angelica2 = CTk.CTkRadioButton(master=frame_Angelica1, text=jadwal_angelica2, variable=selected_jadwal_angelica, value=jadwal_angelica2)
    jadwal_Angelica2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Angelica1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Angelica(selected_jadwal_angelica.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Angelica(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Angelica(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Angelica(selected_jadwal):

        selected_time = selected_jadwal_angelica.get()

        current_booking_count = get_jadwal_Angelica(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=angelica_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Angelica4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Angelica4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Angelica = CTk.CTkLabel(master=frame_Angelica4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Angelica.place(x=10, y=10)
        
        label_payment_Angelica = CTk.CTkLabel(master=frame_Angelica4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Angelica.place(x=10, y=50)

        label_antrian_Angelica = CTk.CTkLabel(master=frame_Angelica4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Angelica.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Angelica(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Angelica("dr.Angelica, Sp.A", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Angelica(jadwal_Angelica1, jadwal_angelica1)
    check_and_disable_jadwal_Angelica(jadwal_Angelica2, jadwal_angelica2)

    frame_Angelica4 = CTk.CTkFrame(master=angelica_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Angelica4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=angelica_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=angelica_window.destroy)
    button_back.place(x=0,y=0)

def poli_anak():
    poli_anak_window = CTk.CTkToplevel(app)
    poli_anak_window.geometry("400x680+100+15")
    poli_anak_window.title("Poli Anak")
    poli_anak_window.resizable("False", "False")
    poli_anak_window.grab_set()

    background = CTk.CTkLabel(master=poli_anak_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_PA1 = CTk.CTkFrame(master=poli_anak_window, width=352, height=80, corner_radius=0)
    frame_PA1.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER)

    dokter_1_PA= ImageTk.PhotoImage(Image.open("dr.Angelica, Sp.A.png"))
    image_label_PA1 = CTk.CTkLabel(master=poli_anak_window, image=dokter_1_PA, text="", fg_color="transparent")
    image_label_PA1.place(x=24, y=48)

    label_PA1 = CTk.CTkLabel(master=frame_PA1, text="dr.Angelica, Sp.A", font=("Century Gothic", 13))
    label_PA1.place(x=85, y=7)

    label_PA2 = CTk.CTkLabel(master=frame_PA1, text="Spesialis Anak", font=("Century Gothic", 10))
    label_PA2.place(x=85, y=27)

    button_PA1 = CTk.CTkButton(master=frame_PA1, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_anak_Angelica)
    button_PA1.place(x=80, y=50)

    frame_PA2 = CTk.CTkFrame(master=poli_anak_window, width=352, height=80, corner_radius=0)
    frame_PA2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    dokter_2_PA = ImageTk.PhotoImage(Image.open("dr.Samuel, Sp.A.png"))
    image_label_PA2 = CTk.CTkLabel(master=poli_anak_window, image=dokter_2_PA, text="", fg_color="transparent")
    image_label_PA2.place(x=295, y=165)

    label_PA3 = CTk.CTkLabel(master=frame_PA2, text="dr.Samuel, Sp.A", font=("Century Gothic", 13))
    label_PA3.place(x=10, y=7)

    label_PA4 = CTk.CTkLabel(master=frame_PA2, text="Spesialis Anak", font=("Century Gothic", 10))
    label_PA4.place(x=10, y=27)

    button_PA2 = CTk.CTkButton(master=frame_PA2, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_anak_Samuel)
    button_PA2.place(x=10, y=50)

    frame_PA3 = CTk.CTkFrame(master=poli_anak_window, width=352, height=80, corner_radius=0)
    frame_PA3.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)

    dokter_3_PA = ImageTk.PhotoImage(Image.open("dr. Jay, Sp.A.png"))
    image_label_PA3 = CTk.CTkLabel(master=poli_anak_window, image=dokter_3_PA, text="", fg_color="transparent")
    image_label_PA3.place(x=24, y=280)

    label_PA5 = CTk.CTkLabel(master=frame_PA3, text="dr.Jay, Sp.A", font=("Century Gothic", 13))
    label_PA5.place(x=85, y=7)

    label_PA6 = CTk.CTkLabel(master=frame_PA3, text="Spesialis Anak", font=("Century Gothic", 10))
    label_PA6.place(x=85, y=27)

    button_PA3 = CTk.CTkButton(master=frame_PA3, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_anak_Jay)
    button_PA3.place(x=85, y=50)

    frame_PA4 = CTk.CTkFrame(master=poli_anak_window, width=352, height=80, corner_radius=0)
    frame_PA4.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER)

    frame_PA5 = CTk.CTkFrame(master=poli_anak_window, width=352, height=80, corner_radius=0)
    frame_PA5.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    dokter_4_PA = ImageTk.PhotoImage(Image.open("dr.Ray.jpg"))
    image_label_PA4 = CTk.CTkLabel(master=poli_anak_window, image=dokter_4_PA, text="", fg_color="transparent")
    image_label_PA4.place(x=295, y=388)

    label_PA7 = CTk.CTkLabel(master=frame_PA4, text="dr.Ray, Sp.A", font=("Century Gothic", 13))
    label_PA7.place(x=10, y=5)

    label_PA8 = CTk.CTkLabel(master=frame_PA4, text="Spesialis Anak", font=("Century Gothic", 10))
    label_PA8.place(x=10, y=27)

    button_PA4 = CTk.CTkButton(master=frame_PA4, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_anak_Ray)
    button_PA4.place(x=10, y=50)

    dokter_5_PA = ImageTk.PhotoImage(Image.open("dr.Zoe.jpg"))
    image_label_PA5 = CTk.CTkLabel(master=poli_anak_window, image=dokter_5_PA, text="", fg_color="transparent")
    image_label_PA5.place(x=24, y=504)

    label_PA9 = CTk.CTkLabel(master=frame_PA5, text="dr.Zoe, Sp.A", font=("Century Gothic", 13))
    label_PA9.place(x=85, y=5)

    label_PA10 = CTk.CTkLabel(master=frame_PA5, text="Spesialis Anak", font=("Century Gothic", 10))
    label_PA10.place(x=85, y=27)

    button_PA5 = CTk.CTkButton(master=frame_PA5, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_anak_Zoe)
    button_PA5.place(x=80, y=50)

    frame_poli_anak4 = CTk.CTkFrame(master=poli_anak_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_poli_anak4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=poli_anak_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=poli_anak_window.destroy)
    button_back.place(x=0,y=0)

#<==========================================================Batas Poli Anak====================================================================>

def poli_umum_Allison():
    Allison_window = CTk.CTkToplevel(app)
    Allison_window.geometry("400x680+100+15")
    Allison_window.title("Poli Umum Allison")
    Allison_window.resizable(False, False)
    Allison_window.grab_set()

    background = CTk.CTkLabel(master=Allison_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Allison1 = CTk.CTkFrame(master=Allison_window, width=372, height=600, corner_radius=0)
    frame_Allison1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Allison2 = CTk.CTkFrame(master=Allison_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Allison2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Allison = ImageTk.PhotoImage(Image.open("Poli Umum_dr. Allison Renee.png"))
    image_label_Allison = CTk.CTkLabel(master=Allison_window, image=img_Allison, text="", fg_color="transparent")
    image_label_Allison.place(x=24, y=63)

    label_Allison1 = CTk.CTkLabel(master=frame_Allison2, text="dr. Allison Renee", font=("Century Gothic", 13))
    label_Allison1.place(x=85, y=5)

    label_Allison2 = CTk.CTkLabel(master=frame_Allison2, text="Dokter Umum", font=("Century Gothic", 10))
    label_Allison2.place(x=85, y=27)

    frame_Allison3 = CTk.CTkFrame(master=Allison_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Allison3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Allison = CTk.CTkLabel(master=frame_Allison3, text="Biodata dr. Allison", font=("Century Gothic", 13))
    label_biodata_Allison.place(x=10, y=10)

    label_Allison3 = CTk.CTkLabel(master=frame_Allison3, text="Dokter Umum, Universitas Gadjah Mada, 2012\nProgram Dokter, Universitas Gadjah Mada, 2014\nMenjadi Dokter Umum selama 5 tahun", font=("Century Gothic", 13), justify="left")
    label_Allison3.place(x=10, y=35)

    def save_jadwal_and_transfer_Allison(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_umum2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_umum2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success","Pemesanan Berhasil")
        Allison_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Allison(selected_time):
        try:
            with open("poli_umum2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry.get("jadwal yang terpilih") == selected_time)

        return count

    selected_jadwal_Allison = tkinter.StringVar()

    jadwal_allison1 = "Senin, 07:00 - 13:00"
    jadwal_allison2 = "Rabu, 15:00 - 21:00"
    
    label_jadwal_Allison = CTk.CTkLabel(master=frame_Allison1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_Allison.place(x=150, y=300)

    jadwal_Allison1 = CTk.CTkRadioButton(master=frame_Allison1, text=jadwal_allison1, variable=selected_jadwal_Allison, value=jadwal_allison1)
    jadwal_Allison1.place(x=10, y=350)

    jadwal_Allison2 = CTk.CTkRadioButton(master=frame_Allison1, text=jadwal_allison2, variable=selected_jadwal_Allison, value=jadwal_allison2)
    jadwal_Allison2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Allison1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Allison(selected_jadwal_Allison.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Allison(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Allison(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Allison(selected_jadwal):
        selected_time = selected_jadwal_Allison.get()

        current_booking_count = get_jadwal_Allison(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Allison_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Allison4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Allison4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Allison = CTk.CTkLabel(master=frame_Allison4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Allison.place(x=10, y=10)
        
        label_payment_Allison = CTk.CTkLabel(master=frame_Allison4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Allison.place(x=10, y=50)

        label_antrian_Allison = CTk.CTkLabel(master=frame_Allison4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Allison.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Allison(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Allison("dr. Allison Renne", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Allison(jadwal_Allison1, jadwal_allison1)
    check_and_disable_jadwal_Allison(jadwal_Allison2, jadwal_allison2)

    frame_Allison4 = CTk.CTkFrame(master=Allison_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Allison4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Allison_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Allison_window.destroy)
    button_back.place(x=0,y=0)

def poli_umum_Lily():
    Lily_window = CTk.CTkToplevel(app)
    Lily_window.geometry("400x680+100+15")
    Lily_window.title("Poli Umum Lily")
    Lily_window.resizable(False, False)
    Lily_window.grab_set()

    background = CTk.CTkLabel(master=Lily_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Lily1 = CTk.CTkFrame(master=Lily_window, width=372, height=600, corner_radius=0)
    frame_Lily1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Lily2 = CTk.CTkFrame(master=Lily_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Lily2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Lily = ImageTk.PhotoImage(Image.open("dr.Lily.jpg"))
    image_label_Lily = CTk.CTkLabel(master=Lily_window, image=img_Lily, text="", fg_color="transparent")
    image_label_Lily.place(x=24, y=63)

    label_Lily1 = CTk.CTkLabel(master=frame_Lily2, text="dr. Lily Thompson", font=("Century Gothic", 13))
    label_Lily1.place(x=85, y=5)

    label_Lily2 = CTk.CTkLabel(master=frame_Lily2, text="DOkter Umum", font=("Century Gothic", 10))
    label_Lily2.place(x=85, y=27)

    frame_Lily3 = CTk.CTkFrame(master=Lily_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Lily3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Lily = CTk.CTkLabel(master=frame_Lily3, text="Biodata dr. Lily Thompson", font=("Century Gothic", 13))
    label_biodata_Lily.place(x=10, y=10)

    label_Lily3 = CTk.CTkLabel(master=frame_Lily3, text="Dokter Umum, Universitas Indonesia, 2010\nProgram Dokter, Universitas Indonesia, 2012\nDokter Umum selama 7 tahun", font=("Century Gothic", 13), justify="left")
    label_Lily3.place(x=10, y=35)

    def save_jadwal_and_transfer_Lily(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_umum2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_umum2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo("Success", "Pemesanan Berhasil")
        Lily_window.destroy()

        try:
            with open("pesanan user.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = []

        user_data.append(data)
        
        with open("pesanan user.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def get_jadwal_Lily(selected_time):
        try:
            with open("poli_umum2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry.get("jadwal yang terpilih") == selected_time)

        return count

    selected_jadwal_Lily = tkinter.StringVar()

    jadwal_lily1 = "Rabu, 07:00 - 13:00"
    jadwal_lily2 = "Jumat, 15:00 - 21:00"
    
    label_jadwal_Lily = CTk.CTkLabel(master=frame_Lily1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_Lily.place(x=150, y=300)

    jadwal_Lily1 = CTk.CTkRadioButton(master=frame_Lily1, text=jadwal_lily1, variable=selected_jadwal_Lily, value=jadwal_lily1)
    jadwal_Lily1.place(x=10, y=350)

    jadwal_Lily2 = CTk.CTkRadioButton(master=frame_Lily1, text=jadwal_lily2, variable=selected_jadwal_Lily, value=jadwal_lily2)
    jadwal_Lily2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Lily1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Lily(selected_jadwal_Lily.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Lily(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Lily(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Lily(selected_jadwal):
        selected_time = selected_jadwal_Lily.get()

        current_booking_count = get_jadwal_Lily(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Lily_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Lily4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Lily4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Lily = CTk.CTkLabel(master=frame_Lily4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Lily.place(x=10, y=10)
        
        label_payment_Lily = CTk.CTkLabel(master=frame_Lily4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Lily.place(x=10, y=50)

        label_antrian_Lily = CTk.CTkLabel(master=frame_Lily4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Lily.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Lily(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Lily("dr. Lily Thompson", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path

    check_and_disable_jadwal_Lily(jadwal_Lily1, jadwal_lily1)
    check_and_disable_jadwal_Lily(jadwal_Lily2, jadwal_lily2)

    frame_Lily4 = CTk.CTkFrame(master=Lily_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Lily4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Lily_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Lily_window.destroy)
    button_back.place(x=0,y=0)

def poli_umum_Grace():
    Grace_window = CTk.CTkToplevel(app)
    Grace_window.geometry("400x680+100+15")
    Grace_window.title("Poli Umum Grace")
    Grace_window.resizable(False, False)
    Grace_window.grab_set()

    background = CTk.CTkLabel(master=Grace_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Grace1 = CTk.CTkFrame(master=Grace_window, width=372, height=600, corner_radius=0)
    frame_Grace1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Grace2 = CTk.CTkFrame(master=Grace_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Grace2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Grace = ImageTk.PhotoImage(Image.open("Poli Umum_dr.Grace Mitcell.png"))
    image_label_Grace = CTk.CTkLabel(master=Grace_window, image=img_Grace, text="", fg_color="transparent")
    image_label_Grace.place(x=24, y=63)

    label_Grace1 = CTk.CTkLabel(master=frame_Grace2, text="dr.Grace Mitcellsss", font=("Century Gothic", 13))
    label_Grace1.place(x=85, y=5)

    label_Grace2 = CTk.CTkLabel(master=frame_Grace2, text="Dokter Umum", font=("Century Gothic", 10))
    label_Grace2.place(x=85, y=27)

    frame_Grace3 = CTk.CTkFrame(master=Grace_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Grace3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata = CTk.CTkLabel(master=frame_Grace3, text="Biodata dr. Grace", font=("Century Gothic", 13))
    label_biodata.place(x=10, y=10)

    label_Grace3 = CTk.CTkLabel(master=frame_Grace3, text="Dokter Umum, Universitas Airlangga, 2011\nProgram Dokter, Universitas Airlangga, 2013\nMenjadi Dokter Umum selama 5 tahun", font=("Century Gothic", 13), justify="left")
    label_Grace3.place(x=10, y=35)

    def save_jadwal_and_transfer_Grace(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_umum2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_umum2.json", "w") as file:
            json.dump(booking_data, file, indent=4)
        messagebox.showinfo('Success', "Pemesanan Berhasil")
        Grace_window.destroy()


    def get_jadwal_Grace(selected_time):
        try:
            with open("poli_umum2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry.get("jadwal yang terpilih") == selected_time)

        return count

    selected_jadwal_Grace = tkinter.StringVar()

    jadwal_grace1 = "Selasa, 07:00 - 13:00"
    jadwal_grace2 = "Kamis, 15:00 - 21:00"

    label_jadwal_Grace = CTk.CTkLabel(master=frame_Grace1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_Grace.place(x=150, y=300)

    jadwal_Grace1 = CTk.CTkRadioButton(master=frame_Grace1, text=jadwal_grace1, variable=selected_jadwal_Grace, value=jadwal_grace1)
    jadwal_Grace1.place(x=10, y=350)

    jadwal_Grace2 = CTk.CTkRadioButton(master=frame_Grace1, text=jadwal_grace2, variable=selected_jadwal_Grace, value=jadwal_grace2)
    jadwal_Grace2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Grace1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Grace(selected_jadwal_Grace.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Grace(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Grace(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Grace(selected_jadwal):
        selected_time = selected_jadwal_Grace.get()

        current_booking_count = get_jadwal_Grace(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Grace_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Grace = CTk.CTkLabel(master=frame4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Grace.place(x=10, y=10)
        
        label_payment_Grace = CTk.CTkLabel(master=frame4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Grace.place(x=10, y=50)

        label_antrian_Grace = CTk.CTkLabel(master=frame4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Grace.place(x=10, y=90)

        selected_bank = tkinter.StringVar(value="BCA")

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)

        current_booking_number = get_jadwal_Grace(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Grace("dr. Grace Mitcellsss", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path


    check_and_disable_jadwal_Grace(jadwal_Grace1, jadwal_grace1)
    check_and_disable_jadwal_Grace(jadwal_Grace2, jadwal_grace2)

    frame_Grace4 = CTk.CTkFrame(master=Grace_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Grace4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Grace_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Grace_window.destroy)
    button_back.place(x=0,y=0)

def poli_umum_Daniel():
    Daniel_window = CTk.CTkToplevel(app)
    Daniel_window.geometry("400x680+100+15")
    Daniel_window.title("Poli Umum Daniel")
    Daniel_window.resizable(False, False)
    Daniel_window.grab_set()

    background = CTk.CTkLabel(master=Daniel_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Daniel1 = CTk.CTkFrame(master=Daniel_window, width=372, height=600, corner_radius=0)
    frame_Daniel1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Daniel2 = CTk.CTkFrame(master=Daniel_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Daniel2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    img_Daniel = ImageTk.PhotoImage(Image.open("Poli Umum_dr. Daniel Alexander.png"))
    image_label_Daniel = CTk.CTkLabel(master=Daniel_window, image=img_Daniel, text="", fg_color="transparent")
    image_label_Daniel.place(x=24, y=63)

    label_Daniel1 = CTk.CTkLabel(master=frame_Daniel2, text="dr. Daniel Alexander", font=("Century Gothic", 13))
    label_Daniel1.place(x=85, y=5)

    label_Daniel2 = CTk.CTkLabel(master=frame_Daniel2, text="Dokter Umum", font=("Century Gothic", 10))
    label_Daniel2.place(x=85, y=27)

    frame_Daniel3 = CTk.CTkFrame(master=Daniel_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Daniel3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Daniel = CTk.CTkLabel(master=frame_Daniel3, text="Biodata dr. Daniel", font=("Century Gothic", 13))
    label_biodata_Daniel.place(x=10, y=10)

    label = CTk.CTkLabel(master=frame_Daniel3, text="Dokter umum, Universitas Indonesia, 2013\nDokter Umum, Universitas Indonesia, 2013\nProgram Dokter, Universitas Indonesia, 2015", font=("Century Gothic", 13), justify="left")
    label.place(x=10, y=35)

    def save_jadwal_and_transfer_Daniel(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }

        try:
            with open("poli_umum2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []

        booking_data.append(data)  

        with open("poli_umum2.json", "w") as file:
            json.dump(booking_data, file, indent=4)  

        messagebox.showinfo("Success", "Pemesanan Berhasil")
        Daniel_window.destroy()

    def get_jadwal_Daniel(selected_time):
        try:
            with open("poli_umum2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry["jadwal yang terpilih"] == selected_time)

        return count

    selected_jadwal_Daniel = tkinter.StringVar()

    jadwal_daniel1 = "Senin, 15:00 - 21:00"
    jadwal_daniel2 = "Kamis, 07:00 - 13:00"
    
    label1_jadwal_Daniel = CTk.CTkLabel(master=frame_Daniel1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label1_jadwal_Daniel.place(x=150, y=300)

    jadwal_Daniel1 = CTk.CTkRadioButton(master=frame_Daniel1, text=jadwal_daniel1, variable=selected_jadwal_Daniel, value=jadwal_daniel1)
    jadwal_Daniel1.place(x=10, y=350)

    jadwal_Daniel2 = CTk.CTkRadioButton(master=frame_Daniel1, text=jadwal_daniel2, variable=selected_jadwal_Daniel, value=jadwal_daniel2)
    jadwal_Daniel2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Daniel1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Daniel(selected_jadwal_Daniel.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Daniel(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Daniel(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Daniel(selected_jadwal):
        selected_time = selected_jadwal_Daniel.get()

        current_booking_count = get_jadwal_Daniel(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Daniel_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Daniel4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Daniel4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Daniel = CTk.CTkLabel(master=frame_Daniel4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Daniel.place(x=10, y=10)
        
        label_payment_Daniel = CTk.CTkLabel(master=frame_Daniel4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Daniel.place(x=10, y=50)

        label_antrian_Daniel = CTk.CTkLabel(master=frame_Daniel4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Daniel.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        current_booking_number = get_jadwal_Daniel(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Daniel("dr. Daniel Alexander", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path


    check_and_disable_jadwal_Daniel(jadwal_Daniel1, jadwal_daniel1)
    check_and_disable_jadwal_Daniel(jadwal_Daniel2, jadwal_daniel2)

    frame_Daniel4 = CTk.CTkFrame(master=Daniel_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Daniel4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Daniel_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Daniel_window.destroy)
    button_back.place(x=0,y=0)


def poli_umum_Ethan():
    Ethan_window = CTk.CTkToplevel(app)
    Ethan_window.geometry("400x680+100+15")
    Ethan_window.title("Poli Umum Ethan")
    Ethan_window.resizable(False, False)
    Ethan_window.grab_set()

    background = CTk.CTkLabel(master=Ethan_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_Ethan1 = CTk.CTkFrame(master=Ethan_window, width=372, height=600, corner_radius=0)
    frame_Ethan1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    frame_Ethan2 = CTk.CTkFrame(master=Ethan_window, width=352, height=80, corner_radius=0, fg_color="#A5BDD2")
    frame_Ethan2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    global img_Ethan
    img_Ethan = ImageTk.PhotoImage(Image.open("dr. Ethan.jpg"))
    image_label_Ethan = CTk.CTkLabel(master=Ethan_window, image=img_Ethan, text="", fg_color="transparent")
    image_label_Ethan.place(x=24, y=63)

    label_Ethan1 = CTk.CTkLabel(master=frame_Ethan2, text="dr. Ethan Hayes", font=("Century Gothic", 13))
    label_Ethan1.place(x=85, y=5)

    label_Ethan2 = CTk.CTkLabel(master=frame_Ethan2, text="Dokter Umum", font=("Century Gothic", 10))
    label_Ethan2.place(x=85, y=27)

    frame_Ethan3 = CTk.CTkFrame(master=Ethan_window, width=352, height=105, corner_radius=0, fg_color="#A5BDD2")
    frame_Ethan3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    label_biodata_Ethan = CTk.CTkLabel(master=frame_Ethan3, text="Biodata dr. Ethan Hayes", font=("Century Gothic", 13))
    label_biodata_Ethan.place(x=10, y=10)

    label_Ethan3 = CTk.CTkLabel(master=frame_Ethan3, text="Dokter Umum, Universitas Airlangga, 2011\nDokter Umum, Universitas Gadjah Mada, 2013\nProgram Dokter, Universitas Airlangga, 2013", font=("Century Gothic", 13), justify="left")
    label_Ethan3.place(x=10, y=35)

    def save_jadwal_and_transfer_Ethan(doctor_name, selected_time, booking_number, bank_name, file_path):
        data = {
            "nama pemesan": user_saat_ini,
            "nama dokter": doctor_name,
            "jadwal yang terpilih": selected_time,
            "nomor antrean": booking_number,
            "bank": bank_name,
            "bukti transfer": file_path
        }
        
        try:
            with open("poli_umum2.json", "r") as file:
                booking_data = json.load(file)
        except FileNotFoundError:
            booking_data = []
        
        booking_data.append(data)
        
        with open("poli_umum2.json", "w") as file:
            json.dump(booking_data, file, indent=4)

        messagebox.showinfo("Success", "Pemesanan Berhasil")
        Ethan_window.destroy()

    def get_jadwal_Ethan(selected_time):
        try:
            with open("poli_umum2.json", "r") as file:
                schedule_data = json.load(file)
        except FileNotFoundError:
            schedule_data = []

        count = sum(1 for entry in schedule_data if entry.get("jadwal yang terpilih") == selected_time)

        return count

    selected_jadwal_Ethan = tkinter.StringVar()

    jadwal_ethan1 = "Selasa, 15:00 - 21:00"
    jadwal_ethan2 = "Jumat, 07:00 - 13:00"
    
    label_jadwal_Ethan = CTk.CTkLabel(master=frame_Ethan1, text="Pilih Jadwal:", font=("Century Gothic", 12))
    label_jadwal_Ethan.place(x=150, y=300)

    jadwal_Ethan1 = CTk.CTkRadioButton(master=frame_Ethan1, text=jadwal_ethan1, variable=selected_jadwal_Ethan, value=jadwal_ethan1)
    jadwal_Ethan1.place(x=10, y=350)

    jadwal_Ethan2 = CTk.CTkRadioButton(master=frame_Ethan1, text=jadwal_ethan2, variable=selected_jadwal_Ethan, value=jadwal_ethan2)
    jadwal_Ethan2.place(x=10, y=385)

    button_payment = CTk.CTkButton(master=frame_Ethan1, text="Lanjutkan Pembayaran →", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, 
                                    command=lambda: open_transfer_frame_Ethan(selected_jadwal_Ethan.get()))
    button_payment.place(x=100, y=480)

    def check_and_disable_jadwal_Ethan(jadwal_button, selected_time):
        current_booking_count = get_jadwal_Ethan(selected_time)
        
        if current_booking_count >= 100:
            jadwal_button.configure(state=tkinter.DISABLED) 
        else:
            jadwal_button.configure(state=tkinter.NORMAL)

    def open_transfer_frame_Ethan(selected_jadwal):
        selected_time = selected_jadwal_Ethan.get()

        current_booking_count = get_jadwal_Ethan(selected_time)
        
        booking_number = current_booking_count + 1

        transfer_frame = CTk.CTkFrame(master=Ethan_window, width=372, height=600, corner_radius=0)
        transfer_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame_Ethan4 = CTk.CTkFrame(master=transfer_frame, width=352, height=120, corner_radius=0, fg_color="#A5BDD2")
        frame_Ethan4.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Transfer Bank", font=("Century Gothic", 16)).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        CTk.CTkLabel(master=transfer_frame, text="Pilih Bank", font=("Century Gothic", 12)).place(x=20, y=200)

        label_payment_info_Ethan = CTk.CTkLabel(master=frame_Ethan4, text=f"Jadwal: {selected_time}", font=("Century Gothic", 14))
        label_payment_info_Ethan.place(x=10, y=10)
        
        label_payment_Ethan = CTk.CTkLabel(master=frame_Ethan4, text="Total Pembayaran: Rp 200.000,-", font=("Century Gothic", 14))
        label_payment_Ethan.place(x=10, y=50)

        label_antrian_Ethan = CTk.CTkLabel(master=frame_Ethan4, text=f"Antrean ke-{booking_number}", font=("Century Gothic", 14))
        label_antrian_Ethan.place(x=10, y=90)

        selected_bank = tkinter.StringVar()

        CTk.CTkRadioButton(master=transfer_frame, text="BCA", variable=selected_bank, value="BCA").place(x=20, y=230)
        CTk.CTkRadioButton(master=transfer_frame, text="Mandiri", variable=selected_bank, value="Mandiri").place(x=20, y=260)
        CTk.CTkRadioButton(master=transfer_frame, text="BRI", variable=selected_bank, value="BRI").place(x=20, y=290)

        CTk.CTkLabel(master=transfer_frame, text="Nomor VA: 1234567890", font=("Century Gothic", 12)).place(x=20, y=320)

        CTk.CTkLabel(master=transfer_frame, text="Unggah Bukti Transfer", font=("Century Gothic", 12)).place(x=20, y=350)

        global file_label
        file_label = CTk.CTkLabel(master=transfer_frame, text="Belum ada file yang dipilih", font=("Century Gothic", 10))
        file_label.place(x=20, y=378)

        CTk.CTkButton(master=transfer_frame, text="Pilih File", command=select_file).place(x=20, y=400)
        current_booking_number = get_jadwal_Ethan(selected_jadwal) + 1
        CTk.CTkButton(master=transfer_frame, text="Konfirmasi Transfer", 
                    command=lambda: [save_jadwal_and_transfer_Ethan("dr. Ethan Hayes", selected_jadwal, current_booking_number,
                                                                selected_bank.get(), file_label.cget("text"))]).place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    def select_file():
        file_path = filedialog.askopenfilename(title="Pilih Bukti Transfer",
                                            filetypes=[("Gambar", "*.png;*.jpg;*.jpeg"), ("Semua File", "*.*")])
        if file_path:
            file_label.configure(text=file_path)
        return file_path


    check_and_disable_jadwal_Ethan(jadwal_Ethan1, jadwal_ethan1)
    check_and_disable_jadwal_Ethan(jadwal_Ethan2, jadwal_ethan2)

    frame_Ethan4 = CTk.CTkFrame(master=Ethan_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Ethan4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=Ethan_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=Ethan_window.destroy)
    button_back.place(x=0,y=0)

def poli_umum():
    poli_umum_window = CTk.CTkToplevel(app)
    poli_umum_window.geometry("400x680+100+15")
    poli_umum_window.title("Poli Umum")
    poli_umum_window.resizable(False,False)
    poli_umum_window.grab_set()

    background = CTk.CTkLabel(master=poli_umum_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame_PU1 = CTk.CTkFrame(master=poli_umum_window, width=352, height=80, corner_radius=0)
    frame_PU1.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER)
    
    dokter_1_PU = ImageTk.PhotoImage(Image.open("Poli Umum_dr. Allison Renee.png"))
    image_label_PU1 = CTk.CTkLabel(master=poli_umum_window, image=dokter_1_PU, text="", fg_color="transparent")
    image_label_PU1.place(x=24, y=48)

    label_PU1 = CTk.CTkLabel(master=frame_PU1, text="dr. Allison Renee", font=("Century Gothic", 13))
    label_PU1.place(x=85, y=7)

    label_PU2 = CTk.CTkLabel(master=frame_PU1, text="Dokter Umum", font=("Century Gothic", 10))
    label_PU2.place(x=85, y=27)

    button_PU1 = CTk.CTkButton(master=frame_PU1, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_umum_Allison)
    button_PU1.place(x=80, y=50)

    frame_PU2 = CTk.CTkFrame(master=poli_umum_window, width=352, height=80, corner_radius=0)
    frame_PU2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    dokter_2_PU = ImageTk.PhotoImage(Image.open("Poli Umum_dr. Daniel Alexander.png"))
    image_label_PU2 = CTk.CTkLabel(master=poli_umum_window, image=dokter_2_PU, text="", fg_color="transparent")
    image_label_PU2.place(x=295, y=165)

    label_PU3 = CTk.CTkLabel(master=frame_PU2, text="dr. Daniel Alexander", font=("Century Gothic", 13))
    label_PU3.place(x=10, y=7)

    label_PU4 = CTk.CTkLabel(master=frame_PU2, text="Dokter Umum", font=("Century Gothic", 10))
    label_PU4.place(x=10, y=27)

    button_PU2 = CTk.CTkButton(master=frame_PU2, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_umum_Daniel)
    button_PU2.place(x=10, y=50)

    frame_PU3 = CTk.CTkFrame(master=poli_umum_window, width=352, height=80, corner_radius=0)
    frame_PU3.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)

    dokter_3_PU = ImageTk.PhotoImage(Image.open("Poli Umum_dr.Grace Mitcell.png"))
    image_label_PU3 = CTk.CTkLabel(master=poli_umum_window, image=dokter_3_PU, text="", fg_color="transparent")
    image_label_PU3.place(x=24, y=280)

    label_PU5 = CTk.CTkLabel(master=frame_PU3, text="dr.Grace Mitcell", font=("Century Gothic", 13))
    label_PU5.place(x=85, y=7)

    label_PU6 = CTk.CTkLabel(master=frame_PU3, text="Dokter Umum", font=("Century Gothic", 10))
    label_PU6.place(x=85, y=27)

    button_PU3 = CTk.CTkButton(master=frame_PU3, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_umum_Grace)
    button_PU3.place(x=80, y=50)

    frame_PU4 = CTk.CTkFrame(master=poli_umum_window, width=352, height=80, corner_radius=0)
    frame_PU4.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER)

    frame_PU5 = CTk.CTkFrame(master=poli_umum_window, width=352, height=80, corner_radius=0)
    frame_PU5.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    dokter_4_PU = ImageTk.PhotoImage(Image.open("dr. Ethan.jpg"))
    image_label_PU4 = CTk.CTkLabel(master=poli_umum_window, image=dokter_4_PU, text="", fg_color="transparent")
    image_label_PU4.place(x=295, y=388)

    label_PU7 = CTk.CTkLabel(master=frame_PU4, text="dr. Ethan Hayes", font=("Century Gothic", 13))
    label_PU7.place(x=10, y=5)

    label_PU8 = CTk.CTkLabel(master=frame_PU4, text="Dokter Umum", font=("Century Gothic", 10))
    label_PU8.place(x=10, y=27)

    button_PU4 = CTk.CTkButton(master=frame_PU4, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_umum_Ethan)
    button_PU4.place(x=10, y=50)

    dokter_5_PU = ImageTk.PhotoImage(Image.open("dr.Lily.jpg"))
    image_label_PU5 = CTk.CTkLabel(master=poli_umum_window, image=dokter_5_PU, text="", fg_color="transparent")
    image_label_PU5.place(x=24, y=504)

    label_PU9 = CTk.CTkLabel(master=frame_PU5, text="dr. Lily Thompson", font=("Century Gothic", 13))
    label_PU9.place(x=85, y=5)

    label_PU10 = CTk.CTkLabel(master=frame_PU5, text="Dokter Umum", font=("Century Gothic", 10))
    label_PU10.place(x=85, y=27)

    button_PU5 = CTk.CTkButton(master=frame_PU5, text="Pilih Dokter", font=("Century Gothic", 10), width=50, height=20, corner_radius=15, command=poli_umum_Lily)
    button_PU5.place(x=80, y=50)

    frame_Poli_umum4 = CTk.CTkFrame(master=poli_umum_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_Poli_umum4.place(x=0,y=0)

    button_back = CTk.CTkButton(master=frame_Poli_umum4, text="⭠ Back", fg_color="transparent", width=30, text_color="Black", font=("Bahnschrift SemiBold",13),command=poli_umum_window.destroy)
    button_back.place(x=0,y=0)

#<===========================================================Batas Poli Umum=============================================================>

def poli_window():
    poli_window = CTk.CTkToplevel(app)
    poli_window.geometry("400x680+100+15")
    poli_window.title("Poli")
    poli_window.resizable(False,False)
    poli_window.grab_set()

    background = CTk.CTkLabel(master=poli_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame1 = CTk.CTkFrame(master=poli_window, width=152, height=200, corner_radius=0)
    frame1.place(x=45, y=36)

    img1 = ImageTk.PhotoImage(Image.open("gbr poli umum.png"))
    image_label = CTk.CTkLabel(master=poli_window, image=img1, text="", fg_color="transparent")
    image_label.place(x=56, y=55)

    label1 = CTk.CTkLabel(master=frame1, text="Poli Umum", font=("Century Gothic", 13))
    label1.place(x=45, y=105)

    button1 = CTk.CTkButton(master=frame1, text="Daftar", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, command=poli_umum)
    button1.place(x=45, y=135)

    frame2 = CTk.CTkFrame(master=poli_window, width=152, height=200, corner_radius=0)
    frame2.place(x=215, y=36)

    img2 = ImageTk.PhotoImage(Image.open("gbr poli gigi.png"))
    image_label = CTk.CTkLabel(master=poli_window, image=img2, text="", fg_color="transparent")
    image_label.place(x=226, y=55)

    label2 = CTk.CTkLabel(master=frame2, text="Poli Gigi", font=("Century Gothic", 13))
    label2.place(x=50, y=105)

    button2 = CTk.CTkButton(master=frame2, text="Daftar", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, command=poli_gigi)
    button2.place(x=45, y=135)

    frame3 = CTk.CTkFrame(master=poli_window, width=152, height=200, corner_radius=0)
    frame3.place(x=45, y=255)

    img3 = ImageTk.PhotoImage(Image.open("gbr poli jantung.png"))
    image_label = CTk.CTkLabel(master=poli_window, image=img3, text="", fg_color="transparent")
    image_label.place(x=56, y=278)

    label3 = CTk.CTkLabel(master=frame3, text="Poli Jantung", font=("Century Gothic", 13))
    label3.place(x=37, y=107)

    button3 = CTk.CTkButton(master=frame3, text="Daftar", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, command=poli_jantung)
    button3.place(x=45, y=135)

    frame4 = CTk.CTkFrame(master=poli_window, width=152, height=200, corner_radius=0)
    frame4.place(x=215, y=255)

    img4 = ImageTk.PhotoImage(Image.open("gbr poli penyakit dalam.png"))
    image_label = CTk.CTkLabel(master=poli_window, image=img4, text="", fg_color="transparent")
    image_label.place(x=228, y=278)

    label4 = CTk.CTkLabel(master=frame4, text="Poli Penyakit Dalam", font=("Century Gothic", 13))
    label4.place(x=15, y=107)

    button4 = CTk.CTkButton(master=frame4, text="Daftar", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, command=poli_penyakit_dalam)
    button4.place(x=45, y=135)

    frame5 = CTk.CTkFrame(master=poli_window, width=152, height=200, corner_radius=0)
    frame5.place(x=45, y=472)

    img5 = ImageTk.PhotoImage(Image.open("gbr poli anak.png"))
    image_label = CTk.CTkLabel(master=poli_window, image=img5, text="", fg_color="transparent")
    image_label.place(x=56, y=493)

    label5 = CTk.CTkLabel(master=frame5, text="Poli Anak", font=("Century Gothic", 13))
    label5.place(x=45, y=105)

    button5 = CTk.CTkButton(master=frame5, text="Daftar", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, command=poli_anak)
    button5.place(x=45, y=135)

    frame6 = CTk.CTkFrame(master=poli_window, width=152, height=200, corner_radius=0)
    frame6.place(x=215, y=472)

    img6 = ImageTk.PhotoImage(Image.open("gbr poli mata.png"))
    image_label = CTk.CTkLabel(master=poli_window, image=img6, text="", fg_color="transparent")
    image_label.place(x=228, y=493)

    label6 = CTk.CTkLabel(master=frame6, text="Poli Mata", font=("Century Gothic", 13))
    label6.place(x=47, y=105)

    button6 = CTk.CTkButton(master=frame6, text="Daftar", font=("Century Gothic", 13), width=50, height=20, corner_radius=15, command=poli_mata)
    button6.place(x=45, y=135)

    frame_poli6= CTk.CTkFrame(master=poli_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_poli6.place(x=0,y=0)

    button_back = CTk.CTkButton(master=poli_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=poli_window.destroy)
    button_back.place(x=0,y=0)

def fasilitas():
    fasilitas_window = CTk.CTkToplevel(app)
    fasilitas_window.geometry("400x680+100+15")
    fasilitas_window.title("Fasilitas")
    fasilitas_window.resizable(False,False)
    fasilitas_window.grab_set()

    background = CTk.CTkLabel(master=fasilitas_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    scrollable_frame = CTk.CTkScrollableFrame(master=fasilitas_window, corner_radius=0, fg_color="#A5BDD2")
    scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

    frame1 = CTk.CTkFrame(master=scrollable_frame, width=350, height=80, corner_radius=15, fg_color="#D9D9D9")
    frame1.pack(pady=10)

    img1 = ImageTk.PhotoImage(Image.open("rawat inap .png"))
    image_label1 = CTk.CTkLabel(master=frame1, image=img1, text="", fg_color="Gainsboro")
    image_label1.place(x=25, y=10)

    label1 = CTk.CTkLabel(master=frame1, text="Rawat Inap", font=("Georgia", 25, ), text_color="black")
    label1.place(x=130, y=30)

    frame2 = CTk.CTkFrame(master=scrollable_frame, width=350, height=80, corner_radius=15, fg_color="#D9D9D9")
    frame2.pack(pady=10)

    img2 = ImageTk.PhotoImage(Image.open("icu.png"))
    image_label2 = CTk.CTkLabel(master=frame2, image=img2, text="", fg_color="Gainsboro")
    image_label2.place(x=25, y=10)

    label2 = CTk.CTkLabel(master=frame2, text="ICU", font=("Georgia", 25), text_color="black")
    label2.place(x=170,y=30)

    frame3 = CTk.CTkFrame(master=scrollable_frame, width=350, height=80, corner_radius=15, fg_color="#D9D9D9")
    frame3.pack(pady=10)

    img3 = ImageTk.PhotoImage(Image.open("ruang bayi.png"))
    image_label3 = CTk.CTkLabel(master=frame3, image=img3, text="", fg_color="Gainsboro")
    image_label3.place(x=25, y=10)

    label3 = CTk.CTkLabel(master=frame3, text="Ruang Bayi", font=("Georgia", 25), text_color="black")
    label3.place(x=130,y=30)

    frame4 = CTk.CTkFrame(master=scrollable_frame, width=350, height=80, corner_radius=15, fg_color="#D9D9D9")
    frame4.pack(pady=10)

    img4 = ImageTk.PhotoImage(Image.open("radiologi.png"))
    image_label4 = CTk.CTkLabel(master=frame4, image=img4, text="", fg_color="Gainsboro")
    image_label4.place(x=25, y=10)

    label4 = CTk.CTkLabel(master=frame4, text="Radiologi", font=("Georgia", 25), text_color="black")
    label4.place(x=140,y=30)

    frame5 = CTk.CTkFrame(master=scrollable_frame, width=350, height=80, corner_radius=15, fg_color="#D9D9D9")
    frame5.pack(pady=10)

    img5 = ImageTk.PhotoImage(Image.open("laboratorium.png"))
    image_label5 = CTk.CTkLabel(master=frame5, image=img5, text="", fg_color="Gainsboro")
    image_label5.place(x=25, y=10)

    label5 = CTk.CTkLabel(master=frame5, text="Laboratorium", font=("Georgia", 25), text_color="black")
    label5.place(x=130,y=30)

    frame6 = CTk.CTkFrame(master=scrollable_frame, width=350, height=80, corner_radius=15, fg_color="#D9D9D9")
    frame6.pack(pady=10)

    img6 = ImageTk.PhotoImage(Image.open("farmasi.png"))
    image_label6 = CTk.CTkLabel(master=frame6, image=img6, text="", fg_color="Gainsboro")
    image_label6.place(x=25, y=10)

    label6 = CTk.CTkLabel(master=frame6, text="Farmasi", font=("Georgia", 25), text_color="black")
    label6.place(x=150,y=30)

    frame7 = CTk.CTkFrame(master=scrollable_frame, width=350, height=80, corner_radius=15, fg_color="#D9D9D9")
    frame7.pack(pady=10)

    img7 = ImageTk.PhotoImage(Image.open("ruang bersalin.png"))
    image_label7 = CTk.CTkLabel(master=frame7, image=img7, text="", fg_color="Gainsboro")
    image_label7.place(x=25, y=10)

    label7 = CTk.CTkLabel(master=frame7, text="Ruang Bersalin", font=("Georgia", 25), text_color="black")
    label7.place(x=120,y=30)

    frame8 = CTk.CTkFrame(master=scrollable_frame, width=350, height=80, corner_radius=15, fg_color="#D9D9D9")
    frame8.pack(pady=10)

    img8 = ImageTk.PhotoImage(Image.open("rehabilitas medik.png"))
    image_label8 = CTk.CTkLabel(master=frame8, image=img8, text="", fg_color="Gainsboro")
    image_label8.place(x=25, y=5)

    label8 = CTk.CTkLabel(master=frame8, text="Rehabilitas Medik", font=("Georgia", 25), text_color="black")
    label8.place(x=100,y=30)

    frame_fasilitas= CTk.CTkFrame(master=fasilitas_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_fasilitas.place(x=0,y=0)

    button_back = CTk.CTkButton(master=fasilitas_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=fasilitas_window.destroy)
    button_back.place(x=0,y=0)


def open_additional_info_form(username):
    def save_additional_info():
        data = {
            "nama_lengkap": nama_lengkap_entry.get(),
            "tanggal_lahir": TTL_entry.get(),
            "jenis_kelamin": Jenis_Kelamin_entry.get(),
            "nomor_hp": Nomor_HP_entry.get(),
            "nik": NIK_entry.get(),
            "riwayat_penyakit": Penyakit_entry.get()
        }

        try:
            with open("additional_info.json", "r") as file:
                additional_info = json.load(file)
        except FileNotFoundError:
            additional_info = {}

        additional_info[username] = data
        with open("additional_info.json", "w") as file:
            json.dump(additional_info, file, indent=4)

        messagebox.showinfo("Success", "Data tambahan berhasil disimpan!")
        additional_info_window.destroy()

    def select_date(event):
            global calendar, date_window
            date_window = CTk.CTkToplevel()
            date_window.grab_set()
            date_window.title("Tentukan tanggal lahir mu")
            date_window.geometry("250x220")

            calendar = Calendar(master=date_window, selectmode="day", date_pattern="dd/mm/yyyy")
            calendar.place(x=0, y=0)

            submit_button = CTk.CTkButton(master=date_window, text="Submit", command=grab_date)
            submit_button.place(x=50, y=190)

    def grab_date():
            TTL_entry.delete(0, END)
            TTL_entry.insert(0, calendar.get_date())
            date_window.destroy()

    additional_info_window = CTk.CTkToplevel(app)
    additional_info_window.geometry("400x680+100+15")
    additional_info_window.title("Isi Data Tambahan")
    additional_info_window.resizable(False, False)

    frame = CTk.CTkFrame(master=additional_info_window, width=360, height=550, fg_color="#70C4E5")
    frame.place(x=20, y=40)

    label1 = CTk.CTkLabel(master=frame, text="Nama Lengkap", font=("Calibri", 15, "bold"))
    label1.place(x=10, y=15)
    nama_lengkap_entry = CTk.CTkEntry(master=frame, width=340, placeholder_text="---xxx---")
    nama_lengkap_entry.place(x=10, y=40)

    label2 = CTk.CTkLabel(master=frame, text="Tanggal Lahir", font=("Calibri", 15, "bold"))
    label2.place(x=10, y=68)
    TTL_entry = CTk.CTkEntry(master=frame, width=340, placeholder_text="DD/MM/Y")
    TTL_entry.place(x=10, y=95)
    TTL_entry.bind("<1>", select_date)

    label3 = CTk.CTkLabel(master=frame, text="Jenis Kelamin", font=("Calibri", 15, "bold"))
    label3.place(x=10, y=123)
    Jenis_Kelamin_entry = CTk.CTkEntry(master=frame, width=340, placeholder_text="Laki-Laki/Perempuan")
    Jenis_Kelamin_entry.place(x=10, y=150)

    label4 = CTk.CTkLabel(master=frame, text="Nomor HP", font=("Calibri", 15, "bold"))
    label4.place(x=10, y=178)
    Nomor_HP_entry = CTk.CTkEntry(master=frame, width=340, placeholder_text="08*******")
    Nomor_HP_entry.place(x=10, y=205)

    label5 = CTk.CTkLabel(master=frame, text="NIK:", font=("Calibri", 15, "bold"))
    label5.place(x=10, y=233)
    NIK_entry = CTk.CTkEntry(master=frame, width=340, placeholder_text="---xxxxxxx---")
    NIK_entry.place(x=10, y=260)

    label6 = CTk.CTkLabel(master=frame, text="Riwayat Penyakit:", font=("Calibri", 15, "bold"))
    label6.place(x=10, y=288)
    Penyakit_entry = CTk.CTkEntry(master=frame, width=340, placeholder_text="contoh:sakit jantung")
    Penyakit_entry.place(x=10, y=315)

    submit_button = CTk.CTkButton(master=frame, text="Submit", command=save_additional_info)
    submit_button.place(x=10, y=410)

    additional_info_window.mainloop()

rating_pelayanan = 0
rating_tempat = 0
star_buttons_pelayanan = []
star_buttons_tempat = []
komentar_pelayanan_entry = None
komentar_tempat_entry = None

def set_rating_pelayanan(new_rating):
    global rating_pelayanan
    rating_pelayanan = new_rating
    update_stars()

def set_rating_tempat(new_rating):
    global rating_tempat
    rating_tempat = new_rating
    update_stars()

def update_stars():
    global star_buttons_pelayanan, star_buttons_tempat
    for i, star in enumerate(star_buttons_pelayanan):
        if i < rating_pelayanan:
            star.configure(text="★", text_color="gold")
        else:
            star.configure(text="☆", text_color="gray")

    for i, star in enumerate(star_buttons_tempat):
        if i < rating_tempat:
            star.configure(text="★", text_color="gold")
        else:
            star.configure(text="☆", text_color="gray")

def reset_rating():
    global rating_pelayanan, rating_tempat, komentar_pelayanan_entry, komentar_tempat_entry
    rating_pelayanan = 0
    rating_tempat = 0
    update_stars()
    if komentar_pelayanan_entry:
        komentar_pelayanan_entry.delete(0, CTk.END)
    if komentar_tempat_entry:
        komentar_tempat_entry.delete(0, CTk.END)

def load_rating():
    global rating_pelayanan, rating_tempat, komentar_pelayanan_entry, komentar_tempat_entry
    try:
        with open("rating2.json", "r") as file:
            data = json.load(file)
            if data:
                last_entry = data[-1]
                rating_pelayanan = last_entry.get("rating_pelayanan", 0)
                rating_tempat = last_entry.get("rating_tempat", 0)
                if komentar_pelayanan_entry:
                    komentar_pelayanan_entry.insert(0, last_entry.get("komentar_pelayanan", ""))
                if komentar_tempat_entry:
                    komentar_tempat_entry.insert(0, last_entry.get("komentar_tempat", ""))
                update_stars()
    except (FileNotFoundError, json.JSONDecodeError):
        pass

def save_rating():
    global rating_pelayanan, rating_tempat, komentar_pelayanan_entry, komentar_tempat_entry
    komentar_pelayanan = komentar_pelayanan_entry.get() if komentar_pelayanan_entry else ""
    komentar_tempat = komentar_tempat_entry.get() if komentar_tempat_entry else ""

    try:
        with open("rating2.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    entry = {
        "rating_pelayanan": rating_pelayanan,
        "rating_tempat": rating_tempat,
        "komentar_pelayanan": komentar_pelayanan,
        "komentar_tempat": komentar_tempat
    }

    data.append(entry)

    try:
        with open("rating2.json", "w") as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Success", "Rating berhasil disimpan")

    except Exception as e:
        messagebox.showerror("Error", "Tidak dapat menyimpan rating")

def rating_window():
    global star_buttons_pelayanan, star_buttons_tempat, komentar_pelayanan_entry, komentar_tempat_entry
    rating_window = CTk.CTkToplevel(app)
    rating_window.title("Rating Dokter dan Layanan")
    rating_window.geometry("400x680+100+15")
    rating_window.resizable(False, False)
    rating_window.grab_set()

    background = CTk.CTkLabel(master=rating_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    label = CTk.CTkLabel(rating_window, text="Berikan Penilaian Anda:", font=("Century Gothic", 19), fg_color="#A5BDD2")
    label.place(x=100, y=30)

    star_buttons_pelayanan = []
    star_frame_pelayanan = CTk.CTkFrame(rating_window, width=300, height=35, corner_radius=0, fg_color="#A5BDD2")
    star_frame_pelayanan.place(x=1, y=120)
    for i in range(5):
        star_button = CTk.CTkButton(
            star_frame_pelayanan,
            text="☆",
            font=("Century Gothic", 36),
            width=60,
            height=60,
            corner_radius=10,
            fg_color="transparent",
            text_color="gray",
            hover=False,
            command=lambda i=i: set_rating_pelayanan(i + 1)
        )
        star_button.grid(row=0, column=i, padx=10)
        star_buttons_pelayanan.append(star_button)

    rating_label_pelayanan = CTk.CTkLabel(rating_window, text="Pelayanan :", font=("Century Gothic", 16), fg_color="#A5BDD2")
    rating_label_pelayanan.place(x=25, y=80)

    komentar_pelayanan_entry = CTk.CTkEntry(rating_window, width=335, height=40, placeholder_text="Berikan komentar Anda")
    komentar_pelayanan_entry.place(x=30, y=190)

    star_buttons_tempat = []
    star_frame_tempat = CTk.CTkFrame(rating_window, width=300, height=35, corner_radius=0, fg_color="#A5BDD2")
    star_frame_tempat.place(x=1, y=320)
    for i in range(5):
        star_button = CTk.CTkButton(
            star_frame_tempat,
            text="☆",
            font=("Century Gothic", 36),
            width=60,
            height=60,
            corner_radius=10,
            fg_color="transparent",
            text_color="gray",
            hover=False,
            command=lambda i=i: set_rating_tempat(i + 1)
        )
        star_button.grid(row=0, column=i, padx=10)
        star_buttons_tempat.append(star_button)

    rating_label_tempat = CTk.CTkLabel(rating_window, text="Tempat :", font=("Century Gothic", 16), fg_color="#A5BDD2")
    rating_label_tempat.place(x=25, y=280)

    komentar_tempat_entry = CTk.CTkEntry(rating_window, width=335, height=40, placeholder_text="Berikan Komentar Anda")
    komentar_tempat_entry.place(x=30, y=390)

    submit_button = CTk.CTkButton(rating_window, text="Kirim Penilaian", font=("Century Gothic", 16), command=save_rating)
    submit_button.place(x=120, y=450)

    frame_rating= CTk.CTkFrame(master=rating_window, width=400, height=30, fg_color="#86A3D6", corner_radius=0)
    frame_rating.place(x=0,y=0)

    button_back = CTk.CTkButton(master=rating_window, text="⭠ Back", fg_color="#86A3D6", width=30, text_color="Black", font=("Bahnschrift SemiBold",13), corner_radius=0 ,command=rating_window.destroy)
    button_back.place(x=0,y=0)

    load_rating()
    reset_rating()

old_data = []

def Pemesanan():
    pemesanan_window = CTk.CTkToplevel(app)
    pemesanan_window.geometry("400x680+100+15")
    pemesanan_window.resizable(False, False)
    pemesanan_window.title("Data Pemesanan")
    pemesanan_window.grab_set()

    background = CTk.CTkLabel(master=pemesanan_window, text="", width=400, height=680, fg_color="#A5BDD2")
    background.place(x=0, y=0)

    frame2 = CTk.CTkFrame(master=pemesanan_window, width=380, height=650)
    frame2.place(x=10, y=20)

    frame3 = CTk.CTkFrame(master=frame2, width=360, height=150,fg_color="#A5BDD2")
    frame3.place(x=10, y=20)

    img = ImageTk.PhotoImage(Image.open("barcode.jpg"))
    image_label = CTk.CTkLabel(master=frame2, image=img, text="", fg_color="transparent")
    image_label.place(x=33, y=250)

    def load_booking_data():
        try:
            with open("pesanan user.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def show_booking_data():
        global old_data
        booking_data = load_booking_data()

        new_entries = [entry for entry in booking_data if entry not in old_data]

        if new_entries:
            entry = new_entries[0]

            for widget in frame3.winfo_children():
                widget.destroy()

            CTk.CTkLabel(frame3, text=f"Nama Pemesan: {entry['nama pemesan']}", font=("Century Gothic", 12)).place(x=10, y=20)
            CTk.CTkLabel(frame3, text=f"Nama Dokter: {entry['nama dokter']}", font=("Century Gothic", 12)).place(x=10, y=50)
            CTk.CTkLabel(frame3, text=f"Jadwal: {entry['jadwal yang terpilih']}", font=("Century Gothic", 12)).place(x=10, y=80)
            CTk.CTkLabel(frame3, text=f"Nomor Antrean: {entry['nomor antrean']}", font=("Century Gothic", 12)).place(x=10, y=110)

            old_data.append(entry)

    def periodic_refresh():
        show_booking_data()
        pemesanan_window.after(1, periodic_refresh)

    periodic_refresh()

def register():
    username = reg_username_entry.get()
    email = reg_email_entry.get()
    password = reg_password_entry.get()

    accounts = load_accounts()
    if any(user_data["email"] == email for user_data in accounts.values()):
        messagebox.showerror("Error", "Email sudah terdaftar")
        return
    elif username in accounts:
        messagebox.showerror("Error", "Username sudah terdaftar")
        return
    elif not username:
        messagebox.showerror("Error", "Please enter a valid username")
        return
    elif not email:
        messagebox.showerror("Error", "Please enter a valid email")
        return
    elif not password:
        messagebox.showerror("Error", "Please enter a valid password")
        return
    else:
        accounts[username] = {"email": email, "password": password}
        save_accounts(accounts)

        messagebox.showinfo("Success", "Register success!")
        register_window.destroy()
        open_additional_info_form(username)

CTk.set_appearance_mode("light")
CTk.set_default_color_theme("blue")
app = CTk.CTk()
app.geometry("400x680+100+15")
app.title("Login")
app.resizable(False,False)

img1 = ImageTk.PhotoImage(Image.open("background.png"))
background = CTk.CTkLabel(master=app, image=img1)
background.pack()

frame = CTk.CTkFrame(master=app, width=320, height=460, corner_radius=15, fg_color="#70C4E5")
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def hide():
    password_entry.configure(show="*")
    show_button.place(x=253, y=213)
    hide_button.place_forget()

def show():
    password_entry.configure(show="")
    hide_button.place(x=253, y=213)
    show_button.place_forget()


show_image = ImageTk.PhotoImage(Image.open("show_image.png"))
hide_image = ImageTk.PhotoImage(Image.open("hide_image.png"))

username_entry = CTk.CTkEntry(master=frame, width=260, placeholder_text="Username")
username_entry.place(x=30, y=170)

password_entry = CTk.CTkEntry(master=frame, width=260, placeholder_text="Password", show="*")
password_entry.place(x=30, y=210)

hide_button = CTk.CTkButton(master=frame, image=hide_image, command=hide, width=0, height=0, fg_color="white", text="")
show_button = CTk.CTkButton(master=frame, image=show_image, command=show, width=0, height=0, fg_color="white", text="")
show_button.place(x=253, y=213)
hide_button.place(x=253, y=213)

label1 = CTk.CTkLabel(master=frame, text="CIVARA HOSPITAL", font=("Broadway", 20))
label1.place(x=70, y=20)

label2 = CTk.CTkLabel(master=frame, text="Don't have an account?", font=("Century Gothic", 14))
label2.place(x=70, y=280)

img = ImageTk.PhotoImage(Image.open("rumahsakit3.jpg"))
image_label = CTk.CTkLabel(master=app, image=img, text="", fg_color="transparent")
image_label.place(x=117, y=170)

button1 = CTk.CTkButton(master=frame, width=260, text="Log In", corner_radius=6, command=login)
button1.place(x=30, y=250)

button2 = CTk.CTkButton(master=frame, width=260, text="Register", corner_radius=6, fg_color="#ACAAAE", command=register_window)
button2.place(x=30, y=310)

app.mainloop()