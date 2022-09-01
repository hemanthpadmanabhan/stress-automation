import glob
import os
import platform
import shutil
import tempfile

from conans import ConanFile, CMake, tools

os.environ['CONAN_KEEP_PYTHON_FILES'] = 'True'

class InspectorConan(ConanFile):
    name = 'inspector'
    description = 'Inspector.'
    url = 'https://github.com/intel-innersource/applications.analyzers.inspector.git'

    settings = 'os', 'build_type'
    options = {'package_type': ['unit_tests', 'testing', 'public', 'nda']}

    def package(self):
        package_type = str(self.options.package_type)
        build_dir = os.environ['BUILD_DIR']
        if package_type=="unit_tests":
            self.copy('*', src=os.path.join(build_dir, 'pack', 'product', 'unit_tests'),
                      dst='unit_tests', excludes='tmp|ut_logs|ut_report')
        if package_type=="testing":
            src_dir=glob.glob(os.path.join(build_dir, 'pack', 'product', 'install', '**/TESTING'), recursive=True)[0]
            self.copy('*', src=src_dir, dst='TESTING')
        if package_type in ('public', 'nda'):
            with tempfile.TemporaryDirectory(dir=os.getcwd()) as tmp_path: 
                tools.unzip(os.environ[f'{package_type.upper()}_PACKAGE'], destination=tmp_path, keep_permissions=True)
                self.copy('*', src=tmp_path, dst=f'{package_type}')
