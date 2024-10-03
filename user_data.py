import datetime

from django.contrib.auth.models import User

from main.models import (Aspect, AssignedEvaluation, Evaluation,
                        EvaluatorOption, Question, QuestionOption,
                        SubQuestion, UserProfile)

password = "@PEKPPPkotaProb"  # The password for all users
users_data = [
    {"username": "SEKRETARIAT DAERAH", "email": "Sekdaprob@mail.com", "role": "assignee"},
    {"username": "SEKRETARIAT DPRD", "email": "sekdprd@mail.com", "role": "assignee"},
    {"username": "INSPEKTORAT", "email": "inspektoratprob@mail.com", "role": "assignee"},
    {"username": "DINAS PENDIDIKAN DAN KEBUDAYAAN", "email": " disdikbudprob@mail.com", "role": "assignee"},
    {"username": "DINAS KESEHATAN, PENGENDALIAN PENDUDUK DAN KELUARGA BERENCANA", "email": "dinkesppkbprob@mail.com", "role": "assignee"},
    {"username": "DINAS PEKERJAAN UMUM, PENATAANRUANG, PERUMAHAN DAN KAWASAN PERMUKIMAN ", "email": "dpuperkimprob@mail.com", "role": "assignee"},
    {"username": "DINAS SOSIAL, PEMBERDAYAAN PEREMPUAN DAN PERLINDUNGAN ANAK", "email": "dinsosppkbprob@mail.com", "role": "assignee"},
    {"username": "DINAS PENANAMAN MODAL DAN PELAYANAN TERPADU SATU PINTU", "email": "dpmptspprob@mail.com", "role": "assignee"},
    {"username": "DINAS LINGKUNGAN HIDUP", "email": "dlhprob@mail.com", "role": "assignee"},
    {"username": "DINAS KEPENDUDUKAN DAN PENCATATAN SIPIL ", "email": "dispendukcapilprob@mail.com", "role": "assignee"},
    {"username": "DINAS PERHUBUNGAN", "email": "dishubprob@mail.com", "role": "assignee"},
    {"username": "DINAS KOMUNIKASI DAN INFORMATIKA", "email": "diskominfo@mail.com", "role": "assignee"},
    {"username": "DINAS KOPERASI, USAHA KECIL DAN MENENGAH, DAN PERDAGANGAN ", "email": "diskoperindag@mail.com", "role": "assignee"},
    {"username": "DINAS KEPEMUDAAN, OLAHRAGA DAN PARIWISATA ", "email": "dispobpar@mail.com", "role": "assignee"},
    {"username": "DINAS PERPUSTAKAAN DAN KEARSIPAN", "email": "disperpusip@mail.com", "role": "assignee"},
    {"username": "DINAS KETAHANAN PANGAN, PERTANIAN DAN PERIKANAN ", "email": "dispertahankan@mail.com", "role": "assignee"},
    {"username": "SATUAN POLISI PAMONG PRAJA ", "email": "satpolpp@mail.com", "role": "assignee"},
    {"username": "DINAS PERINDUSTRIAN DAN TENAGA KERJA ", "email": "disperinaker@mail.com", "role": "assignee"},
    {"username": "BADAN PERENCANAAN PEMBANGUNAN DAERAH, PENELITIAN DAN PENGEMBANGAN", "email": "bappedalitbang@ppkadmail.com", "role": "assignee"},
    {"username": "BADAN PENDAPATAN, PENGELOLAAN KEUANGAN DAN ASET DAERAH ", "email": "bppkad@mail.com", "role": "assignee"},
    {"username": "BADAN KEPEGAWAIAN DAN PENGEMBANGAN SUMBER DAYA MANUSIA", "email": "bkpsdm@mail.com", "role": "assignee"},
    {"username": "BADAN KESATUAN BANGSA DAN POLITIK", "email": "bakesbangkpol@mail.com", "role": "assignee"},
    {"username": "KECAMATAN KADEMANGAN ", "email": "kademangan@mail.com", "role": "assignee"},
    {"username": "KECAMATAN KANIGARAN", "email": "kanigaran@mail.com", "role": "assignee"},
    {"username": "KECAMATAN KEDOPOK ", "email": "kedopok@mail.com", "role": "assignee"},
    {"username": "KECAMATAN MAYANGAN", "email": "mayangan@mail.com", "role": "assignee"},
    {"username": "KECAMATAN WONOASIH ", "email": "wonoasih@mail.com", "role": "assignee"},
    {"username": "BADAN PENANGGULANGAN BENCANA DAERAH", "email": "bpbd@mail.com", "role": "assignee"},
    {"username": "Bagian Organisasi", "email": "Evaluatororganisasi@mail.com", "role": "evaluator"},
    {"username": "Badan Kepegawaian Pengembngan Sumber Daya Manusia", "email": "Evaluatorbkpsdm@mail.com", "role": "evaluator"},
    {"username": "Dinas Pekerjaan Umum, Penataan Ruang, Perumahan dan Kawasan Permukiman", "email": "Evaluatordpuperkim@mail.com", "role": "evaluator"},
    {"username": "Dinas Komunikasi dan Informatika evaluator", "email": "Evaluatordiskominfo@mail.com", "role": "evaluator"},
    {"username": "Dinas Komunikasi dan Informatika evaluator 2", "email": "Evaluatordiskominfo2@mail.com", "role": "evaluator"},
    {"username": "Badan Perencanaan Pembangunan Daerah, Penelitian dan Pengembangan", "email": "Evaluatorbappeda@mail.com", "role": "evaluator"},
]

for user_data in users_data:
    user = User.objects.create_user(username=user_data['username'], email=user_data['email'], password=password, is_staff=True)
    user.save()
    UserProfile.objects.create(user=user, role=user_data['role'])

Evaluation.objects.create(
        name="Evaluasi Formulir Pemerintah Kota"
    )

aspect_data = [
    {"name": "Kebijakan Pelayanan", "evaluator": User.objects.get(username="Bagian Organisasi", email="Evaluatororganisasi@mail.com")},
    {"name": "Profesionalisme SDM", "evaluator":  User.objects.get(username="Badan Kepegawaian Pengembngan Sumber Daya Manusia", email="Evaluatorbkpsdm@mail.com")},
    {"name": "Sarana dan Prasarana", "evaluator":  User.objects.get(username="Dinas Pekerjaan Umum, Penataan Ruang, Perumahan dan Kawasan Permukiman", email="Evaluatordpuperkim@mail.com")},
    {"name": "Sistem Informasi Pelayanan Publik (SIPP)", "evaluator":  User.objects.get(username="Dinas Komunikasi dan Informatika evaluator", email="Evaluatordiskominfo@mail.com")},
    {"name": "Konsultasi dan Pengaduan", "evaluator":  User.objects.get(username="Dinas Komunikasi dan Informatika evaluator 2", email="Evaluatordiskominfo2@mail.com")},
    {"name": "Inovasi", "evaluator":  User.objects.get(username="Badan Perencanaan Pembangunan Daerah, Penelitian dan Pengembangan", email="Evaluatorbappeda@mail.com")},
]

for aspect_data in aspect_data:
    Aspect.objects.create(name=aspect_data['name'], evaluator=aspect_data['evaluator'])

