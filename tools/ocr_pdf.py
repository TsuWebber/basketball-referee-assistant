"""將 PDF 以 Windows 內建 OCR（繁體中文 zh-Hant-TW）轉成逐頁文字檔。僅支援 Windows 10/11，需先安裝繁體中文語言包。
用法：python tools/ocr_pdf.py <輸入.pdf> <輸出.txt> [起始頁] [結束頁]
輸出以「===== 第 N 頁 =====」分隔，可中斷後續跑（已完成的頁會略過）。"""
import sys, os, time, asyncio, warnings, re
warnings.filterwarnings("ignore")
import pymupdf
from winrt.windows.media.ocr import OcrEngine
from winrt.windows.globalization import Language
from winrt.windows.graphics.imaging import BitmapDecoder
from winrt.windows.storage.streams import InMemoryRandomAccessStream, DataWriter

pdf, out = sys.argv[1], sys.argv[2]
first = int(sys.argv[3]) if len(sys.argv) > 3 else 1
last = int(sys.argv[4]) if len(sys.argv) > 4 else 10**6


CJK = "⺀-鿿＀-￯　-〿"
def clean(t):
    t = re.sub(f"(?<=[{CJK}]) +", "", t)
    t = re.sub(f" +(?=[{CJK}])", "", t)
    t = re.sub(r"(?<=[0-9.]) +(?=[0-9.])", "", t)
    return t


async def ocr_png(engine, data: bytes):
    stream = InMemoryRandomAccessStream()
    w = DataWriter(stream)
    w.write_bytes(data)
    await w.store_async()
    await w.flush_async()
    stream.seek(0)
    dec = await BitmapDecoder.create_async(stream)
    bmp = await dec.get_software_bitmap_async()
    res = await engine.recognize_async(bmp)
    return [clean(l.text) for l in res.lines]


async def main():
    engine = OcrEngine.try_create_from_language(Language("zh-Hant-TW"))
    doc = pymupdf.open(pdf)
    n = min(last, len(doc))
    done = set()
    if os.path.exists(out):
        for line in open(out, encoding="utf-8"):
            if line.startswith("===== 第 "):
                done.add(int(line.split()[2]))
    t0 = time.time()
    with open(out, "a", encoding="utf-8") as f:
        for p in range(first, n + 1):
            if p in done:
                continue
            pix = doc[p - 1].get_pixmap(dpi=200)
            lines = await ocr_png(engine, pix.tobytes("png"))
            f.write(f"===== 第 {p} 頁 =====\n" + "\n".join(lines) + "\n\n")
            f.flush()
            print(p, f"{time.time()-t0:.0f}s", flush=True)


asyncio.run(main())
