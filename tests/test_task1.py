import pytest
import sys
import os

# Add parent directory to path to import student's code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def check_hardcoding():
    """Helper function to check for hard-coding with test data"""
    with open('task1.py', 'r') as f:
        code = f.read()
    
    # Replace with test dataset
    modified_code = code.replace('people = 2', 'people = 3')
    modified_code = modified_code.replace('bagA = 23', 'bagA = 30')
    modified_code = modified_code.replace('bagB = 17', 'bagB = 25')
    modified_code = modified_code.replace('bagC = 19', 'bagC = 20')
    
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
    
    # Check for expected values with test dataset
    expected_total = 75
    expected_first_share = 18
    expected_second_share = 15
    
    hardcoded = False
    
    if 'total_candy' in namespace and namespace['total_candy'] != expected_total:
        hardcoded = True
    if str(expected_total) not in output:
        hardcoded = True
    if str(expected_first_share) not in output:
        hardcoded = True
    if str(expected_second_share) not in output:
        hardcoded = True
    
    return hardcoded


class TestHalloweenCandy:
    
    @pytest.fixture(autouse=True)
    def capture_student_output(self, capsys):
        """Run student code and capture output before each test"""
        try:
            import task1
            import importlib
            importlib.reload(task1)
            self.task1 = task1
        except:
            self.task1 = None
        
        self.output = capsys.readouterr().out
    
    def test_01_total_candy_variable_exists(self):
        """Test that total_candy variable exists"""
        assert self.task1 is not None, "Could not import task1.py"
        assert hasattr(self.task1, 'total_candy'), "Missing required variable: total_candy"
    
    def test_02_share_variable_exists(self):
        """Test that share variable exists"""
        assert self.task1 is not None, "Could not import task1.py"
        assert hasattr(self.task1, 'share'), "Missing required variable: share"
    
    def test_03_leftover_variable_exists(self):
        """Test that leftover variable exists"""
        assert self.task1 is not None, "Could not import task1.py"
        assert hasattr(self.task1, 'leftover'), "Missing required variable: leftover"
    
    def test_04_total_candy(self):
        """Test total candy calculation - 2 points"""
        expected_total = 59
        assert str(expected_total) in self.output, "total_candy miscalculated or not printed"
        if self.task1:
            assert self.task1.total_candy == expected_total, "total_candy miscalculated"
        assert not check_hardcoding(), "Hard-coding detected"
    
    def test_05_first_each_share(self):
        """Test first division - share with 3 people - 2 points"""
        expected_share = 19
        assert str(expected_share) in self.output, "share miscalculated in scenario 1"
        assert not check_hardcoding(), "Hard-coding detected"
    
    def test_06_first_leftover(self):
        """Test first division - leftover with 3 people - 2 points"""
        expected_leftover = 2
        assert str(expected_leftover) in self.output, "leftover miscalculated in scenario 1"
        assert not check_hardcoding(), "Hard-coding detected"
    
    def test_07_second_each_share(self):
        """Test second division - share with 4 people - 2 points"""
        expected_share = 14
        lines = self.output.split('\n')
        assert str(expected_share) in '\n'.join(lines[-3:]), "share miscalculated in scenario 2"
        if self.task1:
            assert self.task1.share == expected_share, "share miscalculated in scenario 2"
        assert not check_hardcoding(), "Hard-coding detected"
    
    def test_08_second_leftover(self):
        """Test second division - leftover with 4 people - 2 points"""
        expected_leftover = 3
        lines = self.output.split('\n')
        assert str(expected_leftover) in '\n'.join(lines[-2:]), "leftover miscalculated in scenario 2"
        if self.task1:
            assert self.task1.leftover == expected_leftover, "leftover miscalculated in scenario 2"
        assert not check_hardcoding(), "Hard-coding detected"
