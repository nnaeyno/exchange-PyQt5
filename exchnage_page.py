def is_valid_number(input_text):
    try:
        float(input_text)
        return True
    except ValueError:
        return False