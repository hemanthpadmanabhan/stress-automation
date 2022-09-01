#SCONSTRUCT
# coding=utf-8
# Product component dictionary follows.  Some notes on it:
# The only requierd dictionary element is 'version' which is a string specifying
# a component version  .
#
# For components located in a repository other than 'component' a 'type' element should be
# specified:
#
# 'boost': {'version': '1.55.0.42', 'type': '3rd_parties'}
#
# Some components have names which differ from its repository name for some reasons, to avoid
# warning regarding component name change specify 'name' value in the dictionary:
# 'pin_parts': {'name': 'pin', ...}
#
# Add 'uid':'<path to your uid>' to dictionary of your component to switch svn source location, for example:
# 'my_component': {'version': '3.1.162', 'mode': [], 'uid': 'components/my_component/uid/my_uid/my_component3'},
# in fact, this can be any path, not only uid. E.g you can use it to switch component to the mainline branch.
#
# for git:
# 'mycomponent': {'version': '1.0.0', 'mode': [], 'mainline': 'master', 'uid': 'uid_me',  'vcs': 'git' },
# 'mainline' key in case of git specifies one of masters defaulting to 'master'. In most cases can be omitted
#
# You can also use 'uid':'<local path to your component>' to bind to your local path without going to svn, for example:
# 'my_component': {'version': '3.1.162', 'mode': [], 'uid': 'c:/svn/my_component3'},
#
# If you want to run some UTs during the build add 'run_utest': True to appropriate component dictionary, for example:
# 'my_component': {'version': '3.1.162', 'mode': [], 'uid': 'c:/svn/my_component3', 'run_utest': True},
#
# If you want to specify custom timeout for unit tests run for the component, add 'utest_timeout': <timeout_in_seconds>
# If you want custom timeout for debug mode, specify 'utest_timeout_debug': <timeout_in_seconds>
# Examples:
# 'utest_timeout': 100 - specifies 100s timeout for both debug and release
# 'utest_timeout': 80, 'utest_timeout_debug': 200 - 80s timeout for release and 200s for debug
# 'utest_timeout_debug': 150 - default timeout for release and 150s timeout for debug
#
# If you want  to switch a couple of components from their static versions to the mainline
# (which is a common pattern during feature development), the easiest way to do this is to
# add 'BUILD_BRANCH': 'mainline' elment to the dict:
#
# 'my_component': {'version': '1.1.162', 'BUILD_BRANCH': 'mainline'}
#
# If you want to use component from custom location in the svn repository use 'mainline' element:
# 'my_component': {'version': '1.1.162', 'mainline': 'top/secret/mainline'} # Custom mainline will be used
#

SSBS_INFO = {
    'extract_before_build': {
        'parts': {
            'vcs_type': 'git',
            'vcs_url': 'https://github.com/intel-innersource/applications.analyzers.infrastructure.parts.git',
            'reference': 'v0.11.0.25' },
        'parts-site': {
            'vcs_type': 'git',
            'vcs_url': 'https://github.com/intel-innersource/applications.analyzers.infrastructure.parts-site.git',
            'reference': 'v0.11.0.25' }
    },
    'scons_version': '3.1.2'
}

component_versions = {
    'aggregator': {'version': '3.75.1', 'mode': ['BUILD_FEATURESTAT', 'ENABLE_NEW_SUPP'], 'vcs': 'github'},
    'asdp': {'version': '3.94.1', 'mode': ['ENABLE_NEW_SUPP', 'ENABLE_PROGRESS', 'ENABLE_CPP_DEMANGLER'], 'vcs': 'github'},
    'boost': {'version': '1.75.0.4', 'mode': [], 'vcs': 'github'},
    'ccrt': {'version': '13.15.2', 'mode': ['BUILD_OFFLOAD_SUPPORT'], 'vcs': 'github'},
    'cctrl': {'version': '2.55.4', 'mode': ['BUILD_FEATURESTAT', 'BUILD_USE_FAILED_FROM_FEEDBACK'], 'vcs': 'github'},
    'cfgmgr': {'version': '2.44.7', 'mode': ['BUILD_ENABLE_VARS_SCRIPT','BUILD_ENABLE_NOPOSTFIX_NAMES'], 'vcs': 'github'},
    'cilkabi': {'version': '2.0.2', 'vcs': 'github'},
    'client': {'version': '2.32.27', 'type': 'conf_suite', 'mode':['ENABLE_XE', 'ENABLE_VSDBG', 'ENABLE_FSTAT', 'BUILD_ENABLE_ODLR'], 'vcs': 'github'},
    'clienthelpers': {'version': '1.26.20', 'mode': ['BUILD_COLLECTDLGHELPERS', 'BUILD_FEATURESTAT', 'BUILD_NO_READ_PROJECT_DIRS'], 'vcs': 'github'},
    'clpt': {'version': '3.11.2', 'vcs': 'github'},
    'collectdlg': {'version': '3.41.25', 'mode': ['NONPARALEL_REQUEST'], 'vcs': 'github'},
    'collectunits': {'version': '1.119.3', 'mode': ['TPSS_GEN_IN_VCS_DISABLE','DONOT_BUILD_TPSS_HELPERS'], 'vcs': 'github'},
    'commhelpers': {'version': '1.9.0', 'vcs': 'github'},
    'commondlg': {'version': '3.18.11', 'vcs': 'github'},
    'compiler_libs': {'version': '1.1.14', 'type': '3rd_parties', 'mode': ['ENABLE_OPENMP_RUNTIME'], 'vcs': 'github', 'git_repo': 'compiler-libs.git'},
    'confcli': {'version': '1.12.23', 'mode': ['BUILD_ENABLE_ODLR', 'ENABLE_NEW_SUPP', 'BUILD_FEATURESTAT', 'BUILD_NO_MRTEMODE'], 'vcs': 'github'},
    'configs': {'version': '2.3.8', 'git_repo' : 'confconfigs.git', 'vcs': 'github'},
    'confolh': {'version': '3.0.13', 'name': 'olh', 'vcs': 'github'},
    'confpostinstalldocs': {'version': '5.3.2', 'vcs': 'github'},
    'confpreinstalldocs': {'version': '1.4.0', 'vcs': 'github'},
    'confsamplecode' :  {'version': '1.0.43', 'mode': ['BUILD_HE'], 'vcs': 'github'},
    'cpil': {'version': '2.20.3', 'mode': ['CPIL2_GH2_NULL_POINTER_TO_STRING_SUPPORT', 'CPIL2_UNDEF_U_HACK', 'BUILD_COMPILER_LIBS'], 'vcs': 'github'},
    'cs_eil': {'version': '2.17.50', 'type': 'confhe', 'vcs': 'github', 'git_repo': 'cs-eil.git'},
    'cs_gui_plug': {'version': '2.13.21', 'type': 'confhe', 'mode':['ENABLE_FSTAT'], 'vcs': 'github', 'git_repo': 'cs-gui-plug.git'},
    'curl': {'version' : '7.84.0.1', 'mode': [], 'vcs': 'github'},
    'dbghelp': {'version': '6.11.108', 'type': '3rd_parties', 'vcs': 'github'},
    'dblite': {'version': '1.4.0', 'vcs': 'github'},
    'devutil': {'version': '1.2.83', 'vcs': 'github'},
    'dia': {'version': '14.0.2', 'type': '3rd_parties', 'vcs': 'github'},
    'dnclrprof': {'version': '3.1.3', 'vcs': 'github'},
    'eil': {'version': '1.61.8', 'vcs': 'github'},
    'featurestat': {'version': '1.5.16', 'vcs': 'github'},
    'file_finder': {'version': '2.30.13', 'vcs': 'github', 'git_repo': 'file-finder.git'},
    'formatter': {'version': '5.3.11', 'mode': ['BUILD_ENT_INSTALLS', 'ENABLE_NEW_SUPP', 'BUILD_ENABLE_ODLR'], 'vcs': 'github'},
    'gahelper'   : {'version': '1.2.8', 'vcs': 'github'},
    'ged': {'version': '0.63.2', 'mode' : ['BUILD_INSPXE'], 'vcs': 'github'},
    'gen_helpers': {'version': '2.49.22', 'mode': ['BUILD_NO_JSON'], 'vcs': 'github', 'git_repo': 'gen-helpers.git'},
    'gtpin-parts': {'version': '1.0.7', 'name': 'gtpin', 'vcs': 'github', 'mode': ['BUILD_GTREPLAY']},
    'gui_ut_api': {'version': '1.5.6', 'type': 'component_internal', 'vcs': 'github', 'git_repo': 'gui-ut-api.git'},
    'idvc_base': {'version': '7.5.10', 'vcs': 'github', 'git_repo': 'idvc-base.git'},
    'idvc_frw': {'version': '7.8.3', 'vcs': 'github', 'git_repo': 'idvc-frw.git'},
    'idvc_graph': {'version': '7.0.9', 'vcs': 'github', 'git_repo': 'idvc-graph.git'},
    'idvc_gridctl': {'version': '8.5.5', 'vcs': 'github', 'git_repo': 'idvc-gridctl.git'},
    'idvc_propgrid': {'version': '2.4.5', 'vcs': 'github', 'git_repo': 'idvc-propgrid.git'},
    'idvc_wx': {'version': '7.6.13', 'vcs': 'github', 'git_repo': 'idvc-wx.git'},
    'iga': {'version': '2.15.27', 'mode': ["BUILD_INSPXE"], 'vcs': 'github'},
    'initdqtests': {'version': '1.2.10', 'type': 'component_internal', 'vcs': 'github'},
    'ism': {'version': '3.43.4', 'mode': ['BUILD_CFA', 'BUILD_DWARF_COMPRESSED_SECTIONS_SUPPORT'], 'vcs': 'github'},
    'level_zero': {'version': '1.2.0', 'mode':  [], 'vcs': 'github', 'git_repo': 'level-zero.git'},
    'libunwind': {'version': '0.98.642', 'mainline': 'master_0.98.6', 'vcs': 'github'},
    'libxml': {'version': '2.9.13.0', 'vcs': 'github'},
    'libxslt': {'version': '1.1.35.0', 'type': '3rd_parties', 'vcs': 'github'},
    'log4cplus': {'version': '1.0.4.35', 'vcs': 'github'},
    'lpd': {'version': '2.15.0', 'vcs': 'github'},
    'memorychecker':{'version': '3.15.3', 'mode':['BUILD_ENABLE_THREAD_START', 'BUILD_MC_LOG2', 'BUILD_ENABLE_ODLR', 'BUILD_GPU_SUPPORT'], 'vcs': 'github'},
    'mrtehelpers': {'version': '3.4.15', 'mode': ['BUILD_NO_COLLECTUNITS'], 'vcs': 'github'},
    'mrtesym': {'version': '3.13.17', 'mode': ['BUILD_DEBUG_TOOLS', 'BUILD_JITWRITER_PIN_CRT_USER_LOCKS', 'DISABLE_JITWRITER_PIN_CRT_NATIVE_LOCKS'], 'vcs': 'github'},
    'msngr': {'version': '2.10.11', 'mode': [], 'vcs': 'github'},
    'msngrext': {'version': '1.5.1', 'vcs': 'github'},
    'msngrgui': {'version': '1.0.14', 'vcs': 'github'},
    'panes': {'version': '3.17.7', 'mode':['ENABLE_TIMELINE', 'HE', 'ENABLE_FSTAT', 'ENABLE_NEW_SUPP'], 'vcs': 'github'},
    'pdrdiff': {'version': '3.1.9', 'vcs': 'github'},
    'pin_parts': {'version': '2.5.7', 'name': 'pin', 'mode':['BUILD_VSDEBUGPLUGIN'], 'vcs': 'github', 'git_repo': 'pin-parts.git'},
    'pmeminsp':{'version': '1.1.7', 'mode': ['BUILD_PMEMDEMO_NO_PMDK'], 'vcs': 'github'},
    'qfagent': {'version': '1.11.51', 'vcs': 'github'},
    'qfagentcrashanalyzer': {'version': '1.12.23', 'vcs': 'github'},
    'qfagentfeedback': {'version': '1.13.33', 'mode': ['ENABLE_FSTAT'], 'vcs': 'github'},
    'qfagentgui': {'version': '1.1.26', 'mode': ['ENABLE_FSTAT'], 'vcs': 'github'},
    'qfagentminidump': {'version': '1.20.4', 'vcs': 'github'},
    'rdmgr': {'version': '2.40.10', 'vcs': 'github'},
    'reporter': {'version': '2.7.7', 'git_repo': 'confreporter.git', 'vcs': 'github'},
    'runtool': {'version': '6.25.13', 'mode': ['ENABLE_RUNTC', 'ENABLE_RUNMC', 'BUILD_ENABLE_ODLR'], 'vcs': 'github'},
    'signing': {'version': '1.3.30', 'vcs': 'github'},
    'smip': {'version': '3.31.34', 'mode': ['BUILD_GEN'], 'vcs': 'github'},
    'source_view': {'version': '4.10.5', 'vcs': 'github', 'git_repo': 'source-view.git'},
    'sqlite': {'version': '3.34.1.1', 'vcs': 'github'},
    'stackwalk': {'version': '1.32.2', 'mode': ['BUILD_STACKWALK_CORE'], 'vcs': 'github'},
    'stripchartctrl':{'version': '1.9.39.2', 'ci': False, 'vcs': 'github'},
    'sys_check': {'version': '1.0.8', 'mode': [], 'vcs': 'github', 'git_repo': 'sys-check.git'},
    'tbb': {'version': '2018.4.9', 'vcs': 'github'},
    'tc_dialogs': {'version': '2.43.3', 'mode': ['ENABLE_COLLECTDLG', 'ENABLE_SEARCH_DIR_TABS', 'ENABLE_NEW_SUPP'], 'vcs': 'github', 'git_repo': 'tc-dialogs.git'},
    'tc_engine': {'version': '2.29.0', 'mode': ['ENABLE_DISASSEMBLER', 'ENABLE_KNOBS', 'ENABLE_DIFF', 'ENABLE_DBLAYER', 'ENABLE_FRAME_FILTERS', 'ENABLE_INHERITABLE_STATES'], 'vcs': 'github', 'git_repo': 'tc-engine.git'},
    'tcktests': {'version': '1.2.2', 'vcs': 'github'},
    'tctestdrivers': {'version': '1.3.0', 'vcs': 'github'},
    'threadchecker': {'version': '8.21.2', 'mode': ['BUILD_ENABLE_WHAT_HAPPENS', 'BUILD_ENABLE_TIMESTAMP', 'BUILD_ENABLE_APPDEBUG', 'BUILD_GPU_SUPPORT'], 'vcs': 'github'},
    'ts_cantua_cli_dq': {'version': '1.5.0', 'name': 'cantua_cli_dq', 'vcs': 'github', 'git_repo': 'ts-cantua-cli-dq.git'},
    'ts_cantua_cli_dq_lin': {'version': '1.2.3', 'name': 'cantua_cli_dq_lin', 'vcs': 'github', 'git_repo': 'ts-cantua-cli-dq-lin.git'},
    'ts_cantua_he_gui_dq': {'version': '2.1.240', 'name': 'cantua_he_gui_dq', 'vcs': 'github', 'git_repo': 'ts-cantua-he-gui-dq.git'},
    'ts_cantua_rcat_perf': {'version': '1.0.99', 'name': 'ts_cantua_he_rcat', 'vcs': 'github', 'git_repo': 'ts-cantua-rcat-perf.git'},
    'ts_common': {'version': '1.5.40', 'vcs': 'github', 'git_repo': 'ts-common.git'},
    'ts_cs_helpers': {'version': '5.0.82', 'vcs': 'github', 'git_repo': 'ts-cs-helpers.git'},
    'ts_engine': {'version': '1.6.9', 'vcs': 'github', 'git_repo': 'ts-engine.git'},
    'ts_msaa': {'version': '3.0.2', 'type': 'component_internal', 'vcs': 'github', 'git_repo': 'ts-msaa.git'},
    'ts_panes': {'version': '2.0.6', 'vcs': 'github', 'git_repo': 'ts-panes.git'},
    'ts_ut': {'version': '1.3.0', 'vcs': 'github', 'git_repo': 'ts-ut.git'},
    'ts_vsautomation': {'version': '1.2.13', 'vcs': 'github', 'git_repo': 'ts-vsautomation.git'},
    'tsautomation': {'version': '3.2.4', 'vcs': 'github'},
    'tscsdmperf' : {'version': '1.0.2', 'vcs': 'github'},
    'tsguiengine': {'version': '4.0.38', 'vcs': 'github'},
    'tssourceview': {'version': '1.0.6', 'vcs': 'github'},
    'tswrappers': {'version': '1.1.62', 'vcs': 'github'},
    'tut': {'version': '2.4.6', 'mode': ['BUILD_PIN_TUT'], 'vcs': 'github'},
    'userapi': {'version': '3.24.0', 'mode': ['ENABLE_PKG_ITTNOTIFY', 'BUILD_TPSS_ITTNOTIFY', 'BUILD_ZCA'], 'vcs': 'github'},
    'viewer': {'version': '1.39.66.2', 'mode': [], 'ci': False, 'vcs': 'github'},
    'vssdk': {'version': '11.1.1', 'vcs': 'github'},
    'wx_helpers': {'version': '1.37.13', 'vcs': 'github', 'git_repo': 'wx-helpers.git'},
    'wxwidgets': {'version': '3.0.4.14', 'vcs': 'github'},
    'xed': {'version': '3.3.2', 'ci': False, 'vcs': 'github'},
    'xpti': {'version': '1.2.0', 'mode': ['BUILD_MC_SUBSCRIBER'], 'vcs': 'github'},
    'zlib': {'version': '1.2.1200', 'type': '3rd_parties', 'vcs': 'github'},
}

