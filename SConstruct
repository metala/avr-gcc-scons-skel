# Settings
project_name = 'main'

# Variables
vars = Variables('variables.py')
vars.Add('MCU', 'Microcontroller', 'atmega16')
vars.Add('F_CPU', 'CPU frequency in Hz', 8000000)

# Construct script
cppdefines = {
  'F_CPU' : '${F_CPU}UL', 
}

ccflags = [
    '-mmcu=${MCU}',
    '-g',
    '-Os',
    '-w',
    '-fno-exceptions',
    '-ffunction-sections',
    '-fdata-sections',
]

env = Environment(tools = ['winavr'],
                  variables = vars,
                  CCFLAGS = ccflags,
                  CPPDEFINES = cppdefines)

Help(vars.GenerateHelpText(env))

SConscript('src/SConscript',
           variant_dir = 'build',
					 duplicate = 0,
           exports = ['env', 'project_name'])