
class Model:
    def __init__(self):
        self.selected_file = None

    def search_file(self, search_str):
        try:
            matching_rows = []

            # Open the Excel file for reading
            with open(self.selected_file, 'r', encoding='utf-8') as file:
                data = file.readlines()[1:]
                # Iterate through each line in the file
                for line in data:
                    # Split the line into columns (assuming CSV format)
                    columns = line.strip().split(',')

                    # Check if any column contains the searched value
                    if any(search_str.lower() in column.lower() for column in columns):
                        matching_rows.append(columns)

            return matching_rows

        except Exception as e:
            print("Error searching Excel file:", e)
            return None
