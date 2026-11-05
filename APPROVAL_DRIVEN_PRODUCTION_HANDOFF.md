# APPROVAL-DRIVEN PRODUCTION HANDOFF — V3.2

Dokumen ini melengkapi 01_INSTRUKSI_PROJECT.md, 02A_MODULE_ARCHITECTURE.md, dan 00_SETUP_AND_OPERATIONS.md. Berlaku untuk semua produksi.

## Aturan auto-advance
- Setelah pengguna memilih/menyetujui IDEA, AI langsung mengerjakan RESEARCH sampai dossier dan claim ledger siap ditinjau; berhenti hanya untuk approval RESEARCH.
- Setelah pengguna menyetujui RESEARCH, AI langsung mengerjakan STORY sampai beat sheet, VO, claim mapping, dan risk framing siap ditinjau; berhenti hanya untuk approval STORY.
- Setelah pengguna menyetujui STORY (misalnya `SETUJU` dalam konteks review STORY), AI WAJIB otomatis mengerjakan PRE-PRODUCTION sampai seluruh paket prompt siap pakai. Tidak boleh meminta `LANJUT`, approval PRE-PRODUCTION tambahan, atau meminta pengguna membuka PR/dokumen untuk menyalin prompt.
- Paket prompt mencakup setiap shot: keyframe/image prompt, video prompt, audio prompt atau keputusan silence, negative constraints, asset/reference instructions, acceptance criteria, dan Plan B; ditambah VO, subtitle/timecode, edit assembly, deskripsi/caption TikTok, hashtag, pinned comment/CTA, prompt gambar sampul TikTok (Bahasa Inggris) beserta teks overlay Indonesia, rights/provenance register, serta QA/release checklist sesuai template 03.
- Jika stimulus visual orisinal diperlukan, AI membuatnya dengan kemampuan image generation yang tersedia, lalu memeriksa hasil dan menyiapkan derivatif deterministik bila didukung. Jangan menugaskan pengguna membuat aset perantara yang dapat dikerjakan AI. Jika tool tidak tersedia, berikan prompt copy-ready langsung di chat dan tandai aset belum dibuat.
- Pengguna hanya menjalankan generasi eksternal yang memang manual (saat ini Google Flow), mengembalikan hasil, dan memberi approval manusia yang diwajibkan. AI menyiapkan seluruh prompt dan instruksi; AI tidak boleh mengklaim submit/render/inspect tanpa bukti.
- Setelah prompt pack lengkap, serahkan hasil yang dapat langsung dipakai di chat: seluruh prompt per shot, deskripsi/caption, hashtag, dan prompt gambar sampul TikTok. GitHub hanya arsip/sumber kerja; jangan menjadikan tautan repository sebagai pengganti penyerahan hasil. Jangan melempar tugas administratif seperti membuka PR, mencari bagian dokumen, atau membuat file turunan kepada pengguna.
- Auto-advance tidak melewati blocker sains, hak, keselamatan, karakter kanonik, inspeksi media, pilot/batch approval, atau final release. Bedakan `PROMPT_PACK_READY` dari `GENERATION_AUTHORIZED` dan `RENDER_COMPLETE`.
- Bila ada blocker yang hanya dapat diselesaikan pengguna (mis. tindakan manual di Google Flow atau approval wajib), kerjakan semua bagian lain yang tidak terblokir terlebih dahulu, lalu minta hanya satu tindakan konkret yang benar-benar diperlukan.

## Batas eksekusi
- Auto-advance berarti AI mengerjakan artefak berikutnya tanpa meminta perintah LANJUT atau approval tahap administratif tambahan.
- Auto-advance bukan persetujuan manusia dan tidak menghapus gate hak, keselamatan, sains, karakter kanonik, pilot/batch, inspeksi media, QA, atau rilis.
- Google Flow tetap dijalankan manual oleh Human Producer. AI tidak boleh mengklaim submit/render/inspect tanpa bukti.
- Jika tool tidak tersedia, AI memberi prompt copy-ready dan menyatakan aset belum dibuat. Jangan mengalihkan tugas dokumentasi/prompt kepada pengguna.
