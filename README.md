# Open Directory in Zed (*WIP*)

Inspired by https://github.com/SimBoi/nautilus-open-in-vscode

An extension for Nautilus, adds a menu item to the right-click directory/background to open folder in Zed. Also works for bulk opening files. Make sure that Zed is in your System Path.

## 🚀 Installation

1. Run in the terminal:
   ```bash
	# 1. install packages
	sudo apt update
	sudo apt install -y git curl python3-nautilus
	# 2. download the extension script
	mkdir -p ~/.local/share/nautilus-python/extensions
	curl -L -o ~/.local/share/nautilus-python/extensions/nautilus-open-in-zed.py https://raw.githubusercontent.com/hrbtk/nautilus-open-in-zed/refs/heads/main/nautilus-open-in-zed.py
	# 3. restart nautilus
	nautilus -q
	```

## 🗑️ Uninstallation

1. Run in the terminal:
	```bash
	rm -f ~/.local/share/nautilus-python/extensions/nautilus-open-in-zed.py
	# restart Nautilus
	nautilus -q
	````
