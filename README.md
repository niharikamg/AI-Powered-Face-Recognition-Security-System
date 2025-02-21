# AI-Powered Face Recognition Security System

## Features
- **Captures and stores face data** securely.
- **Recognizes faces in real-time for authentication**.
- **Implements Two-Factor Authentication (OTP via email)**.
- **Logs entry attempts in a SQLite database**.
- **Provides a Web UI using Streamlit**.

## Setup Instructions
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Register a face:
   ```
   python capture_face.py
   ```
3. Authenticate using face recognition:
   ```
   python recognize_face.py
   ```
4. Implement two-factor authentication (OTP):
   ```
   python two_factor_auth.py
   ```
5. Log access attempts:
   ```
   python log_access.py
   ```
6. Start the Web UI:
   ```
   python streamlit_ui.py
   ```

🚀 **Now you have a fully functional face recognition security system!** 🔐
