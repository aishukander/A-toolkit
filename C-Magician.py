import os
import shutil
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

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

def clear_recycle_bin():
    os.system('PowerShell.exe -Command Clear-RecycleBin -Force')

def delete_all_files():
    folder = 'C:\\Windows\\Prefetch'
    for folder in ['C:\\Windows\\Temp', 'C:\\Windows\\Prefetch']:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                 pass

    os.system('PowerShell.exe -Command Clear-RecycleBin -Force')

print('請選擇要執行哪些功能：')
print('1. 刪除Temp中的檔案')
print('2. 刪除Prefetch中的檔案')
print('3. 清空回收桶')
print('4. 全選')

choice = input('請輸入您的選擇（1/2/3/4）：')

if choice == '1':
    delete_temp_files()
elif choice == '2':
    delete_prefetch_files()
elif choice == '3':
    clear_recycle_bin()
elif choice == '4':
    delete_all_files()    
else:
    print('無效的選擇。')