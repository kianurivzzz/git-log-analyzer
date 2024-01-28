# импортирует модуль subprocess
import subprocess


# класс отвечающий за отображение информации о последних коммитах
class SimpleGit:
    # выбор директории
    def __init__(self, git_dir='.'):
        self.git_dir = git_dir

    # показывает историю изменений
    def show(self, branch='main'):
        return self.command(f'git show {branch}')

    # запускает команду
    def command(self, git_cmd):
        try:
            output = subprocess.check_output(git_cmd, shell=True, stderr=subprocess.STDOUT, text=True)
            return output.strip()
        except subprocess.CalledProcessError as e:
            return e.output.strip()

# корневая директория
git = SimpleGit('.')
commit_info = git.show()
print(commit_info)