questions_data = [
# kebijakan pelayanan
    {
        "name": "Tersedia Standar Pelayanan (SP) sesuai dengan ketentuan peraturan perundang-undangan yang berlaku.",
        "point_weight": 17,
        "aspect": "Kebijakan Pelayanan",
        "subquestions": [
            {
                "subquestion_text": "Apakah sudah dibuat Standar Pelayanan, baik sebagian ataupun seluruh jenis pelayanan?",
                "question_type": "yes_or_no", 
            },
            {
                "subquestion_text": "Berapa Jumlah Jenis Pelayanan yang dimiliki?",
                "question_type": "text", 
            },
            {
                "subquestion_text": "Berapa Jumlah Jenis Standar Pelayanan yang dibuat?",
                "question_type": "text", 
            }, {
                "subquestion_text": "Apakah Standar Pelayanan yang disusun telah memenuhi 14 komponen?",
                "question_type": "yes_or_no", 
            },
            {
                "subquestion_text": "Apakah dalam proses penyusunan Standar Pelayanan telah melibatkan unsur masyarakat?",
                "question_type": "yes_or_no", 
            },{
                "subquestion_text": "Apakah Standar Pelayanan telah ditetapkan?",
                "question_type": "yes_or_no", 
            },{
                "subquestion_text": "Apakah Standar Pelayanan yang dimiliki dilakukan monev?",
                "question_type": "yes_or_no", 
            },
        ]
    },
    {
        "name": "Proses penyusunan dan perubahan SP telah melibatkan unsur masyarakat.",
        "point_weight": 14,
        "aspect": "Kebijakan Pelayanan",
        "subquestions": [
            {
                "subquestion_text": "Apakah SP dipublikasikan?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Apakah SP yang dipublikasikan seluruh 6 komponen service delivery",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Media publikasi SP",
                "question_type": "multi_selection",
                "options": ["Media Cetak / Non Elektronik", "Media Elektronik", "Media Sosial", "Website", "Aplikasi yang bisa diunduh", "SIPP Nasional"]
            }, 
        ]
    },
    {
        "name": "Jumlah media publikasi untuk komponen service delivery.",
        "point_weight": 7,
        "aspect": "Kebijakan Pelayanan",
        "subquestions": [
            {
                "subquestion_text": "Apakah SP dipublikasikan?",
                "question_type": "yes_or_no", 
            },
            {
                "subquestion_text": "Apakah SP yang dipublikasikan seluruh 6 komponen service delivery",
                "question_type": "yes_or_no", 
            },
            {
                "subquestion_text": "Media publikasi SP",
                "question_type": "multi_selection",
                "options": [
                  "Media Cetak / Non Elektronik", 
                  "Media Elektronik", 
                  "Media Sosial", 
                  "Website", 
                  "Aplikasi yang bisa diunduh", 
                  "SIPP Nasional"
                ]
            },
        ]
    },
    {
        "name": "Telah dilakukan peninjauan ulang secara berkala terhadap Standar Pelayanan.",
        "point_weight": 14,
        "aspect": "Kebijakan Pelayanan",
        "subquestions": [
            {
                "subquestion_text": "Pernyataan ( jawaban)",
                "question_type": "one_selection",
                "options": ["Tidak dilaksanakan peninjauan ulang secara berkala terhadap Standar Pelayanan.", 
                            "Media Elektronik", 
                            "Dilakukan peninjauan ulang 3 tahun atau lebih terhadap seluruh jenis layanan.", 
                            "Dilakukan peninjauan ulang 2 tahun atau lebih terhadap sebagian jenis layanan.", 
                            "Dilakukan peninjauan ulang 2 tahun atau lebih cepat terhadap seluruh jenis layanan.", 
                            "Dilakukan peninjauan ulang 1 tahun atau lebih cepat terhadap sebagian jenis layanan.",
                            "Dilakukan peninjauan ulang 1 tahun atau lebih cepat terhadap seluruh jenis layanan."]
                            
            }, 
        ]
    },
    {
        "name": "Pemenuhan siklus Maklumat Pelayanan (ketersediaan, penetapan, dan publikasi).",
        "point_weight": 10,
        "aspect": "Kebijakan Pelayanan",
        "subquestions": [
            {
                "subquestion_text": "Apakah tersedia maklumat pelayanan yang ditetapkan?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Apakah isi maklumat pelayanan sesuai dengan peraturan perundangan yang berlaku?",
                "question_type": "yes_or_no",
            },
            {
                "subquestion_text": "Apakah maklumat pelayanan dipublikasikan?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Apa media publikasi yang digunakan?",
                "question_type": "multi_selection",
                "options": ["Elektronik", "Non Elektronik"]
            }, 
        ]
    },
    {
        "name": "SKM yang dilaksanakan sesuai dengan PermenPANRB.",
        "point_weight": 17,
        "aspect": "Kebijakan Pelayanan",
        "subquestions": [
            {
                "subquestion_text": "Apakah Unit Lokus telah melaksanakan Survei Kepuasan Masyarakat?",
                "question_type": "yes_or_no", 
            },
            {
                "subquestion_text": "Berapa kali dalam satu tahun dilaksanakan SKM?",
                "question_type": "text", 
            },
            {
                "subquestion_text": "Tuliskan nilai IKM dalam konversi 100, dan sebutkan periode pelaksanaan SKMnya. Contoh: 89 untuk periode Semester II Tahun 2023)",
                "question_type": "text", 
            },
            {
                "subquestion_text": "Apakah pelaksanaan SKM sesuai dengan PermenPANRB yang berlaku?",
                "question_type": "yes_or_no", 
            },
            {
                "subquestion_text": "Apakah hasil SKM dipublikasikan?",
                "question_type": "yes_or_no", 
            },
            {
                "subquestion_text": "Apa media publikasi yang digunakan?",
                "question_type": "multi_selection",
                "options": ["Elektronik", "Non Elektronik"]
            },
            {
                "subquestion_text": "Apakah hasil SKM dilakukan tindak lanjut?",
                "question_type": "yes_or_no", 
            }
        ]
    },
    {
        "name": "Jumlah media publikasi hasil SKM.",
        "point_weight": 7,
        "aspect": "Kebijakan Pelayanan",
        "subquestions": [
            {
                "subquestion_text": "Pernyataan ( jawaban)",
                "question_type": "one_selection",
                "options": ["Media Cetak / Non Elektronik", "Media Elektronik", "Media Sosial", "Website", "Aplikasi yang bisa diunduh"]
            }, 
        ]
    },
    {
        "name": "Tindak lanjut hasil SKM dan kedalaman ruang lingkup untuk setiap jenis pelayanan.",
        "point_weight": 7,
        "aspect": "Kebijakan Pelayanan",
        "subquestions": [
            {
                "subquestion_text": "Apakah sudah dibuat rencana tindak lanjut dari SKM yang sudah dilaksanakan?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Berapa persen rencana tindak lanjut yang direalisasikan dalam 1 tahun terakhir?",
                "question_type": "text",
            },
            {
                "subquestion_text": "Apakah dibuat laporan tindak lanjut yang dilakukan?",
                "question_type": "yes_or_no",
            }, 
        ]
    },
    {
        "name": "Kecepatan tindak lanjut hasil SKM seluruh jenis pelayanan.",
        "point_weight": 7,
        "aspect": "Kebijakan Pelayanan",
        "subquestions": [
            {
                "subquestion_text": "Apakah hasil SKM ditindaklanjuti?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Berapa lama tindak lanjut hasil SKM?",
                "question_type": "one_selection",
                "options": ["1 tahun setelah laporan SKM terbit", 
                            "9 bulan setelah laporan SKM terbit", 
                            "6 bulan setelah laporan SKM terbit", 
                            "3 bulan setelah laporan SKM terbit", 
                            "1 bulan setelah laporan SKM terbit"]
            },
        ]
    },
  # Profesionalisme SDM
    {
        "name": "Tersedia waktu pelayanan yang memudahkan pengguna layanan.",
        "point_weight": 10,
        "aspect": "Profesionalisme SDM",
        "subquestions": [
            {
                "subquestion_text": "Apakah tersedia waktu pelayanan yang memudahkan pengguna layanan?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Bagaimana pelaksanaan poin nomor 1 tersebut?",
                "question_type": "multi_selection",
                "options": [
                  "Memiliki kebijakan jam pelayanan / kerja", 
                  "Tidak ada jeda pelayanan yang berarti istirahat pegawai dilakukan secara bergilir (shift) yang dapat dibuktikan dari publikasi jam layanan kepada masyarakat.", 
                  "Penambahan waktu layanan di luar jam pelayanan yang sudah ditentukan (masih di hari kerja).", 
                  "Penambahan waktu layanan di luar hari kerja namun dalam kondisi tertentu (Misal: Pembukaan CPNS, LAPOR SPT Tahunan).", 
                  "Penambahan waktu layanan di luar hari kerja namun secara rutin.", 
                  "Layanan 24 Jam: layanan yang merupakan inti pelayanan atau pendaftaran"
                ]
            }, 
        ]
    },
    {
        "name": "Tersedia Kode Etik dan Kode Perilaku Pelaksana dan/atau Budaya Pelayanan di lingkungan instansi.",
        "point_weight": 20,
        "aspect": "Profesionalisme SDM",
        "subquestions": [
            {
                "subquestion_text": "Apakah sudah tersedia Aturan Perilaku dan Kode Etik Pelaksana Pelayanan?",
                "question_type": "yes_or_no",
            },
            {
                "subquestion_text": "Aturan Perilaku dan Kode Etik Pelaksana Pelayanan meliputi:",
                "question_type": "multi_selection",
                "options": [
                  "Nilai dasar hak dan kewajiban", 
                  "Larangan KKN", 
                  "Larangan diskriminasi", 
                  "Sanksi", 
                  "Penghargaan",
                  ]
            }, 
        ]
    },
    {
        "name": "Tersedia mekanisme yang dibangun unit kerja untuk menjaga dan meningkatkan motivasi kerja Pelaksana pelayanan.",
        "point_weight": 20,
        "aspect": "Profesionalisme SDM",
        "subquestions": [
            {
                "subquestion_text": "Apakah tersedia mekanisme yang dibangun Unit Kerja untuk menjaga dan meningkatkan motivasi kerja?",
                "question_type": "yes_or_no",
            },
            {
                "subquestion_text": "Bagaimana mekanisme yang dibangun Unit Kerja untuk menjaga dan meningkatkan motivasi kerja pelaksana pelayanan?",
                "question_type": "multi_selection",
                "options": [
                  "Pemberian penghargaan.", 
                  "Pemberian kesempatan untuk mengikuti diklat.", 
                  "Pengembangan kapasitas melalui kesempatan mengikuti program beasiswa", 
                  "Program konseling.", 
                  "Program team/capacity building.", 
                  "Mekanisme lainnya yang dapat meningkatkan motivasi kerja pegawai."
                  ]
            }, 
        ]
    },
    {
        "name": "Tersedia kriteria pemberian penghargaan bagi pelaksana layanan yang berprestasi.",
        "point_weight": 20,
        "aspect": "Profesionalisme SDM",
        "subquestions": [
            {
                "subquestion_text": "Apakah kriteria yang digunakan dalam pemberian penghargaan?",
                "question_type": "multi_selection",
                "options": [
                  "Kehadiran", 
                  "Kinerja", 
                  "Kerja sama", 
                  "Inovatif/kreatif", 
                  "Penampilan", 
                  "Tidak pernah menerima komplain dari pengguna layanan"
                ]
            }, 
        ]
    },
    {
        "name": "Budaya Pelayanan.",
        "point_weight": 30,
        "aspect": "Profesionalisme SDM",
        "subquestions": [
            {
                "subquestion_text": "Bagaimana budaya pelayanan yang diterapkan oleh unit layanan dan diperlihatkan oleh Pelaksana layanan?",
                "question_type": "multi_selection",
                "options": [
                  "Mengenakan pakaian seragam", 
                  "Mengenakan identitas nama", 
                  "PIN/atribut/logo unit pelayanan", 
                  "Aturan penerapan 5S (Senyum, salam, sapa, sopan dan santun)", 
                  "Nilai-nilai budaya layanan", 
                ]
            }, 
        ]
    },
  # Sarana dan Prasarana
    {
      "name": "Tersedia tempat parkir dengan fasilitas pendukung.",
      "point_weight": 15,
      "aspect": "Sarana dan Prasarana",
      "subquestions": [
          {
              "subquestion_text": "Apakah tersedia tempat parkir kendaraan bermotor bagi pengguna layanan?",
              "question_type": "yes_or_no",
          },
          {
              "subquestion_text": "Apakah terdapat fasilitas parkir: ",
              "question_type": "multi_selection",
              "options": [
                "Ketersediaan parkir roda dua dan roda empat", 
                "Petugas parkir", 
                "Pemeriksaan karcis/kartu parkir", 
                "CCTV", 
                "Penitipan jaket/helm", 
                "Pelindung (Kanopi/atap bahan lain)",
                "Lainnya"
              ]
          }, 
      ]
    },
    {
        "name": "Kelayakan fasilitas ruang tunggu pelayanan",
        "point_weight": 23,
        "aspect": "Sarana dan Prasarana",
        "subquestions": [
            {
                "subquestion_text": "Sebutkan fasilitas pada ruang tunggu di Unit Saudara:",
                "question_type": "multi_selection",
                "options": [
                    "Kursi Tunggu", 
                    "Pendingin sirkulasi ruangan", 
                    "Air minum", 
                    "Bahan bacaan", 
                    "Pengisi daya baterai alat komunikasi/charger booth", 
                    "Mesin antrian dilengkapi monitor",
                    "Televisi",
                    "Hotspot/wifi",
                    "Lainnya",
                ]
            }, 
        ]
        },
    {
        "name": "Tersedia sarana toilet pengguna layanan yang layak pakai.",
        "point_weight": 20,
        "aspect": "Sarana dan Prasarana",
        "subquestions": [
            {
                "subquestion_text": "Apakah tersedia toilet untuk pengguna layanan?",
                "question_type": "yes_or_no",
            },
            {
                "subquestion_text": "Sebutkan fasilitas pada toilet",
                "question_type": "multi_selection",
                "options": [
                    "Ketersediaan toilet pria dan wanita", 
                    "Westafel", 
                    "Toiletries (tissue, sabun, tempat sampah)", 
                    "Air Bersih", 
                    "Monev intensitas petugas membersihkan toilet", 
                    "Lainnya"
                ]
            }, 
        ]
    },
    {
        "name": "Tersedia sarana prasarana bagi pengguna layanan kelompok rentan.",
        "point_weight": 20,
        "aspect": "Sarana dan Prasarana",
        "subquestions": [
            {
                "subquestion_text": "Sebutkan sarana prasarana bagi pengguna layanan kelompok rentan di unit Saudara!",
                "question_type": "multi_selection",
                "options": [
                "Kursi roda/tongkat/kruk", 
                "Pintu masuk yang mudah diakses", 
                "Step lobby/ramp/jalan landai dengan pegangan rambat", 
                "Lift khusus disertai huruf braille (apabila lokasi layanan berada di lantai 2. Apabila di lantai 1, tetap dipilih", 
                "Selasar yang menghubungkan semua ruangan", 
                "Toilet khusus"
                "Loket khusus", 
                "Ruang tunggu khusus", 
                "Guiding block", 
                "Parkir khusus yang mudah diakses", 
                "Alat bantu tuna netra/tuna rungu (huruf braille)", 
                "Arena bermain anak",
                "Ruang Laktasi", 
                "Fasilitas lain sebagai pendukung layanan bagi kelompok rentan (petugas pemandu, petugas yang mampu berbahasa isyarat)"
                ]
            }, 
        ]
    },
    {
        "name": "Tersedia sarana prasarana penunjang .",
        "point_weight": 11,
        "aspect": "Sarana dan Prasarana",
        "subquestions": [
            {
                "subquestion_text": "Apakah tersedia sarana prasarana penunjang berikut di unit pelayanan Saudara?",
                "question_type": "multi_selection",
                "options": [
                    "Fotocopy/ATK", 
                    "P3K", 
                    "APAR", 
                    "Kantin", 
                    "Ruang Ibadah", 
                    "Area merokok di luar ruang pelayanan",
                    "Jalur evakuasi/titik kumpul", 
                    "Ruang Laktasi", 
                    "Tempat Sampah", 
                    "CCTV", 
                    "Lainnya", 
                ]
            }, 
        ]
    },
    {
        "name": "Tersedia Fasilitas pada Sarana Front Office (FO) bagian Informasi di unit layanan.",
        "point_weight": 11,
        "aspect": "Sarana dan Prasarana",
        "subquestions": [
            {
                "subquestion_text": "Fasilitas pada Sarana Front Office (FO) bagian Informasi di unit layanan.",
                "question_type": "multi_selection",
                "options": [
                "Petugas Khusus", 
                "Meja / Kursi", 
                "Layar/display informasi", 
                "Bahan cetak informasi layanan", 
                "Register tamu (manual / elektronik)", 
                "Lainnya"
                ]
            }, 
        ]
    },
    # Sistem Informasi Pelayanan Publik
    {
        "name": "Sistem Informasi Pelayanan Publik",
        "point_weight": 30,
        "aspect": "Sistem Informasi Pelayanan Publik (SIPP)",
        "subquestions": [
            {
                "subquestion_text": "Apakah tersedia sistem informasi pelayanan publik (SIPP)?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Jika Ya, SIPP yang tersedia berupa",
                "question_type": "multi_selection",
                "options": [
                "SIPP secara elektronik", 
                "SIPP secara non elektronik"
                ]
            }, 
            {
                "subquestion_text": "SIPP non elektronik tersedia berupa:",
                "question_type": "multi_selection",
                "options": [
                    "Lisan (pusat informasi)", 
                    "Papan pengumuman", 
                    "Media cetak"
                ]
            }, 
            {
                "subquestion_text": "SIPP elektronik tersedia berupa",
                "question_type": "multi_selection",
                "options": [
                    "Intranet / Belum Online", 
                    "Online / Website"]
            }, 
            {
                "subquestion_text": "Apakah telah menggunakan sistem Informasi Pelayanan Publik Nasional??",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Jika Ya, isikan akun pengguna pada SIPPN:",
                "question_type": "text",
            }, 
            {
                "subquestion_text": "Berapa jumlah layanan yang sudah diinputkan pada Sistem Informasi Pelayanan Publik Nasional?",
                "question_type": "text",
            }, 
        ]
    },
    {
        "name": "Sistem informasi pelayanan publik pendukung operasional pelayanan.",
        "point_weight": 20,
        "aspect": "Sistem Informasi Pelayanan Publik (SIPP)",
        "subquestions": [
            {
                "subquestion_text": "Unsur pendukung sistem informasi pelayanan publik",
                "question_type": "multi_selection",
                "options": [
                    "Layanan Pengelolaan Pengaduan SP4N-LAPOR", 
                    "Pengelolaan keuangan pelayanan publik bagi layanan berbayar", 
                    "Lainnya"]
            }, 
        ]
    },
    {
        "name": "Kualitas penggunaan SIPP Elektronik.",
        "point_weight": 20,
        "aspect": "Sistem Informasi Pelayanan Publik (SIPP)",
        "subquestions": [
            {
                "subquestion_text": "Apakah telah memiliki SIPP Elektronik?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Apakah SIPP Elektronik berbasis website/aplikasi mudah dioperasikan?",
                "question_type": "yes_or_no",
            }, 

            {
                "subquestion_text": "Apakah SIPP Elektronik berbasis website/aplikasi mudah diakses?",
                "question_type": "yes_or_no",
            }, 

            {
                "subquestion_text": "Apakah SIPP Elektronik berbasis website/aplikasi memiliki fungsi yang kompatibel?",
                "question_type": "yes_or_no",
            }, 

            {
                "subquestion_text": "Apakah SIPP Elektronik berbasis website/aplikasi menggunakan kanal resmi pemerintah (domain.go.id)?",
                "question_type": "yes_or_no",
            }, 

            {
                "subquestion_text": "Apakah SIPP Elektronik berbasis website/aplikasi memiliki navigasi yang memudahkan pengguna layanan?",
                "question_type": "yes_or_no",
            }, 
        ]
    },
    {
        "name": "Pemutakhiran data dan informasi kanal digital.",
        "point_weight": 30,
        "aspect": "Sistem Informasi Pelayanan Publik (SIPP)",
        "subquestions": [
            {
                "subquestion_text": "Apakah terdapat pemutakhiran informasi pelayanan publik?",
                "question_type": "yes_or_no",
            },
            {
                "subquestion_text": "Berapa lama jangka waktu pemutakhiran informasi pelayanan publik?",
                "question_type": "one_selection",
                "options": [
                    "Tahunan", 
                    "Per Enam Bulan", 
                    "Bulanan", 
                    "Minggunan", 
                    "Setiap hari"]
            }, 
        ]
    },
    # Konsultasi dan Pengaduan
    {
        "name": "Fasilitas sarana & prasarana konsultasi dan pengaduan:",
        "point_weight": 20,
        "aspect": "Konsultasi dan Pengaduan",
        "subquestions": [
            {
                "subquestion_text": "Fasilitas sarana & prasarana konsultasi dan pengaduan:",
                "question_type": "multi_selection",
                "options": [
                    "Kotak saran/pengaduan", 
                    "Petugas khusus", 
                    "Air minum/makanan ringan", 
                    "Register konsultasi dan pengaduan", 
                    "Publikasi informasi terkait mekanisme konsultasi dan pengaduan (poster/spanduk/leaflet/buku/dokumen/bahan cetak lain)" 
                ]
            }, 
        ]
    },
    {
        "name": "Sarana konsultasi dan pengaduan.",
        "point_weight": 25,
        "aspect": "Konsultasi dan Pengaduan",
        "subquestions": [
            {
                "subquestion_text": "Tersedia sarana konsultasi dan pengaduan yang terdapat pada Unit Lokus:",
                "question_type": "yes_or_no",
            },
            {
                "subquestion_text": "Sarana konsultasi dan pengaduan yang dimiliki",
                "question_type": "multi_selection",
                "options": [
                    "(Tatap muka) Menyatu dengan front office", 
                    "(Tatap muka) Terpisah dengan front office", 
                    "Email", 
                    "Media sosial (Instagram, Facebook, dan Twitter)", 
                    "Website pengaduan mandiri", 
                    "Aplikasi mobile pengaduan mandiri",
                    "SP4N LAPOR!"
                ]
            }, 
        ]
    },
    {
        "name": "Tersedia akuntabilitas hasil konsultasi dan/atau pengaduan.",
        "point_weight": 25,
        "aspect": "Konsultasi dan Pengaduan",
        "subquestions": [
            {
                "subquestion_text": "Apakah terdapat dokumentasi hasil konsultasi dan pengaduan?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Apakah hasil konsultasi dan pengaduan diarsipkan?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Apakah hasil konsultasi dan pengaduan dituangkan dalam laporan?",
                "question_type": "yes_or_no",
            },
            {
                "subquestion_text": "Apakah hasil konsultasi dan pengaduan dilakukan monev?",
                "question_type": "yes_or_no",
            },
            {
                "subquestion_text": "Apakah hasil konsultasi dan pengaduan ditindaklanjuti?",
                "question_type": "yes_or_no",
            },
            {
                "subquestion_text": "Apakah hasil konsultasi dan pengaduan dipublikasikan?",
                "question_type": "yes_or_no",
            },
        ]
    },
    {
        "name": "Berapa persen(%) pengaduan yang masuk ditindaklanjuti hingga selesai dalam satu tahun yang lalu (Januari-Desember)?.",
        "point_weight": 30,
        "aspect": "Konsultasi dan Pengaduan",
        "subquestions": [
            {
                "subquestion_text": "Jumlah konsultasi dan pengaduan yang masuk seluruhnya",
                "question_type": "text",
            }, 
            {
                "subquestion_text": "Jumlah konsultasi dan pengaduan yang ditindaklanjuti seluruhnya hingga selesai",
                "question_type": "text",
            },
            {
                "subquestion_text": "Jumlah konsultasi dan pengaduan yang masuk ke dalam SP4N-LAPOR!",
                "question_type": "text",
            }, 
            {
                "subquestion_text": "Jumlah konsultasi dan pengaduan yang ditindaklanjuti hingga selesai dalam SP4N-LAPOR!",
                "question_type": "text",
            }, 
        ]
    },
    # Inovasi
    {
        "name": "Inovasi Pelayanan Publik.",
        "point_weight": 50,
        "aspect": "Inovasi",
        "subquestions": [
            {
                "subquestion_text": "Apakah terdapat inovasi pelayanan publik?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "sebutkan judul inovasi tersebut beserta penjelasan singkatnya",
                "question_type": "text",
            }, 
            {
                "subquestion_text": "apakah ada inisiatif untuk berinovasi?",
                "question_type": "one_selection",
                "options": ["Tidak", "Ya, masih proses pembelajaran Sebutkan bukti dukung proses pembelajaran (hasil studi tiru, referensi, seminar transfer knowledge, dll)"]
            }, 
            {
                "subquestion_text": "Jika jawaban poin 1 “ya”, sudah berapa lama inovasi dilaksanakan?",
                "question_type": "one_selection",
                "options": ["< 1 tahun", ">= 1 tahun"]
            }, 
            {
                "subquestion_text": "Sebutkan waktu pertama kali inovasi dilaksanakan",
                "question_type": "text",
            }, 
            {
                "subquestion_text": "Apakah inovasi sudah diikutsertakan dalam kompetisi inovasi pelayanan publik?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Apabila sudah diikutkan dalam kompetisi inovasi pelayanan publik, sebutkan penghargaan yang diperoleh :",
                "question_type": "multi_selection",
                "options": ["Instansi (lokal)", "Nasional", "Internasional"]
            }, 
        ]
    },
    {
        "name": "Tersedia sumber daya yang mendukung keberlanjutan Inovasi Pelayanan Publik.",
        "point_weight": 50,
        "aspect": "Inovasi",
        "subquestions": [
            {
                "subquestion_text": "Apakah terdapat sumber daya yang mendukung keberlanjutan inovasi?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Apakah bentuk sumber daya yang mendukung keberlanjutan inovasi?",
                "question_type": "yes_or_no",
            }, 
            {
                "subquestion_text": "Bentuk sumber daya lainnya yang mendukung keberlanjutan inovasi:",
                "question_type": "multi_selection",
                "options": [
                    "Alokasi anggaran terkait keberlanjutan inovasi", 
                    "Sarana dan prasarana pendukung keberlanjutan inovasi", 
                    "SDM yang mendukung keberlanjutan inovasi",
                ]
            }, 
        ]
    },
    # Pertanyaan Tambahan
    # {
    #     "name": "Sistem Antrian.",
    #     "point_weight": 100,
    #     "aspect": "Pertanyaan Tambahan",
    #     "subquestions": [
    #         {
    #             "subquestion_text": "Apakah terdapat sistem antrian di unit pelayanan?",
    #             "question_type": "yes_or_no",
    #         },
    #         {
    #             "subquestion_text": "Fasilitas pada sistem antrian :",
    #             "question_type": "multi_selection",
    #             "options": [
    #               "Sistem pendaftaran online", 
    #               "Nomor Antrian", 
    #               "Media Sosial", 
    #               "Monitor Antrian", 
    #               "Lainnya",
    #             ]
    #         }, 
    #     ]
    # },
]

