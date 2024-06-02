# FiveM Cache Cleaner

This Python script is designed to automatically clean cache folders associated with the 'FiveM' application.

## Main Features:

1. **Automatic FiveM Directory Detection:**
   - The `find_fivem_directory()` function automatically searches for the installation directory of 'FiveM' in the `LOCALAPPDATA` directory of the operating system.
   - If the directory is found, the function returns the path of the 'FiveM' installation directory; otherwise, it returns `None`.

2. **Deletion of Cache Folders:**
   - The `delete_folder()` function uses the path of the 'FiveM' installation directory found by the previous function to construct the paths of the cache folders to be deleted.
   - The cache folders to be deleted include `cache`, `nui-storage`, `server-cache`, and `server-cache-priv`.
   - The user is prompted to confirm the deletion of the cache folders.
   - If confirmed, the folders are deleted one by one using `shutil.rmtree()`, and confirmation messages are displayed after the deletion of each folder.
   - In case of an error during the deletion of a folder, an error message is displayed with the details of the error.

## How to Use (as User):
1. Simply download the .exe file and run it
2. Follow the on-screen instructions to confirm the deletion of cache folders associated with 'FiveM'.
3. Once the script completes the cache clearing process, you can close the terminal or command prompt.
   
## How to Use (as Dev):

1. Make sure you have Python installed on your system.
2. Download the `main.py` script from this repository.
3. Open any idle of your preference.
4. Run the script by executing the following command:
   ```bash
   python main.py
5. Follow the on-screen instructions to confirm the deletion of cache folders associated with 'FiveM'.
6. Once the script completes the cache clearing process, you can close the terminal or command prompt.

> [!NOTE]
> Caution: Ensure critical files are backed up before running the cache cleaner, as the process irreversibly deletes cache data.
