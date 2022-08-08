from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
# MATPLOT
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

# DB
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

# fungsi artikel
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS blogtable(penulis TEXT,judul TEXT,artikel TEXT,tanggal DATE)')

def add_data(penulis,judul,artikel,tanggal):
    c.execute('INSERT INTO blogtable(penulis,judul,artikel,tanggal) VALUES (?,?,?,?)',(penulis,judul,artikel,tanggal))
    conn.commit()

def view_all_notes():
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT judul FROM blogtable')
    data = c.fetchall()
    return data

def get_blog_by_title(judul):
    c.execute('SELECT * FROM blogtable WHERE judul="{}"'.format(judul))
    data = c.fetchall()
    return data

def delete_data(judul):
    c.execute('DELETE FROM blogtable WHERE judul="{}"'.format(judul))
    conn.commit()

avatar1 ="https://www.w3schools.com/howto/img_avatar1.png"
avatar2 ="https://www.w3schools.com/howto/img_avatar2.png"
image = st.image("image/logo.png")

def main():
    title_temp ="""
        <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
        <h4 style="color:white;text-align:center;font:"roboto";">{}</h1>
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
        <h6>Author:{}</h6>
        <br/>
        <br/>   
        <p style="text-align:justify">{}</p>
        </div>
        """

    article_temp ="""
        <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
        <h4 style="color:white;text-align:center;font:"roboto";">{}</h1>
        <h6>Author:{}</h6> 
        <h6>Post Date: {}</h6>
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
        <br/>
        <br/>
        <p style="text-align:justify">{}</p>
        </div>
        """

    head_message_temp ="""
        <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
        <h4 style="color:white;text-align:center;font:"roboto";">{}</h1>
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
        <h6>Author:{}</h6>      
        <h6>Post Date: {}</h6>
        
        </div>
        """

    full_message_temp ="""
        <div style="background-color:silver;padding:10px;border-radius:5px;margin:10px;">
            <p style="text-align:justify;color:black;padding:10px">{}</p>
        </div>
        """

    choice = option_menu(
        menu_title = None,
        options = ["Home","Artikel", "Berita", "Forum", "About Us","Tambah Artikel","Manage Artikel"],
        icons = ['house', 'file-earmark-spreadsheet', 'newspaper','chat-text','file-person','file-plus','gear'],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal",
        styles = {
        "container": {
            "background-color": "#2c75d8"
            },
        "icon": {
            "color": "white",
            "font-size": "25px"
            },
        "nav-link-selected": {
            "background-color": "blue"
            }
        }
    )

    if choice == "Home":
        st.title("Hot Diskusi")
        img_col1,img_col2,img_col3 = st.columns(3)
        with img_col1:
            st.image("image/phising.png")
            st.subheader("Apa itu Kejahatan Email Phishing? Pahami Modus dan Ciri-Cirinya")
        with img_col2:
            st.image("image/hacking.png")
            st.subheader("Cegah Tindak Hacking!! 6 Tips Terjaga Dari Tindak Hacking")
        with img_col3:
            st.image("image/malware.png")
            st.subheader("Malware Menyerang! Waspada Aplikasi Populer Tiruan Hacker")

        st.title("Berita")
        img_col4,img_col5,img_col6 = st.columns(3)
        with img_col4:
            st.image("image/literasi.png")
            st.subheader("Targetkan Literasi Digital Kemkominfo untuk 5,5 Juta Masyarakat Pada Tahun 2022")
        with img_col5:
            st.image("image/zero-day.png")
            st.subheader("Kerentanan Zero-Day Twitter Mengancam Tindak Eskpos Data 5,4 Juta Akun")
        with img_col6:
            st.image("image/bca.png")
            st.subheader("BCA Rogoh Kocek Rp 500 Milyar untuk Perkuat Keamanan Cyber")

        st.title("Artikel")
        img_col7,img_col8,img_col9 = st.columns(3)
        with img_col7:
            st.image("image/wifi.png")
            st.subheader("Bahaya Menggunakan WiFi Publik! Cermati Tips Aman Terkoneksi WiFi Publik.")
        with img_col8:
            st.image("image/pinjol.png")
            st.subheader("Pinjaman Online, Apakah Masih Bisa Aman?")
        with img_col9:
            st.image("image/doxing.png")
            st.subheader("Kenali Apa Itu Doxing di Media Sosial dan Cara Mencegahnya")

    if choice == "Artikel":
        all_titles = [i[0] for i in view_all_titles()]
        postlist = st.selectbox("Posts",all_titles)
        post_result = get_blog_by_title(postlist)
        for i in post_result:
            st.markdown(head_message_temp.format(i[1],i[0],i[3]),unsafe_allow_html=True)
            st.markdown(full_message_temp.format(i[2]),unsafe_allow_html=True)

    if choice == "Berita":
        all_titles = [i[0] for i in view_all_titles()]
        postlist = st.selectbox("Posts",all_titles)
        post_result = get_blog_by_title(postlist)
        for i in post_result:
            st.markdown(head_message_temp.format(i[1],i[0],i[3]),unsafe_allow_html=True)
            st.markdown(full_message_temp.format(i[2]),unsafe_allow_html=True)
        
    if choice == "About Us":
        st.title("Tentang CyberWare")
        st.write("CyberWare merupakan sebuah wadah literai serta edukasi bagi masyarakat mengenai cyber security. Literasi dan edukasi yang diberikan oleh CyberWare berupa artikel yang terdiri dari tips dan trik, informasi, serta berita yang berhubungan dengan isu-isu syber security yang ada di Indonesia maupun diranah global. artikel ataupun konten akan dikemas dalam bentuk yang ringkas serta informatif, sehingga pembahasan mengenai cyber security dapat dikonsumsi dengan mudah oleh khalayak umum. Selain itu, terdapat forum diskusi yang bisa digunakan sebagai sarana bertukar opini dan pemikiran mengenai cyber security.")

        st.title("Profil Tim Aneira")
        st.write("Pembuatan dan pengembangan CyberWare dibuat oleh tim Aneira yang terdiri dari 3 orang perempuan yang memiliki semangat ketertarikan dan keterampilan dalam pengembangan insdustri cyber security.")
        img_col1,img_col2,img_col3 = st.columns(3)
        with img_col1:
            st.image("image/Ratna.png")
            st.write("Ratna Susilawati")
            st.write("Content Writer")
        with img_col2:
            st.image("image/Reka.png")
            st.write("Reka Suhartanti")
            st.write("Content Writer")
        with img_col3:
            st.image("image/ok.png")
            st.write("Tahmidya Kamila PN")
            st.write("Coding Website")

    if choice == "Forum":
        all_titles = [i[0] for i in view_all_titles()]
        postlist = st.selectbox("Posts",all_titles)
        post_result = get_blog_by_title(postlist)
        for i in post_result:
            short_article = str(i[2])[0:115]
            st.write(title_temp.format(i[1],i[0],short_article),unsafe_allow_html=True)
            
    if choice == "Tambah Artikel":
        st.subheader("Tambah Artikel atau Buat Topik Forum")
        choice = st.selectbox("",["Tambah Artikel", "Buat Forum"])
        if choice == "Tambah Artikel":
            create_table()
            blog_title = st.text_input('Judul')
            blog_author = st.text_input("Nama",max_chars=50)
            blog_article = st.text_area("Artikel",height=200)
            blog_post_date = st.date_input("Tanggal")
            if st.button("Add"):
                add_data(blog_author,blog_title,blog_article,blog_post_date)
                st.success("Post::'{}' Saved".format(blog_title))
        
        if choice == "Buat Forum":
            create_table()
            nama = st.text_input("Nama",max_chars=50)
            judul = st.text_input('Judul')
            topik = st.text_area("Topik Diskusi")
            tanggal = st.date_input("Tanggal")
            if st.button("Add"):
                add_data(nama,judul,topik,tanggal)
                st.success("Topik:'{}' Saved".format(judul))
            
    if choice == "Manage Artikel":
        st.subheader("Manage Artikel")
        result = view_all_notes()
        clean_db = pd.DataFrame(result,columns=["Author","Title","Article","Date"])
        st.dataframe(clean_db)
        unique_list = [i[0] for i in view_all_titles()]
        delete_by_title =  st.selectbox("Select Title",unique_list)
        if st.button("Delete"):
            delete_data(delete_by_title)
            st.warning("Deleted: '{}'".format(delete_by_title))

if __name__ == '__main__':
    main()
