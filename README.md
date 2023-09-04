
# S N A R F (0.0.2)

A realist Text to Speech software with minimalist GUI.


## Installation of VENV (Recommended)

Install virtual environment on Linux (Debian based):

```bash
sudo apt install python3-venv
```
```bash
pip3 install virtualenv
``` 

Install virtual environment on Microsoft Windows:

```bash
pip install virtualenv
```
## Cloning repository including VENV

- Linux (Debian based):
```bash
python3 -m venv snarf && source snarf/bin/activate && git clone https//github.com/m0rniac/snarf temp_folder && mv temp_folder/* . && rm -r temp_folder && deactivate
```
```bash
cd snarf/
```
```bash
source bin/activate
```
```bash
pip3 install -r requirements.txt
```


- Microsoft Windows:
```bash
python -m venv snarf && snarf\Scripts\activate.bat && git clone https://github.com/m0rniac/snarf temp_folder && move temp_folder\* . && rmdir /s /q temp_folder && deactivate
```
```bash
cd snarf
```
```bash
.\Scripts\activate
```
```bash
pip install -r requirements.txt
```

## Run:
- Linux (Debian based):
```bash
python3 main.py
```
- Windows:
```bash
python main.py
```
## API Reference

#### from Microsoft Azure:

[More documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt#text-to-speech)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | *Required* |


## Feedback
If you have any feedback, please reach out to me at:

[![instagram](https://img.shields.io/badge/instagram-0A66C2?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/christcastr/)

[![portfolio](https://img.shields.io/badge/buy_me_a_coffee-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.paypal.com/paypalme/christcastr/)