import os


class PathUtil:

    # @staticmethod
    # def get_project_root():
    #     return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def get_project_root():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    @staticmethod
    def get_data_directory(apiSuffix):
        return os.path.join(PathUtil.get_project_root(), 'data', apiSuffix)


    @staticmethod
    def get_success_directory(apiSuffix):
        return os.path.join(PathUtil.get_project_root(), 'data', apiSuffix, 'success.json')


if __name__ == '__main__':
    path = PathUtil.get_project_root()
    print(path)
