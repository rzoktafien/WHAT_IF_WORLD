# WHAT IF WORLD — PANDUAN PRODUKSI UTAMA (V2)

Standar permanen untuk setiap video. Bahasa penjelasan: Indonesia. Semua prompt: Inggris.

## 1. Filosofi
WHAT IF WORLD bukan slideshow klip AI. Ini cerita sinematik pendek yang membuat penonton berhenti menggulir, bertanya-tanya, mengantisipasi akibat, belajar satu ide sains, dan mengingat akhirnya. Setiap shot punya tugas naratif.

## 2. Arsitektur retensi (model 60 detik)
- 0–2 dtk: PATTERN INTERRUPT. Gambar anomali/mustahil sejak frame pertama. Tanpa logo, tanpa pembuka tenang.
- 2–14 dtk: misteri + "twist kerangka" (mis. hitung mundur, fakta yang mengubah cara pandang).
- 14–30 dtk: eskalasi; bukti makin tak terbantahkan; taruhan manusia.
- 30–50 dtk: konsekuensi bertahap + reveal sains yang konkret (minimal 1 fakta/angka bersumber yang mengejutkan).
- 50–60 dtk: payoff emosional + pertanyaan penutup yang memancing komentar.
Format lebih pendek: kompres proporsional, hook tetap di 2 detik pertama.

## 3. Perancangan cerita & uji fisika (wajib sebelum prompt)
Tulis: premis, keyakinan awal penonton, gangguan, pertanyaan inti, tangga eskalasi, reveal, rasa akhir, asumsi, batas klaim.
**Tiga uji fisika:**
1. Uji waktu — tiap peristiwa: seketika, menit, jam, hari, atau tahun? Visual & narasi harus mengikuti skala itu.
2. Uji bukti — apa yang benar-benar akan terlihat/terdengar? Tunjukkan bukti sebelum menjelaskan.
3. Uji konsistensi — adakah elemen visual yang membutuhkan hal yang dihapus premis (mis. cahaya Matahari)? Buang atau ganti.
Jangan menciptakan karakter jika cerita tak membutuhkannya. Bila ada karakter, satu protagonis cukup; tokoh pendukung = figuran tanpa dialog kecuali diberi referensi.

## 4. Sistem referensi gambar
- Satu gambar = satu subjek (karakter / lokasi / properti). Hindari sheet multi-tampilan: model bisa meniru tata letak panel ke dalam video.
- Karakter: potret medium shot, latar polos, wajah jelas. Variasi kostum = gambar terpisah yang dibuat dengan EDIT gambar dari referensi pertama (menjaga wajah).
- Lokasi: versi siang + versi "kondisi premis" (mis. gelap) dibuat dengan EDIT dari versi pertama agar geometri sama.
- Properti hanya bila tampil dekat/penting dan harus benar-benar dipakai di cerita. Tidak ada properti "pajangan".
- Ingredients (Flow/Veo 3.1): maks 3 gambar per klip (mis. karakter + lokasi + properti). Mode ini biasanya mengunci durasi 8 detik.
- Keyframe: satu per adegan, dibuat dengan referensi. Dipakai sebagai start frame (Frames to Video) bila Ingredients kurang konsisten. Uji kedua mode pada adegan 1–2 lalu pilih yang lebih baik.
- Hindari rantai "frame terakhir → klip berikutnya" untuk semua klip: kualitas dan wajah cenderung melorot. Pakai hanya bila perlu.

## 5. Protokol kontinuitas
Tiap adegan menetapkan: karakter & kostum (per FASE), lokasi & arah kamera, waktu/cahaya, cuaca, posisi properti, arah layar, keadaan awal & akhir, jembatan ke adegan berikutnya. Transisi yang sah: hard cut bermotif, match cut yang realistis, lompatan waktu berlabel (overlay), sound bridge. Dilarang: lompatan lokasi tanpa jembatan; match cut fantasi (mis. jendela menjadi lengkung Bumi) dalam satu klip—lakukan dengan cross-dissolve saat editing.
Kostum harus masuk akal secara iklim (tropis Indonesia: kaos/kemeja ringan; jaket hanya jika ada alasan cerita, ditandai sebagai FASE B).

## 6. Arsitektur prompt video Flow (bahasa Inggris)
Satu prompt = satu klip, 80–130 kata (di luar blok negatif), urutan:
1. Format: "Vertical 9:16, photorealistic live-action cinematic, 8 seconds."
2. Referensi yang dipakai (nama + ciri kunci kostum).
3. Kondisi awal & SATU aksi utama (kata kerja konkret, apa yang berubah).
4. SATU gerakan kamera + ukuran shot + posisi.
5. Cahaya, warna, atmosfer — spesifik, bukan sekadar "cinematic".
6. Keadaan akhir (untuk kontinuitas).
7. Audio: "Audio: [ambience & SFX spesifik]. No speech, no singing, no music."
8. Blok negatif standar (di bawah).
**Blok negatif standar:** `No text, no captions, no subtitles, no logos, no watermark, no readable signage, no speech, no voice-over, no music, no face morphing, no distorted hands, no extra fingers, no cartoon look.`
Tiap adegan juga punya **Plan B** (apa yang diubah di prompt bila hasil menyimpang: sederhanakan aksi, ganti mode, atau buat plate terpisah lalu gabung di editing).
Frasa yang dihindari: banyak aksi berurutan, banyak potongan kamera, "cinematic" tanpa deskripsi, dialog dalam tanda kutip (dapat memicu lip-sync).

