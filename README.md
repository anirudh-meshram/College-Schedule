## Requirements

- [Python](https://python.org/downloads)
- [pip](https://pypi.org/project/pip/)

#### Python Dependencies

##### `requests`

- You can install `requests` by using [pip](https://pypi.org/project/pip/):

  ```python
  pip install requests
  ```

##### `tabulate`

- You can install `tabulate` by using [pip](https://pypi.org/project/pip/):

  ```python
  pip install tabulate
  ```

## Configuration

Currently this script displays lectures for **BBA-IT Div-B Sem-V** and **BBA-IT Sem-V Electives**. In order to display lectures for your Program/Divison, **Follow these instructions**:

> Ensure that you have a **code-editor** / **IDE** like [VSCode](https://code.visualstudio.com/download) installed on your system before proceeding further

1. Go to [SICSR's Time-Table](http://time-table.sicsr.ac.in)
2. Click on **Report** on Navigation Bar (On the left of Search Bar)
3. Choose your Divisions/Elective Groups that you want to fetch lectures from under **Match Type** (Use `Ctrl`-Click to select more than one type)

❗ **Ensure that `CSV` is selected under `Format`**

4. Go to **Developer Tools** (`Ctrl`+`Shift`+`I` in Google Chrome)
5. On the website, click **Run Report**

   > After submitting the form, A Request URL gets generated under **Network** tab under **Developer Options**

6. Replace the newly generated Request URL with the variable `request_url` in `main.py` according to the given syntax

## 📝 To-Do List

- [ ] Mobile-Version to work with Siri (iOS)
- [ ] Description for README.md
- [ ] Choosing any other date

---

> Developed by:

### Anirudh Meshram [![LinkedIn](https://icons-for-free.com/iconfiles/png/32/linkedin+square+icon-1320168278649782468.png)](https://www.linkedin.com/in/anirudh-meshram/)

🎓 Symbiosis International (Deemed University)\
💼 Nestlé | Symbiosis Centre for International Education\
📄 [Resume / CV](https://docs.google.com/document/d/1DNtgwjOoLIUEXjDqhiM5x3OZc3uJmC9BC4-K7pix5dM/edit)
