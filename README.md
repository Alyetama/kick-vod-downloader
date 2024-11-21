
# Kick-dl

🚀 **Kick-dl** is a Python package and CLI tool for fetching and downloading VoDs from Kick channels. It supports selecting specific VoDs, listing available streams, downloading all VoDs, and customizing download quality and concurrency.

[![Supported Python versions](https://img.shields.io/badge/Python-%3E=3.7-blue.svg)](https://www.python.org/downloads/) [![PEP8](https://img.shields.io/badge/Code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/) 

---

## 📋 Features
- 🎥 Fetch VoDs from a specified Kick channel.
- 📑 List available VoDs with titles and dates.
- 📥 Download specific VoDs by index or download all available VoDs.
- 🎛 Customize download quality (e.g., `720p60`, `1080p60`).
- ⚡ Supports concurrent downloads for efficiency.
- 🔗 Option to output download URLs without downloading the VoDs.

---

## Requirements
- 🐍 **Python >= 3.7**: [Download Python](https://www.python.org/downloads/)

---

## ⬇️ Installation

Install Kick-dl using `pip`:
```sh
pip install kick-dl
```

---

## ⌨️ Usage

To view all available options, use:
```sh
kick-dl --help
```

**Example Help Output**:
```
usage: kick-dl [-h] -c CHANNEL_NAME [-i VOD_INDEX] [-l] [-a] [-nd] [-q QUALITY] [-C N_CONCURRENT_DOWNLOADS]

Download Kick VoDs from a specified channel.

options:
  -h, --help            show this help message and exit
  -c CHANNEL_NAME, --channel_name CHANNEL_NAME
                        The name of the channel to fetch VoDs from.
  -i VOD_INDEX, --vod_index VOD_INDEX
                        The index or list of indexes of the VoD(s) to download. Use 0 for the most recent VoD, 1 for the second
                        most recent, and so on. Provide a single index or a comma-separated list of integers.
  -l, --list_indexes    List all available VoDs with their titles and dates for easy selection.
  -a, --download_all    Download all available VoDs without selecting specific indexes.
  -nd, --no_download    Do not download the VoD. Instead, output the VoD download URL(s).
  -q QUALITY, --quality QUALITY
                        Specify the desired quality of the VoD. Defaults to the highest quality available. Common options include
                        160p, 360p, 480p, 720p60, and 1080p60.
  -C N_CONCURRENT_DOWNLOADS, --n_concurrent_downloads N_CONCURRENT_DOWNLOADS
                        Set the number of concurrent downloads. Defaults to 1.
```

---

## 📕 Examples

### 1. Download the Latest VoD
```sh
kick-dl -c <channel_name> -i 0
```

### 2. Download Multiple Specific VoDs by Index
```sh
kick-dl -c <channel_name> -i 0,1,2
```

### 3. List All Available VoDs
```sh
kick-dl -c <channel_name> -l
```

### 4. Download All Available VoDs
```sh
kick-dl -c <channel_name> -a
```

### 5. Specify the Quality and Concurrent Downloads
```sh
kick-dl -c <channel_name> -i 0 -q 720p60 -C 3
```

### 6. Output the Download URL Without Downloading
```sh
kick-dl -c <channel_name> -i 0 -nd
```

---

## 📝 License
This project is licensed under the [MIT License](LICENSE).

---
