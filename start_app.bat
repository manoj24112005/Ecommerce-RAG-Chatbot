@echo off
title E-Commerce AI Chatbot Server
cd /d "%~dp0"
echo Starting E-Commerce RAG Chatbot Server...
start http://localhost:8000
.\venv\Scripts\python.exe scripts/run.py api
pause