#   -= End of header =- //please don't remove this comment, it serves as marker for automations

from parts import *
import os
import copy
import collections
import hashlib

# this sets umask to 022 so files won't have group-write permission set
os.umask(0o22)

PrintMessage("Building with Parts", PartVersionString())
if PartsExtensionVersion() < '0.10.10.42':
    PrintError("Error: You must have Parts 0.10.0 or better")
    Exit(1)

PrintMessage("Enabling TCAR Policy Extension")
TcarDefaults()

LocalSetup()
SetOptionDefault('GIT_SERVER','ssh://git@gitlab.devtools.intel.com:29418/')
SetOptionDefault('GIT_CLONE_FLAGS', '--depth=1')


AddOption("--product-variant", "--prod-var",
          dest='product-variant',
          default='he',
          nargs=1,
          type='choice',
          choices=['ms', 'he'],
          action='store',
          help='You can specify the product variant to build. By default "he" is used.')

SetOptionDefault("PRODUCT_VARIANT", GetOption("product-variant"))

AddOption("--css-layout",
          dest='css_layout',
          default=False,
          action="store_true",
          help='Forces CSS layout for install directory')

AddOption("--build-type",
            dest='build-type',
            default='phase',
            nargs=1,
            type='choice',
            choices=['mainline', 'phase', 'ci'],
            action='store',
            help='You can specify mainline or phase build you would like to build')

AddOption("--distributed",
            dest='distributed',
            default=False,
            action="store_true",
            help='Resulting package will use binaries built on other platforms (for example android bits built on linux for windows and macos packages)')

AddOption("--pin-integration",
            dest='pin-integration',
            default=False,
            action="store_true",
            help='Enabling pin integration')

AddOption("--no-utests",
            dest="no-utests",
            default=False,
            action="store_true",
            help="Disabling building utests")

def is_he():
    return GetOption("product-variant") == 'he'

def saveJson(env, target, source):
    import json
    with open(target[0].path, 'w') as f:
        json.dump(env['DATA'], f, indent=4)

def is_ms():
    return GetOption("product-variant") == 'ms'

SetOptionDefault('PAT_VCS_TYPE_MAP',{ 'confhe': 'confhe/components', 'conf_suite_internal' : 'conf_suite/components/_internal'})

SetOptionDefault('LOGGER', '$TEXT_LOGGER')
SetOptionDefault('PART_LOGGER', '$PART_TEXT_LOGGER')
SetOptionDefault('LOG_PART_FILE_NAME', '${PART_NAME}_${PART_VERSION}_${TARGET_PLATFORM}.log')
SetOptionDefault('PARTS_NG_DEPRECATION_HANDLING', 'ignore')


# The compiler_libs component can put only current CRT into package
# so we need to build with current CRT as well
if DefaultEnvironment()['HOST_PLATFORM'] == 'win32-any':
    SetOptionDefault("CPPDEFINES", "_BIND_TO_CURRENT_CRT_VERSION=1")

# When building on Windows 64-bit box, force 32-bit to be native and 64-bit to be cross.
if DefaultEnvironment()['HOST_PLATFORM'] == 'win32-x86_64':
    SetOptionDefault('TARGET_PLATFORM', SystemPlatform(os='win32', arch='x86'))
    DefaultEnvironment()['TARGET_PLATFORM'] = SystemPlatform(os='win32', arch='x86')

# if 32-bit do x86_64 as cross arch build
NativePlatform = DefaultEnvironment()['TARGET_PLATFORM']
if NativePlatform.ARCH == 'x86':
    CrossPlatform = SystemPlatform(arch='x86_64')
    CrossOsBit = 64
    NativeBitness = 32
