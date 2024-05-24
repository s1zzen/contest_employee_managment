class Configuration:
    def __init__(self):
        self.db_path = './db/company.db'
        self.output_dir = './output_files/'

    def get_db_path(self):
        return self.db_path

    def get_output_dir(self):
        return self.output_dir

    def set_db_path(self, db_path):
        self.db_path = db_path

    def set_output_dir(self, output_dir):
        self.output_dir = output_dir
