-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 08, 2024 at 02:11 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sip2b`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `ID_Admin` int(11) NOT NULL,
  `Nama_Admin` varchar(50) DEFAULT NULL,
  `Email_Admin` varchar(100) DEFAULT NULL,
  `Password_Admin` varchar(50) DEFAULT NULL,
  `Role` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`ID_Admin`, `Nama_Admin`, `Email_Admin`, `Password_Admin`, `Role`) VALUES
(1, 'Luqman_19', 'Luqman295@gmail.com', 'Luqman2005', 'super admin database'),
(1001, 'Luqman', 'Luqman295@gmail.com', 'Luqman925', 'perkotaan_database'),
(1005, 'Faiz', 'Faiz284@gmail.com', 'Faiz284', 'pemukiman_database'),
(1010, 'Ezra', 'Ezra233@gmail.com', 'Ezra233', 'proyek_database');

-- --------------------------------------------------------

--
-- Table structure for table `pemukiman`
--

CREATE TABLE `pemukiman` (
  `ID_Pemukiman` int(11) NOT NULL,
  `Nama_Pemukiman` varchar(255) DEFAULT NULL,
  `ID_Perkotaan` int(11) DEFAULT NULL,
  `Jenis_Pemukiman` varchar(255) DEFAULT NULL,
  `Akses_Air_Bersih` varchar(40) DEFAULT NULL,
  `Akses_Sanitasi_Layak` varchar(40) DEFAULT NULL,
  `ID_Admin` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pemukiman`
--

INSERT INTO `pemukiman` (`ID_Pemukiman`, `Nama_Pemukiman`, `ID_Perkotaan`, `Jenis_Pemukiman`, `Akses_Air_Bersih`, `Akses_Sanitasi_Layak`, `ID_Admin`) VALUES
(1, 'Kampung Baru', 1, 'formal', 'Ya', 'Ya', 1005),
(2, 'Perumahan Griya Asri', 1, 'formal', 'Ya', 'Ya', 1005),
(3, 'Kampung Nelayan', 2, 'informal', 'Tidak', 'Tidak', 1005),
(4, 'Perumnas Palem', 5, 'formal', 'Ya', 'Ya', 1005),
(5, 'Bumi Manuntung', 7, 'formal', 'Ya', 'Ya', 1005),
(6, 'Kebun Jeruk', 2, 'informal', 'Tidak', 'Tidak', 1005),
(7, 'Permata Hijau', 10, 'formal', 'Ya', 'Ya', 1005),
(8, 'Sei Tuan', 11, 'informal', 'Tidak', 'Tidak', 1005),
(9, 'Permai Indah', 13, 'formal', 'Ya', 'Ya', 1005),
(10, 'Kampung Bugis', 14, 'informal', 'Tidak', 'Tidak', 1005),
(11, 'Bukit Damai', 15, 'formal', 'Ya', 'Ya', 1005),
(12, 'Perumnas Sidoarjo', 16, 'formal', 'Ya', 'Ya', 1005),
(13, 'Kampung Sawah', 17, 'formal', 'Tidak', 'Tidak', 1005),
(14, 'Perumahan Asri', 18, 'formal', 'Ya', 'Ya', 1005),
(15, 'Kampung Melayu', 19, 'informal', 'Tidak', 'Tidak', 1005),
(16, 'Perumahan Elit', 20, 'formal', 'Ya', 'Ya', 1005),
(17, 'Kampung Cendrawasih', 21, 'informal', 'Tidak', 'Tidak', 1005),
(18, 'Perumahan Taman Asri', 22, 'formal', 'Ya', 'Ya', 1005),
(19, 'Kampung Ujung', 23, 'informal', 'Tidak', 'Tidak', 1005),
(20, 'Perumahan Cluster', 24, 'formal', 'Ya', 'Ya', 1005),
(21, 'Kampung Baru', 25, 'informal', 'Tidak', 'Tidak', 1005),
(22, 'Perumahan Griya Asri', 26, 'formal', 'Ya', 'Ya', 1005),
(23, 'Kampung Nelayan', 27, 'informal', 'Tidak', 'Tidak', 1005),
(24, 'Perumnas Palem', 28, 'formal', 'Ya', 'Ya', 1005),
(25, 'Bumi Manuntung', 29, 'formal', 'Ya', 'Ya', 1005),
(26, 'Kebun Jeruk', 30, 'informal', 'Tidak', 'Tidak', 1005),
(27, 'Permata Hijau', 31, 'formal', 'Ya', 'Ya', 1005),
(28, 'Sei Tuan', 32, 'informal', 'Tidak', 'Tidak', 1005),
(29, 'Permai Indah', 33, 'formal', 'Ya', 'Ya', 1005),
(30, 'Kampung Bugis', 34, 'informal', 'Tidak', 'Tidak', 1005),
(31, 'Bukit Damai', 35, 'formal', 'Ya', 'Ya', 1005),
(32, 'Perumnas Sidoarjo', 36, 'formal', 'Ya', 'Ya', 1005),
(33, 'Kampung Sawah', 37, 'informal', 'Tidak', 'Tidak', 1005),
(34, 'Perumahan Asri', 38, 'formal', 'Ya', 'Ya', 1005),
(35, 'Kampung Melayu', 39, 'informal', 'Tidak', 'Tidak', 1005),
(36, 'Perumahan Elit', 40, 'formal', 'Ya', 'Ya', 1005),
(37, 'Kampung Baru', 37, 'informal', 'Tidak', 'Tidak', 1005),
(38, 'Perumahan Griya Asri', 38, 'formal', 'Ya', 'Ya', 1005),
(39, 'Kampung Nelayan', 39, 'informal', 'Tidak', 'Tidak', 1005),
(40, 'Perumnas Palem', 40, 'formal', 'Ya', 'Ya', 1005);

