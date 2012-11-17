"""
Tool-specific initialization for WinAVR (AVR-GCC).

"""

import os
import re
import subprocess

import SCons.Util
import SCons.Tool.cc as cc

__author__ = "Marin Ivanov"
__copyright__ = "Copyright 2012"
__credits__ = ["Valori Ivanov"]
__license__ = "BSD 2-clause"
__version__ = "1.0.0"
__maintainer__ = "Marin Ivanov"
__email__ = "dev@metala.org"
__status__ = "Development"



compiler = 'avr-gcc'
objcopy  = 'avr-objcopy'

def generate(env):
    """Add Builders and construction variables for gcc to an Environment."""
    cc.generate(env)

    env['CC'] = env.Detect(compiler) or 'avr-gcc'
    env['OBJCOPY'] = env.Detect(objcopy) or 'avr-objcopy'
    env['SHCCFLAGS'] = SCons.Util.CLVar('$CCFLAGS')
    env['SPAWN']  = _echospawn
    env['ESCAPE'] = lambda x:x
    env['WINAVR_PATH'] = _detect_winavr()
    #env['CPPPATH'] = env['WINAVR_PATH'] + '\\avr\\include\\avr'
        
    env.Append(BUILDERS = {
        'Elf': _get_elf_builder(),
        'Hex': _get_hex_builder(),
    })

def exists(env):
    return env.Detect(compiler) and env.Detect(objcopy) 


def _detect_winavr():
    import os
    if (os.environ.has_key('AVR32_HOME')):
        return os.environ['AVR32_HOME']

def _echospawn(sh, escape, cmd, args, env):
    return subprocess.call(args)

def _get_elf_builder():
    return SCons.Builder.Builder(action = "$CC -mmcu=${MCU} -Wl,-Map=${TARGET}.map -Os -Xlinker -Map=${TARGET}.map -Wl,--gc-sections -o ${TARGET} ${SOURCES}")
    
def _get_hex_builder():
    return SCons.Builder.Builder(action = "$OBJCOPY -O ihex -R .eeprom $SOURCES $TARGET") 
