# 資料來源（請自行取得，本 repo 不含這些檔案）

這些文件的著作權屬於原出版者，不在本 repo 內。請到官方管道下載，放進對應資料夾後，agent 才能查詢。連結為撰寫時的搜尋結果，可能隨 FIBA 網站改版而變動，請以官方頁面為準。

## FIBA 官方（英文）
| 文件 | 連結 |
|---|---|
| 官方規則頁面（總入口） | https://about.fiba.basketball/en/our-sport/official-basketball-rules |
| Official Basketball Rules 2024 | https://assets.fiba.basketball/image/upload/documents-corporate-fiba-official-rules-2024-v10a.pdf |
| Official Basketball Rules Interpretations (OBRI) 2024 | https://assets.fiba.basketball/image/upload/documents-corporate-fiba-official-rules-2024-obri-v10a.pdf |
| 2024 規則修訂摘要 | https://assets.fiba.basketball/image/upload/documents-corporate-fiba-official-rules-2024-changes---v20a-eng.pdf |
| FIBA 裁判文件總覽 | https://refereeing.fiba.basketball/fr/documents |
| IOT 手冊（2022 v2.0） | https://refereeing.fiba.basketball/fr/documents/fiba-referees-manual-individual-officiating-techniques-iot-2022-v20 |
| 2PO 手冊（說明頁，內容在 FIBA iRef app） | https://refereeing.fiba.basketball/fr/news/new-2po-manual-published-to-support-national-federations |

> 本專案開發時使用的規則檔是 `v1.0`，FIBA 網站上的檔名為 `v10a`，可能是小幅更正版，未逐項比對。
> 本專案目前引用的官方解釋是 **2022 規則的 2023.06.01 版**；FIBA 已發布 2024 版官方解釋，尚未改用。

## 中文版
中華民國籃球協會編譯的中文規則、官方解釋與裁判手冊，請洽中華民國籃球協會（官網 www.basketball-tpe.org）。我們沒有驗證其下載頁面，所以不附直接連結。

## 資料夾對應
| 資料夾 | 內容 |
|---|---|
| `01_規則與判例/` | 規則與官方解釋 PDF |
| `02_IOT_個人執法技巧/` | IOT 手冊 |
| `03_2PO_二人裁判法/` | 2PO 手冊／教材 |
| `04_3PO_三人裁判法/` | 3PO 手冊（基礎版、進階版） |

## 中文 PDF 的 OCR
中文 PDF 的文字無法直接擷取（字型編碼問題）。取得後用 OCR 重建：

```bash
pip install -r tools/requirements.txt
python tools/ocr_pdf.py "01_規則與判例/<檔名>.pdf" "OCR_文字檔/<檔名>.txt"
```

OCR 需要 Windows 10/11 並安裝繁體中文語言包。辨識結果有少量錯字，數字與條號請回頭對照原文。
