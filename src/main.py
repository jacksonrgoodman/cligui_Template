import ui

# coloring:
ui.info("This is", ui.red, "red",
        ui.reset, "and this is", ui.bold, "bold")

# enumerating:
list_of_things = ["foo", "bar", "baz"]
for i, thing in enumerate(list_of_things):
    ui.info_count(i, len(list_of_things), thing)

# progress indication:
ui.info_progress("Load",  5, 20)
ui.info_progress("Half", 10, 20)
ui.info_progress("Done", 20, 20)

# reading user input:
with_sugar = ui.ask_yes_no("With sugar?", default=False)

fruits = ["apple", "orange", "banana"]
selected_fruit = ui.ask_choice("Choose a fruit", fruits)

#  ... and more!