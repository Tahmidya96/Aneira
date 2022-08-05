from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

# load image
st.image("image/logo.png")

# menu
selected = option_menu(
        menu_title = None,
        options = ["Home", "Artikel", "About Us"],
        icons = ["house", "book", "file-person-fill"],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal",
        styles = {
        "container": {
            "padding": "0!important",
            "background-color": "#2c75d8"
        },
        "icon": {
            "color": "white",
            "font-size": "25px"
        }, 
        "nav-link": {
            "font-size": "25px",
            "text-align": "left", "margin":"0px",
            "--hover-color": "#eee"
        },
        "nav-link-selected": {
            "background-color": "blue"
            }
        }
    )

if selected == "Home":
    st.title(f"Yuk Sebelum Melangkah Lebih Lanjut, Kenalan Dulu sama Kita di About Us Ya!")
    st.subheader(f"Udah kenal sama kita kan ? Nah kalau sudah, yuk pelajari lebih lanjut tentang Cybersecurity.")

    st.image("image/cyber.png")
    st.title(f"Apa Sih Itu Cybersecurity?")
    st.write("Dilansir dari CISCO, cybersecurity adalah proses perlindungan sistem, data, jaringan, dan program dari ancaman atau serangan digital. Biasanya, serangan ini dilakukan oleh pihak tak bertanggung jawab untuk berbagai macam hal. Beberapa contohnya adalah mengakses informasi sensitif, atau bahkan mengubah dan menghancurkan data penting. Motifnya bisa jadi untuk mengganggu sebuah bisnis, atau bisa juga untuk memeras uang dalam jumlah yang biasanya tidak sedikit.")

    st.subheader(f"Nah, dari penjelasan diatas udah tau dong apa sih cybersecurity itu.")
    st.subheader(f"Cuma Itu Aja Manfaatnya? Nggak Ada yang Lain?")
    st.header(f"Eiits.. Jangan salah, Cybersecurity juga punya manfaat lainnya. Yuk ketahui apa aja sih manfaat lain dari Cybersecurity!")
    st.subheader(f"1. Informasi Terjaga.")
    st.write("Manfaat paling utama tentu saja untuk menjaga informasi pribadi. Di era yang serba digital ini, informasi pribadi menjadi sesuatu yang sangat berharga dan rentan untuk disalahgunakan. Jika virus berhasil mengambil informasi pegawai atau bahkan pelanggan, bisa jadi informasi-informasi tersebut diperjualbelikan. Informasi yang didapatkan secara ilegal tersebut juga bisa saja disalahgunakan untuk melakukan pemerasan ke orang yang terkait.")
    st.subheader(f"2. Memastikan Webstie Dapat Selalu Diakses.")
    st.write("Apapun pekerjaanmu, kau selalu membutuhkan website. Ketika hal itu terjadi, tim IT membutuhkan waktu untuk memulihkan sebuah website dan banyak instasi serta sekolah yang terkena dampaknya. Seperti tidak bisa ujian online, bisnis online berbasis website akan kehilangan pelanggan hingga tidak dapat mengakses website informasi-informasi penting seperti mencari pekerjaan, mencari sekolah/universitas.")

    st.subheader(f"Terus Kenapa Kita Harus Aware sama Cybersecurity?")
    st.subheader(f"Tentu saja kita harus aware dengan Cybersecurity karena ancamannya sangat berbahaya.")
    st.image("image/cyberaware.png")
    st.header(f"Apa Saja Ancamannya? Yuk Kita Kenalan dengan Ancaman Cybersecurity.")
    st.subheader(f"1. Hacking")
    st.write("Hacking merupakan bentuk peretasan terhadap device atau social media dengan tujuan pencurian data. Seringkali kegiatan ini dilakukan secara sengaja karena dendam atau tidak sengaja (iseng) dan berakhir mencoba mengambil data pribadi seseorang.")
    st.subheader(f"2. Phising")
    st.write("Phishing merupakan bentuk penipuan yang biasanya hadir melalui email. Penipu akan mengirimkan email menggunakan alamat yang mirip dengan sumber terpercaya. Meskipun begitu, terdapat satu atau dua huruf berbeda yang biasanya tidak terlihat secara kasat mata. Penipuan ini bertujuan untuk mencuri data sensitif seperti nomor keamanan kartu kredit (CVC), password, dan informasi penting lainnya.")

    st.subheader(f"Waahh...Ngeri juga ya ancamannya. Terus gimana caranya agar kita bisa terhindar dari salah satu contoh ancamannya?")
    st.subheader(f"Nah, untuk tau gimana caranya yuk lihat di Artikel kita. Disitu ada beberapa contoh ancaman hacking dan phising beserta cara mengantisipasinya loh!!")

