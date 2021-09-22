from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Eevee', 'Snorlax', 'charmander', 'jigglypuff'])
table.add_column("Type", ['electric', 'normal', 'normal', 'fire', 'fairy'])
print(table)