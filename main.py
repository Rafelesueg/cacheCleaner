import os
import shutil
import time

def delete_folder():
    user = os.getlogin()
    prefix_cache = "cache"
    prefix_nui_storage = "nui-storage"
    prefix_server_cache = "server-cache"
    prefix_server_cache_priv = "server-cache-priv"
    user_input = "null"
    custom_path = False

    print("cacheCleaner for FiveM made by Rafelesueg\nGithub:https://github.com/Rafelesueg\n\n")

    check = input(f"Custom installation path? (y/n): ")
    if check.lower() == "y":
        print("EXAMPLE PATH= Users\{user}\AppData\Local\FiveM\FiveM.app\data MAKE SURE TO INCLUDE 'data' FOLDER ")
        user_input = input("Insert here: ")
        custom_path = True

    if not custom_path:
        path_cache = rf"C:\Users\{user}\AppData\Local\FiveM\FiveM.app\data\{prefix_cache}"
        path_nui_storage = rf"C:\Users\{user}\AppData\Local\FiveM\FiveM.app\data\{prefix_nui_storage}"
        path_server_cache = rf"C:\Users\{user}\AppData\Local\FiveM\FiveM.app\data\{prefix_server_cache}"
        path_server_cache_priv = rf"C:\Users\{user}\AppData\Local\FiveM\FiveM.app\data\{prefix_server_cache_priv}"
    else:
        path_cache = os.path.join(user_input, prefix_cache)
        path_nui_storage = os.path.join(user_input, prefix_nui_storage)
        path_server_cache = os.path.join(user_input, prefix_server_cache)
        path_server_cache_priv = os.path.join(user_input, prefix_server_cache_priv)

    confirm = input(f"Are you sure you want to delete caches? (y/n): ")

    if confirm.lower() == 'y':
        try:
            time.sleep(1)
            print("\nDeleting cache folder")
            shutil.rmtree(path_cache)
            print("Cache folder successfully deleted!")
            print("---------------------------------------------------")
            time.sleep(1)
            print("Deleting nui-storage folder")
            shutil.rmtree(path_nui_storage)
            print("nui-storage folder successfully deleted!")
            print("---------------------------------------------------")
            time.sleep(1)
            print("Deleting server-cache folder")
            shutil.rmtree(path_server_cache)
            print("server-cache folder successfully deleted!")
            print("---------------------------------------------------")
            time.sleep(1)
            print("Deleting server-cache-priv folder")
            shutil.rmtree(path_server_cache_priv)
            print("server-cache-priv folder successfully deleted!")
            print("---------------------------------------------------")
            print("Cache cleared! You can close this window anytime")
        except Exception as e:
            print("---------------------------------------------------")
            print(f"An error occurred while deleting the folder.\nFolder already deleted or does not exist!\nError log: {e}")
    else:
        print("Operation canceled.")

if __name__ == "__main__":
    delete_folder()

    input("\nPress Enter to exit...")