else:  # assume here this is some 64-bit build x86_64 or ia64 so cross is 32-bit
    CrossPlatform = SystemPlatform(arch='x86')
    CrossOsBit = 32
    NativeBitness = 64

SetOptionDefault('OSBITNESS', NativeBitness)

# The following modes are currently supported:
# * 'none' - the cross-compilation is off (default)
# * 'runtime' - cross-compile the collectors
# * 'cli' - cross-compile the collectors the command line client
# * 'gui' - cross-compile the collectors, command line and GUI clients
#
CROSS_NONE = 'none'
CROSS_DEFAULT = 'default'
CROSS_RUNTIME = 'runtime'
CROSS_CLI = 'cli'
CROSS_GUI = 'gui'


# Define code coverage options

is_code_cov = ARGUMENTS.get('codecov', 'False').lower() in ['true', 't', 'yes', 'y', '1']
SetOptionDefault('IS_CODE_COV', is_code_cov)

if is_code_cov:
    if DefaultEnvironment()['HOST_OS'] == 'posix':
        os_path = 'linux'
    elif DefaultEnvironment()['HOST_OS'] == 'win32':
        os_path = 'windows'
    lib_path_x86 = os.path.join(DefaultEnvironment()['INTELC']['INSTALL_ROOT'], os_path, 'compiler', 'lib', 'ia32')
    lib_path_x86_64 = os.path.join(DefaultEnvironment()['INTELC']['INSTALL_ROOT'], os_path, 'compiler', 'lib', 'intel64')
    SetOptionDefault('CODE_COV_LIBPATH', [lib_path_x86, lib_path_x86_64])
    SetOptionDefault('CODE_COV_LINKFLAGS', ['-Wl,-rpath=' + lib_path_x86, '-Wl,-rpath=' + lib_path_x86_64])
    SetOptionDefault('CODE_COV_LIBS', ['libipgo.a', 'libirc.a', 'libc.a', 'libdl.a'])


def get_cross_mode():
    """Determine the cross-compilation mode from scons arguments"""
    do_cross_val = ARGUMENTS.get('do_cross', None)
    if do_cross_val is None:
        return CROSS_DEFAULT
    do_cross_val = do_cross_val.lower()
    if do_cross_val == 'true':
        return CROSS_DEFAULT
    if do_cross_val == 'false':
        return CROSS_NONE
    return do_cross_val


def get_known_cross_modes():
    """Get the list of all known cross modes"""
    return [CROSS_NONE, CROSS_DEFAULT, CROSS_RUNTIME, CROSS_CLI, CROSS_GUI]

def build_type():
    return GetOption("build-type")

#---------------------------------------------------------------------------
# Define support functions
def ToolchainContains(user_toolchain, t):
    if user_toolchain is not None:
        for c in user_toolchain:
            if c[0] == t:
                return True
    return False


def GetToolchain():
    user_toolchain = GetOption('tool_chain')
    if user_toolchain is None:
        tc = ARGUMENTS.get('toolchain', None)
        if tc is not None:
            PrintError("Unsupported option toolchain: Use the --tc option instead")
    return user_toolchain

#----------------------------------------------------------------------------
# If the user sets the toolchain, *that* is the toolchain for most components
user_toolchain = GetToolchain()

if NativePlatform == 'win32':
    def_native_ver =  '15.0'
    def_intel_ver  = '19.0.228'
    def_collector_ver = '15.0'
    def_vssdk_ver = '15.0'  # no way to specify this from command-line
    if ToolchainContains(user_toolchain, 'cl') or ToolchainContains(user_toolchain, 'mstools'):
        def_native_ver = DefaultEnvironment()['MSVC_VERSION']
    if ToolchainContains(user_toolchain, 'icl'):
        def_intel_ver = DefaultEnvironment()['INTELC_VERSION']
    if ToolchainContains(user_toolchain, 'vssdk'):
        def_vssdk_ver = DefaultEnvironment()['VSSDK_VERSION']
elif NativePlatform == 'posix':
    def_native_ver = '6.3'
    def_intel_ver = '19.1.2'
    if is_code_cov:
        def_intel_ver = '19.1.2'
    def_collector_ver =  '6.3'
    def_vssdk_ver = '0.0'  # not used on POSIX platforms
    if ToolchainContains(user_toolchain, 'gcc') or ToolchainContains(user_toolchain, 'gnutools'):
        def_native_ver = DefaultEnvironment()['GCC_VERSION']
    if ToolchainContains(user_toolchain, 'icl'):
        def_intel_ver = DefaultEnvironment()['INTELC_VERSION']
    SetOptionDefault('FORCE_PIE', True)

SetOptionDefault('USE_WINDOWSKIT_VERSION', '10.0.17763.0')

# The new binutils are needed for the 12.1 (and newer) compiler builds.
binutils = ['binutils_2.28']

# Default toolchains to use if the user does not specify one.
#  The default release toolchain is: icl_11.1,mstools_9.0 or gnutools_4.1
#  The default debug toolchain is: cl_9.0 or gcc_4.1
tchain_dict = {
    'win32': {'debug': ['cl_' + def_native_ver],
              'release': ['icl_' + def_intel_ver, 'mstools_' + def_native_ver],
              'codecov': ['icl_' + def_intel_ver, 'mstools_' + def_native_ver]
              },
    'posix': {'debug': ['gcc_' + def_native_ver] + binutils,
              'release': ['icl_' + def_intel_ver, 'gnutools_' + def_native_ver] + binutils,
              'codecov': ['icl_' + def_intel_ver, 'gnutools_' + def_native_ver] + binutils
              }
}
collect_dict = {
    'win32': {  'debug'   : ['cl_' + def_collector_ver],
                'release' : ['cl_' + def_collector_ver],
                'codecov' : ['cl_' + def_collector_ver]
                },
    'posix': {  'debug'   : ['gcc_'+ def_collector_ver] + binutils,
                'release' : ['gcc_'+ def_collector_ver] + binutils,
                'codecov' : ['gcc_'+ def_collector_ver] + binutils
                }
    }

vssdk_dict = {
    'win32': {'debug': ['cl_' + def_native_ver, 'vssdk_' + def_vssdk_ver],
              'release': ['cl_' + def_native_ver, 'vssdk_' + def_vssdk_ver],
              'codecov': ['cl_' + def_native_ver, 'vssdk_' + def_vssdk_ver]
              },
    'posix': {'debug': ['gcc_' + def_native_ver] + binutils,
              'release': ['icl_' + def_intel_ver, 'gnutools_' + def_native_ver] + binutils,
              'codecov': ['icl_' + def_intel_ver, 'gnutools_' + def_native_ver] + binutils
              }
}

if is_code_cov:
    tchain_idx = 'codecov'
elif DefaultEnvironment().isConfigBasedOn('release'):
    tchain_idx = 'release'
else:
    tchain_idx = 'debug'
    if not DefaultEnvironment().isConfigBasedOn('debug'):
        PrintWarning("Unknown configuration: Defaulting to debug toolchain")

collector_tchain = collect_dict[NativePlatform.OS][tchain_idx]
vssdk_tchain = vssdk_dict[NativePlatform.OS][tchain_idx]
if user_toolchain is None:
    user_toolchain = tchain_dict[NativePlatform.OS][tchain_idx]

# Setting the current toolchain after determining it
SetOptionDefault('toolchain', user_toolchain)

# When compiling with Microsoft compiler we want to enable some warnings on
# our level 3 to make sure that builds by Microsoft compiler generate close set
# of warnings:
#
# C4189 'variable' : local variable is initialized but not referenced
# C4263 'function': member function does not override any base class virtual member function
#
if ToolchainContains(user_toolchain, 'cl'):
    SetOptionDefault('CPPFLAGS', ['-w3 4189', '-w3 4263'])
else:
# Intel compiler #2586 warning suppressed because it affects only debug information
    SetOptionDefault('CPPFLAGS', [
        '${CC == "icl" and (TARGET_OS == "win32" and ["/Qwd2586"] or ["-wd2586"]) or []}'
    ])

SetDefaultInstallArguments('CONFIG', allow_duplicates=True)
SetDefaultInstallArguments('MESSAGE', allow_duplicates=True)
SetDefaultInstallArguments('RESOURCE', allow_duplicates=True)
SetDefaultInstallArguments('TOP_LEVEL', allow_duplicates=True)

if str(Platform()) == 'posix':
    SetOptionDefault('CXXFLAGS', ['-std=c++14'])
else:
    SetOptionDefault('CXXFLAGS', ["${INTELC.VERSION and ['/Qstd=c++14'] or []}"])

# Create PDB by default
SetOptionDefault('PDB', '${TARGET.name}.pdb')

SetOptionDefault('AUTO_TAG_INSTALL', [('*.pdb', ConfigValues(no_package=True))])

# TODO: These need to be updated to follow CSS guidelines.  See
# http://pat.intel.com/wiki/Common_Architecture_Issues_AGREED#Switching_products_to_CSS-compliant_directory_layout


class CSS_DIR(object):

    def __call__(self, target, source, env, for_signature):
        host = ""
        arch = ""
        if env['TARGET_OS'] not in ['win32', 'posix'] or env['HOST_OS'] != env['TARGET_OS']:
            host = env['TARGET_OS']
        if env['TARGET_ARCH'] == 'x86':
            arch = 'ia32'
        elif env['TARGET_ARCH'] == 'x86_64':
            arch = 'intel64'
        else:
            arch = env['TARGET_ARCH']
        if host != "":
            return "{0}-{1}".format(host, arch)
        else:
            return arch

SetOptionDefault('CSS_DIR', CSS_DIR)


if GetOption('css_layout'):
    SetOptionDefault('INSTALL_BIN', '${INSTALL_ROOT}/bin/${CSS_DIR()}')
    SetOptionDefault('INSTALL_LIB', '${INSTALL_ROOT}/lib/${CSS_DIR()}')
    SetOptionDefault('INSTALL_ROOT', '#install/${CONFIG}')
    SetOptionDefault('INSTALL_PYTHON', '${INSTALL_ROOT}/lib/python')
    SetOptionDefault('INSTALL_SCRIPT', '${INSTALL_ROOT}/bin')
else:

    SetOptionDefault('INSTALL_BIN', '${INSTALL_ROOT}/bin${OSBITNESS}')
    SetOptionDefault('INSTALL_LIB', '${INSTALL_ROOT}/lib${OSBITNESS}')
    SetOptionDefault('INSTALL_ROOT', '#install')
    SetOptionDefault('INSTALL_PYTHON', '${INSTALL_ROOT}/lib${OSBITNESS}/python')
    SetOptionDefault('INSTALL_SCRIPT', '${INSTALL_ROOT}')

