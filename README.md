# Python-Assignment-Week4

This repository contains solutions for the Python file handling and error handling assignment.

## Files

### file_handling.py
- Reads an input file
- Modifies the content (converts to uppercase)
- Writes the modified content to a new file
- Handles common file operation errors

**Usage:**
```python
from file_handling import process_file
process_file('input.txt', 'output.txt')
```

### error_handling.py
- Interactive program that asks for filenames
- Handles multiple error cases:
  - File not found
  - Permission errors
  - Directory inputs
  - Encoding issues
- Includes a quit option

**Usage:**
```bash
python error_handling.py
```

## How to Test

1. First, create a test file:
```bash
echo "This is a test file" > input.txt
```

2. Test file_handling.py:
```bash
python -c "from file_handling import process_file; process_file('input.txt', 'output.txt')"
```

3. Test error_handling.py:
```bash
python error_handling.py
```
(Then try entering: existing files, non-existent files, directory names or 'quit')

## Assignment Requirements Met

✅ File Read & Write Challenge  
✅ Error Handling Lab  
✅ Robust exception handling  
✅ User-friendly error messages  
✅ Interactive program implementation

## Example Outputs

**Successful file processing:**
```
Successfully processed input.txt and saved to output.txt
```

**Error handling examples:**
```
Error: The file 'missing.txt' does not exist.
Error: You don't have permission to read '/root/file.txt'
Error: 'directory' is a directory, not a file
