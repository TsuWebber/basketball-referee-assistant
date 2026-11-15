# 資料來源（請自行取得，本 repo 不含這些檔案）

這些文件的著作權屬於原出版者，不在本 repo 內。請到官方管道下載，放進對應資料夾後，agent 才能查詢。

| 資料夾 | 檔案 | 出處（版權方） |
|---|---|---|
| `01_規則與判例/` | FIBA Official Basketball Rules 2024 v1.0（英文） | FIBA |
| `01_規則與判例/` | 2022 國際籃球規則中文版、官方解釋 2023.06.01 | 中華民國籃球協會編譯（FIBA 規則） |
| `02_IOT_個人執法技巧/` | FIBA 裁判手冊：個人執法技巧 (IOT) 中文版 | FIBA／中華民國籃球協會編譯 |
| `03_2PO_二人裁判法/` | 二人裁判法教材、Basketball Victoria 2PO Manual | 各自作者／出版單位 |
| `04_3PO_三人裁判法/` | FIBA 三人裁判法基礎版、進階版 中文版 | FIBA／中華民國籃球協會編譯 |

中文 PDF 的文字無法直接擷取（字型編碼問題）。取得後用 OCR 重建：

```bash
pip install -r tools/requirements.txt
python tools/ocr_pdf.py "01_規則與判例/<檔名>.pdf" "OCR_文字檔/<檔名>.txt"
```

OCR 需要 Windows 10/11 並安裝繁體中文語言包。辨識結果有少量錯字，數字與條號請回頭對照原文。