# these are not the part default...might cause build issue some day.
SetOptionDefault('BUILD_DIR_ROOT', '#build')
SetOptionDefault('CHECK_OUT_ROOT', '#vcs')
SetOptionDefault('SDK_ROOT', '#sdks/${CONFIG}_${TARGET_PLATFORM}/${PART_ROOT_NAME}_${PART_VERSION}')
SetOptionDefault('UNIT_TEST_ROOT', '#unit_tests')

SetOptionDefault('PRODUCT_LEGAL_NOPOSTFIX_TM_NAME', u"Intel\N{REGISTERED SIGN} Inspector".encode('utf-8'))
SetOptionDefault('PRODUCT_LEGAL_NOPOSTFIX_NAME', "Intel(R) Inspector")
SetOptionDefault('PRODUCT_LEGAL_NOPOSTFIX_NOTM_NAME', "Intel Inspector")
SetOptionDefault('PRODUCT_LEGAL_NOPOSTFIX_SHORT_NAME', "Inspector")

if is_he():
    SetOptionDefault('PRODUCT_COPYRIGHT_STRING', u"Copyright \N{COPYRIGHT SIGN} 2009-2022 Intel Corporation. All rights reserved.".encode('utf-8'))
    SetOptionDefault('PRODUCT_COPYRIGHT_ASCII_STRING', "Copyright (C) 2009-2022 Intel Corporation. All rights reserved.")
    SetOptionDefault('FULL_INTEL_COPYRIGHT', '''
  ${PRODUCT_COPYRIGHT_STRING}

  The information contained herein is the exclusive property of
  Intel Corporation and may not be disclosed, examined, or reproduced in
  whole or in part without explicit written authorization from the Company.
'''
                     )
    SetOptionDefault('XML_HEADER', '\n<!--\n$FULL_INTEL_COPYRIGHT\n-->\n')

    SetOptionDefault('PRODUCT_LEGAL_NAME', u"Intel\N{REGISTERED SIGN} Inspector 2022.3".encode('utf-8'))
    SetOptionDefault('PRODUCT_LEGAL_ASCII_NAME', "Intel(R) Inspector 2022.3")
    SetOptionDefault('PRODUCT_LEGAL_NOTM_NAME', "Intel Inspector 2022.3")
    SetOptionDefault('PRODUCT_DESCRIPTIVE_ASCII_NAME', "Intel(R) Inspector 2022.3")
    SetOptionDefault('PRODUCT_LEGAL_SHORT_NAME', "Inspector")
    PRODUCT_ABBR = 'inspxe'
    SetOptionDefault('PRODUCT_ABBR', PRODUCT_ABBR)
    SetOptionDefault('PRODUCT_EXE_PREFIX', '%s-' % PRODUCT_ABBR)
    SetOptionDefault('PRODUCT_LIB_PREFIX', '%s_' % PRODUCT_ABBR)
    # name of cl binary
    SetOptionDefault('PRODUCT_CL_TOOL_NAME', '%s-cl' % PRODUCT_ABBR)

    SetOptionDefault('PACKAGE_TYPE', 'ENT')
    SetOptionDefault('PRODUCT_VERSION', '2022.3.0')
    SetOptionDefault('PRODUCT_VERSION_STRING', "")
    SetOptionDefault('INSTALL_DIR_VARIABLE', 'INSPECTOR_2022_DIR')
    PACKAGE_NAME = 'inspector_2022.3'
    PACKAGE_VERSION = '1.0.0'
    SetOptionDefault('PACKAGE_NAME', 'inspector_2022.3')
    SetOptionDefault('PACKAGE_VERSION', '1.0.0')  # TODO: deprecate, use PACKAGE_NAME only
    INTERNAL_PRODUCT_NAME_FOR_REPORTS = 'CantuaHE_master'  # Don't add Beta of Gold tags for mainline

elif is_ms():
    SetOptionDefault('PRODUCT_COPYRIGHT_STRING', u"Copyright \N{COPYRIGHT SIGN} 2008-2022 Intel Corporation. All rights reserved.".encode('utf-8'))
    SetOptionDefault('PRODUCT_COPYRIGHT_ASCII_STRING', "Copyright (C) 2008-2022 Intel Corporation. All rights reserved.")
    SetOptionDefault('FULL_INTEL_COPYRIGHT', '''
  ${PRODUCT_COPYRIGHT_STRING}

  The information contained herein is the exclusive property of
  Intel Corporation and may not be disclosed, examined, or reproduced in
  whole or in part without explicit written authorization from the Company.
'''
                     )
    SetOptionDefault('XML_HEADER', '\n<!--\n$FULL_INTEL_COPYRIGHT\n-->\n')

    SetOptionDefault('PRODUCT_LEGAL_NAME', u"Intel\N{REGISTERED SIGN} Parallel Inspector 2011".encode('utf-8'))
    SetOptionDefault('PRODUCT_LEGAL_ASCII_NAME', "Intel(R) Parallel Inspector 2011")
    SetOptionDefault('PRODUCT_LEGAL_NOTM_NAME', "Intel Parallel Inspector 2011")
    SetOptionDefault('PRODUCT_LEGAL_SHORT_NAME', "Inspector")
    SetOptionDefault('PRODUCT_ABBR', 'insp')
    SetOptionDefault('PRODUCT_EXE_PREFIX', 'insp-')
    SetOptionDefault('PRODUCT_LIB_PREFIX', 'insp_')
    SetOptionDefault('PACKAGE_TYPE', 'MNS')
    SetOptionDefault('PRODUCT_VERSION', '11.0.7')
    SetOptionDefault('PRODUCT_VERSION_STRING', "Update 7")
    PACKAGE_NAME = 'cantua_update7'
    PACKAGE_VERSION = '2.0.0'
    SetOptionDefault('PACKAGE_NAME', 'cantua_update7')
    SetOptionDefault('PACKAGE_VERSION', '2.0.0')  # TODO: deprecate, use PACKAGE_NAME only
    INTERNAL_PRODUCT_NAME_FOR_REPORTS = 'Cantua_5'

SetOptionDefault('PACKAGE_LEGAL_TYPE', '')
SetOptionDefault('PRODUCT_VERSION_PHASE', '')
# This part of the product layout is per CSS
SetOptionDefault('INSTALL_DOC', '${INSTALL_ROOT}/documentation')
SetOptionDefault('INSTALL_HELP', '${INSTALL_DOC}')
SetOptionDefault('INSTALL_SAMPLE', '${INSTALL_ROOT}/samples')

SetOptionDefault('ALIAS_POSTFIX', '_${TARGET_ARCH}')

# Environment for unit testing infrastructure
if PartsExtensionVersion() < '0.10.1':
    SetOptionDefault('UNIT_TEST_ENV', {'COMPONENT_UNDER_UT': '${PART_ROOT_NAME}_${PART_SHORT_VERSION}',
                                       'UT_LOG_FILE': '${ABSPATH("$UNIT_TEST_ROOT")}/ut_logs/${UNIT_TEST_TARGET_NAME}_${TARGET_ARCH}.log',
                                       'TS_PRODUCT_UNDER_TEST': INTERNAL_PRODUCT_NAME_FOR_REPORTS, 'PROF_DIR': '${ABSPATH("$UNIT_TEST_ROOT/..")}/code_coverage/prof_dir',
                                       'TS_SCENARIO_NAME': '${UNIT_TEST_TARGET_NAME}_${TARGET_ARCH}',
                                       'INTEL_DISABLE_FEEDBACK': '1'})
else:
    SetOptionDefault('UNIT_TEST_ENV', {'COMPONENT_UNDER_UT': '${PART_ROOT_NAME}_${PART_SHORT_VERSION}',
                                       'UT_LOG_FILE': '${RELPATH("UNIT_TEST_ROOT", "UNIT_TEST_DIR")}ut_logs/${UNIT_TEST_TARGET_NAME}_${TARGET_ARCH}.log',
                                       'TS_PRODUCT_UNDER_TEST': INTERNAL_PRODUCT_NAME_FOR_REPORTS, 'PROF_DIR': '${RELPATH("UNIT_TEST_ROOT", "UNIT_TEST_DIR")}../code_coverage/prof_dir',
                                       'TS_SCENARIO_NAME': '${UNIT_TEST_TARGET_NAME}_${TARGET_ARCH}',
                                       'INTEL_DISABLE_FEEDBACK': '1'})
SetOptionDefault('RUN_UTEST_TIME_OUT', 300)

# Produce debug information on linux
if HostPlatform() == 'posix-any':
    SetOptionDefault('CCFLAGS', '-g')

# Compiler defenses options set.
if DefaultEnvironment().isConfigBasedOn('release'):
    if HostPlatform() == 'posix-any' or HostPlatform() == 'darwin':
        if is_code_cov:
            SetOptionDefault('CC_COMPILERDEFENSES', ['${INTELC.VERSION >= "12.1" and ["-Wformat", "-Wformat-security"] or []}'])
        else:
            SetOptionDefault('CC_COMPILERDEFENSES', ['${INTELC.VERSION >= "12.1" and ["-D_FORTIFY_SOURCE=2", "-Wformat", "-Wformat-security"] or []}'])
        SetOptionDefault('CPP_COMPILERDEFENSES', ['${[]}'])
        if HostPlatform() == 'darwin':
            SetOptionDefault('LINK_COMPILERDEFENSES', ['${[]}'])
        else:
            SetOptionDefault('LINK_COMPILERDEFENSES', ['${INTELC.VERSION >= "12.1" and ["-z", "noexecstack", "-z", "relro", "-z", "now"] or []}'])
    else: # Windows case
        SetOptionDefault('CC_COMPILERDEFENSES', ['${[]}'])
        SetOptionDefault('CPP_COMPILERDEFENSES', ['${INTELC.VERSION >= "12.1" and ["/DYNAMICBASE"] or []}'])
        SetOptionDefault('LINK_COMPILERDEFENSES', ['${[]}'])

# Install subdirectory for test components
SetOptionDefault('TS_INSTALL_ROOT', 'TESTING')

# Install subdirectory for kernel test components
SetOptionDefault('TS_KERNEL_TEST_ROOT', '${TS_INSTALL_ROOT}/kernel_tests')

packages_info = dict()
packages_info['he'] = {"package": 'he-${TARGET_OS}-any', "sufix": ""}


def create_default_product_info(**kw):
    out = dict()
    if str(Platform()) == 'win32':
        out['PRODUCT_DEFAULT_PROJECT_DIR_NAME'] = "Inspector"
    else:
        out['PRODUCT_DEFAULT_PROJECT_DIR_NAME'] = "insp"

    out['BUILD_MARKER_FILE_INFO'] = {}
    out['BUILD_SET_INSTALL_DIR_VAR'] = "INSPECTOR_2022_DIR"

    return out