-- --------------------------------------------------------

--
-- Table structure for table `perkotaan`
--

CREATE TABLE `perkotaan` (
  `ID_Perkotaan` int(11) NOT NULL,
  `Nama_Kota` varchar(50) DEFAULT NULL,
  `Provinsi` varchar(50) DEFAULT NULL,
  `Jumlah_Penduduk` int(11) DEFAULT NULL,
  `Luas_Wilayah` decimal(10,2) DEFAULT NULL,
  `Indeks_Berkelanjutan_Kota` decimal(10,2) DEFAULT NULL,
  `id_admin` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `perkotaan`
--

INSERT INTO `perkotaan` (`ID_Perkotaan`, `Nama_Kota`, `Provinsi`, `Jumlah_Penduduk`, `Luas_Wilayah`, `Indeks_Berkelanjutan_Kota`, `id_admin`) VALUES
(1, 'Banda Aceh', 'Aceh', 244234, 61.36, 52.40, 1001),
(2, 'Medan', 'Sumatera Utara', 2435275, 250.00, 54.80, 1001),
(3, 'Pekanbaru', 'Riau', 1033777, 632.26, 56.80, 1001),
(4, 'Jambi', 'Jambi', 605479, 203.44, 54.00, 1001),
(5, 'Palembang', 'Sumatera Selatan', 1668479, 400.66, 55.60, 1001),
(6, 'Bengkulu', 'Bengkulu', 345681, 152.30, 52.00, 1001),
(7, 'Padang', 'Sumatera Barat', 90744, 88.30, 53.20, 1001),
(8, 'Bandar Lampung', 'Lampung', 1154973, 234.62, 51.60, 1001),
(9, 'Pangkal Pinang', 'Bangka Belitung', 184444, 62.31, 50.40, 1001),
(10, 'Tanjungpinang', 'Kepulauan Riau', 212435, 144.03, 52.80, 1001),
(11, 'Pontianak', 'Kalimantan Barat', 564921, 107.80, 54.00, 1001),
(12, 'Banjarmasin', 'Kalimantan Selatan', 680376, 70.00, 52.40, 1001),
(13, 'Palangkaraya', 'Kalimantan Tengah', 2665, 619.53, 50.80, 1001),
(14, 'Samarinda', 'Kalimantan Timur', 817357, 720.00, 53.20, 1001),
(15, 'Balikpapan', 'Kalimantan Timur', 688175, 520.66, 51.60, 1001),
(16, 'Makassar', 'Sulawesi Selatan', 1423477, 175.77, 55.20, 1001),
(17, 'Manado', 'Sulawesi Utara', 434275, 156.20, 53.60, 1001),
(18, 'Kendari', 'Sulawesi Tenggara', 343576, 93.90, 52.00, 1001),
(19, 'Gorontalo', 'Gorontalo', 211222, 72.68, 50.40, 1001),
(20, 'Palu', 'Sulawesi Tengah', 365881, 390.00, 48.80, 1001),
(21, 'Ambon', 'Maluku', 349438, 377.00, 51.20, 1001),
(22, 'Ternate', 'Maluku Utara', 204915, 76.00, 49.60, 1001),
(23, 'Jayapura', 'Papua', 346474, 936.00, 50.40, 1001),
(24, 'Manokwari', 'Papua Barat', 14355, 1453.00, 48.80, 1001),
(25, 'Sorong', 'Papua Barat', 22894, 714.00, 48.00, 1001),
(26, 'Mataram', 'Nusa Tenggara Barat', 402242, 60.66, 52.80, 1001),
(27, 'Kupang', 'Nusa Tenggara Timur', 449337, 188.33, 51.20, 1001),
(28, 'Denpasar', 'Bali', 903387, 127.78, 54.40, 1001),
(29, 'Mataram', 'Nusa Tenggara Barat', 402242, 60.66, 52.80, 1001),
(30, 'Bengkulu', 'Bengkulu', 345681, 152.30, 52.00, 1001),
(31, 'Pangkal Pinang', 'Bangka Belitung', 184444, 62.31, 50.40, 1001),
(32, 'Tanjungpinang', 'Kepulauan Riau', 212435, 144.03, 52.80, 1001),
(33, 'Bandar Lampung', 'Lampung', 1154973, 234.62, 51.60, 1001),
(34, 'Yogyakarta', 'Daerah Istimewa Yogyakarta', 388605, 32.25, 53.60, 1001),
(35, 'Semarang', 'Jawa Tengah', 1555444, 78.39, 54.00, 1001),
(36, 'Surabaya', 'Jawa Timur', 2874079, 350.54, 55.20, 1001),
(37, 'Malang', 'Jawa Timur', 888504, 84.20, 53.60, 1001),
(38, 'Bandung', 'Jawa Barat', 2463169, 167.27, 54.80, 1001),
(39, 'Bogor', 'Jawa Barat', 1096800, 118.50, 52.00, 1001),
(40, 'Tangerang', 'Banten', 2003648, 153.29, 53.20, 1001);

-- --------------------------------------------------------

--
-- Table structure for table `proyek`
--

CREATE TABLE `proyek` (
  `ID_Proyek` int(11) NOT NULL,
  `Nama_Proyek` varchar(255) DEFAULT NULL,
  `ID_Pemukiman` int(11) DEFAULT NULL,
  `Deskripsi_Proyek` varchar(1000) DEFAULT NULL,
  `Jenis_Proyek` varchar(255) DEFAULT NULL,
  `Dana_Proyek` int(11) DEFAULT NULL,
  `Status_Proyek` varchar(255) DEFAULT NULL,
  `ID_Admin` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `proyek`
--

INSERT INTO `proyek` (`ID_Proyek`, `Nama_Proyek`, `ID_Pemukiman`, `Deskripsi_Proyek`, `Jenis_Proyek`, `Dana_Proyek`, `Status_Proyek`, `ID_Admin`) VALUES
(1, 'Pembangunan Jalan Sehat Kampung Baru', 1, 'Pembangunan jalan sehat sepanjang 1 km di Kampung Baru', 'Infrastruktur', 100000000, 'Berjalan', 1010),
(2, 'Peningkatan Akses Air Bersih Perumahan Griya Asri', 2, 'Peningkatan akses air bersih bagi warga Perumahan Griya Asri', 'Infrastruktur', 200000000, 'Selesai', 1010),
(3, 'Pembangunan MCK di Kampung Nelayan', 3, 'Pembangunan MCK komunal di Kampung Nelayan', 'Infrastruktur', 50000000, 'Berjalan', 1010),
(4, 'Rehabilitasi Rumah Tidak Layak Huni (RTLH) di Perumnas Palem', 4, 'Rehabilitasi 10 unit RTLH di Perumnas Palem', 'Sosial', 100000000, 'Selesai', 1010),
(5, 'Bantuan Pangan Non Tunai (BPNT) untuk Warga Bumi Manuntung', 5, 'Penyaluran BPNT kepada 100 warga miskin di Bumi Manuntung', 'Sosial', 200000000, 'Berjalan', 1010),
(6, 'Pelatihan Pembuatan Kerajinan Tangan di Kebun Jeruk', 6, 'Pelatihan pembuatan kerajinan tangan bagi warga Kebun Jeruk', 'Ekonomi', 50000000, 'Selesai', 1010),
(7, 'Pengembangan Ekowisata di Permata Hijau', 7, 'Pengembangan ekowisata di kawasan hutan lindung Permata Hijau', 'Ekonomi', 100000000, 'Berjalan', 1010),
(8, 'Pemberdayaan Masyarakat Pesisir di Sei Tuan', 8, 'Pemberdayaan masyarakat pesisir melalui pelatihan dan bantua', 'Ekonomi', 200000000, 'Selesai', 1010),
(9, 'Peningkatan Kualitas Pendidikan di Permai Indah', 9, 'Rehabilitasi ruang kelas dan pengadaan buku pelajaran di SDN', 'Sosial', 100000000, 'Berjalan', 1010),
(10, 'Pembinaan Generasi Muda di Kampung Bugis', 10, 'Pembinaan generasi muda melalui kegiatan kepemudaan dan keag', 'Sosial', 50000000, 'Selesai', 1010),
(11, 'Posyandu Balita Sehat di Loa Janan', 11, 'Pemberian layanan Posyandu untuk kesehatan ibu dan balita', 'Sosial', 50000000, 'Berjalan', 1010),
(12, 'Peningkatan Kapasitas Poskamling di Sungai Kunjang', 12, 'Pelatihan dan peningkatan sigap warga untuk keamanan lingkun', 'Sosial', 20000000, 'Selesai', 1010),
(13, 'Pembangunan Jaringan Irigasi di Landasan Ulin', 13, 'Pembangunan jaringan irigasi sepanjang 2 km untuk sawah warg', 'Infrastruktur', 150000000, 'Berjalan', 1010),
(14, 'Program Bibit Gratis untuk Petani di Semberah', 14, 'Pemberian bantuan bibit unggul gratis kepada petani', 'Ekonomi', 100000000, 'Selesai', 1010),
(15, 'Workshop Kewirausahaan untuk Pemuda di Loa Bakung', 15, 'Pemberian pelatihan dan motivasi berwirausaha bagi pemuda', 'Ekonomi', 30000000, 'Berjalan', 1010),
(16, 'Bazar UMKM di Karang Rejo', 16, 'Penyelenggaraan bazar untuk memasarkan produk UMKM', 'Ekonomi', 40000000, 'Selesai', 1010),
(17, 'Angkutan Jemput Sekolah Gratis di Sungai Pinang', 17, 'Penyediaan layanan angkutan jemput sekolah gratis untuk anak', 'Sosial', 120000000, 'Berjalan', 1010),
(18, 'Renovasi Perpustakaan Umum di Teluk Leran', 18, 'Renovasi gedung dan pengadaan buku baru untuk perpustakaan u', 'Sosial', 80000000, 'Selesai', 1010),
(19, 'Pembangunan Lapangan Olahraga di Kampung Makmur', 19, 'Pembangunan lapangan olahraga untuk menunjang kegiatan pemud', 'Sosial', 180000000, 'Berjalan', 1010),
(20, 'Peningkatan Sarana Prasarana Posyandu di Bukit Alaya', 20, 'Pengadaan peralatan kesehatan dan peningkatan kualitas pelay', 'Sosial', 30000000, 'Selesai', 1010),
(21, 'Penanaman Pohon Mangrove di Muara Sungai Karang Mumus', 21, 'Penanaman pohon mangrove untuk pencegahan abrasi dan perbaik', 'Infrastruktur', 70000000, 'Berjalan', 1010),
(22, 'Sosialisasi dan Pemasangan Panel Tenaga Surya di rumah Warga', 22, 'Program sosialisasi dan pemberian bantuan panel tenaga surya', 'Infrastruktur', 250000000, 'Selesai', 1010),
(23, 'Workshop Peningkatan Kompetensi Digital UMKM', 23, 'Pelatihan digital marketing dan pengelolaan keuangan online', 'Ekonomi', 40000000, 'Berjalan', 1010),
(24, 'Pembangunan Taman Baca Masyarakat di Sembung Raya', 24, 'Pembangunan taman baca untuk meningkatkan minat baca masyara', 'Sosial', 60000000, 'Selesai', 1010),
(25, 'Pengembangan Wisata Kampung Tepian', 25, 'Pelatihan pengelolaan wisata, peningkatan atraksi wisata, da', 'Ekonomi', 200000000, 'Berjalan', 1010),
(26, 'Pagelaran Budaya Lokal di Samarinda Seberang', 26, 'Penyelenggaraan pagelaran budaya untuk pelestarian budaya lo', 'Sosial', 100000000, 'Selesai', 1010),
(27, 'Normalisasi Sungai Karang Amuntai', 27, 'Pengerukan sungai untuk menanggulangi banjir dan perbaikan a', 'Infrastruktur', 300000000, 'Berjalan', 1010),
(28, 'Bantuan Modal Usaha untuk Pedagang Kaki Lima', 28, 'Pemberian bantuan modal usaha kepada pedagang kaki lima untu', 'Ekonomi', 150000000, 'Selesai', 1010),
(29, 'Program Asuransi Kesehatan Gratis untuk Warga Miskin', 29, 'Pendaftaran warga miskin ke dalam program JKN untuk jaminan', 'Sosial', 200000000, 'Berjalan', 1010),
(30, 'Pembangunan MCK dan Tempat Cuci Piring Komunal', 30, 'Pembangunan MCK dan tempat cuci piring komunal untuk sanitas', 'Infrastruktur', 80000000, 'Berjalan', 1010),
(31, 'Pemasangan Lampu Jalan Tenaga Surya di Gang Seroja', 31, 'Pemasangan lampu jalan tenaga surya untuk penerangan jalan l', 'Infrastruktur', 50000000, 'Selesai', 1010),
(32, 'Peningkatan Kapasitas Tempat Penampungan Sampah', 32, 'Perluasan dan peningkatan kapasitas tempat pembuangan sampah', 'Infrastruktur', 200000000, 'Berjalan', 1010),
(33, 'Program Peningkatan Gizi Balita', 33, 'Pemberian makanan tambahan bergizi untuk balita', 'Sosial', 100000000, 'Berjalan', 1010),
(34, 'Pelatihan Tanggap Bencana untuk Masyarakat', 34, 'Pemberian pelatihan dan simulasi menghadapi bencana alam', 'Sosial', 40000000, 'Selesai', 1010),
(35, 'Pembangunan Drainase Perkotaan di Sempaja', 35, 'Pembangunan saluran drainase untuk menanggulangi genangan ai', 'Infrastruktur', 150000000, 'Berjalan', 1010),
(36, 'Pemberian Bantuan Alat Pertanian Kepada Kelompok Tani', 36, 'Distribusi traktor, perontok padi, dan peralatan pertanian l', 'Ekonomi', 250000000, 'Selesai', 1010),
(37, 'Workshop Literasi Digital untuk Masyarakat', 37, 'Pelatihan kecakapan dasar menggunakan internet dan media sos', 'Sosial', 30000000, 'Berjalan', 1010),
(38, 'Pembangunan Balai RW Serbaguna', 38, 'Pembangunan gedung serbaguna untuk kegiatan warga di tingkat', 'Sosial', 120000000, 'Selesai', 1010),
(39, 'Peningkatan Kualitas Pos PAUD di Berambai', 39, 'Renovasi gedung dan peningkatan kualitas pembelajaran PAUD', 'Sosial', 60000000, 'Berjalan', 1010);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID_Admin`);

--
-- Indexes for table `pemukiman`
--
ALTER TABLE `pemukiman`
  ADD PRIMARY KEY (`ID_Pemukiman`),
  ADD KEY `ID_Admin` (`ID_Admin`),
  ADD KEY `ID_Perkotaan` (`ID_Perkotaan`);

--
-- Indexes for table `perkotaan`
--
ALTER TABLE `perkotaan`
  ADD PRIMARY KEY (`ID_Perkotaan`),
  ADD KEY `id_admin` (`id_admin`);

--
-- Indexes for table `proyek`
--
ALTER TABLE `proyek`
  ADD PRIMARY KEY (`ID_Proyek`),
  ADD KEY `ID_Pemukiman` (`ID_Pemukiman`),
  ADD KEY `ID_Admin` (`ID_Admin`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `ID_Admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1011;

--
-- AUTO_INCREMENT for table `pemukiman`
--
ALTER TABLE `pemukiman`
  MODIFY `ID_Pemukiman` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `perkotaan`
--
ALTER TABLE `perkotaan`
  MODIFY `ID_Perkotaan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `proyek`
--
ALTER TABLE `proyek`
  MODIFY `ID_Proyek` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pemukiman`
--
ALTER TABLE `pemukiman`
  ADD CONSTRAINT `pemukiman_ibfk_1` FOREIGN KEY (`ID_Admin`) REFERENCES `admin` (`ID_Admin`),
  ADD CONSTRAINT `pemukiman_ibfk_2` FOREIGN KEY (`ID_Perkotaan`) REFERENCES `perkotaan` (`ID_Perkotaan`);

--
-- Constraints for table `perkotaan`
--
ALTER TABLE `perkotaan`
  ADD CONSTRAINT `perkotaan_ibfk_1` FOREIGN KEY (`id_admin`) REFERENCES `admin` (`ID_Admin`);

--
-- Constraints for table `proyek`
--
ALTER TABLE `proyek`
  ADD CONSTRAINT `proyek_ibfk_1` FOREIGN KEY (`ID_Pemukiman`) REFERENCES `pemukiman` (`ID_Pemukiman`),
  ADD CONSTRAINT `proyek_ibfk_2` FOREIGN KEY (`ID_Admin`) REFERENCES `admin` (`ID_Admin`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
