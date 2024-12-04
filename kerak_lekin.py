import os
import threading
import logging

# Log konfiguratsiyasi
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fayl kirish huquqlari (read, write, read_write)
FILE_PERMISSIONS = {
    'read': 'r',
    'write': 'w',
    'read_write': 'r+'
}

# Foydalanuvchilar va ularning faylga kirish huquqlari
users_permissions = {
    'admin': {'file1.txt': 'read_write', 'file2.txt': 'read_write'},
    'user1': {'file1.txt': 'read'},
    'user2': {'file2.txt': 'write'},
}

# Fayllar uchun qulf (lock) mexanizmlari
file_locks = {
    'file1.txt': threading.Lock(),
    'file2.txt': threading.Lock(),
}


# Faylga kirishni tekshirish
def check_permissions(user, filename, mode):
    permissions = users_permissions.get(user, {})
    if permissions.get(filename) in [mode, 'read_write']:
        return True
    logging.error(f"{user} faylga {mode} huquqi yo'q: {filename}")
    return False


# Fayl o'qish funksiyasi
def read_file(user, filename):
    if not check_permissions(user, filename, 'read'):
        return

    with file_locks[filename]:  # Faylni qulflash
        try:
            with open(filename, FILE_PERMISSIONS['read'], encoding='utf-8') as f:
                logging.info(f"{user} fayldan o'qimoqda: {filename}")
                content = f.read()
                print(f"{user} o'qilgan mazmun: \n{content}")
        except FileNotFoundError:
            logging.error(f"Fayl topilmadi: {filename}")
        except Exception as e:
            logging.error(f"Xatolik yuz berdi: {e}")


# Fayl yozish funksiyasi
def write_file(user, filename, data):
    if not check_permissions(user, filename, 'write'):
        return

    with file_locks[filename]:  # Faylni qulflash
        try:
            with open(filename, FILE_PERMISSIONS['write'], encoding='utf-8') as f:
                logging.info(f"{user} faylga yozmoqda: {filename}")
                f.write(data)
                logging.info(f"{user} faylga yozilgan ma'lumot: {data}")
        except FileNotFoundError:
            logging.error(f"Fayl topilmadi: {filename}")
        except Exception as e:
            logging.error(f"Xatolik yuz berdi: {e}")


# Fayllar bilan ko'p jarayonli ishlash
def user_interaction(user, action, filename, data=None):
    logging.info(f"{user} amaliyot boshladi: {action} fayl {filename}")
    if action == 'read':
        read_file(user, filename)
    elif action == 'write' and data:
        write_file(user, filename, data)
    else:
        logging.error(f"Amal noto'g'ri yoki ma'lumot yo'q: {action}")


# Jarayonlar testlash uchun
if __name__ == "__main__":
    # Fayllarni yaratish (faqat birinchi marta kerak)
    if not os.path.exists('file1.txt'):
        with open('file1.txt', 'w', encoding='utf-8') as f:
            f.write('Bu fayl 1 ning mazmuni.\n')

    if not os.path.exists('file2.txt'):
        with open('file2.txt', 'w', encoding='utf-8') as f:
            f.write('Bu fayl 2 ning mazmuni.\n')

    # Ko'p foydalanuvchi va jarayonlar sinovi
    t1 = threading.Thread(target=user_interaction, args=('admin', 'read', 'file1.txt'))
    t2 = threading.Thread(target=user_interaction, args=('user1', 'read', 'file1.txt'))
    t3 = threading.Thread(target=user_interaction,
                          args=('user2', 'write', 'file2.txt', 'Bu yangi yozilgan maʼlumot.\n'))

    # Barcha jarayonlarni boshlash
    t1.start()
    t2.start()
    t3.start()

    # Jarayonlar tugashini kutish
    t1.join()
    t2.join()
    t3.join()

    logging.info("Barcha jarayonlar tugadi.")