def get_addendum_product_info(name, **kw):
    out = create_default_product_info(**kw)
    out['BUILD_DEFAULT_ADDENDUM'] = False
    out['PRODUCT_WEB_HELP_URL_BASE'] = ""
    out['BUILD_FORCE_USE_32_BIT_PATH'] = True

    windowsDirName = None
    posixDirName = None
    if name == 'he':
        # this is temporary function.
        # It should be rewritten when following variables in SConstruct will stop be used.
        var_names = [
            'PRODUCT_LEGAL_SHORT_NAME',
            'PRODUCT_VERSION_STRING'
        ]
        for var_name in var_names:
            out[var_name] = DefaultEnvironment()[var_name]

        out['PACKAGE_VERSION'] = DefaultEnvironment()['PRODUCT_VERSION']

        productLegalName = DefaultEnvironment()['PRODUCT_LEGAL_NAME'].decode('utf-8') + "%s"
        productLegalNoTmName = DefaultEnvironment()['PRODUCT_LEGAL_NOTM_NAME'] + "%s"
        productLegalAsciiName = DefaultEnvironment()['PRODUCT_LEGAL_ASCII_NAME'] + "%s"
        out['BUILD_DEFAULT_ADDENDUM'] = True
        out['PRODUCT_PHONE_HOME_KEY'] = "inspxe"

    else:
        PrintError("Unsupported addendum name " + name)

    if 'BUILD_MARKER_FILE_INFO' in out:
        if NativePlatform  == 'win32' and windowsDirName != None:
            out['BUILD_MARKER_FILE_INFO'].update({'pntDefaultSettingsDirName':windowsDirName,
                                                  'pntDefaultProjectDirName':windowsDirName})
        elif (NativePlatform  == 'posix' or NativePlatform  == "darwin") and posixDirName != None:
            out['BUILD_MARKER_FILE_INFO'].update({'pntDefaultSettingsDirName':posixDirName,
                                                  'pntDefaultProjectDirName':posixDirName})
        out['BUILD_MARKER_FILE_INFO'].update({"productLeagalNameAddendum":"Memory and Thread Debugging"})
    else:
        out['BUILD_MARKER_FILE_INFO'] ={"productLeagalNameAddendum":"Memory and Thread Debugging"}

    if 'PACKAGE_VERSION' in out:
        out['PRODUCT_VERSION'] = out['PACKAGE_VERSION']

    out['BUILD_ADDENDUM_SUFIX'] = out['BUILD_ADDENDUM_SUFFIX'] = packages_info[name]['sufix']
    out['BUILD_ADDENDUM_PACKAGE'] = packages_info[name]['package']

    version = out['PRODUCT_VERSION_STRING']
    if version != "":
        version = " " + version
    out['PRODUCT_LEGAL_NAME'] = (productLegalName % "").encode('utf-8')
    out['PRODUCT_LEGAL_NOTM_NAME'] = productLegalNoTmName % ""
    out['PRODUCT_LEGAL_ASCII_NAME'] = productLegalAsciiName % ""
    out['PRODUCT_DESCRIPTIVE_NAME'] = (productLegalName % version).encode('utf-8')
    out['PRODUCT_DESCRIPTIVE_NOTM_NAME'] = productLegalNoTmName % version
    out['PRODUCT_DESCRIPTIVE_ASCII_NAME'] = productLegalAsciiName % version

    return out

# Default packages to include into the installation
# This list is extended below if cross-compilation is requested
def_pkg = ['gui-'+str(NativePlatform),
           'cli-'+str(NativePlatform),
           'doc-${TARGET_OS}-any',
           'common-'+str(NativePlatform),
           'gui_common-${TARGET_OS}-any',
           'cli_common-${TARGET_OS}-any',
           'nda-${TARGET_PLATFORM}',
           # addendums
           packages_info['he']['package']
           ]
vsix_pkg = 'vs_extension-${TARGET_PLATFORM}'

if NativePlatform == 'win32-x86':
    def_pkg.append(vsix_pkg)

# Defining product_info
product_info = dict()
for x in ['he']:
    product_info[x] = get_addendum_product_info(x)

# The ReplacePackageGroupCriteria is used to specify that config files
# and message catalogs should get put into the "noarch" packages even
# if the rest of the files in the Part are going into one of the
# architecture specific packages.


def cli_filter(node, packge_cat):
    return (MetaTagValue(node, 'category', 'package') == packge_cat and
           (MetaTagValue(node, 'group', 'package').startswith('cli-')))


def gui_filter(node, packge_cat):
    ret = (MetaTagValue(node, 'category', 'package') == packge_cat and
          (MetaTagValue(node, 'group', 'package').startswith('gui-')))
    return ret

# A helper for recognizing nodes with certain installation path


def target_path_filter(node, path_glob, pkg_group_glob='*'):
    import fnmatch
    ret = fnmatch.fnmatch(str(node), path_glob) \
        and fnmatch.fnmatch(MetaTagValue(node, 'group', 'package'), pkg_group_glob)
    return ret

ReplacePackageGroupCriteria('cli_common-${TARGET_OS}-any',
                            [lambda x: cli_filter(x, 'CONFIG'),
                             lambda x: cli_filter(x, 'MESSAGE'),
                             lambda x: target_path_filter(x, r'*[/\]support.txt'),
                             lambda x: target_path_filter(x, r'*[/\]*genvars.sh')])
ReplacePackageGroupCriteria('gui_common-${TARGET_OS}-any',
                            [lambda x: gui_filter(x, 'CONFIG'),
                             lambda x: gui_filter(x, 'MESSAGE'),
                             lambda x: HasPackageCatagory('RESOURCE')(x) and not target_path_filter(x, r'*[/\]pindata[/\]*')])

# NB! in NDA package now used 1 no usable txt file for NDA package placeholder creation,
#     if real files will need to go to NDA this stub_nda_file.txt should be removed from packaging
#     and !!!removed!!! from packaging in !!!discdqtests!!! component
ReplacePackageGroupCriteria('nda-${TARGET_PLATFORM}', [lambda x: x.name == 'stub_nda_file.txt'])

def InstallConfigFiles(env, src_files, sub_dir, package_info = None):
    return env.InstallConfig(src_files, sub_dir = sub_dir)

def configurePinCrt(env, configure_libs=True, configure_headers=True):
    try:
        # Check if this env object already has dependency on 'pin.py_configure' part
        env['PIN_CONFIGURE_PYTHON_FILE']
    except KeyError:
        # if there is no dependency, then add it
        env.DependsOn([env.Component('pin.py_configure', requires=
                                        requirement.REQ.PIN_CONFIGURE_PYTHON_FILE(public=True, internal=True) |
                                        requirement.REQ.PIN_RELEASE(public=True, internal=True))])

    # load configurePinCrt() function from PIN's python file
    new_locals = {}
    exec(env.File('${PIN_CONFIGURE_PYTHON_FILE}').get_text_contents(), globals(), new_locals)
    configurePinCrtFunc = new_locals['configurePinCrt'] #name of function in imported python file

    # execute it
    configurePinCrtFunc(env, configure_libs, configure_headers)

import re
def GetProductVersionYearStr(env):
    main_ver = re.sub(r'\..', '', env['PRODUCT_VERSION'])
    return main_ver if len(main_ver) > 2 else '20' + main_ver


def Component(name, cross_suffix='', alias=None, parts_file=None,
    mode=[], suffix=None, vcs_type=None, first=True, **kw):
    '''
    Function used to define components in the SConstruct file.
    It picks up most parameters from from component_versions dictionary
    but they can be specified as the arguments as well.
    '''
    alias = alias or (name + cross_suffix)
    component_definition = component_versions[name]

    comp_static_major_version = (component_definition['version']).split('.')[0]
    type = component_definition.get('type') or 'component'
    parts_file = parts_file or (name + '.parts')

    if component_definition.get('run_utest') and not GetOption('clean'):
        run_utest = 'run_utest::name::{0}::'.format(
                component_definition.get('name') or name)
        if not run_utest in BUILD_TARGETS:
            BUILD_TARGETS.append(run_utest)
    build_type = GetOption("build-type")
    vcs_type_name = component_definition.get('vcs', 'git')
    if 'uid' in component_definition and os.path.isabs(component_definition['uid']):
        #for local filesystem uids
        uid = component_definition['uid']
        parts_file = os.path.relpath(uid)
    elif not vcs_type:
        if vcs_type_name.startswith('git'):
            git_branch = None
            git_tag = None
            if 'uid' in component_definition:
                git_branch = component_definition['uid']
            elif build_type == 'ci' and component_definition.get('ci', True):
                git_branch = component_definition.get('mainline', 'master')
            elif build_type == 'mainline':
                git_branch = component_definition.get('mainline', 'master')
            else:
                git_tag = 'v' + component_definition['version']
            if 'VCS_GIT_DIR' not in kw:
                kw['VCS_GIT_DIR'] = '${{CHECK_OUT_ROOT}}/{0}{1}'.format(name, comp_static_major_version)
            repo = component_definition.get('git_repo', '%s.git' % name)
            if vcs_type_name == 'git':
                repo_location = component_definition.get('repo_location', 'DeveloperProducts/Analyzers/Components')
                vcs_type = VcsGit(repo_location + '/' + repo, branch=git_branch, tag=git_tag)
            elif vcs_type_name == 'github':
                repo_location = component_definition.get('repo_location', 'intel-innersource/applications.analyzers.components')
                vcs_type = VcsGit(repo_location + '.' + repo, server='https://github.com/', branch=git_branch, tag=git_tag)
            else:
                PrintError('Unknown git vcs %s for component %s' % (vcs_type_name, name))

            if suffix:
                parts_file = os.path.join(suffix, parts_file)
        else:
            PrintError('Unknown vcs %s for component %s' % (vcs_type_name, name))

    try:
        kw['RUN_UTEST_TIME_OUT'] = component_definition['utest_timeout']
    except KeyError:
        pass
    if DefaultEnvironment().isConfigBasedOn('debug'):
        try:
            kw['RUN_UTEST_TIME_OUT'] = component_definition['utest_timeout_debug']
        except KeyError:
            pass

    return Part(
            name=component_definition.get('name') or name,
            alias=alias, parts_file=parts_file, vcs_type=vcs_type,
            mode=mode + component_definition.get('mode', []),
            configurePinCrt=configurePinCrt,
            InstallConfigFiles=InstallConfigFiles,
            InstallGeneratedConfigFiles=InstallConfigFiles,
            GetProductVersionYearStr=GetProductVersionYearStr,
            **kw
            )

# components
def tut_grp(**kw):
    cross_suffix=kw.get('cross_suffix', '')
    Component('tut', toolchain=collector_tchain, **kw)

