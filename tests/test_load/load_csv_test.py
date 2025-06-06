# -*- coding: utf-8 -*-
"""load_csv_test

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Duu6YY0d_bx9lYqnLJdQ6eZHm0n6tzbw
"""

import pandas as pd
import unittest
import os
import tempfile
from utils.load_data.load_csv import saved_to_csv

class TestLoadCSV(unittest.TestCase):

  def setUp(self):
    # Membuat File Sementara untuk Pengujian Load CSV
    self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    self.filename = self.temp_file.name
    self.temp_file.close()

  def tearDown(self):
    # Menghapus File Setelah Pengujian Load CSV Selesai
    if os.path.exists(self.filename):
      os.remove(self.filename)

  def test_succeeded_data_saved(self):
    # Menguji Keberhasilan Data Disimpan ke dalam CSV
    data = {
        "Title": ["Product A"],
        "Price": [320000],
        "Rating": [3.5],
        "Colors": [5],
        "Size": ["L"],
        "Gender": ["Male"]
    }
    df = pd.DataFrame(data)

    saved_to_csv(df, self.filename)

    self.assertTrue(os.path.exists(self.filename))

    df_saved = pd.read_csv(self.filename)
    pd.testing.assert_frame_equal(df, df_saved, check_dtype=False)

  def test_failed_data_saved(self):
    # Menguji Penanganan Exception Benar atau Tidak jika Path Data Invalid
    data = {
        "Title": ["Product A"],
        "Price": [320000],
        "Rating": [3.5],
        "Colors": [5],
        "Size": ["L"],
        "Gender": ["Male"]
    }
    df = pd.DataFrame(data)

    filename_invalid = "/invalid_path/fashion_studio.csv"

    with self.assertRaises(Exception):
      saved_to_csv(df, filename_invalid)

if __name__ == "__main__":
  unittest.main()