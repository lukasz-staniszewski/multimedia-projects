import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def cv_imshow(img, img_title: str = "image"):
    if (img.dtype == np.float32) or (img.dtype == np.float64):
        img_ = img / 255
    elif img.dtype == np.int16:
        img_ = img * 128
    else:
        img_ = img
    cv2.imshow(img_title, img_)


def calc_entropy(hist):
    # histogram normalization to probabilities
    pdf = hist / hist.sum()
    entropy = -sum([x * np.log2(x) for x in pdf if x != 0])
    return entropy


def calc_bitrate_and_entropy(image, path):
    bitrate = (
        8 * os.stat(path).st_size / (image.shape[0] * image.shape[1])
    )
    print(f"bitrate: {bitrate:.4f}")

    hist_image = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_image = hist_image.flatten()
    H_image = calc_entropy(hist_image)
    print(f"H(image) = {H_image:.4f}")


def get_differential_image(image):
    img_tmp1 = image[:, 1:]  # columns 1 - n
    img_tmp2 = image[:, :-1]  # columns 0 - n-1

    image_hdiff = cv2.addWeighted(
        img_tmp1, 1, img_tmp2, -1, 0, dtype=cv2.CV_16S
    )
    # from 0 col 127 is subtracted
    image_hdiff_0 = cv2.addWeighted(
        image[:, 0], 1, 0, 0, -127, dtype=cv2.CV_16S
    )
    image_hdiff = np.hstack(
        (image_hdiff_0, image_hdiff)
    )  # horizontal direction concatenation

    cv_imshow(image_hdiff, "image_hdiff")
    return image_hdiff


def compare_hist_entropy(image1, image2):
    image_tmp = (image2 + 255).astype(np.uint16)
    hist_hdiff = cv2.calcHist(
        [image_tmp], [0], None, [511], [0, 511]
    ).flatten()
    hist_image = cv2.calcHist(
        [image1], [0], None, [256], [0, 256]
    ).flatten()

    plt.figure()
    plt.subplot(121)
    plt.plot(hist_image, color="blue")
    plt.title("Histogram original image")
    plt.xlim([0, 255])
    plt.subplot(122)
    plt.plot(np.arange(-255, 256, 1), hist_hdiff, color="red")
    plt.title("Histogram differential image")
    plt.xlim([-255, 255])
    plt.show()

    print(f"Entropy original image: {calc_entropy(hist_image):.4f}")
    print(f"Entropy differential image: {calc_entropy(hist_hdiff):.4f}")


def dwt(img):
    """Function determining the DWT of the image"""
    maskL = np.array(
        [
            0.02674875741080976,
            -0.01686411844287795,
            -0.07822326652898785,
            0.2668641184428723,
            0.6029490182363579,
            0.2668641184428723,
            -0.07822326652898785,
            -0.01686411844287795,
            0.02674875741080976,
        ]
    )
    maskH = np.array(
        [
            0.09127176311424948,
            -0.05754352622849957,
            -0.5912717631142470,
            1.115087052456994,
            -0.5912717631142470,
            -0.05754352622849957,
            0.09127176311424948,
        ]
    )

    # negative values in high-pass filtering -> result is 16-bit signed
    bandLL = cv2.sepFilter2D(img, -1, maskL, maskL)[::2, ::2]
    bandLH = cv2.sepFilter2D(img, cv2.CV_16S, maskL, maskH)[::2, ::2]
    bandHL = cv2.sepFilter2D(img, cv2.CV_16S, maskH, maskL)[::2, ::2]
    bandHH = cv2.sepFilter2D(img, cv2.CV_16S, maskH, maskH)[::2, ::2]
    return bandLL, bandLH, bandHL, bandHH


def show_hist_bands(hist_ll, hist_lh, hist_hl, hist_hh):
    """Presents given histograms as a subplot."""
    fig = plt.figure()
    fig.set_figheight(fig.get_figheight() * 2)
    fig.set_figwidth(fig.get_figwidth() * 2)

    plt.subplot(2, 2, 1)
    plt.plot(hist_ll, color="blue")
    plt.title("hist_ll")
    plt.xlim([0, 255])

    plt.subplot(2, 2, 3)
    plt.plot(np.arange(-255, 256, 1), hist_lh, color="red")
    plt.title("hist_lh")
    plt.xlim([-255, 255])

    plt.subplot(2, 2, 2)
    plt.plot(np.arange(-255, 256, 1), hist_hl, color="red")
    plt.title("hist_hl")
    plt.xlim([-255, 255])

    plt.subplot(2, 2, 4)
    plt.plot(np.arange(-255, 256, 1), hist_hh, color="red")
    plt.title("hist_hh")
    plt.xlim([-255, 255])

    plt.show()
    cv2.destroyAllWindows()