def documentation_grp(version='enterprise', **kw):

    if HostPlatform() == 'win32-any':
        DOC_OS = 'windows'
    else:
        DOC_OS = 'linux'

    Component('confolh', parts_file='olh.parts',
        suffix='export/{0}/{1}'.format(DOC_OS, version),
        platform_independent=True,
         **kw)

    Component('confpreinstalldocs',
        suffix='export',
        BUILD_CONFPREINSTALLDOCS_CONFIG=packages_info,
        DOC_VARIANT=version,
        **kw)
    Component('confpostinstalldocs',
        suffix='export/{0}/{1}'.format(DOC_OS, version),
        parts_file='post_install_docs.parts',
        BUILD_CONFPOSTINSTALLDOCS_CONFIG=packages_info,
        **kw)

    Component('confsamplecode',
         BUILD_CONFSAMPLECODE_CONFIG=packages_info,
         **kw)

def common_infra(cross_mode='', **kw):
    '''
    Components that are needed in all the code groups (ie collectors, cli, and GUIs)
    '''
    #import pdb; pdb.set_trace()
    cross_suffix=kw.get('cross_suffix', '')

    for component_name in ['compiler_libs', 'tbb', 'zlib', 'libxml', 'msngr']:
        Component(component_name, **kw)

    Component(
        'boost',
        parts_file='boost.parts',
        **kw
    )

    Component(
        'cpil',
        parts_file='src/cpil2.parts',
        prepend={'CPPDEFINES': ['PAT_ASSERT']},
        **kw
    )

    mrte_runtime_only = (cross_suffix != '') and cross_mode == CROSS_RUNTIME

    Component(
        'collectunits',
        toolchain=collector_tchain,
        mode=['BUILD_RUNTIME_ONLY', 'DONOT_BUILD_UNIT_TESTS'] if mrte_runtime_only else [],
        **kw
    )

    Component(
        'level_zero',
        **kw
    )

    Component(
        'mrtesym',
        toolchain_runtime=collector_tchain,
        **kw
    )

    if HostPlatform() == 'win32-any':
        Component(
            'dbghelp',
            **kw
        )

        Component(
            'dia',
            **kw
        )

        Component(
            'mrtehelpers',
            mode=['BUILD_RUNTIME_ONLY'] if mrte_runtime_only else [],
            **kw
        )

        Component('dnclrprof',
            PRODUCT_CLRPROF_GUID='InspxeClrProfGuid', default=True,
            **kw)

    Component('cfgmgr', CFGMGR_BUILD_PRODUCT_INFO=product_info, BUILD_EXPERIMENTAL_FEATURE_SET=None, **kw)


def messed_up_stuff(alias_ext='', **kw):
    '''
    These component have a broken design in that the CLI has to use them... but
    they also need the whole GUI, so unlike the infra group with is GUI free,
    this stuff is not.
    '''

    # component has interfaces needed in 64-bit and 32-bit cases, but only
    # build 32-bit because of VSIP implementation code internally
    Component(
        'eil',
        parts_file   ='src/eil.parts',
        VSSDK_TOOLCHAIN    =vssdk_tchain,
        **kw
    )

    if kw.get('OSBITNESS', None) == 32:
        Component(
            'vssdk',
            toolchain    =vssdk_tchain,
            **kw
        )


def data_model_grp(**kw):
    Component(
        'file_finder',
        **kw
    )

    for component_name in ['iga', 'ged', 'smip', 'qfagentfeedback', 'qfagentminidump', 'qfagentcrashanalyzer', 'stackwalk',
                           'sqlite', 'commhelpers', 'rdmgr', 'cctrl', 'tc_engine', 'msngrext', 'tscsdmperf', 'sys_check']:
        Component(component_name, **kw)
    Component('dblite', suffix='src', **kw)
    Component('asdp', parts_file='src/asdp.parts', **kw)

    Component('formatter', parts_file='src/formatter.parts',
        append=dict(
        CCFLAGS=['$CC_COMPILERDEFENSES'],
        CPPFLAGS=['$CPP_COMPILERDEFENSES'],
        LINKFLAGS=['$LINK_COMPILERDEFENSES']
        ),
        **kw)
    Component('aggregator', parts_file='src/aggregator.parts', **kw)


def infra_grp(**kw):

    for component_name in ['libxslt', 'clpt', 'featurestat', 'userapi']:
        Component(component_name, **kw)

    Component('gahelper', GA_TRACKING_ID='UA-17808594-21', **kw)

    Component('lpd',
        toolchain_runtime=collector_tchain,
        **kw)

    Component('gen_helpers', parts_file='src/gen_helpers.parts', **kw)

    Component('xpti', **kw)

def collector_infra_grp(**kw):
    if GetOption('pin-integration'):
        Component('pin_parts',
            parts_file  = 'pin.parts',
            toolchain   = collector_tchain,
            PIN_TRY_WEB = 1,
            **kw)
    else:
        Component('pin_parts',
            parts_file  = 'pin.parts',
            PIN_RELEASE = '3.23',
            PIN_KITNO   = '98572',
            toolchain   = collector_tchain,
            **kw)

    Component('gtpin-parts',
            parts_file      = 'gtpin.parts',
            GTPIN_RELEASE   = '2.22.1',
            GTPIN_KITNO     = '2ea19e5194',
            toolchain       = collector_tchain,
            **kw)

    Component('ccrt',
         toolchain=collector_tchain,
         **kw)

def collector_grp(**kw):
    Component('memorychecker',
        mode = ['BUILD_ENABLE_DOTNET'] if HostPlatform() == 'win32' else ['BUILD_ENABLE_GDB_PROBLEM_BRKPT'],
        toolchain=collector_tchain,
        **kw
    )

    Component('cilkabi',
         **kw)

    Component('threadchecker',
        toolchain_runtime=collector_tchain,
        **kw)

    if is_he() and HostPlatform() == 'posix-any':

        Component('libunwind',
             PART_REVERSE_EXPORTS_LIBS=True,
             toolchain=collector_tchain,
             **kw)

def gui_infra_grp(**kw):
    Component(
        'wxwidgets',
        **kw
    )

    Component(
        'clienthelpers',
        append=dict(
        CCFLAGS=['$CC_COMPILERDEFENSES'],
        CPPFLAGS=['$CPP_COMPILERDEFENSES'],
        LINKFLAGS=['$LINK_COMPILERDEFENSES']
        ),
        **kw
    )

    Component(
        'msngrgui',
        **kw
    )

    if is_ms():
        Component(
            'idvc_graph',
            **kw
        )

    Component('qfagentgui',
         **kw)

    Component(
        'idvc_base',
        **kw
    )

    Component(
        'idvc_frw',
        **kw
    )


    Component(
        'idvc_wx',
        **kw
    )

    Component(
        'idvc_gridctl',
        **kw
    )

    Component(
        'idvc_propgrid',
        **kw
    )

    Component(
        'wx_helpers',
        **kw
    )

    Component(
        'tsguiengine',
        **kw
    )

    Component(
        'tswrappers',
        **kw
    )


def gui_grp(**kw):

    if is_he():
        Component('cs_gui_plug', parts_file='src/cs_gui_plug.parts',
            append=dict(
            CCFLAGS=['$CC_COMPILERDEFENSES'],
            CPPFLAGS=['$CPP_COMPILERDEFENSES'],
            LINKFLAGS=['$LINK_COMPILERDEFENSES']
            ),
           **kw)

        Component('stripchartctrl',
            append=dict(
                CCFLAGS=['$CC_COMPILERDEFENSES'],
                CPPFLAGS=['$CPP_COMPILERDEFENSES'],
                LINKFLAGS=['$LINK_COMPILERDEFENSES']
            ),
            **kw)

        Component('collectdlg', **kw)


        Component('cs_eil',
            parts_file='src/cs_eil.parts',
            PRODUCT_INFO=product_info,
            VSSDK_TOOLCHAIN=vssdk_tchain,
            **kw)

        Component('viewer',
            parts_file='src/viewer.parts',
            VIEWER_RES='./res_confhe/viewer.rc',
            mode=(['BUILD_USE_LARGEADDRESSAWARE', 'BUILD_WITH_PROJECT_NAVIGATOR']) +
            (['PKG_NO_INSTALL'] if is_ms() else []),
            **kw
            )
    else:
        pass

    Component('source_view',
        append=dict(
        CCFLAGS=['$CC_COMPILERDEFENSES'],
        CPPFLAGS=['$CPP_COMPILERDEFENSES'],
        LINKFLAGS=['$LINK_COMPILERDEFENSES']
        ),
        **kw)

    Component('commondlg',
         **kw)
    Component('tc_dialogs',
        append=dict(
        CCFLAGS=['$CC_COMPILERDEFENSES'],
        CPPFLAGS=['$CPP_COMPILERDEFENSES'],
        LINKFLAGS=['$LINK_COMPILERDEFENSES']
        ),
        **kw)

    Component('panes',
        append=dict(
        CCFLAGS=['$CC_COMPILERDEFENSES'],
        CPPFLAGS=['$CPP_COMPILERDEFENSES'],
        LINKFLAGS=['$LINK_COMPILERDEFENSES']
        ),
        **kw)

    Component('client',
        append=dict(
        CCFLAGS=['$CC_COMPILERDEFENSES'],
        CPPFLAGS=['$CPP_COMPILERDEFENSES'],
        LINKFLAGS=['$LINK_COMPILERDEFENSES']
        ),
        **kw)


def cli_grp(**kw):

    Component('runtool',
        append=dict(
        CCFLAGS=['$CC_COMPILERDEFENSES'],
        CPPFLAGS=['$CPP_COMPILERDEFENSES'],
        LINKFLAGS=['$LINK_COMPILERDEFENSES']
        ),
        **kw)

    Component('pdrdiff', **kw)

    Component('confcli',
        append=dict(
        CCFLAGS=['$CC_COMPILERDEFENSES'],
        CPPFLAGS=['$CPP_COMPILERDEFENSES'],
        LINKFLAGS=['$LINK_COMPILERDEFENSES']
        ),
        **kw)

    Component('reporter',
        append=dict(
        CCFLAGS=['$CC_COMPILERDEFENSES'],
        CPPFLAGS=['$CPP_COMPILERDEFENSES'],
        LINKFLAGS=['$LINK_COMPILERDEFENSES']
        ),
        **kw)


def config_files_grp(**kw):
   Component('configs', platform_independent=True, **kw)

