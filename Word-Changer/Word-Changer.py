#導入模組
import tkinter
import re
import os
#導入filedialog函數
from tkinter.filedialog import askopenfilename

#隱藏根視窗
tkinter.Tk ().withdraw ()

#打開檔案選擇對話框，並將所選檔案的路徑儲存為filename變數
filename = askopenfilename ()

#讀取txt文本的內容，並儲存為text變數
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

#詢問使用者要替換與被替換的單字，並將其儲存為old變數與new變數
old = input("請輸入您要替換的單字：")
new = input("請輸入您要替換成什麼單字：")

#替換文本中的單字，並將修改後的文本儲存為new_text變數
new_text = re.sub(old, new, text)
#分割檔案名稱和副檔名，並將其儲存為pre和ext變數
pre, ext = os.path.splitext(filename)
#連接新的檔案名稱和副檔名，並將其儲存為new_filename變數
new_filename = pre + " revise" + ext

#寫入修改後的文本到一個新的txt檔案
with open(new_filename, "w", encoding="utf-8") as f:
    f.write(new_text)

#輸出成功訊息
print("文本修改完成，已儲存到" + new_filename)