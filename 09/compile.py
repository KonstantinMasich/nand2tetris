# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
"""Just a short convenience file to call the supplied Jack compiler."""

import os
import pathlib

TARGET_DIR        = 'Tetris'
FULL_TARGET_DIR   = f'{pathlib.Path().resolve()}/{TARGET_DIR}'
COMPILER_LOCATION = '/home/konstantin/study/nand2tetris/tools'

os.system(f'bash {COMPILER_LOCATION}/JackCompiler.sh {TARGET_DIR}')