def calc_mse_psnr(img1, img2):
    """Counts MSE and PSNR for the given images.
    Assumption: pixels in [0, 255]."""
    imax = 255.0 ** 2
    # Negative values significant, so img converted to float64.
    mse = ((img1.astype(np.float64) - img2) ** 2).sum() / img1.size
    psnr = 10.0 * np.log10(imax / mse)
    return mse, psnr


def showHistograms(histograms, hist_names):
    subplots = [131, 132, 133]
    plt.figure()
    for hist, name, sub in zip(histograms, hist_names, subplots):
        plt.subplot(sub)
        plt.plot(hist)
        plt.title(name)
    plt.show()


def task12():
    imageBW = cv2.imread("img/boat2_mono.png", cv2.IMREAD_UNCHANGED)
    calc_bitrate_and_entropy(imageBW, "img/boat2_mono.png")


def task3():
    imageBW = cv2.imread("img/boat2_mono.png", cv2.IMREAD_UNCHANGED)
    image_differential = get_differential_image(imageBW)
    compare_hist_entropy(imageBW, image_differential)


def task4():
    # determination of bands using the DWT transformation
    imageBW = cv2.imread("img/boat2_mono.png", cv2.IMREAD_UNCHANGED)
    ll, lh, hl, hh = dwt(imageBW)
    cv_imshow(ll, "LL2")
    cv_imshow(cv2.multiply(lh, 2), "LH2")
    cv_imshow(cv2.multiply(hl, 2), "HL2")
    cv_imshow(cv2.multiply(hh, 2), "HH2")

    # calculation of histograms with appropriate scaling and conversion for calcHist()
    hist_ll = cv2.calcHist([ll], [0], None, [256], [0, 256]).flatten()
    hist_lh = cv2.calcHist(
        [(lh + 255).astype(np.uint16)], [0], None, [511], [0, 511]
    ).flatten()
    hist_hl = cv2.calcHist(
        [(hl + 255).astype(np.uint16)], [0], None, [511], [0, 511]
    ).flatten()
    hist_hh = cv2.calcHist(
        [(hh + 255).astype(np.uint16)], [0], None, [511], [0, 511]
    ).flatten()

    # entropy calculation
    H_ll = calc_entropy(hist_ll)
    H_lh = calc_entropy(hist_lh)
    H_hl = calc_entropy(hist_hl)
    H_hh = calc_entropy(hist_hh)
    print(
        f"H(LL) = {H_ll:.4f} \nH(LH) = {H_lh:.4f} \nH(HL) ="
        f" {H_hl:.4f} \nH(HH) = {H_hh:.4f} \n"
    )

    # histogram overview
    show_hist_bands(hist_ll, hist_lh, hist_hl, hist_hh)


def task56():
    # images for individual RGB components
    image_col = cv2.imread("img/boat2_col.png")
    image_R = image_col[:, :, 2]
    image_G = image_col[:, :, 1]
    image_B = image_col[:, :, 0]

    # histograms for individual RGB components
    hist_R = cv2.calcHist(
        [image_R], [0], None, [256], [0, 256]
    ).flatten()
    hist_G = cv2.calcHist(
        [image_G], [0], None, [256], [0, 256]
    ).flatten()
    hist_B = cv2.calcHist(
        [image_B], [0], None, [256], [0, 256]
    ).flatten()

    # entropies for individual RGB components
    H_R = calc_entropy(hist_R)
    H_G = calc_entropy(hist_G)
    H_B = calc_entropy(hist_B)
    print(f"H(R) = {H_R:.4f} \nH(G) = {H_G:.4f} \nH(B) = {H_B:.4f}\n")

    # to YUV conversion and histograms for YUV components
    image_YUV = cv2.cvtColor(image_col, cv2.COLOR_BGR2YUV)
    hist_Y = cv2.calcHist(
        [image_YUV[:, :, 0]], [0], None, [256], [0, 256]
    ).flatten()
    hist_U = cv2.calcHist(
        [image_YUV[:, :, 1]], [0], None, [256], [0, 256]
    ).flatten()
    hist_V = cv2.calcHist(
        [image_YUV[:, :, 2]], [0], None, [256], [0, 256]
    ).flatten()

    # entropies for YUV components
    H_Y = calc_entropy(hist_Y)
    H_U = calc_entropy(hist_U)
    H_V = calc_entropy(hist_V)
    print(f"H(Y) = {H_Y:.4f} \nH(U) = {H_U:.4f} \nH(V) = {H_V:.4f}\n")

    # histograms for each components (RGB & YUV)
    showHistograms(
        [hist_R, hist_G, hist_B],
        ["HISTOGRAM(R)", "HISTOGRAM(G)", "HISTOGRAM(B)"],
    )
    showHistograms(
        [hist_Y, hist_U, hist_V],
        ["HISTOGRAM(Y)", "HISTOGRAM(U)", "HISTOGRAM(V)"],
    )