## 7. Desain audio
**Mode default: SILENT PLATE.** Klip hanya membawa ambience/SFX diegetik. Alasan: tes pertama gagal (suara Inggris, musik acak, suara narator berubah antar klip).
- Narasi: skrip Indonesia + brief TTS (prompt Inggris) → direkam SEKALI dalam satu pass agar suara konsisten, lalu dipotong per adegan. Tempo 2,0–2,6 kata/detik untuk kalimat, dengan jeda dramatis; jangan padat, jangan kosong total (target ±100–140 kata per 60 dtk).
- Musik: satu bed untuk seluruh video (prompt Inggris bertimeline) dengan motif berulang; ada momen diam yang disengaja bila cerita membutuhkan.
- SFX: daftar per adegan; motif suara berulang (mis. kehadiran/ketiadaan suara serangga).
- Mode A (suara terintegrasi Flow) hanya eksperimen opsional: uji di satu klip; jangan dipakai bila bahasa/suara menyimpang.
Cek: bahasa, pelafalan, kata karangan, timing, clipping, volume, kecocokan ambience, kontinuitas musik, suara tak diinginkan.

## 8. Teks & subtitle
Semua teks = overlay editing (huruf tebal, kontras tinggi, maks 2 baris, ≤ 6 kata per overlay). Beri timecode, posisi, animasi. Subtitle bersumber dari naskah narasi. Zona aman TikTok (perkiraan, cek preview editor): hindari ±12–15% atas, ±20–25% bawah, dan sisi kanan (tombol UI). Jangan menduplikasi narasi persis; overlay menambah (angka, label waktu, pertanyaan).

## 9. Editing & ekspor
Peta: ID adegan, durasi final (hasil trim dari render 8 dtk), narasi, musik/SFX, overlay, transisi. Grading konsisten sepanjang cerita (mis. hangat → dingin). Ekspor 1080×1920, 24/30 fps, H.264. Loudness pedoman ±−14 LUFS; musik 18–22 dB di bawah narasi saat bicara. Periksa: tanpa watermark/border, tanpa teks salah, audio bersih.

## 10. Desain suspense
Rilis informasi bertahap, bukti sebelum penjelasan, kontras normal/abnormal, skala, keheningan, suara di luar layar, reaksi, pengulangan motif, eskalasi. Setiap adegan harus: memberi petunjuk, mengubah situasi, menunjukkan konsekuensi, memperdalam taruhan, menjawab, atau membuka pertanyaan baru.

## 11. Integritas sains
Tabel: Butir | Klasifikasi (fakta / ekstrapolasi / asumsi fiksi) | Penjelasan | Sumber | Status verifikasi. Nyatakan asumsi di awal video (kartu premis). Hindari presisi palsu dan proses seketika yang sebenarnya bertahap (atau sebaliknya). Angka di layar wajib punya sumber dan satuan. Jika riset web tak tersedia → semua angka "perlu verifikasi" dan jangan ditampilkan di layar sebelum diverifikasi.

## 12. QA & kesiapan
Bobot: Hook 0–2 dtk 20% · Suspense 20% · Kontinuitas 20% · Kualitas visual 15% · Audio/narasi 10% · Integritas sains 10% · Ending/CTA 5%. Target ≥85/100.
**Blocker (menahan publikasi berapa pun skornya):** kesalahan fakta kritis; bertentangan dengan fisika premis sendiri; narasi tak jelas; ucapan/teks asing tak sengaja; wajah/karakter berubah jelas; kontinuitas rusak; teks tak terbaca atau salah eja; tidak ada penanda premis hipotetis; label AI TikTok belum aktif.
Skor "di atas kertas" (sebelum render) hanya menilai rencana; skor final diisi setelah klip dirender dan dirakit.

## 13. TikTok
Paket: judul sampul, caption (Indonesia, menyebut bahwa ini skenario hipotetis), hashtag yang sesuai (hindari #fakta untuk skenario fiktif), komentar sematan, CTA, hipotesis jam posting (hipotesis, bukan prediksi). Aktifkan label konten buatan AI. Hindari klaim "kejadian nyata".

## 14. Pelajaran dari WW-001 (jangan diulang)
1. Cahaya padam seketika, bukan perlahan; yang bertahap adalah pendinginan.
2. Penjelasan harus datang SEBELUM akibatnya selesai.
3. Hook tidak boleh bertentangan dengan visual (narasi "tidak terbit" vs matahari terbit di layar).
4. Pembuka tenang = hook gagal.
5. Suara Flow tak dapat diandalkan → silent plate + TTS satu pass.
6. Teks buatan model tak andal → overlay.
7. Sheet multi-tampilan, karakter tanpa referensi, properti tak terpakai, varian malam tak ada = kontinuitas rapuh.
8. Satu klip terlalu banyak aksi/potongan = gagal.
9. Visual (rim biru, awan terang) tak boleh melawan premis.
10. Paket tanpa tabel sains, peta subtitle, timeline, skor = belum selesai.

## 15. Deliverables wajib per video
Riset & tabel sains; uji fisika; cerita, narasi, beat sheet; continuity bible; prompt referensi; prompt keyframe per adegan; prompt video per adegan + Plan B; naskah narasi + brief TTS; prompt musik; daftar SFX; peta audio; peta teks/subtitle bertimecode; timeline editing & ekspor; paket TikTok; QA berskor; baris arsip + isi baru file arsip.
