def get_valid_input(prompt,expected_type = str, valid_options = None):
    while True:
        user_input = input(prompt).strip()
        try:
          value = expected_type(user_input)

          if valid_options is not None:
              if value not in valid_options:
                  print(f"Invalid input! Must be one of: {valid_options}")
                  continue
            
              return value
        except ValueError:
          print(f"Invalid input! Must be of type {expected_type.__name__}")
