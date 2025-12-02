@echo off
echo  Installing Cyber Guardian Dependencies...
echo.
echo [1/2] Installing Frontend Dependencies...
cd frontend
call npm install
cd ..
echo.
echo [2/2] Installing Backend Dependencies...
cd backend
call venv\Scripts\activate.bat
pip install -r requirements.txt
cd ..
echo.
echo  Installation Complete!
pause
