python -m venv venv2
call venv2/Scripts/activate
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install imutils
pip install -r  requirements.txt
pip install opencv-python
py .\main.py
deactivate