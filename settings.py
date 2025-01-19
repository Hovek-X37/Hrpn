from pathlib import Path    # Path manipulation
import json                 # JSON file handling


class HRPNS():

    def __init__(self, args):
        self.settings = {}
        self.registry = {}
        if args.commandline is True:
            self.cmdline = True
            if args.prompt is None:
                self.settings.update({'prompt': ':'})
            else:
                self.settings.update({'prompt': args.prompt})
            if args.stacksize is None:
                self.settings.update({'stacksize': int(4)})
            else:
                self.settings.update({'stacksize': args.stacksize})
            if args.decimalplaces is None:
                self.settings.update({'decimalplaces': int(2)})
            else:
                self.settings.update({'decimalplaces': args.decimalplaces})
            self.settings.update({'hideheader': args.hideheader})
            self.settings.update({'hidestack': args.hidestack})
            self.settings.update({'registry': False})
        else:
            self.cmdline = False
            self.path = Path(args.file)
            self.regpath = Path('registry.json')
            if self.path.exists():
                self.settings = json.loads(self.path.read_text())
                if args.prompt is not None:
                    self.settings.update({'prompt': args.prompt})
                if args.stacksize is not None:
                    self.settings.update({'stacksize': args.stacksize})
                if args.decimalplaces is not None:
                    self.settings.update({'decimalplaces': args.decimalplaces})
                if args.hideheader is not None:
                    self.settings.update({'hideheader': args.hideheader})
                if args.hidestack is not None:
                    self.settings.update({'hidestack': args.hidestack})
                if args.orientation is not None:
                    self.settings.update({'orientation': args.orientation})
                else:
                    self.settings.update({'orientation': 'v'})
                if args.noregistry is True:
                    self.settings.update({'registry': False})
                else:
                    self.settings.update({'registry': True})
            else:
                self.settings.update({'prompt': ':'})
                self.settings.update({'stacksize': int(4)})
                self.settings.update({'decimalplaces': int(2)})
                self.settings.update({'hideheader': False})
                self.settings.update({'hidestack': False})
                self.settings.update({'registry': True})
                self.settings.update({'orientation': 'v'})
                self.path.write_text(json.dumps(self.settings))

    def change_app_settings(self):
        self.clear_screen()
        while True:
            print("Current settings:")
            for key, value in self.settings.items():
                print(f"{key}: {value}")
            expl = ""
            expl = "([p]rompt, [ss]stacksize, [dp]decimalplaces, [hh]hideheader \
([p]rompt, [ss]stacksize, [dp]decimalplaces, [hh]hideheader)\n"
            expl = expl + "Enter the setting you would like to change, or q to quit:"
            which = input(expl)
            if which == "p":
                self.change_prompt()
            elif which == "ss":
                self.change_stacksize()
            elif which == "dp":
                self.change_decimalplaces()
            elif which == "hh":
                self.change_hideheader()
            elif which == "sh":
                self.change_hidestack()
            elif which == "so":
                self.change_orientation()
            elif which == "r":
                self.change_registry()
            elif which == "s":
                self.save_settings()
            elif which == "q":
                self.clear_screen()
                return
            else:
                print("Invalid input")

    def change_prompt(self):
        self.clear_screen()
        prompt = input("Enter new prompt: ")
        self.settings.update({'prompt': prompt})
        return prompt

    def change_stacksize(self):
        self.clear_screen()
        stacksize = input("Enter new stack size: ")
        self.settings.update({'stacksize': int(stacksize)})
        return stacksize

    def change_decimalplaces(self):
        self.clear_screen()
        while True:
            decimalplaces = input("Enter new decimal places,0 disables rounding:")
            if decimalplaces.lstrip("-").isdigit():
                self.settings.update({'decimalplaces': int(decimalplaces)})
                return decimalplaces
            else:
                print("Invalid input")

    def change_hideheader(self):
        self.clear_screen()
        while True:
            hideheader = input("Hide header? (y/n): ")
            if hideheader == "y":
                hideheader = True
                self.settings.update({'hideheader': hideheader})
                return hideheader
            elif hideheader == "n":
                hideheader = False
                self.settings.update({'hideheader': hideheader})
                return hideheader
            else:
                print("Invalid input")

    def change_orientation(self):
        self.clear_screen()
        while True:
            if 'orientation' in self.settings:
                print(f"Current orientation: {self.settings['orientation']}")
            else:
                print("Orientation not set")
            orientation = input("Orientation? (v/h): ")
            if orientation == "v":
                self.settings.update({'orientation': orientation})
                return orientation
            elif orientation == "h":
                self.settings.update({'orientation': orientation})
                return orientation
            else:
                print("Invalid input")

    def change_hidestack(self):
        self.clear_screen()
        while True:
            hidestack = input("Hide stack? (y/n): ")
            if hidestack == "y":
                hidestack = True
                self.settings.update({'hidestack': hidestack})
                return hidestack
            elif hidestack == "n":
                hidestack = False
                self.settings.update({'hidestack': hidestack})
                return hidestack
            else:
                print("Invalid input")

    def change_registry(self):
        self.clear_screen()
        while True:
            registry = input("Use registry file? (y/n): ")
            if registry == "y":
                registry = True
                self.settings.update({'registry': registry})
                return registry
            elif registry == "n":
                registry = False
                self.settings.update({'registry': registry})
                return registry
            else:
                print("Invalid input")

    def clear_screen(self):
        print("\033[H\033[J")

    def save_settings(self):
        self.path.write_text(json.dumps(self.settings))
        return

    def get_settings(self):
        return self.settings

    def ret_setting(self, key):
        return self.settings[key]

    def get_registry(self):
        return self.registry

    def cmd_line(self):
        return self.cmdline
