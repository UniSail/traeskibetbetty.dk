 

#!/bin/bash

 

# Define the date and draft values

DATE="2024-03-23T17:29:33+02:00"

DRAFT="false"

 

# Find all .md files and process each one

find . -type f -name "*.md" | while read -r file; do

  # Extract the filename without the extension

  TITLE=$(basename "$file" .md)

 

  # Create a temporary file

  TEMP_FILE=$(mktemp)

 

  # Create the string to prepend

  PREPEND_STRING="---

date: \"$DATE\"

draft: $DRAFT

title: \"$TITLE\"

---"

 

  # Write the prepend string to the temporary file

  echo "$PREPEND_STRING" > "$TEMP_FILE"

 

  # Append the original file content to the temporary file

  cat "$file" >> "$TEMP_FILE"

 

  # Move the temporary file to the original file

  mv "$TEMP_FILE" "$file"

done