for question_data in questions_data:
    aspect, created = Aspect.objects.get_or_create(name=question_data["aspect"])
    question = Question.objects.create(
        name=question_data["name"], 
        point_weight=question_data["point_weight"], 
        aspect=aspect
    )
    
    for subquestion_data in question_data["subquestions"]:
        subquestion = SubQuestion.objects.create(
            question=question, 
            question_text=subquestion_data["subquestion_text"],
            question_type=subquestion_data["question_type"], 
        )
        if subquestion_data["question_type"] in ["one_selection", "multi_selection"]:
          for option_text in subquestion_data["options"]:
            QuestionOption.objects.get_or_create(
                subquestion=subquestion, 
                option_text=option_text
            )

evaluator_responses_data = [
    # Kebijakan Pelayanan
    {
        "name": "Tersedia Standar Pelayanan (SP) sesuai dengan ketentuan peraturan perundang-undangan yang berlaku.",
        "options": [
            {"option_text": "Tidak tersedia Standar Pelayanan", "option_score": 0},
            {"option_text": "Tersedia SP namun tidak memenuhi 14 komponen.", "option_score": 1},
            {"option_text": "Tersedia SP yang memenuhi 14 komponen", "option_score": 2},
            {"option_text": "Tersedia SP yang memenuhi 14 komponen dan dilakukan penetapan.", "option_score": 3},
            {"option_text": "Tersedia SP yang memenuhi 14 komponen, melibatkan masyarakat dalam penyusunan SP, dan dilakukan penetapan.", "option_score": 4},
            {"option_text": "Tersedia SP yang memenuhi 14 komponen, melibatkan masyarakat dalam penyusunan SP, dilakukan penetapan, dan dilakukan monev.", "option_score": 5},
        ]
    },
    {
        "name": "Proses penyusunan dan perubahan SP telah melibatkan unsur masyarakat.",
        "options": [
            {"option_text": "Penyusunan SP tanpa melibatkan unsur masyarakat dan pihak terkait (stakeholder).", "option_score": 0},
            {"option_text": "Penyusunan SP telah melibatkan minimal 1 unsur masyarakat", "option_score": 1},
            {"option_text": "Penyusunan SP telah melibatkan minimal 2 unsur masyarakat.", "option_score": 2},
            {"option_text": "Penyusunan SP telah melibatkan minimal 3 unsur masyarakat.", "option_score": 3},
            {"option_text": "Penyusunan SP telah melibatkan minimal 4 unsur masyarakat.", "option_score": 4},
            {"option_text": "Penyusunan SP telah melibatkan lebih dari 4 unsur masyarakat.", "option_score": 5},
        ]
    },
    {
        "name": "Jumlah media publikasi untuk komponen service delivery.",
        "options": [
            {"option_text": "Tidak ada publikasi SP.", "option_score": 0},
            {"option_text": "Tersedia publikasi SP hanya sebagian dari komponen service delivery baik pada media cetak/non elektronik maupun media elektronik..", "option_score": 1},
            {"option_text": "Tersedia publikasi SP seluruh komponen service delivery pada 2 atau lebih media publikasi namun belum dipublikasikan pada SIPP Nasional", "option_score": 2},
            {"option_text": "Tersedia publikasi SP seluruh komponen service delivery pada 2 media publikasi dan pada SIPP Nasional.", "option_score": 3},
            {"option_text": "Tersedia publikasi SP seluruh komponen service delivery pada 3 media publikasi dan pada SIPP Nasional.", "option_score": 4},
            {"option_text": "Tersedia publikasi SP seluruh komponen service delivery pada 4 atau lebih media publikasi dan pada SIPP Nasional.", "option_score": 5},
        ]
    },
    {
        "name": "Telah dilakukan peninjauan ulang secara berkala terhadap Standar Pelayanan.",
        "options": [
            {"option_text": "Tidak dilaksanakan peninjauan ulang secara berkala terhadap Standar Pelayanan.", "option_score": 0},
            {"option_text": "Dilakukan peninjauan ulang 3 tahun atau lebih terhadap seluruh jenis layanan.", "option_score": 1},
            {"option_text": "Dilakukan peninjauan ulang 2 tahun sekali terhadap sebagian jenis layanan.", "option_score": 2},
            {"option_text": "Dilakukan peninjauan ulang 2 tahun sekali terhadap seluruh jenis layanan", "option_score": 3},
            {"option_text": "Dilakukan peninjauan ulang 1 tahun sekali atau lebih cepat terhadap sebagian jenis layanan.", "option_score": 4},
            {"option_text": "Dilakukan peninjauan ulang 1 tahun sekali atau lebih cepat terhadap seluruh jenis layanan.", "option_score": 5},
        ]
    },
    {
        "name": "Pemenuhan siklus Maklumat Pelayanan (ketersediaan, penetapan, dan publikasi).",
        "options": [
            {"option_text": "Tidak tersedia Maklumat Pelayanan", "option_score": 0},
            {"option_text": "Tersedia Maklumat Pelayanan namun belum ditetapkan.", "option_score": 1},
            {"option_text": "Tersedia Maklumat Pelayanan yang sudah ditetapkan namun isinya belum sesuai dengan peraturan perundangan yang berlaku.", "option_score": 2},
            {"option_text": "Tersedia Maklumat Pelayanan yang sudah ditetapkan dan isinya telah sesuai dengan peraturan perundangan yang berlaku", "option_score": 3},
            {"option_text": "Tersedia Maklumat Pelayanan yang sudah ditetapkan, isinya telah sesuai dengan peraturan perundangan yang berlaku, dan dipublikasikan pada media non elektronik.", "option_score": 4},
            {"option_text": "Tersedia Maklumat Pelayanan yang sudah ditetapkan, isinya telah sesuai dengan peraturan perundangan yang berlaku, dan dipublikasikan pada media non elektronik dan elektronik.", "option_score": 5},
        ]
    },
    {
        "name": "SKM yang dilaksanakan sesuai dengan PermenPANRB.",
        "options": [
            {"option_text": "Belum melaksanakan SKM.", "option_score": 0},
            {"option_text": "Sudah melaksanakan SKM namun tidak sesuai dengan Peraturan Menteri PANRB yang berlaku", "option_score": 1},
            {"option_text": "Sudah melaksanakan SKM sesuai dengan Peraturan Menteri PANRB yang berlaku.", "option_score": 2},
            {"option_text": "Sudah melaksanakan SKM sesuai dengan PermenPANRB yang berlaku dan dipublikasikan pada media non-elektronik", "option_score": 3},
            {"option_text": "Sudah melaksanakan SKM sesuai dengan PermenPANRB yang berlaku dan dipublikasikan pada media non-elektronik dan elektronik.", "option_score": 4},
            {"option_text": "Sudah melaksanakan SKM sesuai dengan PermenPANRB yang berlaku dan dipublikasikan pada media non-elektronik dan elektronik serta dilakukan tindak lanjut hasil SKM.", "option_score": 5},
        ]
    },
    {
        "name": "Jumlah media publikasi hasil SKM.",
        "options": [
            {"option_text": "Tidak dipublikasikan.", "option_score": 0},
            {"option_text": "SKM dipublikasikan pada 1 (satu) media publikasi", "option_score": 1},
            {"option_text": "SKM dipublikasikan pada 2 (dua) media publikasi.", "option_score": 2},
            {"option_text": "SKM dipublikasikan pada 3 (tiga) media publikasi.", "option_score": 3},
            {"option_text": "SKM dipublikasikan pada 4 (empat) media publikasi.", "option_score": 4},
            {"option_text": "SKM dipublikasikan pada lebih dari 4 (empat) media publikasi lainnya.", "option_score": 5},
        ]
    },
    {
        "name": "Tindak lanjut hasil SKM dan kedalaman ruang lingkup untuk setiap jenis pelayanan.",
        "options": [
            {"option_text": "Tidak ada rencana tindak lanjut SKM.", "option_score": 0},
            {"option_text": "Ada rencana tindak lanjut tapi belum dilaksanakan.", "option_score": 1},
            {"option_text": "Tindak lanjut hasil SKM dilaksanakan kurang dari 30%, dibuktikan dengan laporan pelaksanaannya.", "option_score": 2},
            {"option_text": "Tindak lanjut hasil SKM dilaksanakan 30-80%, dibuktikan dengan laporan pelaksanaannya.", "option_score": 3},
            {"option_text": "Tindak lanjut hasil SKM dilaksanakan lebih dari 80%, dibuktikan dengan laporan pelaksanaannya.", "option_score": 4},
            {"option_text": "Tindak lanjut hasil SKM dilaksanakan 100%, dibuktikan dengan laporan pelaksanaannya.", "option_score": 5},
        ]
    },
    {
        "name": "Kecepatan tindak lanjut hasil SKM seluruh jenis pelayanan.",
        "options": [
            {"option_text": "Rekomendasi hasil SKM tidak ditindaklanjuti.", "option_score": 0},
            {"option_text": "Rekomendasi hasil SKM ditindaklanjuti seluruhnya 1 tahun setelah laporan SKM diterbitkan.", "option_score": 1},
            {"option_text": "Rekomendasi hasil SKM ditindaklanjuti seluruhnya 9 bulan setelah laporan SKM diterbitkan.", "option_score": 2},
            {"option_text": "Rekomendasi hasil SKM ditindaklanjuti seluruhnya 6 bulan setelah laporan SKM diterbitkan.", "option_score": 3},
            {"option_text": "Rekomendasi hasil SKM ditindaklanjuti seluruhnya 6 bulan setelah laporan SKM diterbitkan.", "option_score": 4},
            {"option_text": "Rekomendasi hasil SKM ditindaklanjuti seluruhnya 6 bulan setelah laporan SKM diterbitkan.", "option_score": 5},
        ]
    },
    # Profesionalisme SDM
    {
        "name": "Tersedia waktu pelayanan yang memudahkan pengguna layanan.",
        "options": [
            {"option_text": "Tersedia waktu pelayanan yang memudahkan pengguna layanan.", "option_score": 0},
            {"option_text": "Memiliki kebijakan jam pelayanan/kerja.", "option_score": 1},
            {"option_text": "Memiliki kebijakan jam pelayanan/kerja dan 1 unsur lainnya.", "option_score": 2},
            {"option_text": "Memiliki kebijakan jam pelayanan/kerja dan 2 unsur lainnya.", "option_score": 3},
            {"option_text": "Memiliki kebijakan jam pelayanan/kerja dan 3 unsur lainnya.", "option_score": 4},
            {"option_text": "Memiliki kebijakan jam pelayanan/kerja dan 4 atau lebih unsur lainnya.", "option_score": 5},
        ]
    },
    {
        "name": "Tersedia Kode Etik dan Kode Perilaku Pelaksana dan/atau Budaya Pelayanan di lingkungan instansi.",
        "options": [
            {"option_text": "Tidak tersedia aturan kode etik dan kode perilaku.", "option_score": 0},
            {"option_text": "Aturan kode etik dan kode perilaku Pelaksana Pelayanan hanya meliputi nilai dasar hak dan kewajiban.", "option_score": 1},
            {"option_text": "Aturan kode etik dan kode perilaku Pelaksana Pelayanan meliputi nilai dasar hak kewajiban dan 1 (satu) unsur lainnya.", "option_score": 2},
            {"option_text": "Aturan kode etik dan kode perilaku Pelaksana Pelayanan meliputi nilai dasar hak dan kewajiban dan 2 (dua) unsur lainnya.", "option_score": 3},
            {"option_text": "Aturan kode etik dan kode perilaku Pelaksana Pelayanan meliputi nilai dasar hak dan kewajiban dan 3 (tiga) unsur lainnya.", "option_score": 4},
            {"option_text": "Aturan kode etik dan kode perilaku Pelaksana Pelayanan meliputi nilai dasar hak dan kewajiban dan 4 (empat) unsur lainnya.", "option_score": 5},
        ]
    },
    {
        "name": "Tersedia mekanisme yang dibangun unit kerja untuk menjaga dan meningkatkan motivasi kerja Pelaksana pelayanan.",
        "options": [
            {"option_text": "Tidak tersedia mekanisme peningkatan motivasi kerja.", "option_score": 0},
            {"option_text": "Tersedia 1 jenis mekanisme peningkatan motivasi kerja", "option_score": 1},
            {"option_text": "Tersedia 2 jenis mekanisme peningkatan motivasi kerja", "option_score": 2},
            {"option_text": "Tersedia 3 jenis mekanisme peningkatan motivasi kerja", "option_score": 3},
            {"option_text": "Tersedia 4 jenis mekanisme peningkatan motivasi kerja", "option_score": 4},
            {"option_text": "Tersedia lebih dari 4 jenis mekanisme peningkatan motivasi kerja", "option_score": 5},
        ]
    },
    {
        "name": "Tersedia kriteria pemberian penghargaan bagi pelaksana layanan yang berprestasi.",
        "options": [
            {"option_text": "Tidak ada pemberian penghargaan.", "option_score": 0},
            {"option_text": "Ada pemberian penghargaan hanya berdasarkan 1-2 unsur kecuali kinerja.", "option_score": 1},
            {"option_text": "Ada pemberian penghargaan berdasarkan 3-5 unsur kecuali kinerja.", "option_score": 2},
            {"option_text": "Ada pemberian penghargaan berdasarkan 1-2 unsur kinerja.", "option_score": 3},
            {"option_text": "Ada penghargaan 3-4 unsur kinerja.", "option_score": 4},
            {"option_text": "Ada pemberian penghargaan berdasarkan 5-6 unsur termasuk kinerja.", "option_score": 5},
        ]
    },
    {
        "name": "Budaya Pelayanan.",
        "options": [
            {"option_text": "Tidak menerapkan budaya layanan.", "option_score": 0},
            {"option_text": "Pelaksana pelayanan menerapkan 1 (satu) unsur budaya pelayanan.", "option_score": 1},
            {"option_text": "Pelaksana pelayanan menerapkan 2 (dua) unsur budaya pelayanan.", "option_score": 2},
            {"option_text": "Pelaksana pelayanan menerapkan 3 (tiga) unsur budaya pelayanan.", "option_score": 3},
            {"option_text": "Pelaksana pelayanan menerapkan 4 (empat) unsur budaya pelayanan.", "option_score": 4},
            {"option_text": "Pelaksana pelayanan menerapkan 5 (lima) unsur budaya pelayanan.", "option_score": 5},
        ]
    },
    # Sarana dan Prasarana
    {
      "name": "Tersedia tempat parkir dengan fasilitas pendukung.",
      "options": [
            {"option_text": "Tidak tersedia tempat parkir", "option_score": 0},
            {"option_text": "Tersedia tempat parkir dan memiliki 1 fasilitas parkir.", "option_score": 1},
            {"option_text": "Tersedia tempat parkir dan memiliki 2 fasilitas parkir.", "option_score": 2},
            {"option_text": "Tersedia tempat parkir dan memiliki 3 fasilitas parkir.", "option_score": 3},
            {"option_text": "Tersedia tempat parkir dan memiliki 4 fasilitas parkir.", "option_score": 4},
            {"option_text": "Tersedia tempat parkir dan memiliki 5 atau lebih fasilitas parkir.", "option_score": 5},
        ]
    },
    {
      "name": "Kelayakan fasilitas ruang tunggu pelayanan",
      "options": [
            {"option_text": "Tidak tersedia fasilitas apapun.", "option_score": 0},
            {"option_text": "Tersedia fasilitas wajib.", "option_score": 1},
            {"option_text": "Tersedia fasilitas wajib dan 1 fasilitas pelengkap.", "option_score": 2},
            {"option_text": "Tersedia fasilitas wajib dan 2 fasilitas pelengkap.", "option_score": 3},
            {"option_text": "Tersedia fasilitas wajib dan 3 fasilitas pelengkap.", "option_score": 4},
            {"option_text": "Tersedia fasilitas wajib dan 4 atau lebih fasilitas pelengkap.", "option_score": 5},
        ]
    },
    {
      "name": "Tersedia sarana toilet pengguna layanan yang layak pakai.",
      "options": [
            {"option_text": "Tidak tersedia toilet pengguna layanan.", "option_score": 0},
            {"option_text": "Toilet pengguna layanan dengan 1 kondisi.", "option_score": 1},
            {"option_text": "Toilet pengguna layanan dengan 2 kondisi.", "option_score": 2},
            {"option_text": "Toilet pengguna layanan dengan 3 kondisi.", "option_score": 3},
            {"option_text": "Toilet pengguna layanan dengan 4 kondisi.", "option_score": 4},
            {"option_text": "Toilet pengguna layanan dengan lebih dari 4 kondisi.", "option_score": 5},
        ]
    },
    {
      "name": "Tersedia sarana prasarana bagi pengguna layanan kelompok rentan.",
      "options": [
            {"option_text": "Tidak tersedia sarana prasarana bagi pengguna layanan kelompok rentan.", "option_score": 0},
            {"option_text": "Tersedia 1-3 sarana prasarana bagi pengguna layanan kelompok rentan.", "option_score": 1},
            {"option_text": "Tersedia 4-6 sarana prasarana bagi pengguna layanan kelompok rentan.", "option_score": 2},
            {"option_text": "Tersedia 7-9 sarana prasarana bagi pengguna layanan kelompok rentan.", "option_score": 3},
            {"option_text": "Tersedia 10-12 sarana prasarana bagi pengguna layanan kelompok rentan.", "option_score": 4},
            {"option_text": "Tersedia 13 atau lebih sarana prasarana bagi pengguna layanan kelompok rentan.", "option_score": 5},
        ]
    },
    {
      "name": "Tersedia sarana prasarana penunjang .",
      "options": [
            {"option_text": "Tidak tersedia fasilitas penunjang.", "option_score": 0},
            {"option_text": "Tersedia 1 fasilitas penunjang.", "option_score": 1},
            {"option_text": "Tersedia 2 fasilitas penunjang.", "option_score": 2},
            {"option_text": "Tersedia 3 fasilitas penunjang.", "option_score": 3},
            {"option_text": "Tersedia 4 fasilitas penunjang.", "option_score": 4},
            {"option_text": "Tersedia 5 atau lebih fasilitas penunjang.", "option_score": 5},
        ]
    },
    {
      "name": "Tersedia Fasilitas pada Sarana Front Office (FO) bagian Informasi di unit layanan.",
      "options": [
            {"option_text": "Tidak tersedia sarana FO informasi layanan.", "option_score": 0},
            {"option_text": "Tersedia sarana FO informasi layanan dengan 1 fasilitas.", "option_score": 1},
            {"option_text": "Tersedia sarana FO informasi layanan dengan 2 fasilitas.", "option_score": 2},
            {"option_text": "Tersedia sarana FO informasi layanan dengan 3 fasilitas.", "option_score": 3},
            {"option_text": "Tersedia sarana FO informasi layanan dengan 4 fasilitas.", "option_score": 4},
            {"option_text": "Tersedia sarana FO informasi layanan dengan 5 atau lebih fasilitas.", "option_score": 5},
        ]
    },
    # Sistem Informasi Pelayanan Publik
    {
        "name": "Sistem Informasi Pelayanan Publik",
        "options": [
            {"option_text": "Tidak tersedia sistem informasi pelayanan publik baik elektronik maupun non elektronik.", "option_score": 0},
            {"option_text": "Tersedia sistem informasi pelayanan publik non elektronik melalui media lisan (pusat informasi).", "option_score": 1},
            {"option_text": "ersedia sistem informasi pelayanan publik non elektronik melalui media lisan (pusat informasi) serta media papan pengumuman dan media cetak.", "option_score": 2},
            {"option_text": "Tersedia Sistem informasi pelayanan publik elektronik namun belum online (e-kiosk/ display TV/ layar monitor).", "option_score": 3},
            {"option_text": "ersedia Sistem informasi pelayanan publik berbasis online/website.", "option_score": 4},
            {"option_text": "Sistem informasi pelayanan publik telah online/website dan terhubung dengan sistem informasi pelayanan publik nasional serta telah menginput layanan yang ditetapkan ke dalam sistem informasi pelayanan publik nasional.", "option_score": 5},
        ]
    },
    {
        "name": "Sistem informasi pelayanan publik pendukung operasional pelayanan.",
        "options": [
            {"option_text": "Tidak tersedia sistem informasi pendukung operasional pelayanan publik.", "option_score": 0},
            {"option_text": "Tersedia sistem informasi pendukung operasional pelayanan dengan 1 kondisi.", "option_score": 1},
            {"option_text": "Tersedia sistem informasi pendukung operasional pelayanan dengan 2 kondisi.", "option_score": 2},
            {"option_text": "Tersedia sistem informasi pendukung operasional pelayanan dengan 3 kondisi.", "option_score": 3},
            {"option_text": "Tersedia sistem informasi pendukung operasional pelayanan dengan 4 kondisi.", "option_score": 4},
            {"option_text": "Tersedia sistem informasi pendukung operasional pelayanan dengan lebih dari 4 kondisi.", "option_score": 5},
        ]
    },
    {
        "name": "Kualitas penggunaan SIPP Elektronik.",
        "options": [
            {"option_text": "SIPP Elektronik tidak terhubung secara daring.", "option_score": 0},
            {"option_text": "SIPP Elektronik berbasis website/aplikasi mudah dioperasikan.", "option_score": 1},
            {"option_text": "SIPP Elektronik berbasis website/aplikasi mudah dioperasikan, mudah diakses.", "option_score": 2},
            {"option_text": "SIPP Elektronik berbasis website/aplikasi mudah dioperasikan, mudah diakses, kompatibel.", "option_score": 3},
            {"option_text": "SIPP Elektronik berbasis website/aplikasi yang mudah mudah kompatibel, kanal digital resmi pemerintah (domain.go.id).", "option_score": 4},
            {"option_text": "IPP Elektronik berbasis website/aplikasi yang dioperasikan, diakses, merupakan mudah dioperasikan, mudah diakses, kompatibel, merupakan kanal digital resmi pemerintah (domain.go.id) dan navigasi yang mudah dipahami.", "option_score": 5},
        ]
    },
    {
        "name": "Pemutakhiran data dan informasi kanal digital.",
        "options": [
            {"option_text": "Tersedia data dan informasi pelayanan publik yang tidak dimutakhirkan.", "option_score": 0},
            {"option_text": "Pemutakhiran data dan informasi pelayanan publik telah dilakukan secara tahunan.", "option_score": 1},
            {"option_text": "Pemutakhiran data dan informasi pelayanan publik telah dilakukan secara semesteran.", "option_score": 2},
            {"option_text": "Pemutakhiran data dan informasi pelayanan publik secara bulanan.", "option_score": 3},
            {"option_text": "Pemutakhiran data dan informasi pelayanan publik dilakukan secara mingguan.", "option_score": 4},
            {"option_text": "Pemutakhiran data dan informasi pelayanan publik dilakukan secara mingguan.", "option_score": 5},
        ]
    },
    # Konsultasi dan Pengaduan
    {
        "name": "Fasilitas sarana & prasarana konsultasi dan pengaduan:",
        "options": [
            {"option_text": "Tidak tersedia Sarana konsultasi pengaduan pengguna layanan.", "option_score": 0},
            {"option_text": "Sarana konsultasi pengaduan pengguna layanan dengan 1 fasilitas.", "option_score": 1},
            {"option_text": "Sarana konsultasi pengaduan pengguna layanan dengan 2 fasilitas.", "option_score": 2},
            {"option_text": "Sarana konsultasi pengaduan pengguna layanan dengan 3 fasilitas.", "option_score": 3},
            {"option_text": "Sarana konsultasi pengaduan pengguna layanan dengan 4 fasilitas.", "option_score": 4},
            {"option_text": "Sarana konsultasi pengaduan pengguna layanan dengan 5 atau lebih fasilitas.", "option_score": 5},
        ]
    },
    {
        "name": "Sarana konsultasi dan pengaduan.",
        "options": [
            {"option_text": "Tidak ada sarana dan petugas.", "option_score": 0},
            {"option_text": "Hanya terdapat media konsultasi dan pengaduan secara offline menyatu dengan front office.", "option_score": 1},
            {"option_text": "Hanya terdapat media konsultasi dan pengaduan secara offline namun terpisah dengan front office.", "option_score": 2},
            {"option_text": "Terdapat media konsultasi dan pengaduan secara offline menyatu satu dengan front office dan tersedia secara online.", "option_score": 3},
            {"option_text": "Terdapat media konsultasi dan pengaduan secara offline secara terpisah dari front office, serta tersedia secara online.", "option_score": 4},
            {"option_text": "Terdapat media konsultasi dan pengaduan secara offline terpisah dari front office, dan terhubung dengan SP4N-LAPOR!", "option_score": 5},
        ]
    },
    {
        "name": "Tersedia akuntabilitas hasil konsultasi dan/atau pengaduan.",
        "options": [
            {"option_text": "Tidak ada dokumentasi.", "option_score": 0},
            {"option_text": "Terdapat dokumentasi yang diarsipkan.", "option_score": 1},
            {"option_text": "Terdapat dokumentasi yang diarsipkan dan dituangkan dalam laporan.", "option_score": 2},
            {"option_text": "Terdapat dokumentasi diarsipkan dituangkan dalam laporan, dan,dilakukan monev.", "option_score": 3},
            {"option_text": "Terdapat dokumentasi diarsipkan, dituangkan dalam laporan, dilakukan monev, dan ditindaklanjuti", "option_score": 4},
            {"option_text": "Terdapat dokumentasi diarsipkan, dituangkan dalam laporan, dilakukan monev, ditindaklanjuti, dan dipublikasikan.", "option_score": 5},
        ]
    },
    {
        "name": "Berapa persen(%) pengaduan yang masuk ditindaklanjuti hingga selesai dalam satu tahun yang lalu (Januari-Desember)?.",
        "options": [
            {"option_text": "Tidak ada konsultasi atau pengaduan yang ditindaklanjuti.", "option_score": 0},
            {"option_text": "< 50% konsultasi atau pengaduan ditindaklanjuti hingga selesai yang tidak menggunakan SP4N- LAPOR!.", "option_score": 1},
            {"option_text": "≥ 50% konsultasi atau pengaduan ditindaklanjuti hingga selesai yang tidak menggunakan SP4N- LAPOR!.", "option_score": 2},
            {"option_text": "< 50% konsultasi atau pengaduan yang masuk ke SP4N-LAPOR! dan ditindaklanjuti hingga selesai.", "option_score": 3},
            {"option_text": "≥ 50% - 90% konsultasi atau pengaduan yang masuk ke SP4N-LAPOR! dan ditindaklanjuti hingga selesai.", "option_score": 4},
            {"option_text": " ≥ 90% konsultasi atau pengaduan yang masuk ke SP4N-LAPOR! dan ditindaklanjuti hingga selesai", "option_score": 5},
        ]
    },
    # Inovasi
    {
        "name": "Inovasi Pelayanan Publik.",
        "options": [
            {"option_text": "Tidak tersedia inovasi.", "option_score": 0},
            {"option_text": "Belum ada inovasi, masih dalam proses pembelajaran berinovasi.", "option_score": 1},
            {"option_text": "Sudah ada inovasi namun kurang dari 1 tahun.", "option_score": 2},
            {"option_text": "Sudah ada inovasi lebih dari 1 tahun namun belum diikutsertakan dalam kompetisi (level apapun).", "option_score": 3},
            {"option_text": "Sudah ada inovasi lebih dari 1 tahun dan sudah diikutsertakan dalam kompetisi level apapun.", "option_score": 4},
            {"option_text": "Inovasi yang dilaksanakan sudah mendapatkan prestasi pada level (apapun).", "option_score": 5},
        ]
    },
    {
        "name": "Tersedia sumber daya yang mendukung keberlanjutan Inovasi Pelayanan Publik.",
        "options": [
            {"option_text": "Belum ada sumber daya yang mendukung keberlanjutan inovasi.", "option_score": 0},
            {"option_text": "Sumber daya yang mendukung keberlanjutan inovasi dalam bentuk rancangan payung hukum.", "option_score": 1},
            {"option_text": "Sumber daya yang mendukung keberlanjutan inovasi dalam bentuk payung hukum.", "option_score": 2},
            {"option_text": "Sumber daya yang mendukung keberlanjutan inovasi dalam bentuk payung hukum dan 1 kondisi lainnya", "option_score": 3},
            {"option_text": "Sumber daya yang mendukung keberlanjutan inovasi dalam bentuk payung hukum dan 2 kondisi lainnya", "option_score": 4},
            {"option_text": "Sumber daya yang mendukung keberlanjutan inovasi dalam bentuk payung hukum dan 3 kondisi lainnya", "option_score": 5},
        ]
    },
    # Pertanyaan Tambahan
    # {
    #     "name": "Sistem Antrian.",
    #     "options": [
    #         {"option_text": "Tidak tersedia sistem antrian.", "option_score": 0},
    #         {"option_text": "Tersedia sistem antrian dengan 1 fasilitas.", "option_score": 1},
    #         {"option_text": "Tersedia sistem antrian dengan 2 fasilitas.", "option_score": 2},
    #         {"option_text": "Tersedia sistem antrian dengan 3 fasilitas.", "option_score": 3},
    #         {"option_text": "Tersedia sistem antrian dengan 4 fasilitas.", "option_score": 4},
    #         {"option_text": "Tersedia sistem antrian dengan lebih dari 4 fasilitas.", "option_score": 5},
    #     ]
    # },
]

for response_data in evaluator_responses_data:
    question = Question.objects.get(name=response_data["name"])

    for option_data in response_data["options"]:
        EvaluatorOption.objects.create(
            question=question,
            name=option_data["option_text"],
            score=option_data["option_score"]
        )

for user_data in users_data:
    if user_data['role'] == 'assignee':
        AssignedEvaluation.objects.create(
            date_start=datetime.date(2024, 10, 30),
            date_end=datetime.date(2024, 12, 31),
            date_deadline=datetime.date(2024, 12, 1),
            evaluation=Evaluation.objects.get(name="Evaluasi Formulir Pemerintah Kota"),
            assigned_user=User.objects.get(username=user_data['username'])
            )