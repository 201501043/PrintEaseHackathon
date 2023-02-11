def convert_to_embedded_code(link):
    # Replace "edit" with "pubhtml" in the link
    embedded_link = link.replace("edit", "pubhtml")
    
    # Construct the embedded code
    embedded_code = '<iframe src="{}" width="100%" height="500"></iframe>'.format(embedded_link)
    
    return embedded_code
link = "https://docs.google.com/spreadsheets/d/1imyk85dGOq23YidKMh2KsdymkoF1Ef34/edit?usp=sharing&ouid=108317268897548490108&rtpof=true&sd=true"
embedded_code = convert_to_embedded_code(link)
print(embedded_code)