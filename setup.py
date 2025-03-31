from cx_Freeze import setup, Executable

executables = [Executable("TrabalhoMain.py")]

setup(
    name = "JUMP OR DIE - with ogres",
    version = "1.0",
    description = "JUMP OR DIE - with ogres app",
    options = {"build_exe": {"packages": ["pygame"]}},
    executables = executables
    )
