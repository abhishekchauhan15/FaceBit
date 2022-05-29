<div align="center">
   <img alt="Logo" src="https://user-images.githubusercontent.com/76480451/170880452-d858f20b-7e70-4b29-994e-6138cad82534.png" width="100" />
</div>
<h1 align="center">
  FaceBit- AI Procturing 
</h1>
<p align="center">

<a href="https://www.netlify.com/" target="_blank">Netlify</a>
<a href="https://app.netlify.com/sites/brittanychiang/deploys" target="_blank">
![Screenshot 2022-05-29 212832](https://user-images.githubusercontent.com/76480451/170881325-3735c58f-434d-4c2f-b5e6-ca83c280e522.png)

  </a>
</p>

## 🚨 Forking this repo (please read!)

Many people have contacted me asking me if they can use this code for their own website, and the answer to that question is usually **yes, with attribution**.

I value keeping my site open source, but as you all know, _**plagiarism is bad**_. It's always disheartening whenever I find that someone has copied my site without giving me credit. I spent a non-trivial amount of effort building and designing this iteration of my website, and I am proud of it! All I ask of you all is to not claim this effort as your own.

Please also note that I did not build this site with the intention of it being a starter theme, so if you have questions about implementation, please refer to the [Gatsby docs](https://www.gatsbyjs.org/docs/).

### TL;DR

Yes, you can fork this repo. Please give me proper credit by linking back to [brittanychiang.com](https://brittanychiang.com). Thanks!

## 🛠 Installation & Set Up

1. Clone the repo

   ```sh
   git clone https://github.com/abhishekchauhan15/FaceBit.git
   ```

2. Install all the requirements [NVM](https://github.com/nvm-sh/nvm)

   ```sh
   pip install -r requirements.txt
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

7. Open phpMyAdmin on browser

   ```sh
    http://localhost/phpmyadmin/index.php
   ```

8. Import MySql file

   ```sh
   Import the sql commands to set up the database in database folder named quizappstructure.sql
   ```

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
✅ System allows only one login per user, so that user can’t do any unfair means. <br>
✅ System will verify image of user at every time of login and also in exam using face recognition technology.

<br>

# 🐱‍🏍Professor

✅ Using AI , professor can generate questions & answers <br>
✅ Professor can create exam, view exam history, share details of exam with students, view questions, update, delete questions, but update & delete questions will not work at the time of exam & after the exam. <br>
✅ Professor can insert marks of subjective & practical exam & also publish the results, view results. <br>
✅ Professor can view Live Monitoring of Exam & also can view proctoring logs of the students. <br>
✅ Professor can report problems, recharge exam wallet, view FAQ, contact us.

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
✅ Support for Calculator for Mathematical type of Exam <br>
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
