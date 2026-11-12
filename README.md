# YtFusion Skills

Skill opsional untuk agen AI yang mengoperasikan YtFusion. Paket ini terpisah
dari aplikasi dan dapat diperbarui sendiri.

The workflow instructions use the Agent Skills format. The agent should answer
in the user's language and use the tools available in its own environment.

## HDS Home Production

Membantu membuat Master baru, menyiapkan channel dan stok, mengkurasi referensi,
membagi koleksi, serta menjalankan atau melanjutkan produksi melalui HDS.
Lihat [kemampuan dan contoh perintah](skills/hds-home-production/references/capabilities.md).

## YtFusion Domain and VPS

Memeriksa domain dan koneksi VPS, memasang HTTPS, serta memindahkan alamat
dashboard melalui **YouTube API Setup** dan **Server Transfer** di instalasi
YtFusion. Lihat [instruksi skill](skills/ytfusion-domain-vps/SKILL.md).

    Pakai $ytfusion-domain-vps untuk cek HTTPS dan koneksi Server Transfer VPS saya.
    Cek status saja.

## Pasang

Untuk Codex yang menyediakan skill-installer, gunakan permintaan:

    Gunakan skill-installer untuk memasang skill dari
    https://github.com/kisanakclub/ytfusion-skills/tree/main/skills/hds-home-production

    Gunakan skill-installer untuk memasang skill dari
    https://github.com/kisanakclub/ytfusion-skills/tree/main/skills/ytfusion-domain-vps

Untuk agen lain yang mendukung Agent Skills, pasang folder
skill yang ingin dipakai pada lokasi yang didukung agen tersebut.
Cara pemasangan dan akses alat mengikuti dokumentasi agen masing-masing.
Menyalin folder sumber ke lokasi biasa belum membuatnya otomatis aktif.

Paket ini berisi instruksi dan satu helper Python read-only. Ini tidak memasang
YtFusion, tidak membuat koneksi agen ke komputer, dan tidak menambahkan provider
ke edisi aplikasi yang tidak menyediakannya.

## Mulai

    Pakai HDS Home Production. Jelaskan kemampuan yang tersedia pada device ini.

Atau langsung beri tugas:

    Buat Master baru untuk 12 channel berbahasa Spanyol, masing-masing 50 judul.
    Siapkan sampai setup saja. Gunakan referensi yang cocok jika tersedia.

    Lanjutkan koleksi yang saya pilih sampai gambar dan thumbnail selesai.
    Pertahankan hasil yang sudah valid.

Agen memerlukan akses yang sesuai ke instalasi HDS dan koleksi yang dikerjakan.
HDS Master tidak wajib tersedia pada device pelaksana: koleksi produksi yang
mandiri dapat dikerjakan tanpa membawa seluruh bank Master.

## Private dan Shared

Prosedur skill dapat dipakai dengan kedua edisi, sesuai fitur yang tersedia.
Provider, preset dan target produksi mengikuti instalasi serta pilihan pengguna.
Skill tidak membawa engine Private dan tidak mengganti provider diam-diam.

## Data pengguna

Master pribadi, stok judul, gambar referensi, Batch, hasil produksi dan kredensial
disimpan terpisah dari repo ini. Master starter dapat menjadi paket pendamping
opsional; versi awal ini tidak menyertakan starter atau media pihak ketiga.

## Verifikasi pengembangan

    python3 -m unittest discover -s tests -v

Helper menggunakan pustaka standar Python 3.9 atau lebih baru. Pemeriksaan
diagnostik tidak membuktikan readiness native atau kualitas hasil produksi.
Pengujian lintas agen, lintas edisi dan antar-device dicatat terpisah di
[catatan kompatibilitas](skills/hds-home-production/references/compatibility.md).
