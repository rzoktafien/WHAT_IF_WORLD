# WHAT IF WORLD — PANDUAN PRODUKSI UTAMA V3

## 1. Prinsip produk
WHAT IF WORLD menghasilkan cerita hipotetis yang memicu rasa ingin tahu, memberi pemahaman sains yang benar, dan memiliki identitas visual konsisten. Konten bukan berita, bukan simulasi prediktif, dan bukan rekaman kejadian nyata. Kualitas diukur dari ketepatan, kejernihan cerita, kualitas audiovisual, dan kejujuran framing—bukan janji viral.

## 2. Arsitektur cerita 45–60 detik
Gunakan sebagai pola awal, bukan aturan kaku:
- 0–2 dtk: visual anomaly/pattern interrupt.
- 2–8 dtk: pertanyaan dan asumsi premis.
- 8–20 dtk: bukti pertama + perubahan cara pandang.
- 20–38 dtk: eskalasi sebab-akibat dan taruhan manusia.
- 38–52 dtk: reveal sains dan konsekuensi yang paling berarti.
- 52–60 dtk: payoff, batas ketidakpastian, pertanyaan penonton.
Untuk durasi lain, rancang ulang beat berdasarkan fungsi; jangan sekadar mempercepat narasi.

## 3. Story design
Sebelum menulis prompt, tetapkan: pertanyaan inti, premis, kondisi awal, variabel yang diubah, variabel yang tetap, mekanisme kausal, skala waktu, ruang lingkup geografis, konsekuensi langsung/tidak langsung, dan batas model. Gunakan satu sudut cerita yang kuat, bukan katalog bencana.

## 4. Sains dan sumber
- Buat claim ledger terpisah dari naskah.
- Sumber primer: lembaga ilmiah/pemerintah, data resmi, paper peer-reviewed, dokumentasi teknis, operator sistem. Sumber sekunder hanya untuk konteks atau triangulasi.
- Catat judul, organisasi/penulis, tanggal publikasi, tanggal peristiwa/data, URL, tanggal akses, jenis sumber, klaim yang didukung, dan keterbatasan.
- Klaim kritis: minimal satu sumber primer yang langsung mendukung; bila tidak ada, dua sumber independen kuat dan label confidence turun.
- Pisahkan korelasi, mekanisme, atribusi sebab, proyeksi, dan spekulasi. Kutip angka dengan satuan, basis, wilayah, dan rentang waktu.
- Jangan memakai angka hanya demi “wow factor”. Jika klaim tidak dibutuhkan untuk cerita atau tidak cukup kuat, hapus.
- Setiap video memuat penanda bahwa ini skenario hipotetis, dan menyebut asumsi utama bila penting untuk pemahaman.

## 5. Desain suspense dan informasi
Tampilkan bukti yang dapat diamati sebelum penjelasan, tetapi jangan menunda penjelasan kausal sampai penonton salah memahami rangkaian. Gunakan pola: anomali → pertanyaan → bukti → interpretasi → konsekuensi → batas/nuansa → payoff. Setiap shot harus mengubah informasi, emosi, skala, atau taruhan.

## 6. Visual development
- Gaya: live-action photorealistic, realistic cinematic/documentary, naturalistic physics, bukan ilustrasi generik.
- Kunci karakter: wajah, usia, rambut, warna kulit, proporsi, kostum per fase, aksesori, perilaku.
- Kunci lokasi: geometri, arah, cuaca, waktu, sumber cahaya, landmark.
- Kunci properti: bentuk, warna, skala, posisi, fungsi naratif.
- Satu referensi per subjek; buat varian lokasi/karakter melalui edit referensi jika menjaga konsistensi.
- Shot prompt: satu aksi utama, satu gerak kamera, keadaan awal dan akhir jelas. Hindari multi-cut, banyak aktor, dan banyak perubahan simultan.
- Setiap shot memiliki ID, tujuan naratif, durasi target, asset refs, keyframe, prompt, negative constraints, Plan B, dan kriteria penerimaan.

## 7. Generative production
Sebelum batch, lakukan pilot 1–2 shot. Catat tool, model, versi, mode, aspect ratio, duration, resolution, seed bila tersedia, prompt, assets, dan output path. Bandingkan mode hanya pada variabel yang sedang diuji. Jangan menganggap seed selalu menjamin hasil identik lintas versi/model.
Default silent plate. Bila generator tidak dapat menjamin audio, jangan minta dialog/VO. Rekam VO terpisah; musik dan SFX terpisah; mixing dilakukan di editor.

## 8. Audio
- VO: satu sesi TTS dengan voice ID/model/setting konsisten; cek pengucapan nama dan angka; potong berdasarkan timecode setelah render.
- Musik: satu bed atau beberapa cue yang ditandai; hak komersial harus diperiksa.
- SFX/ambience: diegetik, tidak menutupi VO; hindari ambience yang bertentangan dengan premis.
- Mix: atur loudness dan true peak berdasarkan target platform/editor; angka LUFS adalah target kerja, bukan hukum universal. Dengarkan dengan headphone dan speaker ponsel.

