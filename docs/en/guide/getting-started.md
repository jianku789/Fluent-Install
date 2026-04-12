# Quick Start

## About FluentInstall

FluentInstall is a free and open-source Steam game library tool based on SteamTools. This project uses the cai-install backend with a self-made Fluent Design frontend to provide users with a beautiful, simple, and efficient experience.

### Main Features

- **Game Search & Library Addition**: Search by game name or AppID and add to library with one click
- **Multiple Manifest Sources**: Support for various sources including SWA V2, Walftech, SteamAutoCracks, etc.
- **Installed Games Management**: Easily view and manage games already in your library
- **Steam Restart**: One-click Steam restart to apply library additions
- **Theme Customization**: Light/Dark themes with multiple color options
- **Multi-Language Support**: Simplified Chinese, Traditional Chinese, English, French, Russian, German, Japanese, Korean, Spanish

---

## Download

| Source | Link |
| --- | --- |
| GitHub | [Download](https://github.com/zhouchentao666/Fluent-Install/releases/latest) |
| Cloud Drive (China) | [Download](https://wwazq.lanzoub.com/b00odsy2kd) (Password: 1234) |
| Open Source | [GitHub](https://github.com/zhouchentao666/Fluent-Install/) |

---

## Tutorial

### 1. Pre-Installation Preparation

1. **Install SteamTools**
   - Go to [3a.lol](https://3a.lol) to download and install SteamTools
   - Make sure SteamTools is running properly after installation

2. **Repair Steam**
   - Use SteamTools' repair function to fix your Steam client
   - Ensure Steam can log in and run normally

### 2. Install FluentInstall

1. **Download the Program**
   - Download the latest version of FluentInstall from the links above
   - Extract the zip file to any folder

2. **Install Dependencies**
   - Run `fluent_install.bat` to install necessary dependencies
   - Wait for the installation to complete

3. **Launch the Program**
   - Run `python main.py` to start the program
   - Or run `run_fluent.bat` for quick launch

### 3. Using the Program

#### 1. Search and Add Games

1. Click **"Search Library"** in the left navigation bar
2. Enter the game name or AppID in the search box
3. Click the **"Search"** button
4. Select the game you want to add from the search results
5. Select a **Manifest Source** (if one fails, try another)
6. Check the addition options as needed:
   - **Add All DLC**: Add all DLCs for the game
   - **Patch Depot Key**: Add game's workshop content
   - **Patch Manifest** (not recommended, only select if not working): Fix manifest files
7. Click the **"Add Game"** button

#### 2. Manage Installed Games

1. Click **"Home"** in the left navigation bar
2. View the list of all added games
3. You can switch view modes (List/Card) and sorting options
4. Click the **"Delete"** button on a game card to remove it from the library

#### 3. Restart Steam

1. After adding games, click the **"Restart Steam"** button in the top right
2. After confirmation, Steam will automatically close and restart
3. After restart, the added games will appear in your library

### 4. Settings

1. Click **"Settings"** in the left navigation bar
2. You can configure the following options:
   - **Steam Path**: Manually specify Steam installation path (leave empty for auto-detection)
   - **Theme Mode**: Light/Dark/Follow System
   - **Theme Color**: Choose your preferred theme color
   - **Language**: Switch interface language
   - **Default Page**: Set the default page displayed after startup
   - **Unlocker Mode**: Auto Detect/Force SteamTools/Force GreenLuma
   - **Download Timeout**: Increase if your network is slow

### 5. Notes

1. **Ensure SteamTools is installed and running properly**
2. **It's recommended to restart SteamTools before adding games**
3. **If addition fails, try switching to a different manifest source**
4. **Some games may require specific manifest sources to work**
5. **You must restart Steam to see the added games**

---

## FAQ

If you encounter issues, please check the [FAQ](/en/faq/)

---

If you find this useful, please give the project a **star** ⭐ or buy the author a coffee!
