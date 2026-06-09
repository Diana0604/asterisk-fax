from PIL import Image
import random, glob

# audience_faxes = "/fax/tifs/output"
# merged_path = "/fax/tifs"

audience_faxes = "./tifs/output"
merged_path = "./tifs/merged.tif"

# Standard fax A4 dimensions at 204x196 DPI
FAX_WIDTH = 1728
FAX_HEIGHT = 2156

def pad_to_a4(img):
    img = img.convert("1")
    if img.height == FAX_HEIGHT:
        return img  # already A4
    
    # Create white A4 canvas
    canvas = Image.new("1", (FAX_WIDTH, FAX_HEIGHT), 1)
    # Paste original at top (or centre if preferred)
    canvas.paste(img, (0, 0))
    return canvas

def merge_random_faxes():
    print("merging")
    files = glob.glob(f"{audience_faxes}/*.tif")
    random.shuffle(files)
    print(files)

    frames = []

    for i in range(0, 5):
        if i >= len(files):
            break
        f = files[i]
        img = Image.open(f)
        for i in range(img.n_frames):
            img.seek(i)
            frames.append(pad_to_a4(img.copy()))  # 1-bit, standard for fax

    frames[0].save(
        merged_path,
        format="TIFF",
        save_all=True,
        append_images=frames[1:],
        compression="group4",
        dpi=(204, 196),
        resolution_unit=2,
    )


merge_random_faxes()
