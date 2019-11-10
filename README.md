# A Little Single-User Dungeon

Welcome to the class project for CYBER-2101-A500, Python Essentials!

## Running

First, download the files via GitHub Desktop or the git command line, so that you can keep them up to date.

Next, you'll need to navigate to the project folder via the command line and run `pip install -r requirements.txt`. This will install the required extra Python libraries the game needs.

Then, you can run individual files by going into your terminal, navigating to the containing folder, and running `python [filename]`.

As we continue to build this project, we will eventually make the different files more connected and will eventually have a main file that will launch and run the game.

## Contributing

1. Pull/sync the `master` branch using your Git tool to make sure you have the latest version of the code.
1. Create a new branch with a descriptive name. You can use `/` in them to create "folders." While most characters are allowed, it's best practice to avoid spaces and instead use dashes (`-`) or underscores (`_`), and to avoid apostrophes, quotation marks, and other non-alphanumeric characters. An example of a good branch name is `joe-smith/add-movement-grid`.
1. Write your code.
    - Write your code directly into existing files, or create new files that relate to the application, itself. There's no need to make copies of the existing files or to create files like `myname-feature.py`.
    - When creating new files, avoid spaces, apostrophes, and other non-alphanumeric characters other than dashes and underscores (similar to the guidelines for branch names).
1. Commit your changes with a descriptive commit message. This can be pretty freeform and it's common to include a bulleted list of fixes or feature additions. It can also be useful to write explanations of the feature or fix, or why you chose a solution that you did.
1. Push your change to Github with your Git tool.
1. Create a pull request on the Pull Requests tab. Like commit messages, Pull Requests messages can and should be detailed. This is a particularly good place to explain the "why" in your decisions.
    - Be sure to review other people's pull requests and offer feedback (**do not merge**, I will do that after reviewing the PR). This will allow everyone to learn.

### Adding External Packages That Aren't Part of Python Core

If you find a module or package that is useful, but it's not part of the main Python library, you'll want to add it to the `requirements.txt` file. This is a list (with one library on each line) of the project and vesion the program needs. You can get this text by using the terminal to navigate to your working folder and entering `pip freeze`. Then, scroll through the list to find the package you added and copy that line into the requirements file.

### Adding Non-Code Assets

What do we do if we want images or other files that aren't Python? We need to make sure we include them in the repository. They should go into an `assets` folder (you may need to create it if other assets haven't been created yet). I also recommend you create subfolders for the asset types (ie - create an `images` folder to house images).