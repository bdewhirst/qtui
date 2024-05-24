import sys

import PySide6.QtCore as psqt_core
import PySide6.QtWidgets as psqt_widg

QT_STYLES = ["windows", "windowsvista", "fusion", "macos"]

windows = []  # Store references to our created windows.

def parse(app):
    """Parse the arguments and options of the given app object."""

    parser = psqt_core.QCommandLineParser()
    parser.addHelpOption()
    parser.addVersionOption()

    parser.addPositionalArgument("file", "Files to open.", "[file file file...]")

    maximize_option = psqt_core.QCommandLineOption(
        ["m", "maximize"],
        "Maximize the window on startup."
    )
    parser.addOption(maximize_option)

    style_option = psqt_core.QCommandLineOption(
        "s",
        "Use the specified Qt style, one of: " + ', '.join(QT_STYLES),
        "style"
    )
    parser.addOption(style_option)

    parser.process(app)

    has_maximize_option = parser.isSet(maximize_option)
    app_style = parser.value(style_option)

    if app_style and app_style in QT_STYLES:
        app.setStyle(app_style)

    # Check for positional arguments (files to open).
    arguments = parser.positionalArguments()

    # Iterate all arguments and open the files.
    for tfile in arguments:
        try:
            with open(tfile, 'r') as f:
                text = f.read()
        except Exception:
            # Skip this file if there is an error.
            continue

        window = psqt_widg.QPlainTextEdit(text)

        # Open the file in a maximized window, if set.
        if has_maximize_option:
            window.showMaximized()
        # Keep a reference to the window in our global list, to stop them
        # being deleted. We can test this list to see whether to show the
        # help (below) or start the event loop (at the bottom).
        windows.append(window)

    if not windows:
        # If we haven't created any windows, show the help.
        parser.showHelp()


app = psqt_widg.QApplication(sys.argv)
app.setApplicationName("My Application")
app.setApplicationVersion("1.0")

parse(app)

if windows:
    # We've created windows, start the event loop.
    app.exec()