if selected == "Artikel":
    choice = st.selectbox("", ["Email Phising", "Free WiFi", "Pinjaman Online", "Doxing"])
    
    if choice == "Email Phising":
        # konten email phising
        st.title("Apa itu Kejahatan Email Phising? Pahami Modus dan Ciri-cirinya")
        st.image("image/phising.png")
   
        st.write("Salah satu modus kejahatan yang sering terjadi di dunia maya adalah email phishing. Secara umum, cara kerja email phishing adalah mengelabuhi korban dengan cara menyamar sebagai karyawan atau lembaga jasa keuangan yang resmi. Pelaku email phishing sering membuat pengguna mengungkapkan informasi keuangan, kredensial sistem, atau data sensitif lainnya.")
    
        st.write("Di Indonesia, ancaman phishing paling banyak mengincar sektor keuangan terutama sektor perbankan. Menurut data dari Kaspersky pada periode Februari hingga April tahun 2022 menunjukkan terdapat sekitar 47,08% upaya phishing yang mengincar keuangan. Data-data yang diincar oleh pelaku biasanya berupa: username, password, PIN ATM, nomor kartu kredit, dan kode OTP. Oleh karena itu, masyarakat atau pengguna perlu waspada dan berhati-hati agar tidak terjerumus dalam kejahatan email phishing ini dengan cara memahami ciri-ciri email phishing.")
        st.write("Berikut ciri-ciri email phising: ")
        st.write("1. Email yang dikirim memberikan rasa takut dan urgensi yang mendesak agar pengguna cepat memberikan keputusan. Biasanya pelaku phishing memberi tahu pengguna bahwa akun mereka dibatasi atau akan ditangguhkan jika pengguna yang ditargetkan tidak menanggapi email. Ketakutan ini membuat pengguna akhirnya mengabaikan tanda peringatan umum dan melupakan pendidikan phishing mereka.")
        st.write("2. Menggunakan sapaan yang bersifat general. Biasanya, email phishing dikirim ke sebanyak mungkin orang, jadi sapaannya biasa saja.")
        st.write("3. Menggunakan nama akun yang mirip dengan lembaga resmi. Biasanya, email phishing menggunakan nama akun yang mirip dan menggunakan logo perusahaan resmi, tetapi alamat pengirim tidak akan menyertakan domain perusahaan resmi. Oleh karena itu, pengguna sebaiknya mengklik detail alamat pengirim untuk memastikan keabsahan sebuah email. Alamat pengirim hanyalah salah satu tanda peringatan, tetapi tidak boleh menjadi satu-satunya hal yang digunakan untuk menentukan keabsahan sebuah pesan.")
        st.write("4. Memberikan tautan/link atau file palsu. Pelaku email phishing biasanya akan meminta pengguna untuk mengklik link atau dokumen palsu dengan iming-iming hadiah, diskon, atau berita. Lampiran tautan tersebut dapat berupa halaman web, skrip shell (misalnya PowerShell), atau dokumen Microsoft Office dengan makro berbahaya. Makro dan skrip ini dapat digunakan untuk mengunduh malware atau mengelabui pengguna agar membocorkan kredensial akun pengguna.")

        st.write("Nah, itu lah beberapa ciri-ciri dari email phishing. Apabila Anda menerima email dengan ciri-ciri di atas, segera pastikan dan hubungi lembaga terkait untuk memastikan, apakah email yang dikirim tersebut resmi, benar, dan aman.")

        st.title("Sumber")
        st.write("1. https://money.kompas.com/read/2022/05/31/110800226/apa-itu-penipuan-email-phishing-simak-modus-dan-ciri-cirinya")
        st.write("2. https://www.proofpoint.com/us/threat-reference/phishing#:~:text=Phishing%20is%20when%20attackers%20send,credentials%20or%20other%20sensitive%20data")
        st.write("3. https://www.indotelko.com/read/1655238141/47-upaya-phishing-di-indonesia-sasar-sektor-keuangan")

    if choice == "Free WiFi":
        st.title(choice)
        # konten free wifi
        st.image("image/wifi.png")
        st.write("WiFi publik sering kita jumpai di tempat umum. Kehadiran WiFi publik atau Free WiFi tentu membuat pengakses merasakan kenyamanan terkoneksi internet dengan mudah dan gratis. Dibalik kenyamanan yang diberikan WiFi publik, perlu kita waspadai bahwa WiFi publik rentan terjadi peretasan (Hacker) yaitu pencurian data pribadi dan data riwayat akses yang bersifat sensitif ketika pengguna mengakses masuk atau login ke akun sosial media menggunakan WiFi publik, sebab riwayat akses tersebut dapat ikut terekam oleh WiFi publik.")

        st.header(f"Tips Aman Terkoneksi Wifi Publik")
        st.subheader(f"1. Perhatikan Nama Jaringan WiFi Publik Resmi dan Terpercaya")
        st.image("image/nama.png")
        st.write("Pastikan terlebih dahulu nama WiFi publik resmi sebelum terkoneksi. Pengguna dapat memeriksa dari segi urutan kata, pergantian antara huruf dengan angka, simbol, dan lain-lain sesuai dengan nama WiFi resmi. Jika terdapat dua atau lebih nama WiFi yang mirip, sebaiknya pengguna jangan langsung terkoneksi dengan WiFi tersebut dan dapat mengkonfirmasi kepada pemilik WiFi untuk mengetahui nama resmi WiFi tersebut. Pihak peretas dapat melakukan kejahatan dengan membuat jaringan palsu yang menggunakan nama WiFi serupa dengan WiFi resmi pada tempat tersebut. Sehingga korban dengan mudah dan percaya mengakses jaringannya.")
        st.subheader(f"2. Jangan Mengakses Informasi Sensitif Ketika Menggunakan Wifi Publik.")
        st.image("image/koneksi.png")
        st.write("Hindari melakukan kegiatan pengaksesan login akun sosial media, email, transaksi perbankan dan informasi sensitif yang mengandung data diri ketika menggunakan WiFi publik. Pengguna dapat menggunakan data seluler pribadi ketika mengakses informasi sensitif untuk menjaga keamanan. Kemampuan WiFi publik yang dapat merekam seluruh kegiatan pengaksesnya dapat memunculkan serangan dari peretas.")
        st.subheader(f"3. Aktifkan Keamanan Pada Perangkat (Enksipsi Password, Firewall dan Antivirus.)")
        st.image("image/security.png")
        st.write("Amankan kata sandi dengan public key atau private key untuk menjaga keamanan ketika mengakses WiFi publik. Enkripsi kata sandi adalah metode pengamanan data dengan mengkode acak data, sehingga hanya dapat diketahui pihak yang mengetahui kunci akses tersebut. Mengaktifkan Firewall pada Windows untuk menjaga keamanan jaringan dengan memonitori kegiatan jaringan yang masuk maupun keluar dan dapat mencegah pengguna asing untuk mengintip perangkat pengguna. Mengaktifkan Antivirus yang memiliki fitur pemeriksaan sambungan jaringan ke device dari Antivirus bawaan perangkat smartphone ataupun komputer dapat melindungi perangkat pengguna dari serangan peretas ketika mengakses WiFi publik. Menggunakan keamanan tambahan seperti Tor, Do Not Track, maupun VPN resmi dan terpercaya. VPN melindungi informasi pengguna dengan menyamarkan dan mengenkripsi data sebelum mengirimkannya ke router jaringan.")
        st.subheader(f"4. Perhatikan Halaman Website Terenkripsi HTTPS.")
        st.image("image/web.png")
        st.write("Pastikan ketika mengakses halaman web harus terdapat https yang menunjukkan bahwa situs tersebut aman. Situs https sudah tersertifikasi digital yang valid dengan enkripsi SSL/ TLS yang meminimalisir adanya MITM (Man-In-The-Middle Attack) dan pencurian data pengakses.")
        st.subheader(f"5. Non-aktifkan Koneksi Otomatis Pada Perangkat.")
        st.image("image/auto.png")
        st.write("Mematikan fitur koneksi otomatis ke jaringan terbuka atau WiFi publik dan jangan lupa setelah menggunakan WiFi publik pilih opsi “Lupakan jaringan” atau “forget network”. Pengguna juga harus mematikan berbagi WiFi (Tethering) jika tidak dipergunakan lagi. Pengaktifan terhubung otomatis jaringan memang mempermudah pengguna, namun hal tersebut dapat memberi kesempatan peretas dalam menyebarkan malware dan mencuri data pribadi pengguna.")

        st.title("Sumber")
        st.write("1. https://unida.ac.id/teknologi/artikel/cara-aman-menggunakan-wifi-publik-agar-terhindar-dari-hacker.html")
        st.write("2. https://kharismaworld.co.id/blog/bahaya-menggunakan-wifi-publik")
        st.write("3. https://m.liputan6.com/tekno/read/4636663/5-tips-aman-menggunakan-wifi-publik")

    if choice == "Pinjaman Online":
        # konten pinjol(pinjaman online)
        st.title("Pinjaman Online, Apakah Masih Bisa Aman ?")
        st.image("image/pinjol.png")
        st.write("Butuh dana cepat? Anda membutuhkan uang? Kami siap memberikan dengan bunga ringan!")
        st.title("Apakah anda tidak asing dengan pesan-pesan seperti diatas?")
        st.write("Tawaran dana cepat dengan persyaratan yang mudah membuat orang akan tergiur dan memilih untuk mengikuti anjuran pesan tersebut. Tuntutan mendapatkan uang banyak, memenuhi gaya hidup mendorong masyarakat memilih melakukan pinjaman online. Maraknya pinjaman online yang ditawarkan melalui pesan singkat tidak menutup kemungkinan adanya penipuan atau pinjaman secara ilegal. Dilansir dari merdeka, sistem kerja pinjaman online secara ilegal menawarkan kemudahan pengajuan pinjaman. Hanya dengan mendownload aplikasi, peminjam kemudian diminta menyerahkan data diri dan mengisi nomor rekening, dan tidak lama kemudian uang pinjaman bisa dicairkan. Namanya pinjaman tentu harus dikembalikan. Namun, sistematika penagihan yang tidak ramah dikeluhkan masyarakat. Otoritas Jasa Keuangan (OJK) menerima 19.711 pengaduan korban pinjaman online pada rentang waktu 2019-2021. Sebagian besar pengaduan masyarakat adalah pencairan dana pinjaman tanpa persetujuan pemohon, ancaman penyebaran data pribadi, dan intimidasi dalam penagihan pinjaman. Pemerintah memiliki kewajiban dalam melindungi keamanan masyarakat dalam keadaan ini. Jika melihat UU Nomor 19 tahun 2016 tentang Informasi dan Transaksi Elektronik, tepatnya pada pasal 40, dijelaskan bahwa pemerintah harus melindungi kepentingan masyarakat dari gangguan pada saat melakukan transaksi elektronik.")
        st.write("Untuk menghadapi masalah tersebut, pemerintah melalui Otoritas Jasa Keuangan (OJK) memberikan solusi dengan menyediakan sarana pinjaman online yang legal. Berdasarkan data OJK Per April 2022  terdapat 102 perusahaan fintech yang menyediakan pinjaman online secara legal. Perusahaan yang terdapat dapat dilihat melalui website ojk.go.id Layanan pinjaman online legal memberikan dana dengan prosedur penagihan yang tepat yaitu dengan jatuh tempo 90 hari. Selain keamanan transaksi, memilih jalan legal bisa membantu kita untuk lebih bijak dalam menggunakan uang sesuai kebutuhan. Adanya upaya pemerintah dalam mengatasi pinjaman online ilegal juga diimbangi oleh sikap masyarakat. Meskipun adanya desakan ekonomi jangan sampai menutup diri untuk berpikiran jernih. Oleh karena itu, berhati-hatilah, kejahatan akan melihat celah dari kelengahan anda.")

        st.title("Sumber")
        st.write("1. https://lsc.bphn.go.id/konsultasiView?id=5089#:~:text=Sedangkan%2C%20untuk%20pinjol%20legal%20cara,90%20hari%20dari%20jatuh%20tempo")
        st.write("2. https://www.merdeka.com/peristiwa/sistem-kerja-pinjol-ilegal-cari-mangsa.html")
        st.write("3. UU ITE No. 19 Tahun 2016")

    if choice == "Doxing":
        # konten doxing
        st.title(f"Kenali Apa itu Doxing di Media Sosial dan Cara Mencegahnya.")
        st.image("image/doxing.png")
        st.write("Di zaman digital saat ini, hampir setiap orang pasti memiliki akun media sosial. Media sosial juga sangat beragam, mulai dari Facebook, Instagram, TikTok, YouTube, hingga WhatsApp. Tak jarang, bagi seseorang menempatkan identitas pribadinya di media sosial. Tanpa disadari, kebiasaan ini dapat memicu terjadinya doxing.")
        st.subheader(f"Apa itu Doxing?")
        st.write("Doxing atau bisa ditulis juga sebagai doxxing merupakan sebuah tindakan mengungkapkan informasi identitas seseorang secara online, seperti nama asli, alamat rumah, tempat kerja, telepon, keuangan, dan informasi pribadi lainnya. Semua informasi tersebut kemudian diedarkan ke publik tanpa seizin pihak yang bersangkutan. Pengambilan identitas tanpa persetujuan dari pemiliknya dapat berakibat buruk terhadap korban terutama soal privasinya. Seringkali aktivitas doxing dilakukan untuk motif negatif. Terkadang, beberapa pihak melakukannya untuk mengitimidasi dan membungkam korban, bullying, ataupun memperlakukan pihak yang ditarget. Hal tersebut dilakukan dengan cara menyebarkan informasi pribadi korban seperti gambar atau video. Kemudian, disisi lain doxing juga dapat dilakukan untuk memperlihatkan kepada publik mengenai perbuatan salah atau pelanggaran yang telah dilakukan oleh seseorang. Aktivitas doxing ini merupakan isu yang serius dan tentu bisa merugikan. Oleh karena itu, kita perlu melakukan beberapa cara pencegahan agar kita tidak menjadi korban doxing oleh pihak yang tidak bertanggungjawab.")
        st.subheader(f"Bagaimana sih Cara Mencegah Doxing ?")
        st.write("Jika Anda pernah memposting di forum online, berpartisipasi dalam menandatangani petisi online, atau berbelanja secara online, maka data Anda tersedia untuk umum. Untuk itu, ada beberapa cara yang dapat Anda lakukan untuk melindungi informasi Anda. Berikut cara yang bisa Anda lakukan.")
        st.subheader(f"1. Proteksi IP Adress Menggunakan VPN.")
        st.write("VPN atau jaringan pribadi virtual menawarkan perlindungan yang sangat baik terhadap pengungkapan alamat IP. VPN mengambil lalu lintas internet pengguna, mengenkripsinya, dan mengirimkannya melalui salah satu server layanan sebelum menuju ke internet publik, sehingga memungkinkan Anda menjelajahi internet secara anonim.")
        st.subheader(f"2. Latih Keamanan Cyber yang Baik.")
        st.write("Menggunakan perangkat lunak pendeteksi virus dan malware dapat menghentikan perilaku pencurian data melalui aplikasi yang ilegal. Perangkat lunak yang diperbaharui secara berkala membantu mencegah terjadinya celah keamanan apa pun yang dapat menyebabkan diretas atau doxing.")
        st.subheader(f"3. Gunakan Kata Sandi yang Kuat.")
        st.write("Pastikan membuat kombinasi kata sandi yang kuat, biasanya terdiri dari kombinasi huruf besar dan huruf kecil kemudian ditambah angka dan simbol. Hindari menggunakan kata sandi yang sama untuk beberapa akun, dan pastikan Anda mengubah kata sandi secara teratur.")
        st.subheader(f"4. Gunakan Nama Pengguna Terpisah untuk Platform yang Berbeda.")
        st.write("Jika Anda menggunakan beberapa media sosial yang berbeda, pastikan menggunakan nama pengguna yang terpisah di setiap platformnya. Dengan menggunakan nama yang sama, pelaku doxing dapat menelusuri komentar Anda di platform yang berbeda dan menggunakan informasi tersebut untuk menyusun gambaran rinci tentang Anda.")
        st.subheader(f"5. Tinjau Pengaturan Privasi Anda di Media Sosial.")
        st.write("Tinjau pengaturan privasi di profil media sosial Anda dan pastikan Anda merasa nyaman dengan jumlah informasi yang dibagikan dan dengan siapa.")
        st.subheader(f"6. Gunakan Otentikasi Multi-Faktor.")
        st.write("Gunakan otentikasi menggunakan kata sandi dan nomor telepon Anda. Hal ini jelas dapat mempersulit peretas untuk mengakses perangkat atau akun online seseorang karena mengetahui kata sandi korban saja tidak cukup, tetapi perlu juga verifikasi melalui nomor telepon.")
        st.subheader(f"7. Singkirkan Profil Usang.")
        st.write("Tinjau berapa banyak situs atau akun yang memiliki informasi Anda. Misalnya, situs seperti MySpace mungkin sekarang sudah ketinggalan zaman, profil yang dipasang lebih dari satu dekade masih terlihat dan dapat diakses dipublik. Coba untuk menghapus profil usang dan lama atau tidak digunakan jika Anda bisa.")
        st.subheader(f"8. Waspada Terhadap Email Phising.")
        st.write("Pelaku doxing mungkin menggunakan penipuan email phishing untuk mengelabuhi Anda agar dapat mengungkapkan beberapa informasi pribadi, seperti alamat rumah, kata sandi, atau bahkan kode PIN. Berhati-hatilah setiap kali Anda menerima email yang diduga mengatasnamakan lembaga keuangan atau kartu kredit yang meminta informasi pribadi Anda. Lembaga keuangan tidak akan pernah meminta informasi ini melalui email.")
        st.write("Doxing adalah masalah serius yang dimungkinkan oleh akses mudah ke informasi pribadi secara online. Tetap aman di dunia online terutama media sosial tidak selalu mudah, tetapi mengikuti praktik terbaik keamanan siber dapat membantu meminimalisir hal tersebut. Jadi, tetap waspada dan bijak dalam bermedsos agar kita bisa terhindar dari upaya tindak kejahatan siber.")
        st.header(f"Sumber")
        st.write("1. https://www.kaspersky.com/resource-center/definitions/what-is-doxing#:~:text=Doxing%20")
        st.write("2. https://tirto.id/mengenal-doxing-di-media-sosial-bahaya-dan-cara-mencegahnya-f5lm")
        st.write("3. https://yoursay.suara.com/news/2021/07/05/134254/mengenal-bahaya-doxing-di-media-sosial-ini-cara-menghindarinya")