## 9. Editing
Gunakan timeline frame-accurate bila memungkinkan. Pisahkan tracks: video, VO, music, ambience/SFX, titles, subtitles. Simpan project file dan export preset. Gunakan format timeline interchange (mis. OTIO) bila workflow/editor mendukung; media tetap dikelola sebagai aset eksternal. Validasi frame rate, aspect ratio, codec, audio, safe zones, captions, dan watermark.

## 10. Rights, safety, and provenance
Catat pemilik/sumber, lisensi, batas komersial, attribution, tanggal unduh, dan modifikasi untuk semua aset pihak ketiga. Jangan meniru suara orang nyata tanpa hak/izin. Jangan menampilkan logo/brand secara menyesatkan. Hindari gambar bencana sintetis yang dipasarkan sebagai kejadian aktual. Simpan catatan disclosure AI sesuai kebijakan platform saat publikasi.

## 11. QA model
Rubrik 100 poin:
- Hook/clarity 15
- Story causality & suspense 15
- Scientific integrity 20
- Visual continuity 15
- Shot execution 10
- Audio/VO 10
- Editing/readability 10
- Ending/CTA/framing 5

Target ≥85. Blocker selalu mengalahkan skor. Beri skor hanya jika ada bukti yang diperiksa. Pisahkan `PLAN_QA` dari `RENDER_QA`. Publikasi memerlukan semua blocker lulus dan persetujuan manusia.

## 12. Deliverables wajib
Production dossier; intelligence provenance; source & claim ledger; story beat sheet; VO script; continuity bible; asset register; shot register; keyframe/video prompts; generation log; audio map; subtitle file/table; edit timeline; rights register; render QA; release checklist; archive update.

## 13. Failure taxonomy
- `SCIENCE_FAIL`: klaim salah/tidak didukung → tahan naskah, revisi ledger.
- `STORY_FAIL`: kausalitas/retensi tidak jelas → revisi beat sheet sebelum prompt.
- `CONTINUITY_FAIL`: karakter/lokasi/objek berubah → perbaiki referensi dan shot plan; rerender hanya shot terdampak.
- `GENERATION_FAIL`: output cacat → simpan output, prompt, parameter, failure note; jalankan Plan B.
- `AUDIO_FAIL`: VO/ambience/music tidak konsisten → re-render track terpisah.
- `EDIT_FAIL`: timing, safe-zone, codec, sync → perbaiki timeline/export.
- `RIGHTS_FAIL`: hak pakai tidak jelas → ganti aset atau tahan rilis.
- `RELEASE_FAIL`: disclosure/metadata/caption/approval belum lengkap → jangan publish.

## 14. Status produksi
`IDEA_CANDIDATE → IDEA_APPROVED → RESEARCH → STORY → PREPRODUCTION → GENERATION → EDITING → QA → RELEASE_APPROVED → PUBLISHED → ARCHIVED`
Cabang: `HOLD`, `REWORK`, `REJECTED`. Status tidak boleh dinaikkan tanpa bukti dan approval yang ditentukan.

## 15. Google Flow prompt handoff — standar V3.2
Untuk setiap shot yang digenerasi di Google Flow, dossier WAJIB menyediakan tiga prompt terpisah dan siap salin:
1. **KEYFRAME IMAGE PROMPT** — menghasilkan gambar referensi awal yang menetapkan komposisi, subjek, lingkungan, tekstur, pencahayaan, sudut/lensa, dan framing.
2. **VIDEO PROMPT** — menggerakkan keyframe yang sama; wajib menyebut durasi, aspect ratio, satu aksi utama, satu gerak kamera, kondisi awal/akhir, serta elemen yang harus dipertahankan.
3. **AUDIO PROMPT** — menghasilkan audio diegetik shot tersebut (ambience/SFX) secara terpisah dari prompt video. Nyatakan perspektif, intensitas, tekstur, dan larangan suara yang tidak sesuai. Default: tanpa musik dan tanpa VO.

**Workflow operator:** Human Producer menyalin prompt keyframe ke image generation; memilih hasil terbaik; memasukkan hasil itu sebagai visual reference untuk video; lalu memasukkan prompt video dan prompt audio secara terpisah pada fitur Google Flow yang tersedia di akun/mode aktual. ChatGPT tidak mengasumsikan nama model, dukungan audio, durasi, atau parameter yang belum diverifikasi pada UI akun. Catat model/mode/setting yang benar-benar terlihat.

**Continuity:** keyframe adalah anchor visual per shot. Video harus mempertahankan komposisi, geometri, identitas, objek, pencahayaan, dan kondisi yang ditetapkan keyframe. Untuk elemen berulang lintas shot, gunakan canonical reference yang sama; jangan mengandalkan teks saja bila image reference tersedia.

**Audio policy:** musik adalah track master terpisah yang dipilih saat editing/posting; jangan meminta musik generatif per shot. VO dibuat/direkam terpisah dan disinkronkan saat editing. Audio prompt per shot hanya ambience/SFX yang relevan. Jika fitur audio tidak tersedia pada mode akun yang dipakai, tandai AUDIO_PROMPT_READY / AUDIO_GENERATION_UNAVAILABLE dan siapkan fallback SFX manual; jangan klaim audio berhasil dibuat.

**Minimal handoff:** tampilkan hanya ID/durasi, keyframe prompt, video prompt, audio prompt, dan Plan B. Penjelasan editorial panjang tidak masuk ke blok prompt.
