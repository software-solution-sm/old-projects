connectors = {
    "Coordination": ["and", "but", "or", "yet", "so"],
    "Subordination": ["because", "although", "after", "if", "until", "since", "when", "while"],
    "Correlation": ["both...and", "either...or", "neither...nor", "not only...but also"]
}

def print_table(connectors):
  """Prints a table of connectors and their functions.

  Args:
    connectors: A dictionary of connectors and their functions.
  """

  print("| Function | Connector | Example |")
  print("|---|---|---|")
  for function, connectors in connectors.items():
    for connector in connectors:
      example = "I like {} and {}.".format(connector, connector)
      print("| {} | {} | {} |".format(function, connector, example))

if __name__ == "__main__":
  print_table(connectors)
