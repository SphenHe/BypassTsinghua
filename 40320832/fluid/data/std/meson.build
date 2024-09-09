project('fluid-std', 'cpp',
  version : '0.1',
  default_options : ['warning_level=3',
                     'cpp_std=c++17'])

rapidjson = dependency('RapidJSON')
hdf5 = dependency('hdf5', language: 'cpp', required: true)

incdir = include_directories('include/eigen', 'include/misc')

srcs = [
  'src/fluid.cpp'
]

exe = executable('fluid_std', srcs, include_directories: incdir, dependencies: [rapidjson, hdf5])

test('basic', exe)
