CALLS_PATH = '/fax/calls/'
call_files = os.listdir(CALLS_PATH)

TIFS_PATH = '/fax/calls/'
tifs_files = os.listdir(TIFS_PATH)

#extensions_custom = '/fax/extensions_custom.conf'
extensions_custom = '/fax/extensions_custom_fax.conf'

for tif_file in tif_files:
  number = tif_files[0:1]
  next_line = ""