# -*- mode: python -*-

block_cipher = None


a = Analysis(['Starter.py'],
             pathex=['D:\\VkSpammer V1.0\\model\\Start'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Starter',
          debug=False,
          strip=False,
          upx=True,
          console=False )
