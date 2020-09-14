from os.path import join
import matplotlib.pyplot as plt


def get_grid_image(output_dir, original_image, raw_output_image, final_output_image):
    start = original_image.rfind('/')
    result_grid_filename = join(output_dir, original_image[start+1:-4] + '_grid' + original_image[-4:])

    # Create plt plot:
    fig, axes = plt.subplots(1, 3)

    plt_image = plt.imread(original_image)
    axes[0].imshow(plt_image)
    axes[0].set_title("Original Image")
    axes[0].axis('off')
    plt_image = plt.imread(raw_output_image)
    axes[1].imshow(plt_image)
    axes[1].set_title("Raw Output")
    axes[1].axis('off')
    plt_image = plt.imread(final_output_image)
    axes[2].imshow(plt_image)
    axes[2].set_title("Final Output")
    axes[2].axis('off')

    plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
    plt.savefig(result_grid_filename)
    return result_grid_filename


original_image = "../data/imgs/train22.png"
raw_output_image = "../data/results/segcapsr3/split_0/raw_output/20200902-024237_raw_output.png"
final_output_image = "../data/results/segcapsr3/split_0/final_output/20200902-024237_final_output.png"

get_grid_image(".", original_image, raw_output_image, final_output_image)
