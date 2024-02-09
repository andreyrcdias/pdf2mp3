import argparse
import os

import PyPDF2
from gtts import gTTS
from rich import print
from rich.progress import track


def convert_pdf_to_mp3(input_path: str, output_path: str):
    try:
        with open(input_path, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            pdf_text = ""

            for page in track(range(len(pdf_reader.pages)), description="Converting PDF to text"):
                pdf_text += pdf_reader.pages[page].extract_text()

        tts = gTTS(text=pdf_text, lang="en", tld="com.br", slow=False)
        tts.save(output_path)
        print(f"Audio file saved as {output_path}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert a PDF file to an MP3 audio file."
    )
    parser.add_argument("input_path", type=str, help="Input PDF file path")
    parser.add_argument("output_path", type=str, help="Output MP3 file path")
    args = parser.parse_args()
    if not os.path.isfile(args.input_path):
        print(f"Input file {args.input_path} does not exist.")
        exit(1)
    convert_pdf_to_mp3(args.input_path, args.output_path)


if __name__ == "__main__":
    main()
