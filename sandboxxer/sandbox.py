from .executor import CodeExecutor

class Sandbox:

    def __init__(self):
        self.executor = CodeExecutor()
        self.EXIT_MSG = "Exiting sandbox."

    def run(self):
        """Run the interactive sandbox."""
        print("Sandboxxer - Enter your code (type 'exit' or 'quit' or 'q' to quit or press 'Ctrl+Z' to exit):")
        while True:
            try:
                code = input(">>> ")
                if code.lower() == 'exit' or code.lower() == 'quit' or code.lower() == 'q':
                    print(self.EXIT_MSG)
                    break
                self.executor.execute(code)
            except (EOFError, KeyboardInterrupt):  # Handle Ctrl+Z (EOF), Ctrl+C (KeyboardInterrupt)
                print(self.EXIT_MSG)
                break
            except Exception as e:
                print(e)