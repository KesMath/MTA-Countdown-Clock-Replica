from PIL import Image, ImageDraw, ImageFont


BLACK_TEXT = (0, 0, 0)

# x-coord is 2 pixels rightwards of train logo to introduce padding
# y-coord is halfway the display size
TEXT_LOCATION = (6, 8)
RGB_MATRIX_DIMENSION = (64, 16)
MASKING_CIRCLE = (15, 15, 115, 115)


# TODO: I believe it may be best to stitch image first then resize to display dimensions
# TODO: instead working in the confinements of the desired dimensions which posed some display issues
TMP_DIMENSION = (525, 525)
TMP_TEXT_LOCATION = (250, 250)
PASTE_LOCATION = (33, 184)

def generate_png_image(train_logo_fp, train_info: tuple):
    """
    Performs a horizontal merge with:

    :param train_logo_fp: filepath of png file containing train logo
    :param train_info: tuple(0) = stop name, tuple(1) = departure time.
    NOTE: The tuple will serve as contrasting black text against a
    white background image with necessary white-spacing

    :return: a png image that mocks a countdown clock as such:
    https://brooklyneagle.com/wp-content/uploads/2017/09/subway-countdown-clock-02-by-mary-frost-b.jpg
    with the exception of just containing one train departure row for now.
    """

    def draw_elliptal_mask(img):
        """
        :param img: image object to copy size from
        :return: an circular image object that will be used to remove the black rectangular border of train logo img
        """
        mask_im = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask_im)
        draw.ellipse(xy=MASKING_CIRCLE, fill=255)
        mask_im.save('aux/mask_circle.png')
        return mask_im


    whitespace = 5 * ' '
    info_img = Image.new(mode="RGB", size=TMP_DIMENSION,
                       color=(256, 256, 256))

    draw = ImageDraw.Draw(info_img)

    font = ImageFont.truetype('fonts/Helvetica.ttc', size=15)
    draw.text(xy=TMP_TEXT_LOCATION, text=train_info[0] + whitespace + train_info[1], fill=BLACK_TEXT, font=font)

    logo_img = Image.open(train_logo_fp)

    #logo to take up 25% of display. May want to reduce by a higher factor to indroduce whitespacing around logo
    logo_img = logo_img.resize((int(TMP_DIMENSION[0] * 0.25), int(TMP_DIMENSION[1] * 0.25))) # == (131, 131)

    info_img.paste(im=logo_img, box=PASTE_LOCATION, mask=draw_elliptal_mask(logo_img))

    # TODO: confirm with C++ image writer package to see if resizing to this dimension is accurate
    # info_img = info_img.resize(RGB_MATRIX_DIMENSION)
    info_img.save("./countdown_img.png")
    return info_img


def convert_to_ppm_image(png_image):
    """
    :param png_image:
    :return: saves a .png photo to ppm which is the accepted file format for
    the rgb-led-matrix panel
    """
    pass

if __name__ == '__main__':
    convert_to_ppm_image(
        generate_png_image(train_logo_fp = "NYCS-bull-trans-2-Std.png",
                           train_info = ("Flatbush Av - Brooklyn College", "13 min")))