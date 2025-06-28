from gi.repository import Nautilus, GObject
from typing import List


class OpenInZedEditorExtention(GObject.GObject, Nautilus.MenuProvider):
    def get_file_items(
        self,
        files: List[Nautilus.FileInfo],
    ) -> List[Nautilus.MenuItem]:
        return self.generate_menu(files, False)

    def get_background_items(
        self,
        current_folder: Nautilus.FileInfo,
    ) -> List[Nautilus.MenuItem]:
        return self.generate_menu([current_folder], True)

    def generate_menu(
        self,
        files: List[Nautilus.FileInfo],
        is_background: bool,
    ) -> List[Nautilus.MenuItem]:
        menu_item = Nautilus.MenuItem(
            name="OpenInZedEditorExtention::OpenInZed" + "Background" if is_background else "",
            label="Open in Zed",
            tip="Open the selected files in Zed Editor.",
            icon="",
        )
        menu_item.connect(
            "activate",
            lambda menu_item, files=files: self.open_in_zed(files),
        )
        return [
            menu_item,
        ]

    def open_in_zed(self, files: List[Nautilus.FileInfo]) -> None:
        import subprocess
        if len(files) == 1 and files[0].is_directory():
            # Open folder in Zed if only one directory is selected
            folder_path = files[0].get_location().get_path()
            subprocess.run(["zed", "-n", folder_path])
        else:
            # Open files in Zed if multiple files are selected, disregarding directories
            file_paths = [file.get_location().get_path() for file in files if not file.is_directory()]
            subprocess.run(["zed"] + file_paths)
