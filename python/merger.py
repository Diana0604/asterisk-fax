import asterisk
from PIL import Image
import random, glob

audience_faxes = "/fax/tifs/output"
merged_path = "/fax/tifs/merged.tif"

# audience_faxes = "./tifs/output"
# merged_path = "./tifs/merged.tif"

FAX_WIDTH = 1728


def normalise_resolution(img):
    img_copy = img.copy().convert("1")
    # If vertical DPI is 98, scale up to 196 to unsquash
    dpi = img.info.get("dpi", (204, 196))
    if dpi[1] <= 100:  # low res vertical
        new_height = img_copy.height * 2
        width = img_copy.width
        img_copy = img_copy.resize(
            (width, new_height), Image.NEAREST  # NEAREST preserves hard 1-bit edges
        )
    return img_copy


def merge_random_faxes():
    # print("merging")
    files = glob.glob(f"{audience_faxes}/*.tif")
    print(files)
    random.shuffle(files)
    print(files)

    frames = []

    for i in range(0, 3):
        if i >= len(files):
            break
        f = files[i]
        img = Image.open(f)
        for i in range(img.n_frames):
            img.seek(i)
            frames.append(normalise_resolution(img.copy()))  # 1-bit, standard for fax

    frames[0].save(
        merged_path,
        format="TIFF",
        save_all=True,
        append_images=frames[1:],
        compression="group4",
        dpi=(204, 196),
        resolution_unit=2,
    )


def merge_loop():
    need_merging = asterisk.get_from_database("prep_feed")
    if need_merging != "True":
        return
    merge_random_faxes()
    asterisk.add_to_database("prep_feed", "False")


# merge_loop()
