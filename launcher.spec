# launcher.spec
block_cipher = None

a = Analysis(
    ['frontend/launcher.py'],      # Entry script
    pathex=['.'],                  # Project root
    datas=[
        ('core', 'core'),
        ('frontend', 'frontend'),
        ('gui', 'gui'),
        ('tests', 'tests'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[]
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='vitru',
    icon=None,        # ← Add icon here if needed: 'app.ico'
    console=False,    # GUI mode (no black console)
    strip=False,
    upx=False,
)