def build_box_grp(**kw):
    if DefaultEnvironment().isConfigBasedOn('release'):
	#on posix mostly flexlm deprecated conversion from string constant to 'XXXX' [-Wwrite-strings]
        warning_threshold = 100 if HostPlatform() == 'posix-any' else 200

    else:
        warning_threshold = 20000 if HostPlatform() == 'posix-any' else 800

    Component(
        'devutil',
        # Use VCS_SMART_SVN_DIR to force the directory layout that SSBS expects.
        VCS_SMART_SVN_DIR = '${CHECK_OUT_ROOT}/devutil',
        # Additional wazup script configuration values.
        # The values will be placed to wazup.cfg file next to SConstruct one.
        # The file will be used by wazup script executed by SSBS to collect warnings info.
        WAZUP_CONFIG={
            # Allow up to exitCodeThreshold warnings during the product build
            'exitCodeThreshold': warning_threshold,

            # Ignore warnings which are not detected by wazup script older than of version 1.1.6.
            'filterExclude': [[
                # D9025 : overriding 'XXXX' with 'XXXX'
                ('category', 'cl-cmdline-warning'),

                # 10122: overriding 'XXXX' with 'XXXX'"
                # 10121: overriding 'XXXX' with 'XXXX'
                ('category', 'icl-cmdline-warning'),

                # LNK4068: /MACHINE not specified; defaulting to X86
                # LNK4221: no public symbols found; archive member will be inaccessible
                # LNK4099: PDB 'XXXX' was not found with 'XXXX' or at 'XXXX'; linking object as if no debug info
                ('category', 'ms-link-warning'),

                # Warnings of the following categories are produced by light and candle tools.
                # The tools are currently used only by install_scripts on Windows.
                ('category', 'wix-link-warning'),
                ('category', 'wix-cl-warning'),

                # Warnings like "PREBUILT_SERVER is deprecated. Please use FILE_SYSTEM_SERVER instead"
                ('category', 'parts-locless-warning'),
            ]],
        },
        # checkpermissions.py script configuration settings.
        # These values will be put to permissions.cfg file next to SConstruct
        # MASK_PERMISSIONS is list of rules to check against binary files
        # Most specific rules (exclusion) must be first, less specific (general) rules
        # must be least.
        CHECKPERMISSIONS_CONFIG={
            'MASK_PERMISSIONS': [
                # This file is put to install/bin dir by pin.configuration
                # it is not shipped with the product but it must be there
                # as a workaround. See vcs/pin_parts/configuration.parts for details
                ('*install/bin*/configuration.parts', 0o644),
                # Execuutables must have 'rwxr-xr-x' permissions
                ('*install/bin*/*', 0o755),
                # Shared libraries must have 'rwxr-xr-x' permissions
                ('*install/lib*/**lib*.so*', 0o755),
                ('*install/lib*/*/*lib*.so*', 0o755),
                ('*install/lib*/*/*/*lib*.so*', 0o755),
            ],
        },
        **kw
    )

def gui_unit_testing_grp(alias_ext='', **kw):

    Component(
        'gui_ut_api',
        **kw
    )

def gui_ts_grp(**kw):
    Component('ts_panes', **kw)
    Component('tssourceview', **kw)


def testing_gui_infra(cross_mode='', **kw):
    Component(
        'ts_msaa',
        **kw
    )


def top_level_testing_grp(**kw):

    Component(
        'ts_ut',
        **kw
    )

    Component(
        'ts_common',
        platform_independent=True,
        **kw
    )

    Component(
        'ts_engine',
        TS_PRODUCT_CODE_NAME=INTERNAL_PRODUCT_NAME_FOR_REPORTS,
        platform_independent=True,
        **kw
    )

    Component(
        'initdqtests',
        platform_independent=True,
        **kw
    )

    Component(
        'ts_vsautomation',
        platform_independent=True,
        **kw
    )

    Component(
        'tsautomation',
        platform_independent=True,
        **kw
    )

    if str(Platform()) == 'win32':
        Component('ts_cantua_cli_dq', suffix='src', parts_file='cantua_cli_dq.parts', **kw)
    if str(Platform()) == 'posix':
        Component('ts_cantua_cli_dq_lin', suffix='src', parts_file='cantua_cli_dq_lin.parts', **kw)

    Component('ts_cs_helpers', **kw)

    Component('ts_cantua_he_gui_dq', suffix='src', parts_file='cantua_he_gui_dq.parts', **kw)

    Component('ts_cantua_rcat_perf',
         parts_file='ts_cantua_he_rcat.parts', **kw
         )

##########################
    Part(alias='tc_dialogs_wrappers',
         vcs_type=VcsUsePriorPart('tc_dialogs'),
         parts_file='tc_dialogs_wrappers.parts', **kw
         )

    # Cantua kernel tests
    if 'BUILD_KERNEL_TESTS' in ARGUMENTS.get('mode', []) or 'BUILD_TC_TESTS' in ARGUMENTS.get('mode', []):
        Component('tctestdrivers', **kw)

        Component('tcktests', **kw)

    if ('BUILD_KERNEL_TESTS' in ARGUMENTS.get('mode', []) or 'BUILD_ISM_TESTS' in ARGUMENTS.get('mode', [])
       or ARGUMENTS.get('BUILD_KERNEL_TESTS', False) or ARGUMENTS.get('BUILD_ISM_TESTS', False)):
        # ism kernel tests
        Part(alias='ismtests',
             parts_file='./tests/ism_tests.parts',
             vcs_type=VcsUsePriorPart('ism'), **kw
             )

def symbol_resolution_grp(cross_mode='', **kw):
    for component_name in ['ism', 'qfagent', 'curl', 'log4cplus', 'xed']:
        Component(component_name, **kw)

    cross_suffix=kw.get('cross_suffix', '')

    Part('staticxed',
        alias       ='staticxed' + cross_suffix,
        parts_file  = 'xed.parts',
        mode        =['BUILD_STATIC_XED'],
        vcs_type    = VcsUsePriorPart('xed' + cross_suffix),
        toolchain   = collector_tchain,
        **kw)
    Part('curl_static',
        alias='curl_static' + cross_suffix,
        parts_file ='curl.parts',
        mode=['CURL_STATIC'],
        vcs_type=VcsUsePriorPart('curl' + cross_suffix),
        **kw)


def pmeminsp_grp(**kw):
    Component('pmeminsp', toolchain_runtime=collector_tchain, **kw)

# Enable building the unit tests by default
if 'all' in BUILD_TARGETS and (ARGUMENTS.get('noutest', None) == None) and (not GetOption('no-utests')) and (not is_code_cov):
    BUILD_TARGETS.extend([
        "utest::aggregator::",
        "utest::asdp::",
        "utest::ccrt::",
        "utest::cctrl::",
        "utest::cfgmgr::",
        "utest::client::",
        "utest::clienthelpers::",
        "utest::clpt::",
        "utest::collectdlg::",
        "utest::commhelpers::",
        "utest::commondlg::",
        "utest::confcli::",
        "utest::cpil::",
        "utest::dblite::",
        "utest::featurestat::",
#commented out because latest versions of these component utests are failing
#        "run_utest::file_finder::",
#        "run_utest::formatter::",
#        "utest::gen_helpers::",
        "utest::gui_ut_api::",
        "utest::idvc_base::",
        "utest::idvc_frw::",
        "utest::idvc_propgrid::",
        "utest::idvc_wx::",
        "utest::memorychecker::",
        "utest::msngr::",
        "utest::msngrext::",
        "utest::msngrgui::",
        "utest::panes::",
        "utest::qfagent::",
        "utest::pmeminsp::",
        "utest::rdmgr::",
        "utest::reporter::",
        "utest::runtool::",
        "utest::smip::",
        "utest::source_view::",
        "utest::stripchartctrl::",
        "utest::tc_dialogs::",
        "utest::tc_engine::",
        "utest::threadchecker::",
        "utest::userapi::",
        "utest::wx_helpers::",
        "utest::zlib::",
    ])
#TODO: enable this after adding support to parts_ng (or workaround somehow)
#    if HostPlatform() == 'win32-any':
#        BUILD_TARGETS.extend(["utest::install_scripts@target:x86::"])

cross_mode = get_cross_mode()
if cross_mode == CROSS_DEFAULT:
    if HostPlatform() == 'posix-x86_64':
        cross_mode = CROSS_GUI
    elif HostPlatform() == 'win32-any':
        cross_mode = CROSS_GUI
    else:
        # posix-x86 or unknown
        cross_mode = CROSS_NONE

if cross_mode not in get_known_cross_modes():
    PrintError("Error: invalid cross-compilation mode -- `%s'" % cross_mode)
    Exit(1)

PrintMessage("Compiling with cross mode `%s'" % cross_mode)


# native build or what ever is targeted
# always do this

nativeKw = dict(TARGET_PLATFORM=NativePlatform, OSBITNESS=NativeBitness)

# minimal amount of stuff almost always needed
common_infra(package_group='common-${TARGET_PLATFORM}')
infra_grp(package_group='common-${TARGET_PLATFORM}')
symbol_resolution_grp(package_group='common-${TARGET_PLATFORM}')
collector_infra_grp(package_group='common-${TARGET_PLATFORM}', vsix_package_group=vsix_pkg)
tut_grp()

# collector groups needed for CLI and GUI
collector_grp(package_group='cli-${TARGET_PLATFORM}')

# data model components needed for CLI and GUI
data_model_grp(package_group='common-${TARGET_PLATFORM}')

# stuff needed for a full command line package
cli_grp(package_group='cli-${TARGET_PLATFORM}')

# the config files actually end up in common_cli-*-any, see ReplacePackageGroupCriteria above
# thus, they don't need to be remade for cross architecture below
config_files_grp(package_group='cli-${TARGET_PLATFORM}')
documentation_grp(version='enterprise', package_group='doc-${TARGET_OS}-any')

# gui stuff
gui_unit_testing_grp()
gui_ts_grp()
gui_infra_grp(package_group='gui-${TARGET_PLATFORM}')
messed_up_stuff(package_group='gui-${TARGET_PLATFORM}', **nativeKw)
gui_grp(package_group='gui-${TARGET_PLATFORM}', vsix_package_group=vsix_pkg, **nativeKw)

# infrastructure stuff:
#NB!!! package_group='nda-${TARGET_PLATFORM}' is temporary solution to enable fake file for nda package,
#      so please remove any package from followign test group, like top_level_testing_grp()
top_level_testing_grp(package_group='nda-${TARGET_PLATFORM}')
testing_gui_infra()
build_box_grp()

# Persistence Inspector package (64-bit version only)
if NativePlatform.ARCH == 'x86_64':
    pmeminsp_grp(package_group='cli-${TARGET_PLATFORM}', **nativeKw)

