# plugins/data.py

from config import OWNER_USERNAME  # Pastikan OWNER_USERNAME didefinisikan di config.py

class DataProduk:
    pricelist_vps = [
        "*List Harga VPS NyxianNetwork:*\n",
        "---",
        "*Harga VPS dan Benefit*\n",
        "- VPS 2GB RAM, 1 Core — Rp20.000/bulan",
        "- VPS 2GB RAM, 2 Core — Rp32.000/bulan",
        "- VPS 4GB RAM, 2 Core — Rp45.000/bulan",
        "- VPS 8GB RAM, 2 Core — Rp50.000/bulan",
        "- VPS 8GB RAM, 4 Core — Rp55.000/bulan",
        "- VPS 16GB RAM, 4 Core — Rp70.000/bulan\n",
        "*Benefit:*",
        "- Gratis Instal Panel Pterodactyl",
        "- Gratis Instal Wings/Node",
        "- Gratis Instal Tema Panel (khusus RAM 8GB - 16GB)",
        "- Gratis Pilih Wilayah Server",
        "- Gratis Pilih OS (Sistem Operasi)",
        "- Gratis Pilih Versi yang Diinginkan",
        "- VPS Aktif Selama 30 Hari",
        "- Garansi 25 Hari (1x penggantian jika ada masalah)\n",
        "---",
        "Harga ini sudah termasuk berbagai benefit di atas untuk kenyamanan dan kebutuhan server Anda.\n",
        ":: Contact Me ::",
        f"› [Katsu](https://t.me/{OWNER_USERNAME}) ‹"
    ]

    pricelist_userbot = [
        "*Jasa Deploy Userbot*\n",
        "❏ *NyxianUserbot*",
        "├• *UbotPrem*: Rp20.000/bulan",
        "├• *Private Userbot*: Rp150.000/bulan",
        "└• *Notes NyxianUserbot*: ",
        "- Jika kalian order Private Userbot, kalian akan mendapatkan bot seperti NyxianUserbot, bisa membuat sampai 15 akun userbot."
    ]

    pricelist_bot_fsub = [
        "*JASA DEPLOY BOT FSUB/ASUPAN*\n",
        "❏ *FsubPremiumbot*",
        "├ *Premium*: Rp25.000/bulan (2 button)",
        "└• *Notes*: ",
        "- Untuk FsubPremiumbot, bisa tambah button dengan harga Rp10.000/button",
        "- Apabila bot Anda ter-banned, Anda bisa membuat bot lagi secara gratis sesuai dengan sisa masa aktif bot Anda.\n",
        f"Order? Chat [Katsu](https://t.me/{OWNER_USERNAME})"
    ]

class Pay:
    """Class to hold payment information."""
    payment_info = (
        "Untuk pembayaran/donasi, silakan kirim ke DANA 081398871823."
    )
