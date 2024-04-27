import os
import platform


class Terminator:

    @staticmethod
    def clear():
        # 返回系统平台/OS的名称，如Linux，Windows，Java，Darwin
        system = platform.system()
        if system == "Windows":
            os.system("cls")
        else:
            os.system("clear")