if cross_mode != CROSS_NONE:
    crossKw = dict(cross_suffix=CrossPlatform.ARCH, cross_mode=cross_mode, TARGET_PLATFORM=CrossPlatform, OSBITNESS=CrossOsBit)

    def_pkg += ['common-'+str(CrossPlatform)]

    tut_grp(**crossKw)

    vsix_cross_pkg = 'vs_extension-'+str(CrossPlatform)

    common_infra(package_group='common-${TARGET_PLATFORM}', **crossKw)
    infra_grp(package_group='common-${TARGET_PLATFORM}', **crossKw)
    symbol_resolution_grp(package_group='common-${TARGET_PLATFORM}', **crossKw)
    collector_infra_grp(package_group='common-${TARGET_PLATFORM}', vsix_package_group=vsix_cross_pkg, **crossKw)
    collector_grp(package_group='common-${TARGET_PLATFORM}', **crossKw)
    data_model_grp(package_group='common-${TARGET_PLATFORM}', **crossKw)

    # Persistence Inspector package (64-bit version only)
    if CrossPlatform.ARCH == 'x86_64':
        pmeminsp_grp(package_group='cli-${TARGET_PLATFORM}', **crossKw)

    if cross_mode in [CROSS_GUI, CROSS_CLI]:
        def_pkg += ['cli-'+str(CrossPlatform)]

        cli_grp(package_group='cli-${TARGET_PLATFORM}', **crossKw)

    if cross_mode == CROSS_GUI:
        def_pkg += ['gui-'+str(CrossPlatform)]

        if CrossPlatform == 'win32-x86':
            def_pkg.append(vsix_cross_pkg)

        gui_infra_grp(package_group='gui-${TARGET_PLATFORM}', **crossKw)
        messed_up_stuff(package_group='gui-${TARGET_PLATFORM}', **crossKw)
        gui_grp(package_group='gui-${TARGET_PLATFORM}', vsix_package_group=vsix_cross_pkg, **crossKw)
        gui_unit_testing_grp(**crossKw)
        gui_ts_grp(**crossKw)

    testing_gui_infra(**crossKw)

pkg_filename = PACKAGE_NAME + '-' + PACKAGE_VERSION

Alias("package", DefaultEnvironment().BOMPackage(pkg_filename, def_pkg))

if HostPlatform() == 'win32-any':
    PACKAGE_MAP = {
        'public': {
            'boms': [
                ('inspector_oneapi.txt', ['cli-win32-x86', 'cli-win32-x86_64', 'cli_common-win32-any', 'common-win32-x86', 'common-win32-x86_64', 'doc-win32-any', 'gui-win32-x86', 'gui-win32-x86_64', 'gui_common-win32-any', 'he-win32-any']),
                ('inspector_oneapi_ide.txt', ['vs_extension-win32-x86'])
            ]
        },
        'nda': {
            'boms': [
                ('inspector_oneapi.txt', ['cli-win32-x86', 'cli-win32-x86_64', 'cli_common-win32-any', 'common-win32-x86', 'common-win32-x86_64', 'doc-win32-any', 'gui-win32-x86', 'gui-win32-x86_64', 'gui_common-win32-any', 'he-win32-any', 'nda-win32-x86']),
                ('inspector_oneapi_ide.txt', ['vs_extension-win32-x86'])
            ]
        }
    }
elif HostPlatform() == 'posix-any':
    PACKAGE_MAP = {
        'public': {
            'boms': [
                ('inspector_oneapi.bom', ['cli_common-posix-any', 'cli-posix-x86', 'common-posix-x86', 'gui_common-posix-any', 'gui-posix-x86', 'cli-posix-x86_64', 'common-posix-x86_64', 'doc-posix-any', 'gui-posix-x86_64', 'he-posix-any'])
           ]
        },
        'nda': {
            'boms': [
                ('inspector_oneapi.bom', ['cli_common-posix-any', 'cli-posix-x86', 'common-posix-x86', 'gui_common-posix-any', 'gui-posix-x86', 'cli-posix-x86_64', 'common-posix-x86_64', 'doc-posix-any', 'gui-posix-x86_64', 'he-posix-any', 'nda-posix-x86_64'])
            ]
        }
    }
else:
    PACKAGE_MAP = None

DROP_CONFIG = {
        'head' : '',
        'destination_prefix': 'inspector/<version>/',
        'drop_types': ['public', 'nda'],
        'pkg_subdir': '',
        'has_product.ini': False,
        'drop_contents': PACKAGE_MAP
    }

Alias("package",
    Command(["#/drop_config.json"], [],
    Action(saveJson, varlist='DATA'),
    DATA=DROP_CONFIG))

if GetOption('distributed'):
    # keys of this dictionary are packaging buildes platforms, values - list of build platforms
    # should complete before starting packaging builder. All platform names are 'buildbot' names
    # You can see that names as platform subdirectory names in uploaded build directory
    REQUIRED_BUILDS_FOR_PACKAGE = {
        'windows' : ['windows'],
        'linux'   : ['linux'],
        'darwin'  : ['darwin'],
    }

    PACKAGING_INFO = {
        'REQUIRED_BUILDS_FOR_PACKAGE' : REQUIRED_BUILDS_FOR_PACKAGE,
        'INSTALL_ROOT' : DefaultEnvironment().subst('$INSTALL_ROOT'),
        'PACKAGING_SUBDIR': ''
    }

    Alias("package",
            Command(["#packaging_info.json"], [],
            Action(saveJson, varlist='DATA'),
            DATA=PACKAGING_INFO))

def initSigning(env): #adds binary signing during env.InstallXXX() calls
    if env['PART_NAME'] == 'signing':
        return
    env.DependsOn([env.Component('signing', requires=requirement.REQ.ADD_SIGN_INSTALLED_FILES)])
    env['DEPENDS']['signing']['ADD_INSTALLED_FILES_SIGNING'](env)

if ARGUMENTS.get('official_build') and 'BUILD_KERNEL_TESTS' not in ARGUMENTS.get('mode',[]):
    if build_type() != 'ci':
        Component('signing', platform_independent=True)
        AddPartEnvPostProcessFunction(initSigning)

# ----------------------------------------------------------------------------------------------
# Testing Plan
# ----------------------------------------------------------------------------------------------

def get_install_cmd(os_type):
    install_scripts = {
        'linux': './install_ss.sh',
        'windows': 'install_ss.bat',
        'darwin': './install_ss.sh',
    }

    install_script = install_scripts[os_type]
    cmd = {
        'title': 'Install Advisor',
        'cmd': ' '.join([
            install_script,
            '--product-codename={}'.format(PACKAGE_NAME),
            '--path-to-build={path_to_build}',
            '--build-type={build_type}',
            '--build-number={build_number}',
            '--build-mode={build_mode}',
        ])
    }
    return cmd

def get_testing_cmd(os_type, test_runner_script, test_runner_options, vs):
    test_scripts = {
        'linux': './run_tests.sh',
        'windows': 'run_tests.bat',
        'darwin': './run_tests.sh',
    }
    test_script = test_scripts[os_type]
    cmd = {
        'title': 'Run tests',
        'cmd': ' '.join([
            test_script,
            '--test-runner-script={}'.format(test_runner_script),
            test_runner_options,
            '--vs={}'.format(vs) if vs else '',
            '--under-buildbot',
            '--path-to-developer-pkg=AUTO',
            '--cleanup-before-run',
            '--official',
            '--analyze-defects',
            '--build-number={build_number}',
            '--product-codename={}'.format(PACKAGE_NAME),
            '--submit',
            '--attach-tags={traqs_tags}',
        ])
    }
    return cmd

def get_cmd_list(os_type, test_runner_script, vs=None, test_runner_options=''):
    cmd_list = {
        'commands': [
            get_install_cmd(os_type),
            get_testing_cmd(os_type, test_runner_script, test_runner_options, vs),
        ]
    }
    return cmd_list

TESTING_PLAN = {
    # Testing in Virtual environment
    'Debian 10 @ Xeon Gold 6152 (Skylake EP) Hyper-V': {
        'he': {
            'ST' :get_cmd_list(os_type='linux', test_runner_script='run_sanity_cli'),
        },
    },
    'Fedora 33 @ Xeon Gold 6152 (Skylake EP) Hyper-V': {
        'he': {
            'ST' : get_cmd_list(os_type='linux', test_runner_script='run_sanity_cli'),
        },
    },
    'RHEL 7 U9 @ Xeon Gold 6152 (Skylake EP) Hyper-V': {
        'he': {
            'ST' : get_cmd_list(os_type='linux', test_runner_script='run_sanity_cli'),
        },
    },
    'SLES 12 SP5 @ Xeon Gold 6152 (Skylake EP) Hyper-V': {
        'he': {
            'ST' :get_cmd_list(os_type='linux', test_runner_script='run_sanity_cli'),
        },
    },
    'SLES 15 SP1 @ Xeon Gold 6152 (Skylake EP) Hyper-V': {
        'he': {
            'ST' : get_cmd_list(os_type='linux', test_runner_script='run_sanity_cli'),
        },
    },
    'Ubuntu 18.04 @ Xeon Gold 6152 (Skylake EP) Hyper-V': {
        'he': {
            'ST' : get_cmd_list(os_type='linux', test_runner_script='run_sanity_cli'),
        },
    },
    'Ubuntu 19.10 @ Xeon Gold 6152 (Skylake EP) Hyper-V': {
        'he': {
            'ST' : get_cmd_list(os_type='linux', test_runner_script='run_sanity_cli'),
        },
    },
    'Ubuntu 20.04 @ Xeon Gold 6152 (Skylake EP) Hyper-V': {
        'he': {
            'ST' : get_cmd_list(os_type='linux', test_runner_script='run_sanity_cli'),
        },
    },
    'Ubuntu 20.10 @ Xeon Gold 6152 (Skylake EP) Hyper-V': {
        'he': {
            'ST' : get_cmd_list(os_type='linux', test_runner_script='run_sanity_cli'),
        },
    },
}

TESTING_PLAN_TAGS = set()
TESTING_PLAN_WITH_TAGS = dict()

for platform_name, product_variants in TESTING_PLAN.items():
    TESTING_PLAN_WITH_TAGS[platform_name] = dict()
    for product_variant, testing_type in product_variants.items():
        TESTING_PLAN_WITH_TAGS[platform_name][product_variant] = dict()
        for testing_type_name, cmd_line in testing_type.items():
            tag_hash = hashlib.md5((platform_name + testing_type_name).encode())
            unique_tag = tag_hash.hexdigest()[0:10]
            if unique_tag in TESTING_PLAN_TAGS:
                PrintError("Testing plan tag: '{}' already in use".format(unique_tag))
            TESTING_PLAN_TAGS.add(unique_tag)
            tags = [unique_tag]
            if testing_type_name == "GPU":
                tags.append('gpu')
            upd_cmd_line = dict(cmd_line)
            upd_cmd_line['tags'] = ':'.join(tags)
            upd_cmd_line['tag'] = upd_cmd_line['tags']
            TESTING_PLAN_WITH_TAGS[platform_name][product_variant][testing_type_name] = upd_cmd_line
TESTING_PLAN = TESTING_PLAN_WITH_TAGS

Alias("package",
    Command(["#/testing_plan.json"], [],
    Action(saveJson, varlist='DATA'),
    DATA=TESTING_PLAN))

# DO NOT REMOVE: this line helps to avoid tab/spaces mess when VIM editor is used
# vim: set et ts=4 sw=4 ai ft=python :
