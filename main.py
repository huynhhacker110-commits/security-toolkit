#!/usr/bin/env python3
"""
Security Toolkit - Red Team + Blue Team Framework
Main entry point for the application
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from red_team.scanner import Scanner
from blue_team.monitor import Monitor
from core.logger import setup_logger

logger = setup_logger(__name__)

def main():
    parser = argparse.ArgumentParser(
        description='Security Toolkit - Red Team + Blue Team Framework',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Red Team Scan:
    python main.py --mode red --target 192.168.1.1 --scan-type full
  
  Blue Team Monitor:
    python main.py --mode blue --monitor --output report.html
        """
    )
    
    # Mode selection
    parser.add_argument(
        '--mode',
        choices=['red', 'blue'],
        required=True,
        help='Select operation mode: Red Team (offensive) or Blue Team (defensive)'
    )
    
    # Red Team arguments
    red_group = parser.add_argument_group('Red Team Options')
    red_group.add_argument(
        '--target',
        help='Target IP or hostname to scan'
    )
    red_group.add_argument(
        '--scan-type',
        choices=['quick', 'standard', 'full', 'custom'],
        default='standard',
        help='Type of scan to perform'
    )
    red_group.add_argument(
        '--ports',
        help='Specific ports to scan (e.g., 22,80,443 or 1-1000)'
    )
    red_group.add_argument(
        '--enumerate-services',
        action='store_true',
        help='Attempt to identify service versions'
    )
    
    # Blue Team arguments
    blue_group = parser.add_argument_group('Blue Team Options')
    blue_group.add_argument(
        '--monitor',
        action='store_true',
        help='Enable real-time monitoring'
    )
    blue_group.add_argument(
        '--output',
        help='Output file for security report'
    )
    blue_group.add_argument(
        '--alert-level',
        choices=['low', 'medium', 'high', 'critical'],
        default='medium',
        help='Alert sensitivity level'
    )
    
    # Common arguments
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    parser.add_argument(
        '--config',
        default='config/default.yaml',
        help='Configuration file path'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.mode == 'red' and not args.target:
        parser.error('--target is required for Red Team mode')
    
    if args.mode == 'blue' and not args.output:
        parser.error('--output is required for Blue Team mode')
    
    # Set logging level
    if args.verbose:
        logger.setLevel('DEBUG')
    
    logger.info(f"Security Toolkit started in {args.mode.upper()} Team mode")
    
    # Execute selected mode
    try:
        if args.mode == 'red':
            scanner = Scanner(config_file=args.config, verbose=args.verbose)
            scanner.scan(args.target, args.scan_type, args.ports, args.enumerate_services)
        
        elif args.mode == 'blue':
            monitor = Monitor(config_file=args.config, verbose=args.verbose)
            monitor.start_monitoring(args.alert_level, args.output)
    
    except Exception as e:
        logger.error(f"Error during execution: {str(e)}")
        sys.exit(1)
    
    logger.info("Security Toolkit completed successfully")

if __name__ == '__main__':
    main()
