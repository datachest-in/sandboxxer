from .executor import CodeExecutor

class Sandbox:
    def __init__(self):
        self.executor = CodeExecutor()

    def run(self):
        """Run the interactive sandbox."""
        print("Sandboxxer - Enter your code (type 'exit' or 'quit' or 'q' to quit or press 'Ctrl+Z' to exit):")
        while True:
            try:
                code = input(">>> ")
                if code.lower() == 'exit' or code.lower() == 'quit' or code.lower() == 'q':
                    break
                self.executor.execute(code)
            except EOFError:  # Handle Ctrl+Z (EOF)
                print("\nExiting sandbox.")
                break
            except KeyboardInterrupt:  # Handle Ctrl+C
                print("\nExiting sandbox.")
                break
            except Exception as e:
                print(e)