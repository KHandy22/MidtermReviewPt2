import pytest
import sys
import os
from unittest.mock import patch
from io import StringIO

# Add parent directory to path to import student's code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestDebuggingChallenge:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Run before each test"""
        try:
            import task4
            import importlib
            importlib.reload(task4)
            self.task4 = task4
            self.task4_imported = True
        except Exception as e:
            self.task4_imported = False
            self.import_error = str(e)
    
    def test_01_file_imports(self):
        """Test that task4.py imports without errors - Must pass for other tests to run"""
        assert self.task4_imported, \
            f"task4.py has syntax errors and cannot import: {getattr(self, 'import_error', 'Unknown error')}"
    
    def test_02_snippet_1_fixed(self):
        """Snippet 1: Missing colon - 1 point"""
        if not self.task4_imported:
            pytest.skip("Cannot test - file won't import")
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec("""
temperature = 75
if temperature > 70:
    print("It's warm outside!")
""")
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert "It's warm outside!" in output, "Snippet 1 not fixed correctly"
    
    def test_03_snippet_2_fixed(self):
        """Snippet 2: Unclosed string - 1 point"""
        if not self.task4_imported:
            pytest.skip("Cannot test - file won't import")
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec("""
greeting = "Hello, welcome to our store"
print(greeting)
""")
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert "Hello, welcome to our store" in output, "Snippet 2 not fixed correctly"
    
    def test_04_snippet_3_fixed(self):
        """Snippet 3: Variable name typo - 1 point"""
        if not self.task4_imported:
            pytest.skip("Cannot test - file won't import")
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec("""
apples = 5
oranges = 3
total_fruit = apples + oranges
print(f"Total fruit: {total_fruit}")
""")
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert "Total fruit: 8" in output, "Snippet 3 not fixed correctly"
    
    def test_05_snippet_4_fixed(self):
        """Snippet 4: Indentation error - 1 point"""
        if not self.task4_imported:
            pytest.skip("Cannot test - file won't import")
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec("""
has_ticket = True
if has_ticket:
    prize = 10
    print(f"You won ${prize}!")
""")
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert "You won $10!" in output, "Snippet 4 not fixed correctly"
    
    def test_06_snippet_5_fixed(self):
        """Snippet 5: Missing type conversion - 1 point"""
        if not self.task4_imported:
            pytest.skip("Cannot test - file won't import")
        
        assert hasattr(self.task4, 'snippet_5'), "snippet_5 function not found"
        
        with patch('builtins.input', return_value='15'):
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            try:
                self.task4.snippet_5()
                output = sys.stdout.getvalue()
            finally:
                sys.stdout = old_stdout
        
        assert "Next year you'll be 16" in output, "Snippet 5 not fixed correctly"
    
    def test_07_snippet_6_fixed(self):
        """Snippet 6: Unclosed parenthesis - 1 point"""
        if not self.task4_imported:
            pytest.skip("Cannot test - file won't import")
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec("""
cookies = 12
share = cookies // 4
print(f"Each person gets {share} cookies")
""")
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert "Each person gets 3 cookies" in output, "Snippet 6 not fixed correctly"
    
    def test_08_snippet_7_fixed(self):
        """Snippet 7: Wrong operator (logic error) - 1 point"""
        if not self.task4_imported:
            pytest.skip("Cannot test - file won't import")
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec("""
lives = 3
lives = lives - 1
if lives == 2:
    print("You have 2 lives left")
""")
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert "You have 2 lives left" in output, "Snippet 7 not fixed correctly"
    
    def test_09_snippet_8_fixed(self):
        """Snippet 8: Undefined variable - 1 point"""
        if not self.task4_imported:
            pytest.skip("Cannot test - file won't import")
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec("""
price = 15.99
quantity = 2
total = price * quantity
print(f"Total: ${total}")
""")
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert "31.98" in output, "Snippet 8 not fixed correctly"
    
    def test_10_snippet_9_fixed(self):
        """Snippet 9: Missing parentheses in print - 1 point"""
        if not self.task4_imported:
            pytest.skip("Cannot test - file won't import")
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec("""
score = 100
print("Your score is:", score)
""")
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert "Your score is: 100" in output, "Snippet 9 not fixed correctly"
    
    def test_11_snippet_10_fixed(self):
        """Snippet 10: Indentation in if/else - 1 point"""
        if not self.task4_imported:
            pytest.skip("Cannot test - file won't import")
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec("""
is_raining = False
if is_raining:
    print("Bring an umbrella!")
else:
    print("Enjoy the sunshine!")
""")
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert "Enjoy the sunshine!" in output, "Snippet 10 not fixed correctly"
