[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
![version](https://img.shields.io/badge/version-1.0.0-red)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Kaminyou/ZED-Record-GUI/blob/main/LICENSE)
![linting workflow](https://github.com/Kaminyou/ZED-Record-GUI/actions/workflows/main.yml/badge.svg)
# ZED-Record-GUI
A GUI implemented by Python for ZED video recording

## Dependency
### `tkinter`
```
$ sudo apt-get install python3-tk
```

### `pyinstaller`
```
$ pip install pyinstaller
```

### `pyzed`
Please refer to the [official document of ZED](https://www.stereolabs.com/docs/app-development/python/install).

## Build
```
$ pyinstaller --hidden-import=tkinter --hidden-import=tkinter.filedialog main.py --onefile -w
```
Then the executable file will be `dist/main`

