![screenshot](./screenshots/screenshot.jpg)

<center>🎒 <i> Keep track of your college schedule right from your terminal! </i> 💻</center>

## Inspiration

During my college days 🎒 , I have noticed a limitation in the existing PHP-based time-table website of my college. It only allowed users to view one schedule type at a time, either their Division or Elective Group's schedule. This inconvenience sparked my idea to create something compelling and user-friendly!

## Features

Inspired by the limitations of the PHP-based website, I developed a Python script that makes viewing today's timetable a bit simpler. Here's what it can do:

- **🔄 Automatic Module Installation**: To ensure a seamless user experience, my script automatically downloads the required modules during its first execution, making it easy for anyone to set up and use.

- **🔍 HTTP Request with Requests Library**: The script utilizes Python's 'requests' library to make HTTP requests and fetch the necessary CSV data from the time-table website.

- **📊 Tabulate Library for Tabular Display**: Once the data is captured, my script uses the 'tabulate' library to process and present it in a neat and organized tabular format, making it user-friendly and visually appealing.

- **🔄 Live Data**: This script utilizes Python's 'BeautifulSoup' library that fetches the latest list of Courses, Elective Lists, etc. from the [Time-Table website](https://time-table.sicsr.ac.in) to ensure the script works even if there are additions in Courses, Elective Lists, etc.

- **🔄 Auto-Update**: To ensure that the user has the latest version of this script, I have implemented auto-update feature which checks for any changes in this repository and automatically downloads new files and alters the existing ones.

## Configuration

#### UPDATE

I have successfully eliminated the need to edit `requestURL.txt` by providing a feature which lets the user to decide their Course, Elective Groups, etc.

![match_type](./screenshots/match_type.png)

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

##### `BeautifulSoup`

- You can install `bs4` by using [pip](https://pypi.org/project/pip/):

  ```python
  pip install bs4
  ```

> These dependencies are automatically installed on `main.py`'s first execution and is ensured by `.ensure_dependencies` in the project folder.

## 📝 To-Do List

- [ ] Mobile-Version to work with Siri (iOS)
- [x] Check and auto-install dependencies
- [ ] Description for README.md
- [ ] Choosing any other date

---

> Developed by:

### Anirudh Meshram [![LinkedIn](https://icons-for-free.com/iconfiles/png/32/linkedin+square+icon-1320168278649782468.png)](https://www.linkedin.com/in/anirudh-meshram/)

🎓 Symbiosis International (Deemed University)\
💼 Nestlé | Symbiosis Centre for International Education\
📄 [Resume / CV](https://docs.google.com/document/d/1DNtgwjOoLIUEXjDqhiM5x3OZc3uJmC9BC4-K7pix5dM/edit)
