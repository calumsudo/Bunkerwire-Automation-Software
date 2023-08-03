import PyPDF2
import re

#MFHOD00 Houston VLSFO 0.5% Data Function
def extract_mfhod00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "MFHOD00" in the text (assuming it's in the format "MFHOD00 ")
            mfhod00_pattern = r'MFHOD00\s+'
            match = re.search(mfhod00_pattern, page_text)

            if match:
                # Extract the "Mid" value after "MFHOD00"
                mid_pattern = r'\d+\.\d+'
                mid_match = re.search(mid_pattern, page_text[match.end():])

                if mid_match:
                    return float(mid_match.group())

    # If the "MFHOD00" or "Mid" value is not found, return None
    return None

#AAGPD00 Houston IFO380 Data Function
def extract_aagpd00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AAGPD00" in the text (assuming it's in the format "AAGPD00 ")
            aagpd00_pattern = r'AAGPD00\s+'
            match = re.search(aagpd00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (481.000 in the example)
                    return float(mid_values[2])

    # If the "AAGPD00" or "Mid" value is not found, return None
    return None


#AAWWX00 Houston MGO 0.1% Data Function
def extract_aawwx00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AAWWX00" in the text (assuming it's in the format "AAWWX00 ")
            aawwx00_pattern = r'AAWWX00\s+'
            match = re.search(aawwx00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (481.000 in the example)
                    return float(mid_values[2])

    # If the "AAWWX00" or "Mid" value is not found, return None
    return None

#MFRDD00 RDAM VLSFO 0.5%
def extract_mfrdd00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "MFRDD00" in the text (assuming it's in the format "MFRDD00 ")
            mfrdd00_pattern = r'MFRDD00\s+'
            match = re.search(mfrdd00_pattern, page_text)

            if match:
                # Extract the "Mid" value after "MFRDD00"
                mid_pattern = r'\d+\.\d+'
                mid_match = re.search(mid_pattern, page_text[match.end():])

                if mid_match:
                    return float(mid_match.group())

    # If the "MFHOD00" or "Mid" value is not found, return None
    return None

#PUAFN00
def extract_puafn00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "PUAFN00" in the text (assuming it's in the format "PUAFN00 ")
            puafn00_pattern = r'PUAFN00\s+'
            match = re.search(puafn00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (481.000 in the example)
                    return float(mid_values[2])

    # If the "PUAFN00" or "Mid" value is not found, return None
    return None
#AARTG00
def extract_aartg00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AARTG00" in the text (assuming it's in the format "AARTG00 ")
            aartg00_pattern = r'AARTG00\s+'
            match = re.search(aartg00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (481.000 in the example)
                    return float(mid_values[2])

    # If the "AARTG00" or "Mid" value is not found, return None
    return None
#MFGBD00
def extract_mfgbd00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "MFGBD00" in the text (assuming it's in the format "MFGBD00 ")
            mfgbd00_pattern = r'MFGBD00\s+\d+\.\d{1,3}'
            match = re.search(mfgbd00_pattern, page_text)

            if match:
                # Extract the "Mid" value after "MFGBD00"
                mid_pattern = r'\d+\.\d{1,3}'
                mid_match = re.search(mid_pattern, match.group())

                if mid_match:
                    return float(mid_match.group())

    # If the "MFGBD00" or "Mid" value is not found, return None
    return None
#AAKAB00

def extract_aakab00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AAKAB00" in the text (assuming it's in the format "AAKAB00 ")
            aakab00_pattern = r'AAKAB00\s+'
            match = re.search(aakab00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (e.g., 522.000)
                    return float(mid_values[2])

    # If the "AAKAB00" or "Mid" value is not found, return None
    return None

#AARSU00
def extract_aarsu00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AARSU00" in the text (assuming it's in the format "AARSU00 ")
            aarsu00_pattern = r'AARSU00\s+'
            match = re.search(aarsu00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (e.g., 633.000)
                    return float(mid_values[2])

    # If the "AARSU00" or "Mid" value is not found, return None
    return None
#MFFJD00
def extract_mffjd00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "MFFJD00" in the text (assuming it's in the format "MFFJD00 ")
            mffjd00_pattern = r'MFFJD00\s+'
            match = re.search(mffjd00_pattern, page_text)

            if match:
                # Extract the "Mid" value after "MFFJD00"
                mid_pattern = r'\d+\.\d+'
                mid_match = re.search(mid_pattern, page_text[match.end():])

                if mid_match:
                    return float(mid_match.group())

    # If the "MFFJD00" or "Mid" value is not found, return None
    return None
#PUAXP00
def extract_puaxp00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "PUAXP00" in the text (assuming it's in the format "PUAXP00 ")
            puaxp00_pattern = r'PUAXP00\s+'
            match = re.search(puaxp00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (e.g., 123.456)
                    return float(mid_values[2])

    # If the "PUAXP00" or "Mid" value is not found, return None
    return None
#AARKH00
def extract_aarkh00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AARKH00" in the text (assuming it's in the format "AARKH00 ")
            aarkh00_pattern = r'AARKH00\s+'
            match = re.search(aarkh00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (e.g., 789.012)
                    return float(mid_values[2])

    # If the "AARKH00" or "Mid" value is not found, return None
    return None
#AAXYP00
def extract_aaxyp00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AAXYP00" in the text (assuming it's in the format "AAXYP00 ")
            aaxyp00_pattern = r'AAXYP00\s+'
            match = re.search(aaxyp00_pattern, page_text)

            if match:
                # Extract the "Mid" value after "AAXYP00"
                mid_pattern = r'\d+\.\d+'
                mid_match = re.search(mid_pattern, page_text[match.end():])

                if mid_match:
                    return float(mid_match.group())

    # If the "AAXYP00" or "Mid" value is not found, return None
    return None
#MFSPD00
def extract_mfspd00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "MFSPD00" in the text (assuming it's in the format "MFSPD00 ")
            mfspd00_pattern = r'MFSPD00\s+'
            match = re.search(mfspd00_pattern, page_text)

            if match:
                # Extract the "Mid" value after "MFSPD00"
                mid_pattern = r'\d+\.\d+'
                mid_match = re.search(mid_pattern, page_text[match.end():])

                if mid_match:
                    return float(mid_match.group())

    # If the "MFSPD00" or "Mid" value is not found, return None
    return None
#PUAFT00
def extract_puaft00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "PUAFT00" in the text (assuming it's in the format "PUAFT00 ")
            puaft00_pattern = r'PUAFT00\s+'
            match = re.search(puaft00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (e.g., 123.456)
                    return float(mid_values[2])

    # If the "PUAFT00" or "Mid" value is not found, return None
    return None
#AALMZ00
def extract_aalmz00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AALMZ00" in the text (assuming it's in the format "AALMZ00 ")
            aalmz00_pattern = r'AALMZ00\s+'
            match = re.search(aalmz00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (e.g., 123.456)
                    return float(mid_values[2])

    # If the "AALMZ00" or "Mid" value is not found, return None
    return None
#AAXYO00
def extract_aaxyo00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AAXYO00" in the text (assuming it's in the format "AAXYO00 ")
            aaxyo00_pattern = r'AAXYO00\s+'
            match = re.search(aaxyo00_pattern, page_text)

            if match:
                # Extract the "Mid" value after "AAXYO00"
                mid_pattern = r'\d+\.\d+'
                mid_match = re.search(mid_pattern, page_text[match.end():])

                if mid_match:
                    return float(mid_match.group())

    # If the "AAXYO00" or "Mid" value is not found, return None
    return None
#MFSKD00
def extract_mfskd00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "MFSKD00" in the text (assuming it's in the format "MFSKD00 ")
            mfskd00_pattern = r'MFSKD00\s+'
            match = re.search(mfskd00_pattern, page_text)

            if match:
                # Extract the "Mid" value after "MFSKD00"
                mid_pattern = r'\d+\.\d+'
                mid_match = re.search(mid_pattern, page_text[match.end():])

                if mid_match:
                    return float(mid_match.group())

    # If the "MFSKD00" or "Mid" value is not found, return None
    return None
#PUAFR00
def extract_puafr00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "PUAFR00" in the text (assuming it's in the format "PUAFR00 ")
            puafr00_pattern = r'PUAFR00\s+'
            match = re.search(puafr00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (e.g., 123.456)
                    return float(mid_values[2])

    # If the "PUAFR00" or "Mid" value is not found, return None
    return None
#AAVBN00
def extract_aavbn00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AAVBN00" in the text (assuming it's in the format "AAVBN00 ")
            aavbn00_pattern = r'AAVBN00\s+'
            match = re.search(aavbn00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d{1,3}'
                mid_values = re.findall(mid_pattern, page_text[match.end():])

                if len(mid_values) >= 3:
                    # Assuming the "Mid" value is the third number found (e.g., 123.456)
                    return float(mid_values[2])

    # If the "AAVBN00" or "Mid" value is not found, return None
    return None
#AAXYS00
def extract_aaxys00_mid(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()

            # Look for "AAXYS00" in the text (assuming it's in the format "AAXYS00 ")
            aaxys00_pattern = r'AAXYS00\s+'
            match = re.search(aaxys00_pattern, page_text)

            if match:
                # Extract the "Mid" value (both values in the range)
                mid_pattern = r'\d+\.\d+'
                mid_match = re.search(mid_pattern, page_text[match.end():])

                if mid_match:
                    return float(mid_match.group())

    # If the "AAXYS00" or "Mid" value is not found, return None
    return None
