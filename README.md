# Instagram Request Withdraw Bot

This script automates the process of withdrawing follow requests on Instagram using Selenium. It logs in using stored cookies (if available) or manually logs in, saves cookies, and processes a list of profile links from an Excel file.

## 📌 Features:
✅ Uses **cookies** to avoid repeated logins  
✅ Withdraws **follow requests** from profile links in `requests.xlsx`  
✅ **Random wait times** to mimic human behavior  
✅ **Auto-saves login session** for future use  

---

## 🚀 **How to Use**# Instagram Request Withdraw Bot

This script automates the process of **withdrawing follow requests** on Instagram using **Selenium**. It logs in using stored cookies (if available) or manually logs in, saves cookies, and processes a list of **profile links from an Excel file** to withdraw follow requests.

---

## 📌 Features:
✅ **Uses cookies** to avoid repeated logins  
✅ Withdraws **follow requests** from profile links in `requests.xlsx`  
✅ **Random wait times** to mimic human behavior  
✅ **Auto-saves login session** for future use  
✅ **Takes random breaks (8-12 minutes)** to prevent detection  
✅ **Handles 2FA authentication** if required  

---

## 🚀 **How to Use**

### 1️⃣ Install Python & Dependencies  
Make sure you have **Python 3.x** installed.  
Then, install the required dependencies by running:  
pip install -r requirements.txt

---

### 2️⃣ Set Up Login Credentials
Create a file named credentials.txt in the same directory as the script.

#### 📌 Format of credentials.txt:

your_email@example.com 

your_password

#### 📌 Example:

**john.doe@gmail.com**

**mypassword123**

🔹 Make sure this file is in the same folder as the script.

🔹 Make sure that email/username is first line and password in second line.

🔹 DO NOT SHARE this file with anyone, as it contains sensitive login details.

---
### 3️⃣ Prepare the Excel File (requests.xlsx)
Create an Excel file (requests.xlsx) where:

Odd-numbered rows (1st, 3rd, 5th, etc.) contain Instagram profile links

Even-numbered rows (2nd, 4th, 6th, etc.) contain dates (or can be left empty)

### 4️⃣ Run the Script
Start the script by running:

**python withdraw_requests.py**

🔹 If it's the first time, it will ask for a 2FA code (if enabled).

🔹 If cookies exist, it will log in automatically without asking for credentials.

### 5️⃣ How the Script Works
🔹 Logs in to Instagram using stored cookies (or manually if needed).

🔹 Reads profile links from requests.xlsx.

🔹 Withdraws follow requests from each profile.

🔹 Waits randomly (30-90 seconds) between requests to prevent detection.

🔹 After every request, waits 8-12 minutes before continuing.

🔹 Closes the browser automatically when done.

### ⚠️ Important Notes
✅ Where to Change Credentials?

🔹 Open credentials.txt and update email and password.

🔹 If Instagram asks for login every time, delete the old cookie file:

🔹 **rm your_email@example.com.pkl**, then rerun the script to generate a new session.

✅ Where to Change Excel File?

The script reads Instagram profile links from requests.xlsx.

Make sure only odd-numbered rows contain valid profile links.

✅ If Instagram changes its layout, you might need to update the CSS selectors in the script.

✅ Avoid running the script too frequently to prevent account restrictions.

### 🔧 Requirements
🔹 Python 3.x

🔹 Mozilla Firefox (Web browser)

🔹 Geckodriver (Download from here)

🔹 Dependencies (installed via requirements.txt)

🔹 pip install -r requirements.txt

🔹 Excel file (requests.xlsx) containing Instagram profile links

### 🛠️ Troubleshooting

❌ **selenium.common.exceptions.NoSuchElementException**

🔹 Instagram may have changed the button's class names. Update the CSS selectors in the script accordingly.

❌ **cookies not found**

🔹 The script couldn't find a saved session. Delete the cookies file once to generate cookies again. 

❌ **Login to see photos**

🔹 Instagram may have logged you out. Try rerunning the script or deleting cookies and logging in again.

