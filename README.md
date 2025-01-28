# 🕸️ Network Analysis Tool

## 🖖 Overview
This is my first working desktop application made with Python and Pyqt. Mostly this is just for proving to potential employers that I can figure out how to code enough to get a job. 

Welcome to the **Network Analysis Tool** – your trusty sidekick in the thrilling realm of network troubleshooting! Whether you're a seasoned sysadmin or just someone with a curious mind, this tool is here to make network tasks **less painful** and (dare I say) **fun**. Think of it as your own tricorder but for networks! 🖖


This desktop application is a **working prototype** and **proof of concept**, built to help you tackle network tasks with ease. Here's what it can do:

1. **Connectivity (Ping)**: Test if an IP address is reachable by sending packets (because what’s a network without packets, right?).
2. **Ports**: Scan ranges of ports or even test Telnet connections for those "Is this thing on?" moments.
3. **Routes**: Wrangle your routing table – view it, add to it, delete from it, or find specific routes like a pro.
4. **Path**: Trace routes and run MTR to uncover the epic journey of your packets through the digital ether. 🌌

---

## 🛠️ Installation
Ready to embark on your network adventure? You can download the standalone executable from the `dist/` directory, or, if you're the "roll your own code" type, follow the steps below to build it from source.

### ⚙️ Build from Source
Here's how you can summon this app into existence:

1. **Clone the repository** (like pulling a book of spells from a shelf):
   ```bash
   git clone https://github.com/Cramessar/Network_app
   ```

2. **Install dependencies**:
   Ensure you’ve got Python (the snake, not the comedy troupe) and PyQt5 installed:
   ```bash
   pip install PyQt5
   ```

3. **Run the app**:
   Cast the magic command to launch the app:
   ```bash
   python main.py
   ```

4. **Build the standalone executable** (Optional, for wizards who prefer `.exe` spells):
   Use PyInstaller to bundle it up:
   ```bash
   pyinstaller --onefile --noconsole --add-data "Path/ping.py;." --add-data "Path/ports.py;." --add-data "Path/routes.py;." --add-data "Path/path.py;." "Path/main.py"
   ```
   Your shiny new executable will appear in the `dist/` directory.

---

## 🧙 Features
Here’s what this tool brings to your network arsenal:
- **Ping**: Send packets to check if an IP is alive and well (or stubbornly silent).
- **Port Scanning**: Peek into a range of ports to see who’s listening. Bonus: Telnet testing!
- **Route Management**: Get nerdy with routes. Add them, find them, or show them the door.
- **Trace Route and MTR**: Map your packets’ epic voyage, uncovering every hop along the way.

---

## 📜 License and Contribution
This project is free and open to all fellow geeks, nerds, and network enthusiasts. Contributions are not just welcome – they're **encouraged**! Want to add a feature, squash a bug, or suggest improvements? Your ideas are as good as gold pressed latinum.

Drop your pull requests or recommendations, and let’s make this tool the Swiss Army Knife of network analysis. 🛠️

---

## 📬 Contact
Got suggestions? Found a bug? Want to say hi? Open an issue on GitHub or submit a pull request. I’d love to hear from you!

Happy packet hunting! 🖥️⚡
