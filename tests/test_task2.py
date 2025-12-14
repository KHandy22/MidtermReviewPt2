import pytest
import sys
import os

# Add parent directory to path to import student's code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def check_hardcoding():
    """Helper function to check for hard-coding with test data"""
    with open('task2.py', 'r') as f:
        code = f.read()
    
    # Replace with test dataset
    modified_code = code.replace('allowance = 10', 'allowance = 15')
    modified_code = modified_code.replace('dishes, room, trash, lawn, laundry, vacuum = 3, 5, 2, 8, 4, 6',
                                         'dishes, room, trash, lawn, laundry, vacuum = 4, 6, 3, 10, 5, 7')
    modified_code = modified_code.replace('candy, soda, game, movie, toy, snack = 4, 2, 15, 10, 7, 3',
                                         'candy, soda, game, movie, toy, snack = 5, 3, 20, 12, 9, 4')
    
    # Execute modified code and capture output
    from io import StringIO
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        namespace = {}
        exec(modified_code, namespace)
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Calculate expected values with test dataset
    # Week 1: 15 + 4 + 6 - 5 = 20
    # Week 2: 20 * 2 + 10 - 20 = 30
    # Week 3: 30 / 2 = 15.0
    expected_final = 15.0
    
    hardcoded = False
    
    if 'allowance' in namespace and namespace['allowance'] != expected_final:
        hardcoded = True
    if str(expected_final) not in output and "15.0" not in output:
        hardcoded = True
    
    return hardcoded


class TestAllowanceTracker:
    
    @pytest.fixture(autouse=True)
    def capture_student_output(self, capsys):
        """Run student code and capture output before each test"""
        try:
            import task2
            import importlib
            importlib.reload(task2)
            self.task2 = task2
        except:
            self.task2 = None
        
        self.output = capsys.readouterr().out
    
    def test_01_allowance_variable_exists(self):
        """Test that allowance variable exists"""
        assert self.task2 is not None, "Could not import task2.py"
        assert hasattr(self.task2, 'allowance'), "Missing required variable: allowance"
    
    def test_02_week1_operations(self):
        """Test Week 1 operations - 3 points"""
        # After dishes (+3), room (+5), candy (-4): should be 14
        expected_after_week1 = 14
        # Check if code produces correct intermediate or final result
        # Since we can't easily check intermediate values, we'll verify through final output
        assert self.task2 is not None, "Could not import task2.py"
        assert not check_hardcoding(), "Hard-coding detected"
    
    def test_03_week2_operations(self):
        """Test Week 2 operations - 3 points"""
        # After doubling (14*2=28), lawn (+8=36), game (-15=21)
        assert self.task2 is not None, "Could not import task2.py"
        assert not check_hardcoding(), "Hard-coding detected"
    
    def test_04_week3_operations(self):
        """Test Week 3 operations - 2 points"""
        # After dividing by 2: 21/2 = 10.5
        expected_final = 10.5
        assert self.task2 is not None, "Could not import task2.py"
        if self.task2:
            assert self.task2.allowance == expected_final, "allowance miscalculated in Week 3"
        assert not check_hardcoding(), "Hard-coding detected"
    
    def test_05_output_format(self):
        """Test output format - 2 points"""
        expected_final = 10.5
        # Check for "Allowance: $10.5" format
        assert "Allowance:" in self.output or "allowance:" in self.output, "Output missing 'Allowance:'"
        assert str(expected_final) in self.output, "Output missing final allowance value"
        assert not check_hardcoding(), "Hard-coding detected"
