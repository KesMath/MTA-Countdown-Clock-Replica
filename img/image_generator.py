from PIL import Image, ImageDraw, ImageFont


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
    pass


def convert_to_ppm_image(png_image):
    """
    :param png_image:
    :return: resizes and saves a .png photo to ppm which is the accepted file format for
    the rgb-led-matrix panel
    """
    pass

if __name__ == '__main__':
    convert_to_ppm_image(
        generate_png_image(train_logo_fp = "NYCS-bull-trans-2-Std.png",
                           train_info = ("Flatbush Av - Brooklyn College","13 min")))