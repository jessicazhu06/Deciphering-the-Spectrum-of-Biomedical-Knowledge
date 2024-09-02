# Download downloads the annual PubMed dataset, which is distributed across 1,219 individual XML files (number of files may change every year).

import xml.etree.ElementTree as ET
import pandas as pd
import os

def extract_text(element, tag):
    try:
        return element.find(tag).text
    except AttributeError:
        return None

def extract_date(pub_date):
    try:
        year = pub_date.find('Year').text
        month = pub_date.find('Month').text
        return f"{year}-{month}"
    except AttributeError:
        return None

def parse_mesh_headings(mesh_list):
    if mesh_list is None:
        return None
    headings = [mh.find('DescriptorName').text for mh in mesh_list.findall('MeshHeading') if mh.find('DescriptorName') is not None]
    return '; '.join(headings) if headings else None

def parse_keywords(keyword_list):
    if keyword_list is None:
        return None
    keywords = [kw.text for kw in keyword_list.findall('Keyword') if kw.text is not None]
    return '; '.join(keywords) if keywords else None

def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing {file_path}: {e}")
        return []

    records = []
    
    for article in root.findall('PubmedArticle'):
        date_element = article.find('.//PubDate')
        title_element = article.find('.//ArticleTitle')
        abstract_element = article.find('.//Abstract/AbstractText')
        mesh_list_element = article.find('.//MeshHeadingList')
        keyword_list_element = article.find('.//KeywordList')
        
        date = extract_date(date_element)
        title = title_element.text if title_element is not None else None
        abstract = abstract_element.text if abstract_element is not None else None
        mesh_headings = parse_mesh_headings(mesh_list_element)
        keywords = parse_keywords(keyword_list_element)
        
        records.append({
            'Date': date,
            'Title': title,
            'Abstract': abstract,
            'MeshHeading': mesh_headings,
            'Keywords': keywords
        })
    
    return records

def save_records_to_csv(records, output_file):
    df = pd.DataFrame(records)
    if not os.path.isfile(output_file):
        df.to_csv(output_file, index=False)
    else:
        df.to_csv(output_file, mode='a', header=False, index=False)
    print(f"Data successfully saved to {output_file}")

def process_directory(directory_path, output_csv_file, start_number=None):
    all_records = []
    error_log = []
    start_processing = False if start_number else True

    for filename in sorted(os.listdir(directory_path)):
        if filename.endswith('.xml'):
            # Check if we should start processing based on start_number
            if not start_processing and filename.startswith(f'pubmed24n{start_number:04d}'):
                start_processing = True
            
            if start_processing:
                file_path = os.path.join(directory_path, filename)
                print(f"Processing file: {file_path}")
                try:
                    records = parse_xml(file_path)
                    if records:
                        save_records_to_csv(records, output_csv_file)  # Save after processing each file
                except Exception as e:
                    error_message = f"Error processing {file_path}: {e}"
                    print(error_message)
                    error_log.append(error_message)
    
    if error_log:
        error_log_file = os.path.join(directory_path, 'error_log.txt')
        with open(error_log_file, 'w') as f:
            for error in error_log:
                f.write(error + "\n")
        print(f"Error log saved to {error_log_file}")

# Example usage
directory_path = os.path.dirname(os.path.abspath(__file__))
output_csv_file = os.path.join(directory_path, 'output_file.csv')
start_number = 0 # Change this to the number you want to start from

# Process all XML files in the directory and save to a CSV file
process_directory(directory_path, output_csv_file, start_number)

