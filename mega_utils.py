from mega import Mega

class MegaUtils:
    def __init__(self, email, password):
        self.mega = Mega()
        self.email = email
        self.password = password
        self.m = self.mega.login(email, password)

    def get_file_links(self, folder_name):
        file_links = []
        for key, value in self.m.get_files().items():
            for key, value in m.get_files().items():
				if "n" in value["a"]:
					file_links.append(value["a"]["n"])
        return file_links

    def download_file(self, file_name, local_path):
        file = self.m.find(file_name)
        self.m.download(file, local_path)

    def remove_file(self, local_path):
        os.remove(local_path)
