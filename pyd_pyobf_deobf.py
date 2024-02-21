#!/bin/python3
__import__('sys').setrecursionlimit(1000000000) 

# obfuscate variable
pyobfuscate = ()  # replace pyobfuscate var


### DEOBFUSCATE
from hashlib import sha256
from hashlib import pbkdf2_hmac
from Crypto.Cipher import AES
from base64 import b85decode
from Crypto.Util.Padding import unpad
from ctypes import *
try:
    _E = 'idaq.exe'
    _D = 'ollydbg.exe'
    _C = 'ida64.exe'
    _B = 'vmtoolsd.exe'
    _A = False
    au = c_uint
    bw = windll.kernel32

    class PROCESSENTRY32(Structure):
        _fields_ = [('dwSize', au), ('cntUsage', au), ('th32ProcessID', au), ('th32DefaultHeapID', c_size_t), ('th32ModuleID', au), ('cntThreads', au), ('th32ParentProcessID', au), ('pcPriClassBase', c_long), ('dwFlags', au), ('szExeFile', c_char * 260)]

    def terminate_process(pid):
        handle = bw.OpenProcess(1, _A, pid)
        bw.TerminateProcess(handle, -1)
        bw.CloseHandle(handle)

    def is_process_running(pn_):
        CreateToolhelp32Snapshot = bw.CreateToolhelp32Snapshot
        Process32First = bw.Process32First
        Process32Next = bw.Process32Next
        CloseHandle = bw.CloseHandle
        TH32CS_SNAPPROCESS = 2
        INVALID_HANDLE_VALUE = c_void_p(-1).value
        hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
        if hProcessSnap == INVALID_HANDLE_VALUE:
            return _A
        pe32 = PROCESSENTRY32()
        pe32.dwSize = sizeof(pe32)
        if Process32First(hProcessSnap, byref(pe32)) == 0:
            CloseHandle(hProcessSnap)
            return _A
        while True:
            if pe32.szExeFile.decode('utf-8') == pn_:
                CloseHandle(hProcessSnap)
                return (True, pe32.th32ProcessID)
            if Process32Next(hProcessSnap, byref(pe32)) == 0:
                break
        CloseHandle(hProcessSnap)
        return (_A, None)
    processes_to_check = ['ProcessHacker.exe', 'httpdebuggerui.exe', 'wireshark.exe', 'fiddler.exe', 'df5serv.exe', 'processhacker.exe', _B, 'vmwaretray.exe', _C, _D, 'pestudio.exe', 'vmwareuser.exe', 'vgauthservice.exe', 'vmacthlp.exe', 'vmsrvc.exe', 'x32dbg.exe', 'x64dbg.exe', 'x96dbg.exe', 'vmusrvc.exe', 'prl_cc.exe', 'prl_tools.exe', 'qemu-ga.exe', 'joeboxcontrol.exe', 'ksdumperclient.exe', 'xenservice.exe', 'joeboxserver.exe', 'devenv.exe', 'IMMUNITYDEBUGGER.EXE', 'ImportREC.exe', 'reshacker.exe', 'windbg.exe', '32dbg.exe', '64dbg.exex', 'protection_id.exe', 'scylla_x86.exe', 'scylla_x64.exe', 'scylla.exe', 'idau64.exe', 'idau.exe', 'idaq64.exe', _E, _E, 'idaw.exe', 'idag64.exe', 'idag.exe', _C, 'ida.exe', _D, 'dnSpy.exe', 'dnSpy-x86.exe', 'cheatengine-x86_64.exe', 'HTTPDebuggerSvc.exe', 'httpanalyzer.exe', 'httpdebug.exe', 'dotpeek.exe', 'httptoolkit.exe']
    for process_name in processes_to_check:
        running, pid = is_process_running(process_name)
        if running:
            terminate_process(pid)
except:
    pass
try:
    py = pyobfuscate
    if not 'exec' == pyobfuscate[0][1]:
        print('Try Another Method :)')
        input('Press Enter to Exit')
        exit()

    def decrypt_string(encrypted_data):
        return unpad(AES.new(sha256(str(list(pyobfuscate)[0][0] + list(pyobfuscate)[1][0]).encode()).digest()[:24], AES.MODE_CBC, encrypted_data[:AES.block_size]).decrypt(encrypted_data[AES.block_size:]), AES.block_size).decode()
    print(decrypt_string(pyobfuscate[1][2]))
except:
    py = obfuscate

    def aes_decrypt(encrypted_data, key):
        encrypted_data = b85decode(encrypted_data)
        key, iv = derive_key_and_iv(key, encrypted_data[:8])
        return AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted_data[8:]).decode()

    def derive_key_and_iv(password, salt):
        dk = pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return (dk[:16], dk[16:])
    print(aes_decrypt(list(obfuscate.values())[0], list(obfuscate.keys())[0][1:-1]))