if selected == "About Us":
    st.write(f"CyberWare merupakan wadah literasi serta edukasi bagi masyarakat mengenai cybersecurity. Literasi dan edukasi yang diberikan oleh CyberWare berupa artikel yang terdiri dari tips dan trik, informasi, serta berita yang berhubungan dengan isu-isu cybersecurity yang ada di Indonesia maupun diranah global. Artikel ataupun konten akan dikemas dalam bentuk yang ringkas serta informatif, sehingga pembahasan mengenai cybersecurity dapat dikonsumsi dengan mudah oleh khalayak umum.")
    
    st.title(f"Data Diri Tim Aneira")
    st.write(f"Pembuatan dan pengembangan CyberWare dibuat oleh tim Aneira yang terdiri dari 3 orang perempuan yang memiliki semangat ketertarikan dan keterampilan dalam pengembangan industri cybersecurity")
    
    with st.container():
        img_col1,img_col2,img_col3 = st.columns(3)

        with img_col1:
            st.image("image/Ratna.png")
            st.write("Ratna Susilawati")
            st.write("Content Writer")
            st.write("Bisnis Digital")
            st.write("Universitas Pendidikan Indonesia")

        with img_col2:
            st.image("image/Reka.png")
            st.write("Reka Suhartanti")
            st.write("Content Writer")
            st.write("Ilmu Komunikasi")
            st.write("Universitas Tidar")

        with img_col3:
            st.image("image/ok.png")
            st.write("Tahmidya Kamila PN")
            st.write("Coding Website")
            st.write("Sistem Informasi")
            st.write("Universitas Brawijaya")