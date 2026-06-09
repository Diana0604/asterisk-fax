from PIL import Image
import random, glob

# audience_faxes = "/fax/tifs/output"
# merged_path = "/fax/tifs"

audience_faxes = "./tifs/output"
merged_path = "./tifs/merged.tif"


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
            frames.append(img.copy().convert("1"))  # 1-bit, standard for fax

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
