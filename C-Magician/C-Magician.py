import os
import shutil
import ctypes

#檢測是否用管理員身分開啟
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#告知未使用管理員身分開啟
if not is_admin():
    print("*********************************************************")
    print("*                                                       *")
    print("*                                                       *")
    print("*                                                       *")
    print("*               請以系統管理員身分執行此程式            *")
    print("*                                                       *")
    print("*                                                       *")
    print("*                                                       *")
    print("*********************************************************")
    input("按任意鍵繼續...")
    exit()

#清理Temp資料夾
def delete_temp_files():
    folder = 'C:\\Windows\\Temp'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
             pass

#清理Prefetch資料夾
def delete_prefetch_files():
    folder = 'C:\\Windows\\Prefetch'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
             pass

#清理回收桶
def clear_recycle_bin():
    os.system('PowerShell.exe -Command Clear-RecycleBin -Force')

#顯示選單
while True:
    print('請選擇要執行哪些功能：')
    print('1. 刪除Temp中的檔案')
    print('2. 刪除Prefetch中的檔案')
    print('3. 清空回收桶')
    print('4. 全選')

    #詢問選擇
    choice = input('請輸入您的選擇（1/2/3/4）：')

    if choice == '1':
        delete_temp_files()
        break
    elif choice == '2':
        delete_prefetch_files()
        break
    elif choice == '3':
        clear_recycle_bin()
        break
    elif choice == '4':
        delete_temp_files()
        delete_prefetch_files()
        clear_recycle_bin()
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
