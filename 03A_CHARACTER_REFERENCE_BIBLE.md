# WHAT IF WORLD — CHARACTER REFERENCE BIBLE V1

Status: standard operasional. Setiap profil karakter tetap DRAFT sampai disetujui produser manusia.

## Tujuan
Menjaga identitas visual karakter berulang/kritis lintas shot. Karakter latar satu kali tidak perlu dossier penuh kecuali kontinuitas naratif menuntutnya.

## Kontrak identitas
- ID permanen: AST-CHAR-###. Jangan pernah mendaur ulang ID.
- Catat production ID, versi profil semver, nama/label fiksi, status, pemilik, timestamp, dan shot terkait.
- Catat ciri visual yang diperlukan untuk kontinuitas: bentuk wajah, fitur pembeda, rambut, warna kulit bila relevan secara visual, postur/build, dan ciri invariant.
- Pisahkan identitas invariant dari ekspresi, pose, pencahayaan, kondisi basah/kotor, riasan luka, dan wardrobe.
- Simpan canonical reference: URI gambar master atau prompt referensi persis, provenance, creator/source, rights status, checksum bila tersedia.
- Wardrobe variants harus diberi ID dan shot/fase pemakaian.
- Catat prohibited drift dan perubahan yang diizinkan.
- Hindari inferensi identitas orang nyata, etnisitas, kondisi medis, atau atribut sensitif dari gambar generatif.

## Hierarki referensi
1. Canonical character sheet yang disetujui.
2. Wardrobe/phase reference yang disetujui.
3. Keyframe shot untuk pose, ekspresi, pencahayaan, dan komposisi.
4. Prompt teks sebagai instruksi pendukung, bukan pengganti referensi visual yang tersedia.
Jika referensi bertentangan, HOLD dan rekonsiliasi. Jangan menggabungkan dua wajah atau mengganti master secara diam-diam.

## Lifecycle
DRAFT → REVIEW → APPROVED → SUPERSEDED atau REJECTED.
- DRAFT: usulan, belum kanonik.
- REVIEW: siap dibandingkan dengan cerita, hak, dan continuity.
- APPROVED: disetujui secara eksplisit oleh produser manusia.
- SUPERSEDED: diganti versi baru; sejarah tetap disimpan.
- REJECTED: bukan referensi kanonik; simpan alasan bila berguna.
File gambar yang ada bukan bukti persetujuan.

## Prosedur pembuatan
1. Buat master netral (frontal, 3/4, profil bila alat mendukung), ekspresi netral, pencahayaan sederhana.
2. Periksa geometri wajah, siluet rambut, proporsi, penanda pembeda, dan wardrobe.
3. Simpan prompt, model/tool/version/mode, parameter, seed bila ada, provenance, dan rights.
4. Master asli immutable; setiap edit menjadi versi baru dan catat parent asset.
5. Buat wardrobe/condition variant dari identitas yang sudah disetujui.
6. Hubungkan setiap shot ke character ID dan profile version yang dipakai; simpan versi itu pada character_reference_versions di shot.
7. Bila tool tidak menerima image reference, gunakan identity-lock prompt dan naikkan continuity risk.

## Pemeriksaan per shot
Periksa wajah, rambut, build, wardrobe sesuai fase cerita, aksesori/prop, umur visual, screen direction, eyeline, geografi, cahaya, perubahan keadaan, extra character, identity blending, teks/logo/artifact. Catat PASS/REWORK/HOLD dan bukti. Perubahan master membuat semua shot dependen STALE sampai diperiksa ulang. Validator memeriksa bahwa ID dan versi referensi pada shot cocok dengan profil karakter.

## Hak dan privasi
Catat creator/source, lisensi/izin, hak komersial, atribusi, dan tanggal akses. Jangan gunakan likeness/voice orang nyata tanpa hak dan persetujuan terdokumentasi. "Ditemukan online" bukan lisensi.

## Kontrak data
Gunakan schemas/character_reference.schema.json. Manifest menyimpan character_references; shot menghubungkan karakter melalui character_ids dan mengikat versi profil melalui character_reference_versions. ID selalu AST-CHAR-###.

## Template ringkas
```yaml
id: AST-CHAR-001
production_id: WW-003
version: 1.0.0
name: "[label karakter fiksi]"
status: DRAFT
identity:
  face_shape: "[bentuk wajah]"
  distinctive_features: ["[fitur]"]
  hair: "[rambut]"
  invariant_traits: ["[ciri yang tidak boleh berubah]"]
canonical_reference:
  kind: prompt
  prompt: "[prompt referensi persis dalam bahasa Inggris]"
  uri: null
  provenance: "originally generated for this project"
  checksum: null
wardrobe_variants: []
rights_status: NOT_REQUIRED
linked_shots: ["SH-001"]
approval:
  by: null
  at: null
```
Template ini bukan karakter yang telah disetujui. Isi, tinjau, dan minta persetujuan manusia sebelum dipakai sebagai kanon.
