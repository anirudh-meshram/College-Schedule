![screenshot](./screenshots/screenshot.jpg)

<center>🎒 <i> Keep track of your college schedule right from your terminal! </i> 💻</center>

## Inspiration

During my college days 🎒 , I have noticed a limitation in the existing PHP-based time-table website of my college. It only allowed users to view one schedule type at a time, either their Division or Elective Group's schedule. This inconvenience sparked my idea to create something compelling and user-friendly!

## Features

Inspired by the limitations of the PHP-based website, I developed a Python script that makes viewing today's timetable a bit simpler. Here's what it can do:

- **🔍 HTTP Request with Requests Library**: The script utilizes Python's 'requests' library to make HTTP requests and fetch the necessary CSV data from the time-table website.

- **📊 Tabulate Library for Tabular Display**: Once the data is captured, my script uses the 'tabulate' library to process and present it in a neat and organized tabular format, making it user-friendly and visually appealing.

- **🔄 Automatic Module Installation**: To ensure a seamless user experience, my script automatically downloads the required modules during its first execution, making it easy for anyone to set up and use.

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

> These dependencies are automatically installed on `main.py`'s first execution and is ensured by `.ensure_dependencies` in the project folder.

## Configuration

Currently this script displays lectures for **BBA-IT Div-B Sem-V** and **BBA-IT Sem-V Electives**. In order to display lectures for your Program/Divison, **Follow these instructions**:

> Ensure that you have a **code-editor** / **IDE** like [VSCode](https://code.visualstudio.com/download) installed on your system before proceeding further

1. Go to [SICSR's Time-Table](http://time-table.sicsr.ac.in)
2. Click **Report** on Navigation Bar (On the left of Search Bar)
3. Choose your Divisions/Elective Groups that you want to fetch lectures from under **Match Type** (Use `Ctrl`-Click to select more than one type)

❗ **Ensure that `CSV` is selected under `Format`**

4. Go to **Developer Tools** (`Ctrl`+`Shift`+`I` in Google Chrome)
5. On the website, click **Run Report**

   > After submitting the form, A Request URL gets generated under **Network** tab under **Developer Options**

6. Replace the newly generated Request URL in the file `requestURL.txt`

7. Run `main.py` to install the dependencies and run the program to view today's college schedule

## 📝 To-Do List

- As of 24/7/2023, I am working on a feature that lets the user choose their match type from the terminal itself, eliminating the need to follow the current configuration steps.

> Current progress:

```
  S. No  Subject
-------  --------------------------------
      0  BCA (V) - Div. A
      1  BCA (V) - Div. B
      2  BCA (V) - Div. C
      3  BCA (V) - Div. D
      4  BCA (V) - Div. E
      5  BCA (V) - Elective
      6  BCA (III) - Div. A
      7  BCA (III) - Div. B
      8  BCA (III) - Div. C
      9  BCA (III) - Div. D
     10  BCA (III) - Div. E
     11  BCA (III) - Div. F
     12  BCA(Honours) (V) - Elective
     13  BCA(Honours) (III) - Elective
     14  BBA-IT (V) - Div. A
     15  BBA-IT (V) - Div. B
     16  BBA-IT (V) - Div. C
     17  BBA-IT (V) - Elective
     18  BBA-IT (III) - Div. A
     19  BBA-IT (III) - Div. B
     20  BBA-IT (III) - Div. C
     21  BBA-IT (III) - Elective
     22  BBA-IT(Honours) (III) - Elective
     23  MSC-CA (I)
     24  MSC-CA (III)
     25  MSC-CA (III) - SD
     26  MSC-CA (III) - DS
     27  MBA-DT (I)
     28  MBA-DT (III)
     29  MBA-IT (I) - Div. A
     30  MBA-IT (I) - Div. B
     31  MBA-IT (III)
     32  MBA-IT (III) - DA
     33  MBA-IT (III) - ITIM
     34  Meetups/Placement
     35  EXAM
     36  Elective
     37  Common Batch
     38  Guest Lecture
     39  BBA-IT (I) - Div. A
     40  BBA-IT (I) - Div. B
     41  BBA-IT (I) - Div. C
     42  BREAK
     43  BCA (I) - Div. A
     44  BCA (I) - Div. B
     45  BCA (I) - Div. C
     46  BCA (I) - Div. D
     47  BCA (I) - Div. E
     48  BCA (I) - Div. F
     49  type.x
     50  type.y
     51  type.z
Enter your choices separated by commas
For example: 0,2        OR       1,3,5
```

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
