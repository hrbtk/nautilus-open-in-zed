# Open Directory in Zed (*WIP*)

Inspired by https://github.com/SimBoi/nautilus-open-in-vscode

An extension for Nautilus, adds a menu item to the right-click directory/background to open folder in Zed. Also works for bulk opening files.

## 🚀 Installation

1. Run in the terminal:
   ```bash
	# 1. install packages
	sudo apt update
	sudo apt install -y git curl python3-nautilus
	# 2. download the extension script
	mkdir -p ~/.local/share/nautilus-python/extensions
	curl -L -o ~/.local/share/nautilus-python/extensions/nautilus-open-in-zed.py https://raw.githubusercontent.com/hrbtk/nautilus-open-in-zed/refs/heads/main/nautilus-open-in-zed.py
	# 3. add Zed to your System Path (if it's not)
	sudo ln -s ~/.local/bin/zed /usr/local/bin/zed
	# 4. restart nautilus
	nautilus -q
	```

## 🗑️ Uninstallation

1. Run in the terminal:
	```bash
	# 1. remove extension
	rm -f ~/.local/share/nautilus-python/extensions/nautilus-open-in-zed.py
	# 2. remove Zed symlink
	sudo unlink /usr/local/bin/zed
	# 3. restart Nautilus
	nautilus -q
	````
