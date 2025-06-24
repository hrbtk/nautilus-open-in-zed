from gi.repository import Nautilus, GObject
from typing import List


class OpenInVSCodeExtension(GObject.GObject, Nautilus.MenuProvider):
    def get_file_items(
        self,
        files: List[Nautilus.FileInfo],
    ) -> List[Nautilus.MenuItem]:
        menu_item = Nautilus.MenuItem(
            name="OpenInVSCodeExtension::OpenInVSCode",
            label="Open in VSCode",
            tip="Open the selected files in Visual Studio Code.",
            icon="vscode",
        )
        menu_item.connect(
            "activate",
            lambda menu_item, files=files: self.open_in_vscode(files),
        )
        return [
            menu_item,
        ]

    def get_background_items(
        self,
        current_folder: Nautilus.FileInfo,
    ) -> List[Nautilus.MenuItem]:
        menu_item = Nautilus.MenuItem(
            name="OpenInVSCodeExtension::OpenInVSCodeBackground",
            label="Open in VSCode",
            tip="Open the current folder in Visual Studio Code.",
            icon="vscode",
        )
        menu_item.connect(
            "activate",
            lambda menu_item, files=current_folder: self.open_in_vscode([files]),
        )
        return [
            menu_item,
        ]

    def open_in_vscode(self, files: List[Nautilus.FileInfo]) -> None:
        import subprocess
        if len(files) == 1 and files[0].is_directory():
            # Open folder in VSCode if only one folder is selected
            folder_path = files[0].get_location().get_path()
            subprocess.run(["code", "-n", folder_path])
        else:
            # Open files in VSCode if multiple files are selected
            file_paths = [file.get_location().get_path() for file in files if not file.is_directory()]
            subprocess.run(["code"] + file_paths)
