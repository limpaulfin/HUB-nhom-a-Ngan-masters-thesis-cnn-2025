import os
import requests
import time
from urllib.parse import urljoin
import bibtexparser

# Danh sách các papers cần tải
papers = [
    {
        "title": "Deep learning",
        "authors": "LeCun, Y., Bengio, Y., & Hinton, G.",
        "year": "2015",
        "doi": "10.1038/nature14539",
        "url": "https://doi.org/10.1038/nature14539",
        "alternative_urls": [
            "https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf",
            "https://www.researchgate.net/publication/277411157_Deep_Learning"
        ]
    },
    {
        "title": "ImageNet classification with deep convolutional neural networks",
        "authors": "Krizhevsky, A., Sutskever, I., & Hinton, G. E.",
        "year": "2012",
        "doi": "10.1145/3065386",
        "url": "https://doi.org/10.1145/3065386",
        "alternative_urls": [
            "http://www.cs.toronto.edu/~kriz/imagenet_classification_with_deep_convolutional.pdf",
            "https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf"
        ]
    },
    {
        "title": "Deep residual learning for image recognition",
        "authors": "He, K., Zhang, X., Ren, S., & Sun, J.",
        "year": "2016",
        "doi": "10.1109/CVPR.2016.90",
        "url": "https://doi.org/10.1109/CVPR.2016.90",
        "alternative_urls": [
            "https://arxiv.org/pdf/1512.03385.pdf"
        ]
    },
    {
        "title": "Very deep convolutional networks for large-scale image recognition",
        "authors": "Simonyan, K., & Zisserman, A.",
        "year": "2015",
        "url": "https://arxiv.org/abs/1409.1556"
    },
    {
        "title": "Fast and accurate deep network learning by exponential linear units (ELUs)",
        "authors": "Clevert, D. A., Unterthiner, T., & Hochreiter, S.",
        "year": "2016",
        "url": "https://arxiv.org/abs/1511.07289"
    },
    {
        "title": "A survey on deep learning in medical image analysis",
        "authors": "Litjens, G., et al.",
        "year": "2017",
        "doi": "10.1016/j.media.2017.07.005",
        "url": "https://doi.org/10.1016/j.media.2017.07.005",
        "alternative_urls": [
            "https://arxiv.org/pdf/1702.05747.pdf"
        ]
    },
    {
        "title": "Deep learning for sensor-based activity recognition",
        "authors": "Wang, J., Chen, Y., Hao, S., Peng, X., & Hu, L.",
        "year": "2019",
        "doi": "10.1016/j.patrec.2018.02.010",
        "url": "https://doi.org/10.1016/j.patrec.2018.02.010"
    },
    {
        "title": "Understanding deep learning requires rethinking generalization",
        "authors": "Zhang, C., Bengio, S., Hardt, M., Recht, B., & Vinyals, O.",
        "year": "2017",
        "url": "https://arxiv.org/abs/1611.03530"
    }
]

def download_paper(paper, output_dir):
    """Download a paper and save it to the specified directory."""
    filename = f"{paper['year']}_{paper['title'].replace(' ', '_')}.pdf"
    filepath = os.path.join(output_dir, filename)

    if os.path.exists(filepath):
        print(f"Paper already exists: {filename}")
        return

    # List of URLs to try
    urls_to_try = [paper["url"]]
    if "alternative_urls" in paper:
        urls_to_try.extend(paper["alternative_urls"])

    for url in urls_to_try:
        try:
            print(f"Attempting to download: {paper['title']}")
            print(f"Trying URL: {url}")

            if "arxiv.org" in url:
                # For arXiv papers
                arxiv_id = url.split("/")[-1]
                if not arxiv_id.endswith(".pdf"):
                    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                else:
                    pdf_url = url
            else:
                pdf_url = url

            response = requests.get(pdf_url, allow_redirects=True)

            if response.status_code == 200 and (
                response.headers.get('content-type', '').lower() == 'application/pdf' or
                pdf_url.endswith('.pdf')
            ):
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"Successfully downloaded: {filename}")
                return  # Exit after successful download
            else:
                print(f"Could not download from: {url}")

        except Exception as e:
            print(f"Error downloading from {url}: {str(e)}")

        # Wait between attempts
        time.sleep(2)

    # If all attempts failed
    print(f"Could not download paper: {paper['title']}")
    print("Please try manual download from the following sources:")
    for url in urls_to_try:
        print(f"- {url}")

def main():
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)

    # Download each paper
    for paper in papers:
        download_paper(paper, output_dir)
        print("\n")  # Add spacing between papers

    print("\nDownload attempts completed.")
    print("Note: Some papers may require manual download due to access restrictions.")
    print("Please check README.md for papers that need to be downloaded manually and alternative sources.")

if __name__ == "__main__":
    main()
