# Bulk Delete Repos

## Steps:
1. Open in a new tab all your github repositories that you want to delete.
2. Use the [OneTab](https://chromewebstore.google.com/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall) extension to convert them into a list.
3. Clone this repository and navigate to the directory.
  ``` bash
  git clone https://github.com/bhavya-dang/bulk-delete-repos.git
  cd bulk-delete-repos
  ```
4. Create a file named `repos.txt` and paste the list of repositories into it.
5. Run the python script to clean and format the list of repositories. This will generate a new file called `output.txt`.
  ``` bash
  python clean_repos_list.py
  ```
6. Run the script to delete the repositories.

    **For Windows**
    ``` bash
    ./bulk_delete_repos.ps1
    ```

    **For Linux or macOS**
    ``` bash
    ./bulk_delete_repos.sh
    ```