def task7():
    image_col = cv2.imread("img/boat2_col.png", cv2.IMREAD_UNCHANGED)
    xx = []  # bitrate
    ym = []  # MSE
    yp = []  # PSNR

    # quality loop
    for quality in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]:
        out_file_name = f"img/out_image_q{quality:03d}.jpg"
        # to jpg save
        cv2.imwrite(
            out_file_name,
            image_col,
            (cv2.IMWRITE_JPEG_QUALITY, quality),
        )
        # reading compressed img, bitrate and PSNR calculation
        image_compressed = cv2.imread(
            out_file_name, cv2.IMREAD_UNCHANGED
        )
        bitrate = (
            8
            * os.stat(out_file_name).st_size
            / (image_col.shape[0] * image_col.shape[1])
        )
        mse, psnr = calc_mse_psnr(image_col, image_compressed)
        xx.append(bitrate)
        ym.append(mse)
        yp.append(psnr)

    # plotting
    fig = plt.figure()
    fig.set_figwidth(fig.get_figwidth() * 2)
    plt.suptitle("R-D CHARACTERISTICS")
    plt.subplot(1, 2, 1)
    plt.plot(xx, ym, "-.")
    plt.title("MSE(R)")
    plt.xlabel("bitrate")
    plt.ylabel("MSE", labelpad=0)
    plt.subplot(1, 2, 2)
    plt.plot(xx, yp, "-o")
    plt.title("PSNR(R)")
    plt.xlabel("bitrate")
    plt.ylabel("PSNR [dB]", labelpad=0)
    plt.show()

    # compression ratio calculation
    size_png = os.stat("img/boat2_col.png").st_size
    size_jpg_100 = os.stat("img/out_image_q100.jpg").st_size
    size_jpg_10 = os.stat("img/out_image_q010.jpg").st_size
    print("COMPRESSION LEVELS:")
    print(
        "- Compression ratio at quality=100:"
        f" {size_png / size_jpg_100:.4f}"
    )
    print(
        "- Compression ratio at quality=10:"
        f" {size_png / size_jpg_10:.4f}"
    )

    # capacity calculation
    print("CAPACITY:")
    image_col = cv2.imread("img/boat2_col.png", cv2.IMREAD_UNCHANGED)
    bitrate_col = (
        8
        * os.stat("img/boat2_col.png").st_size
        / (image_col.shape[0] * image_col.shape[1])
    )
    image_bw = cv2.imread("img/boat2_mono.png", cv2.IMREAD_UNCHANGED)
    bitrate_bw = (
        8
        * os.stat("img/boat2_mono.png").st_size
        / (image_bw.shape[0] * image_bw.shape[1])
    )
    image_jpg = cv2.imread(
        "img/out_image_q100.jpg", cv2.IMREAD_UNCHANGED
    )
    bitrate_jpg = (
        8
        * os.stat("img/out_image_q100.jpg").st_size
        / (image_jpg.shape[0] * image_jpg.shape[1])
    )
    print(f"- Capacity for RGB PNG: {bitrate_col:.4f} bpp")
    print(f"- Capacity for MONO PNG: {bitrate_bw:.4f} bpp")
    print(f"- Capacity for RGB JPG: {bitrate_jpg:.4f} bpp")


if __name__ == "__main__":
    task12()
    # task3()
    # task4()
    # task56()
    # task7()
