def function_with_unclosed_file(filename):
    try:
        f = open(filename, 'r')
        # ... some code that processes the file ...
    except Exception as e:
        print(f"An error occurred: {e}")
    # Missing f.close() here!