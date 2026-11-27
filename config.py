"""Konfigurasi aplikasi. Ubah sesuai komputer Anda (default cocok untuk XAMPP)."""
import os

SECRET_KEY = os.environ.get("SECRET_KEY", "ganti-dengan-kunci-rahasia-anda")

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": int(os.environ.get("DB_PORT", "3306")),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),   # default XAMPP: kosong
    "database": os.environ.get("DB_NAME", "putra_laundry"),
    "use_pure": True,
}
