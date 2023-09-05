#導入模組
import re
import os
from importlib import import_module

#檢測模組是否有安裝
try:
    import pyperclip
    pyperclip = ("yes")
except ImportError:
    print("pyperclip模組未安裝")
    pyperclip = ("no")
try:
    import tkinter
    tkinter = ("yes")
except ImportError:
    print("tkinter模組未安裝")
    tkinter = ("no")

#根據不同的作業系統，使用不同的命令
if os.name == "nt": #如果是Windows系統
    if pyperclip == ("no"):
       print(f"正在嘗試安裝所需的模組")
       os.system(f"python -m pip install pyperclip")
else: #如果是Linux或macOS系統
    if pyperclip == ("no"):
       if tkinter == ("no"):
          print(f"正在嘗試安裝所需的模組")
          os.system(f"sudo apt install python3-tk")
          os.system(f"sudo apt install python3-pyperclip")
#導入模組
import tkinter
import pyperclip
#導入filedialog函數
from tkinter.filedialog import askopenfilename

#文本型
def text():
    #詢問使用者要修改的文本，並將其儲存為text變數
    text = input("請輸入要修改的文本：")

    #詢問使用者要替換與被替換的單字，並將其儲存為old變數與new變數
    old = input("請輸入要替換的單字：")
    new = input("請輸入要替換成的單字：")

    #替換文本中的單字，並將修改後的文本儲存為new_text變數
    new_text = re.sub(old, new, text)

    #將修改後的文本複製到剪貼簿
    pyperclip.copy(new_text)

    #輸出成功訊息
    print("文本修改完成，已複製到剪貼簿。")

#文檔型
def document():
    #隱藏根視窗
    tkinter.Tk ().withdraw ()

    #打開檔案選擇對話框，並將所選檔案的路徑儲存為filename變數
    filename = askopenfilename ()

    #讀取txt文本的內容，並儲存為text變數
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    #詢問使用者要替換與被替換的單字，並將其儲存為old變數與new變數
    old = input("請輸入要替換的單字：")
    new = input("請輸入要替換成的單字：")

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

#顯示選單
while True:
    print('請選擇使用方式：')
    print('1. 選取文檔型')
    print('2. 告知文本型')

    #詢問選擇
    choice = input('請輸入您的選擇（1/2）：')

    if choice == '1':
        document()
        break
    elif choice == '2':
        text()
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("********************************************************")
        print("*                                                      *")
        print("*                                                      *")
        print("*                                                      *")
        print("*                       無效選項                       *")
        print("*                                                      *")
        print("*                                                      *")
        print("*                                                      *")
        print("********************************************************")
        input('按任意鍵繼續...')
        os.system('cls' if os.name == 'nt' else 'clear')