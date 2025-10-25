import logging
import sys
from pathlib import Path
from datetime import datetime

class CustomLogger:
    """Custom logger for test automation with file and console output."""
    
    _loggers = {}
    
    @staticmethod
    def get_logger(name="TestAutomation", log_file=None, level=logging.INFO):
        """
        Get or create logger instance.
        
        Args:
            name: Logger name
            log_file: Path to log file (auto-generated if None)
            level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            
        Returns:
            Logger instance
        """
        # Return existing logger if already created
        if name in CustomLogger._loggers:
            return CustomLogger._loggers[name]
        
        # Create new logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        
        # Prevent duplicate handlers
        if logger.handlers:
            return logger
        
        # Create log directory
        log_dir = Path(__file__).parent.parent / "artifacts" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate log file path
        if log_file is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            log_file = log_dir / f"test_log_{timestamp}.log"
        else:
            log_file = log_dir / log_file
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # File handler
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # Store logger
        CustomLogger._loggers[name] = logger
        
        logger.info(f"Logger initialized: {name}")
        logger.info(f"Log file: {log_file}")
        
        return logger
    
    @staticmethod
    def get_test_logger(test_name):
        """
        Get logger for specific test.
        
        Args:
            test_name: Name of the test
            
        Returns:
            Logger instance
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = f"{test_name}_{timestamp}.log"
        return CustomLogger.get_logger(test_name, log_file)


# Convenience functions for quick logging

def log_info(message, logger_name="TestAutomation"):
    """Log info message."""
    logger = CustomLogger.get_logger(logger_name)
    logger.info(message)

def log_debug(message, logger_name="TestAutomation"):
    """Log debug message."""
    logger = CustomLogger.get_logger(logger_name)
    logger.debug(message)

def log_warning(message, logger_name="TestAutomation"):
    """Log warning message."""
    logger = CustomLogger.get_logger(logger_name)
    logger.warning(message)

def log_error(message, logger_name="TestAutomation"):
    """Log error message."""
    logger = CustomLogger.get_logger(logger_name)
    logger.error(message)

def log_critical(message, logger_name="TestAutomation"):
    """Log critical message."""
    logger = CustomLogger.get_logger(logger_name)
    logger.critical(message)


# Step logger for test steps

class StepLogger:
    """Logger for test steps with step numbering."""
    
    def __init__(self, test_name):
        """
        Initialize step logger.
        
        Args:
            test_name: Name of the test
        """
        self.logger = CustomLogger.get_test_logger(test_name)
        self.step_number = 0
    
    def step(self, message):
        """
        Log a test step.
        
        Args:
            message: Step description
        """
        self.step_number += 1
        self.logger.info(f"STEP {self.step_number}: {message}")
    
    def info(self, message):
        """Log info message."""
        self.logger.info(f"  → {message}")
    
    def success(self, message):
        """Log success message."""
        self.logger.info(f"  ✓ {message}")
    
    def failure(self, message):
        """Log failure message."""
        self.logger.error(f"  ✗ {message}")
    
    def warning(self, message):
        """Log warning message."""
        self.logger.warning(f"  ⚠ {message}")


# Example usage in conftest.py fixture

def setup_test_logging(test_name):
    """
    Setup logging for a test.
    
    Args:
        test_name: Name of the test
        
    Returns:
        Logger instance
    """
    return CustomLogger.get_test_logger(test_name)
