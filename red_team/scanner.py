#!/usr/bin/env python3
"""
Red Team Scanner Module
Handles port scanning, service detection, and vulnerability scanning
"""

import nmap
from typing import Dict, List, Tuple
from core.logger import setup_logger

logger = setup_logger(__name__)

class Scanner:
    """Red Team Scanner for network reconnaissance"""
    
    def __init__(self, config_file: str = None, verbose: bool = False):
        self.nm = nmap.PortScanner()
        self.verbose = verbose
        self.results = {}
        logger.info("Red Team Scanner initialized")
    
    def scan(self, target: str, scan_type: str = 'standard', ports: str = None, 
             enumerate_services: bool = False) -> Dict:
        """
        Execute network scan on target
        
        Args:
            target: Target IP or hostname
            scan_type: Type of scan (quick, standard, full, custom)
            ports: Specific ports to scan
            enumerate_services: Whether to detect service versions
        
        Returns:
            Dictionary containing scan results
        """
        logger.info(f"Starting {scan_type} scan on {target}")
        
        # Define scan arguments based on type
        scan_args = self._get_scan_args(scan_type, ports, enumerate_services)
        
        try:
            self.nm.scan(target, arguments=scan_args)
            self.results = self._parse_results()
            logger.info(f"Scan completed. Found {len(self.results['open_ports'])} open ports")
            return self.results
        
        except Exception as e:
            logger.error(f"Scan failed: {str(e)}")
            raise
    
    def _get_scan_args(self, scan_type: str, ports: str = None, 
                       enumerate_services: bool = False) -> str:
        """
        Build nmap arguments based on scan type
        """
        args_map = {
            'quick': '-sS -p 1-1000',
            'standard': '-sS -p 1-10000 -sV',
            'full': '-sS -p- -sV -sC',
            'custom': f'-sS {f"-p {ports}" if ports else "-p 1-10000"}'
        }
        
        args = args_map.get(scan_type, args_map['standard'])
        
        if enumerate_services:
            args += ' -sV -O'
        
        return args
    
    def _parse_results(self) -> Dict:
        """
        Parse nmap scan results
        """
        results = {
            'open_ports': [],
            'services': {},
            'vulnerabilities': []
        }
        
        for host in self.nm.all_hosts():
            if self.nm[host].state() == 'up':
                for proto in self.nm[host].all_protocols():
                    ports = self.nm[host][proto].keys()
                    for port in ports:
                        state = self.nm[host][proto][port]['state']
                        if state == 'open':
                            results['open_ports'].append(port)
                            service_info = {
                                'port': port,
                                'name': self.nm[host][proto][port].get('name', 'Unknown'),
                                'version': self.nm[host][proto][port].get('version', '')
                            }
                            results['services'][port] = service_info
        
        return results
    
    def get_results(self) -> Dict:
        """Get the latest scan results"""
        return self.results
