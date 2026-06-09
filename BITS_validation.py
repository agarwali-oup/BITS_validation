from lxml import etree

def validate_xml(xml_file, dtd_file):
    try:
        # Load DTD
        with open(dtd_file, 'rb') as f:
            # dtd = etree.DTD(f)
            dtd = etree.DTD(file=dtd_file)

        # Parse XML
        tree = etree.parse(xml_file)

        # Validate
        if dtd.validate(tree):
            print(f"✅ {xml_file} is valid against the DTD")
        else:
            print(f"❌ {xml_file} is NOT valid")
            for error in dtd.error_log:
                print(error)

    except Exception as e:
        print(f"Error: {e}")


# Example usage
validate_xml(r"C:\Users\agarwais\English\Physics_books\XML-BITS\10__1088_2053-2563_aae109.xml", r"C:\Users\agarwais\Downloads\BITS-OASIS-XHTML-TABLES-DTD\BITS-OASIS-XHTML-TABLES-DTD\BITS-book-oasis2.dtd")