<div align="center">
   <img alt="Logo" src="https://user-images.githubusercontent.com/76480451/170880452-d858f20b-7e70-4b29-994e-6138cad82534.png" width="100" />
</div>
<h1 align="center">
  FaceBit- AI Procturing 
</h1>

First Page:

![Screenshot 2022-05-29 212832](https://user-images.githubusercontent.com/76480451/170881325-3735c58f-434d-4c2f-b5e6-ca83c280e522.png)

Teacher Dashboard
![Screenshot 2022-05-29 233946](https://user-images.githubusercontent.com/76480451/170885175-0719288a-608e-452c-93c4-bd4108ec5477.png)

Student Dashboard
![Screenshot 2022-05-29 234604](https://user-images.githubusercontent.com/76480451/170885513-66e54966-30b1-4f17-9e82-04067f8e289e.png)
Past Test Conducted History
![Screenshot 2022-05-29 234420](https://user-images.githubusercontent.com/76480451/170885519-64eaf3ae-4f0e-4c2e-a39e-b00f69d6a4d8.png)
Giving Test
![Screenshot 2022-05-29 234639](https://user-images.githubusercontent.com/76480451/170885542-c1edec8f-90b4-4e77-8fce-b37cacac448d.png)
Proctor Logs 
![Screenshot 2022-05-29 234709](https://user-images.githubusercontent.com/76480451/170885527-54d47c6e-6f3b-4257-bd70-17832d591225.png)

# For More Watch The Demo Video : 
  https://www.youtube.com/watch?v=l9pxWba17so




## 🛠 Installation & Set Up

1. Clone the repo

   ```sh
   git clone https://github.com/abhishekchauhan15/FaceBit.git
   ```

2. Install all the requirements 

   ```sh
   pip install -r requirements.txt
   ```
2. Install virtual environment 

   ```sh
   pip install virtualenv
   ```
2. Create a new virtual environment. 
   ```sh
    virtualenv env
   ```
2. Run
   ```sh
    Set-ExecutionPolicy unrestricted
   ```
   Note : If it throws an error, run the same command in Admin PowerShell, and when prompted press `A`.

2. Enable virtualenv
   ```sh
   .\env\Scripts\activate.ps1
   ```


3. Download MySql

   ```sh
   https://www.mysql.com/downloads/
   ```

4. Download XAAMP

   ```sh
   https://www.apachefriends.org/download.html
   ```

5. Set MySql Port

   ```sh
   Set Port of MySql at 8111
   ```

6. Download these Folders into Project Folder

   ```sh
   https://drive.google.com/drive/folders/1vQqg-QO3ogs1W9QaS43812HVIq6hXAWm?usp=sharing

   ```
Final Set Up should look like this 

![Screenshot 2022-05-29 225124](https://user-images.githubusercontent.com/76480451/170883248-3c406355-cadf-440d-ae40-b7cd9cfeec45.png)

7. Open phpMyAdmin on browser

   ```sh
    http://localhost/phpmyadmin/index.php
   ```

8. Import MySql file

   ```sh
   Import the sql commands to set up the database in database folder named quizappstructure.sql
   ```
   ![Screenshot 2022-05-29 225644](https://user-images.githubusercontent.com/76480451/170883474-374fd74d-c4b7-4eae-8464-f344e3219e8e.png)



## 🚀 Running on local server

7. Run the App file

   ```sh
   Run the python file named app.py
   ```

8. Open the on localhost

   ```sh
   http://localhost:5000/
   ```

   Sometimes http://127.0.0.1:5000/ does no work so open on http://localhost:5000/ only

#
<br>

# Tech Stack Used

Frontend: HTML , CSS , Javascript

Backend : Flask

<br>

# 🎇 Authentication with Image Verification

✅ Basic Login, Register, Forgot Password, Change Password, etc <br>
✅ Only one login per user <br>
✅ Verify image of user at every time of login and also in    exam using face recognition technology.

<br>

# 🐱‍🏍Professor

✅ Using AI , professor can generate questions & answers <br>
✅ Professor can create exam <br>
✅ view exam history <br>
✅ Share details of exam with students <br>
✅ View questions <br>
✅ Update Questions <br>
✅ Delete questions <br>
✅ Update & delete questions will not work at the time of exam & after the exam. <br>
✅ Professor can view proctoring logs of the students. <br>
✅ Professor can report problems view FAQ, contact us.

<br>

# 🌟Students

✅ Give/Take Exam <br>
✅ Check Exam History <br>
✅ Check Results <br>
✅ Report Problems <br>

<br>

# ✨ Exam

✅ If webpage is refresh then the timer will not be refreshed <br>
✅ Support for Negative Marking. <br>
✅ Support for randomize questions. <br>
✅ For Objective type of Exam:

- Single page per question
- Bookmark question
- Question Grid with previous & next button
- At the time of exam submission all questions statistics will be showed to user for confirmation.

<br>

# 🌈 Proctoring

✅ Making logs of window events whenever user changes tab or opens a new tab. <br>
✅ Making logs of audio frequency at every 5 seconds of the students. <br>
✅ Detection of Mobile phone. <br>
✅ Detection of More than 1 person in the exam. <br>
✅ Gaze Estimation: Estimating the position of student body & eyes movements. <br>
✅ Taking Students images logs at every 5 seconds. <br>
✅ CUT, COPY, PASTE, Taking Screenshots Function is disabled. <br>
